# Módulo que gerencia os tiros disparados pelo player

from code.Const import ENTITY_SPEED
from code.Entity import Entity


class PlayerShot(Entity):
    # Método construtor que inicializa com a posição e informações do tiro do player
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    # Método que faz o tiro do player se mover
    def move(self):
        self.rect.centerx += ENTITY_SPEED[self.name]