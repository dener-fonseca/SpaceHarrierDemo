# Módulo que controla elementos de fundo do jogo

from code.Const import (WIN_WIDTH, ENTITY_SPEED)
from code.Entity import Entity


class Background(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        
    # Função que move os elementos de fundo do jogo das fases
    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]
        if self.rect.right <= 0:
            self.rect.left = WIN_WIDTH