# Módulo que define os inimigos com seus comportamentos como se mover e atirar automaticamente

from code.Const import ENTITY_SHOT_DELAY, ENTITY_SPEED 
from code.EnemyShot import EnemyShot
from code.Entity import Entity


class Enemy(Entity):
    # Método construtor que inicializa com o nome e posição do inimigo
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]

    # Método que faz os inimigos se moverem automaticamente
    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]

    #Método que faz os inimigos atirarem automaticamente
    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            return EnemyShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))