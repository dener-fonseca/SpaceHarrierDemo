# Módulo que mostra se você passou os niveis 1 e 2, mostra que concluiu a demo ou mostra game over caso o player perca em uma das fases

import pygame
import sys
from code.Const import COLOR_WHITE, WIN_WIDTH, WIN_HEIGHT

class LevelEndScreen:
    def __init__(self, screen, font, level_number, success=True, max_level=3):
        self.screen = screen
        self.font = font
        self.level_number = level_number
        self.success = success
        self.max_level = max_level
        self.finished = False

        # Código para carregar o background da fase atual
        self.background = self.load_background()

    def load_background(self):
        try:
            bg = pygame.image.load(f"assets/Level{self.level_number}Background.png").convert()
            # Redimensiona para cobrir toda a tela
            bg = pygame.transform.scale(bg, (self.screen.get_width(), self.screen.get_height()))
            return bg
        except pygame.error:
            print(f"Imagem de fundo da fase {self.level_number} não encontrada.")
            return None

    def show(self):
        clock = pygame.time.Clock()
        
        while not self.finished:
            clock.tick(60)
            
            # Eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                        self.finished = True
            
            # Desenha o fundo
            if self.background:
                self.screen.blit(self.background, (0, 0))
            else:
                self.screen.fill((0, 0, 0))  # Fundo preto se não conseguir carregar
            
            # Determina a mensagem baseada no sucesso e nível
            if self.success:
                if self.level_number == self.max_level:
                    title = "PARABÉNS! DEMO CONCLUÍDA!"
                    subtitle = "Você completou todos os níveis!"
                else:
                    title = f"NÍVEL {self.level_number} CONCLUÍDO!"
                    subtitle = f"Preparando para o Nível {self.level_number + 1}..."
            else:
                title = "GAME OVER"
                subtitle = "Você foi derrotado!"
            
            # Renderiza o texto
            title_surface = self.font.render(title, True, COLOR_WHITE)
            subtitle_surface = self.font.render(subtitle, True, COLOR_WHITE)
            continue_surface = self.font.render("Pressione ENTER para continuar", True, COLOR_WHITE)
            
            # Centraliza o texto
            title_rect = title_surface.get_rect(center=(WIN_WIDTH // 2, WIN_HEIGHT // 2 - 50))
            subtitle_rect = subtitle_surface.get_rect(center=(WIN_WIDTH // 2, WIN_HEIGHT // 2))
            continue_rect = continue_surface.get_rect(center=(WIN_WIDTH // 2, WIN_HEIGHT // 2 + 100))
            
            # Desenha o texto
            self.screen.blit(title_surface, title_rect)
            self.screen.blit(subtitle_surface, subtitle_rect)
            self.screen.blit(continue_surface, continue_rect)
            
            pygame.display.flip()

    def show_old(self):
        # Código que toca a música da tela de fim de fase
        try:
            pygame.mixer.music.load("assets/LevelEndScreen.mp3") # Código para carregar a música de fim de fase
            pygame.mixer.music.set_volume(0.3) # Código para definir o volume da música
            pygame.mixer.music.play(-1)  # Código para repetir a música indefinidamente enquanto a tela estiver ativa
        except pygame.error as e:
            print(f"Erro ao carregar a música de fim de fase: {e}")
        
        # Código que define a mensagem principal
        if self.success:
            if self.level_number == self.max_level:
                message = "VOCÊ COMPLETOU A DEMO!!!"
            else:
                message = f"VOCÊ PASSOU O NÍVEL {self.level_number}!!!"
        else:
            message = "GAME OVER!!!"

        sub_message = "Aperte ENTER para continuar..."

        clock = pygame.time.Clock()
        while not self.finished:
            if self.background:
                self.screen.blit(self.background, (0, 0))
            else:
                # fundo preto padrão
                self.screen.fill((0, 0, 0))

            # Código para renderizar os textos
            text_surface = self.font.render(message, True, (255, 255, 255))
            sub_surface = self.font.render(sub_message, True, (200, 200, 200))

            text_rect = text_surface.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() // 2 - 20))
            sub_rect = sub_surface.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() // 2 + 20))

            self.screen.blit(text_surface, text_rect)
            self.screen.blit(sub_surface, sub_rect)

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    self.finished = True

            clock.tick(60)
            
        # Código que para a música quando sai da tela
        pygame.mixer.music.stop()