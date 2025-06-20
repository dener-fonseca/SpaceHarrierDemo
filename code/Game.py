# Módulo que controla o loop principal do jogo, os estados do menu, dos níveis e integra todos os componentes

import sys
import pygame
from code import Const
from code.Level import Level
from code.Menu import Menu
from code.Score import Score
from code.LevelEndScreen import LevelEndScreen

class Game:
    def __init__(self):
        pygame.init()
        # Inicializa o mixer
        pygame.mixer.init()
        # Carrega os sons
        self.load_sounds()
        # Captura a resolução nativa da tela
        info = pygame.display.Info()
        Const.WIN_WIDTH = info.current_w
        Const.WIN_HEIGHT = info.current_h

        # Cria a janela em modo tela cheia com resolução nativa
        self.window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        pygame.display.set_caption("Space Harrier")
        
    def load_sounds(self):
        self.sounds = {
            'move_option': pygame.mixer.Sound('./assets/MoveOption.mp3'),
            'enter_option': pygame.mixer.Sound('./assets/EnterOption.mp3'),
            'shot': pygame.mixer.Sound('./assets/Shot.mp3'),
            'explosion': pygame.mixer.Sound('./assets/Explosion.mp3'),
            'damage': pygame.mixer.Sound('./assets/Damage.mp3')
        }

    def run(self):
        while True:
            score = Score(self.window,self.sounds)
            menu = Menu(self.window,self.sounds)
            menu_return = menu.run()

            if menu_return in [Const.MENU_OPTION[0], Const.MENU_OPTION[1], Const.MENU_OPTION[2]]:
                player_score = [0, 0]
                
                for level_number in range(1,4):
                    level = Level(self.window, f'Level{level_number}', menu_return, player_score, self.sounds)
                    level_result = level.run(player_score)
                    
                    # Se perdeu (single ou ambos no multiplayer)
                    if not level_result:
                        end_screen = LevelEndScreen(
                            screen=self.window,
                            font=pygame.font.SysFont("DM Serif Display", 24),
                            level_number=level_number,
                            success=False
                        )
                        end_screen.show()
                        # Vai para score
                        break
                    
                    # Se venceu o último nível
                    if level_number == 3:
                        end_screen = LevelEndScreen(
                            screen=self.window,
                            font=pygame.font.SysFont("DM Serif Display", 24),
                            level_number=level_number,
                            success=True
                        )
                        end_screen.show()
                        # Vai para score
                        break
                    
                    # Se venceu um nível intermediário
                    end_screen = LevelEndScreen(
                        screen=self.window,
                        font=pygame.font.SysFont("DM Serif Display", 24),
                        level_number=level_number,
                        success=True
                    )
                    end_screen.show()
                    
                # Após fim do jogo (vitória ou derrota)
                score.save(menu_return, player_score)
                

            elif menu_return == Const.MENU_OPTION[3]:
                score.show()

            elif menu_return == Const.MENU_OPTION[4]:
                pygame.quit()
                quit()

            else:
                pygame.quit()
                sys.exit()