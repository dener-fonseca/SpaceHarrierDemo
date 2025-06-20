# Módulo que controla e gerencia o sistema de pontuação dos players

import sys
import pygame
from datetime import datetime
from pygame import Surface, Rect, KEYDOWN, K_RETURN, K_BACKSPACE, K_ESCAPE
from pygame.font import Font
from code.Const import (C_BLUE, C_WHITE, MENU_OPTION, SCORE_POS)
from code.DBProxy import DBProxy


class Score:
    def __init__(self, window: Surface, sounds):
        self.window = window
        self.sounds = sounds
        self.surf = pygame.image.load('./assets/ScoreBg.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)
        self.error_timer = 0

    def save(self, game_mode: str, player_score: list[int]):
        pygame.mixer.music.load('./assets/Score.mp3')
        pygame.mixer.music.play(-1)

        db_proxy = DBProxy('DBScore')
        name = ''
        self.error_timer = 0

        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.score_text(48, 'VOCÊ VENCEU!!', C_BLUE, SCORE_POS['Title'])

            text = 'Digite o nome do Jogador 1 (4 letras):'
            score = player_score[0]

            if game_mode == MENU_OPTION[1]:
                score = (player_score[0] + player_score[1]) / 2
                text = 'Digite o nome da Equipe (4 letras):'
            elif game_mode == MENU_OPTION[2]:
                if player_score[0] >= player_score[1]:
                    score = player_score[0]
                    text = 'Digite o nome do Jogador 1 (4 letras):'
                else:
                    score = player_score[1]
                    text = 'Digite o nome do Jogador 2 (4 letras):'

            self.score_text(20, text, C_WHITE, SCORE_POS['EnterName'])

            # Mensagem de erro se o nome for inválido
            if self.error_timer > 0:
                self.score_text(18, 'O nome deve ter 4 letras!!!', (255, 0, 0), SCORE_POS['Error'])
                self.error_timer -= 1

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                elif event.type == KEYDOWN:
                    if event.key == K_RETURN:
                        if len(name.strip()) == 4:
                            name = name.strip().upper()
                            self.sounds['enter_option'].play()
                            db_proxy.save({'name': name, 'score': score, 'date': get_formatted_date()})
                            self.show()
                            return
                        else:
                            self.sounds['move_option'].play()
                            self.error_timer = 60

                    elif event.key == K_BACKSPACE:
                        name = name[:-1]
                        self.sounds['move_option'].play()

                    else:
                        if len(name) < 4:
                            name += event.unicode.upper()
                            self.sounds['move_option'].play()

            self.score_text(20, name, C_WHITE, SCORE_POS['Name'])
            pygame.display.flip()

    def show(self):
        pygame.mixer.music.load('./assets/Score.mp3')
        pygame.mixer.music.play(-1)

        self.window.blit(source=self.surf, dest=self.rect)

        self.score_text(48, 'TOP 10 PONTUAÇÕES', C_BLUE, SCORE_POS['Title'])
        self.score_text(20, 'NOME     PONTOS           DATA      ', C_BLUE, SCORE_POS['Label'])

        db_proxy = DBProxy('DBScore')
        list_score = db_proxy.retrieve_top10()
        db_proxy.close()

        for i, player_score in enumerate(list_score):
            id_, name, score, date = player_score
            self.score_text(20, f'{name}     {score:05d}     {date}', C_BLUE, SCORE_POS[i])

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.mixer.music.stop()
                        return
            pygame.display.flip()

    def score_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="DM Serif Display", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)


def get_formatted_date():
    current_datetime = datetime.now()
    current_time = current_datetime.strftime("%H:%M")
    current_date = current_datetime.strftime("%d/%m/%y")
    return f"{current_time} - {current_date}"