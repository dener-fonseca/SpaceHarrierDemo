# Módulo que controla elementos de fundo do jogo

from code.Const import ENTITY_SPEED, WIN_WIDTH
from code.Entity import Entity


class Background(Entity):
    # Método construtor que inicializa com nome e a posição do background
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
    
    # Método que faz o background se mover automáticamente
    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]
        if self.rect.right <= 0:
            self.rect.left = WIN_WIDTH