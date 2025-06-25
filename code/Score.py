# Módulo que cria a tela de pontuação com seus atributos e comportamentos como mostrar mensagem que o jogador ganhou, pedir que ele escreva seu nome e salvar a pontuação no banco de dados

import sys
import pygame
from datetime import datetime
from pygame.font import Font
from pygame import Surface, Rect, KEYDOWN, K_RETURN, K_BACKSPACE, K_ESCAPE
from code.Const import (COLOR_YELLOW, SCORE_POS, MENU_OPTION, COLOR_WHITE, WIN_WIDTH, WIN_HEIGHT)
from code.DBProxy import DBProxy


class Score:
    def __init__(self, window: Surface):
        self.window = window
        self.surf = pygame.image.load('./assets/ScoreBackground.png').convert_alpha()
        self.surf = pygame.transform.scale(self.surf, (WIN_WIDTH, WIN_HEIGHT))
        self.rect = self.surf.get_rect(left=0, top=0)
        self.typing_sound = pygame.mixer.Sound('./assets/MoveOption.mp3')
        self.confirm_sound = pygame.mixer.Sound('./assets/EnterOption.mp3')
        pass

    def save(self, game_mode: str, player_score: list[int]):
        pygame.mixer_music.load('./assets/ScoreSound.mp3')
        pygame.mixer_music.set_volume(0.5)
        pygame.mixer_music.play(-1)
        db_proxy = DBProxy('DBScore')
        name = ''
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.score_text(48, 'Você Venceu!!!', COLOR_YELLOW, SCORE_POS['Title'])
            text = 'Jogador 1 - Escreva seu nome (4 letras):'
            score = player_score[0]
            if game_mode == MENU_OPTION[0]:
                score = player_score[0]
            if game_mode == MENU_OPTION[1]:
                score = (player_score[0] + player_score[1]) / 2
                text = 'Time - Escreva seu nome (4 letras):'
            if game_mode == MENU_OPTION[2]:
                if player_score[0] >= player_score[1]:
                    score = player_score[0]
                else:
                    score = player_score[1]
                    text = 'Jogador 2 - Escreva seu nome (4 letras):'
            self.score_text(20, text, COLOR_WHITE, SCORE_POS['EnterName'])

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                # Adição de código que só pemite que o jogador confirme o nome quando ele tiver 4 letras
                elif event.type == KEYDOWN:
                    if event.key == K_RETURN:
                        if len(name) == 4:
                            self.confirm_sound.play()
                            pygame.time.delay(150)
                            db_proxy.save({'name': name, 'score': score, 'date': get_formatted_date()})
                            self.show()
                            return
                    elif event.key == K_BACKSPACE:
                        name = name[:-1]
                        self.typing_sound.play()
                    else:
                        if len(name) < 4:
                            name += event.unicode
                            self.typing_sound.play()
            self.score_text(20, name, COLOR_WHITE, SCORE_POS['Name'])
            pygame.display.flip()
            pass

    def show(self):
        pygame.mixer_music.load('./assets/ScoreSound.mp3')
        pygame.mixer_music.set_volume(0.5)
        pygame.mixer_music.play(-1)
        self.window.blit(source=self.surf, dest=self.rect)
        self.score_text(50, 'TOP 10 PONTUAÇÃO', COLOR_YELLOW, SCORE_POS['Title'])
        self.score_text(22, 'NOME     PONTUAÇÃO           DATA      ', COLOR_YELLOW, SCORE_POS['Label'])
        db_proxy = DBProxy('DBScore')
        list_score = db_proxy.retrieve_top10()
        db_proxy.close()

        for player_score in list_score:
            id_, name, score, date = player_score
            self.score_text(20, f'{name}     {score:05d}     {date}', COLOR_YELLOW,
                            SCORE_POS[list_score.index(player_score)])
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
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