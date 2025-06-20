# Módulo que gerencia os tiros disparados pelos inimigos

from code.Const import ENTITY_SPEED
from code.Entity import Entity


class EnemyShot(Entity):
    #Método construtor que inicializa com nome e posição do tiro do inimigo automaticamente
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
    
    # Método que faz o tiro do inimigo se mover automáticamente
    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]