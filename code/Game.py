# Módulo que controla o loop principal do jogo, os estados do menu, dos níveis e integra todos os componentes

import pygame
import sys
import code.Const as Const
from code.Level import Level
from code.LevelEndScreen import LevelEndScreen
from code.Menu import Menu
from code.Score import Score


class Game:
    def __init__(self):
        pygame.init()
        # Inicializa o mixer com tratamento de erro
        self.audio_enabled = True
        try:
            pygame.mixer.init()
            # Carrega os sons após a inicialização bem-sucedida do mixer
            self.load_sounds()
        except pygame.error:
            print("Áudio não está disponível.")
            self.audio_enabled = False
            self.sounds = {}
        # Define resolução fixa para evitar problemas de escala
        Const.WIN_WIDTH = 1024
        Const.WIN_HEIGHT = 768

        # Atualiza SCORE_POS com a resolução definida
        Const.SCORE_POS = Const.generate_score_pos(Const.WIN_WIDTH, Const.WIN_HEIGHT)

        # Cria a janela com resolução fixa
        self.window = pygame.display.set_mode((Const.WIN_WIDTH, Const.WIN_HEIGHT))
        pygame.display.set_caption("Space Harrier")

    # Método para carregar os sons do jogo
    def load_sounds(self):
        sound_files = ['MoveOption.mp3', 'EnterOption.mp3', 'Shot.mp3', 'Explosion.mp3', 'Damage.mp3']
        sound_names = ['move_option', 'enter_option', 'shot', 'explosion', 'damage']
        
        self.sounds = {}
        
        if self.audio_enabled:
            for name, file in zip(sound_names, sound_files):
                try:
                    self.sounds[name] = pygame.mixer.Sound(f'./assets/{file}')
                except pygame.error as e:
                    print(f"Erro ao carregar som {file}: {e}")
                    # Som vazio como fallback
                    self.sounds[name] = None
        else:
            # Sons vazios quando áudio não está disponível
            for name in sound_names:
                self.sounds[name] = None

    # Método que inicia o loop principal do jogo
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

                    # Aparece tela de fim de nivel e verifica se o player venceu ou perdeu
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

                # Tela de pontuação aparece após o fim do jogo
                score.save(menu_return, player_score)


            elif menu_return == Const.MENU_OPTION[3]:
                score.show()

            elif menu_return == Const.MENU_OPTION[4]:
                pygame.quit()
                quit()

            else:
                pygame.quit()
                sys.exit()