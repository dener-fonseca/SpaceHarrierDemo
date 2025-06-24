# Módulo que gerencia a explosão dos players e inimigos quando são destruídos

import pygame
from code.Entity import Entity

class Explosion(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.image = pygame.image.load('./assets/Explosion.png').convert_alpha()
        self.rect = self.image.get_rect(center=position)
        self.timer = 30

    # Método que não deixa a explosão se mover
    def move(self):
        pass

    # Método que atualiza o tempo da explosão
    def update(self):
        self.timer -= 1
        if self.timer <= 0:
            self.health = 0