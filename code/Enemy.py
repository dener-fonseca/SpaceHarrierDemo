# Módulo que define o comportamento dos 3 inimigos de se mover e atirar automaticamente

from code.Const import (ENTITY_SPEED, ENTITY_SHOT_DELAY)
from code.EnemyShot import EnemyShot
from code.Entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]
        
    # Função que define o comportamento de se mover dos inimigos
    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]
        
    # Função que define o comportamento de atirar dos inimigos
    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            return EnemyShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))