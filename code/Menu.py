# Módulo que gerencia a tela de menu inicial do jogo

import pygame.image
import sys
from code.Const import (COLOR_BLUE, COLOR_GREY, COLOR_WHITE, MENU_OPTION)
from pygame.font import Font
from pygame import Surface, Rect


class Menu:
    def __init__(self, window, sounds):
        self.window = window
        self.sounds = sounds
        self.surf = pygame.image.load('./assets/MenuBg.png').convert_alpha()
        # Redimensiona o fundo para cobrir toda a tela
        self.surf = pygame.transform.scale(self.surf, self.window.get_size())
        self.rect = self.surf.get_rect(left=0, top=0)
        # Pega largura e altura reais da janela
        self.win_width, self.win_height = self.window.get_size()
    
    def run(self):
        menu_option = 0
        try:
            pygame.mixer.music.load('./assets/Menu.mp3')
            pygame.mixer.music.play(-1)
        except pygame.error:
            pass  # O programa não para se o arquivo de som não for encontrado
        
        clock = pygame.time.Clock()
        
        while True:
            clock.tick(60)
            
            self.window.blit(source=self.surf, dest=self.rect)

            # Criação do título do jogo
            self.menu_text(50, "SPACE HARRIER", COLOR_BLUE, (self.win_width / 2, 70))
            self.menu_text(50, "Demo", COLOR_GREY, (self.win_width / 2, 120))

            # Criação das opções do menu
            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(20, MENU_OPTION[i], COLOR_GREY, (self.win_width / 2, 200 + 25 * i))
                else:
                    self.menu_text(20, MENU_OPTION[i], COLOR_WHITE, (self.win_width / 2, 200 + 25 * i))
            
            pygame.display.flip()

            # Criação dos eventos do teclado
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        self.sounds['move_option'].play()
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0
                    if event.key == pygame.K_UP:
                        self.sounds['move_option'].play()
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1
                    if event.key == pygame.K_RETURN:
                        self.sounds['enter_option'].play()
                        return MENU_OPTION[menu_option]
    
    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="DM Serif Display", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)