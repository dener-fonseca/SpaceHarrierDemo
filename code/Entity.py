# Módulo que trabalha como classe base genérica para todos os objetos do jogo

import pygame.image
from abc import ABC, abstractmethod
from code.Const import ENTITY_HEALTH, ENTITY_DAMAGE, ENTITY_SCORE


class Entity(ABC):
    def __init__(self, name: str, position: tuple):
        self.name = name
        try:
            self.surf = pygame.image.load(f'./assets/{name}.png').convert_alpha()
        except pygame.error:
            print(f"Erro ao carregar imagem: {name}.png")
            # Cria uma superficie vazia como fallback
            self.surf = pygame.Surface((32, 32))
            self.surf.fill((255, 0, 255))  # Cor magenta para indicar erro
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = 0
        self.health = ENTITY_HEALTH[self.name]
        self.damage = ENTITY_DAMAGE[self.name]
        self.score = ENTITY_SCORE[self.name]
        self.last_dmg = 'None'

    @abstractmethod
    def move(self):
        pass