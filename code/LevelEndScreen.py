# Módulo que mostra se você passou os niveis 1 e 2, mostra que concluiu a demo ou mostra game over caso o player perca em uma das fases

import pygame

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
            return pygame.image.load(f"assets/Level{self.level_number}Background.png").convert()
        except:
            print(f"Imagem de fundo da fase {self.level_number} não encontrada.")
            return None

    def show(self):
        # Código que toca a música da tela de fim de fase
        try:
            pygame.mixer.music.load("assets/LevelEndScreen.mp3")
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