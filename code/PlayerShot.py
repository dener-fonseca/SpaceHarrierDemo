# Módulo que gerencia os tiros disparados pelo jogador

from code.Const import ENTITY_SPEED
from code.Entity import Entity


class PlayerShot(Entity):
    # Método construtor da classe PlayerShot
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        
    # Função que move o tiro do jogador
    def move(self):
        self.rect.centerx += ENTITY_SPEED[self.name]