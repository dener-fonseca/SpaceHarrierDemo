# Módulo que trabalha como classe base genérica para todos os objetos do jogo

import pygame.image
from abc import ABC, abstractmethod
from code.Const import (ENTITY_HEALTH, ENTITY_DAMAGE, ENTITY_SCORE, SCALE_MAP, WIN_WIDTH, WIN_HEIGHT)


class Entity(ABC):
    def __init__(self, name: str, position: tuple):
        self.name = name
        self.surf = pygame.image.load('./assets/' + name + '.png').convert_alpha()
        
        # Ajuste apenas para imagens de fundo, tamanho dos jogadores, inimigos e tiros
        if 'Bg' in name:
            self.surf = pygame.transform.scale(self.surf, (WIN_WIDTH, WIN_HEIGHT))
        if name in SCALE_MAP:
            self.surf = pygame.transform.scale(self.surf, SCALE_MAP[name])
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = 0
        self.health = ENTITY_HEALTH[self.name]
        self.damage = ENTITY_DAMAGE[self.name]
        self.score = ENTITY_SCORE[self.name]
        self.last_dmg = 'None'

    @abstractmethod
    def move(self):
        pass