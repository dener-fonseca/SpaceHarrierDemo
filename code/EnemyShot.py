# Módulo que gerencia os tiros disparados pelos 3 inimigos

from code.Const import ENTITY_SPEED
from code.Entity import Entity


class EnemyShot(Entity):
    # Método construtor da classe EnemyShot
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        
    # Função que move o tiro dos inimigos
    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]