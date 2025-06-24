# Módulo que define o player com seus comportamentos como se mover e atirar

import pygame
from code.Const import (ENTITY_SHOT_DELAY, ENTITY_SPEED, PLAYER_KEY_UP, PLAYER_KEY_DOWN, PLAYER_KEY_LEFT, PLAYER_KEY_RIGHT, PLAYER_KEY_SHOOT, WIN_HEIGHT, WIN_WIDTH)
from code.Entity import Entity
from code.PlayerShot import PlayerShot


class Player(Entity):
    # Método construtor que inicializa com o nome e a posição do player
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]

    # Método para o player se mover
    def move(self):
        pressed_key = pygame.key.get_pressed()
        # Movimento vertical com margens de segurança
        if pressed_key[PLAYER_KEY_UP[self.name]] and self.rect.top > 10:
            self.rect.centery -= ENTITY_SPEED[self.name]
        if pressed_key[PLAYER_KEY_DOWN[self.name]] and self.rect.bottom < WIN_HEIGHT - 10:
            self.rect.centery += ENTITY_SPEED[self.name]
        # Movimento horizontal com margens de segurança
        if pressed_key[PLAYER_KEY_LEFT[self.name]] and self.rect.left > 10:
            self.rect.centerx -= ENTITY_SPEED[self.name]
        if pressed_key[PLAYER_KEY_RIGHT[self.name]] and self.rect.right < WIN_WIDTH - 10:
            self.rect.centerx += ENTITY_SPEED[self.name]
        
        # Garante que o player não saia da tela mesmo com variações de tamanho
        self.rect.clamp_ip(pygame.Rect(0, 0, WIN_WIDTH, WIN_HEIGHT))

    # Método para o player atirar
    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            pressed_key = pygame.key.get_pressed()
            if pressed_key[PLAYER_KEY_SHOOT[self.name]]:
                return PlayerShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))
            else:
                return None
        else:
            return None