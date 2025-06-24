# Módulo que cria entidades baseado em algum tipo de configuração

import random
from code.Background import Background
from code.Const import WIN_HEIGHT, WIN_WIDTH
from code.Enemy import Enemy
from code.Player import Player


class EntityFactory:
    # Método estático que retorna lista de entidades
    @staticmethod
    def get_entity(entity_name: str):
        match entity_name:
            case 'Level1Bg':
                list_bg = []
                for i in range(7):
                    # Primeiro background na posição inicial
                    bg1 = Background(f'Level1Bg{i}', (0, 0))
                    list_bg.append(bg1)
                    # Segundo background posicionado imediatamente após o primeiro
                    bg2 = Background(f'Level1Bg{i}', (bg1.rect.width, 0))
                    list_bg.append(bg2)
                return list_bg

            case 'Level2Bg':
                list_bg = []
                for i in range(8):
                    # Primeiro background na posição inicial
                    bg1 = Background(f'Level2Bg{i}', (0, 0))
                    list_bg.append(bg1)
                    # Segundo background posicionado imediatamente após o primeiro
                    bg2 = Background(f'Level2Bg{i}', (bg1.rect.width, 0))
                    list_bg.append(bg2)
                return list_bg

            case 'Level3Bg':
                list_bg = []
                for i in range(5):
                    # Primeiro background na posição inicial
                    bg1 = Background(f'Level3Bg{i}', (0, 0))
                    list_bg.append(bg1)
                    # Segundo background posicionado imediatamente após o primeiro
                    bg2 = Background(f'Level3Bg{i}', (bg1.rect.width, 0))
                    list_bg.append(bg2)
                return list_bg

            case 'Player1':
                return Player('Player1', (10, WIN_HEIGHT / 2 - 30))

            case 'Player2':
                return Player('Player2', (10, WIN_HEIGHT / 2 + 30))

            case 'Enemy1':
                return Enemy('Enemy1', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))

            case 'Enemy2':
                return Enemy('Enemy2', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))

            case 'Enemy3':
                return Enemy('Enemy3', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))