# Módulo que cria o menu com seus atributos e comportamentos como o título do jogo e o menu de opções

import pygame.image
from pygame import Surface, Rect
from pygame.font import Font
from code.Const import (WIN_WIDTH, WIN_HEIGHT, COLOR_BLUE, COLOR_RED, MENU_OPTION, COLOR_WHITE, COLOR_GREY)


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./assets/MenuBackground.png').convert_alpha()
        self.surf = pygame.transform.scale(self.surf, (WIN_WIDTH, WIN_HEIGHT))
        self.rect = self.surf.get_rect(left=0, top=0)
        self.move_sound = pygame.mixer.Sound('./assets/MoveOption.mp3')
        self.enter_sound = pygame.mixer.Sound('./assets/EnterOption.mp3')
        
    # Função que roda o menu do jogo
    def run(self):
        menu_option = 0
        pygame.mixer_music.load('./assets/MenuSound.mp3')
        pygame.mixer_music.set_volume(0.5)
        pygame.mixer_music.play(-1)
        while True:
            # Código que desenha a janela do menu
            self.window.blit(source=self.surf, dest=self.rect)
            #Código que escreve o nome do jogo na tela
            self.menu_text(50, "SPACE HARRIER", COLOR_BLUE, ((WIN_WIDTH / 2), 70))
            self.menu_text(40, "DEMO", COLOR_RED, ((WIN_WIDTH / 2), 120))

            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(25, MENU_OPTION[i], COLOR_GREY, ((WIN_WIDTH / 2), 200 + 25 * i))
                else:
                    self.menu_text(20, MENU_OPTION[i], COLOR_WHITE, ((WIN_WIDTH / 2), 200 + 25 * i))
            pygame.display.flip()

            # Código que checa os eventos do programa
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Fecha a janela
                    quit()  # Fecha o pygame
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:  # Tecla DOWN
                        self.move_sound.play()
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0
                    if event.key == pygame.K_UP:  # Tecla UP
                        self.move_sound.play()
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1
                    if event.key == pygame.K_RETURN:  # Tecla ENTER
                        self.enter_sound.play()
                        pygame.time.delay(150)
                        return MENU_OPTION[menu_option]
                        
    # Função que cria o texto do menu
    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="DM Serif Display", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)