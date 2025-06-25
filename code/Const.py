# Módulo que contém todas as constantes que serão usadas no projeto prático

import pygame

# Cores do jogo

COLOR_BLUE = (0, 0, 255)
COLOR_RED = (255,0, 0)
COLOR_GREY = (128, 128, 128)
COLOR_WHITE = (255, 255, 255)
COLOR_YELLOW = (255, 255, 0)
COLOR_PURPLE = (128, 0, 128)

# Evento para criar inimigos

EVENT_ENEMY = pygame.USEREVENT + 1

# Evento para atualizar o tempo do jogo

EVENT_TIMEOUT = pygame.USEREVENT + 2

# Entidade que determina velocidade de movimento dos cenários, jogadores, inimigos e tiros

ENTITY_SPEED = {
    'Level1Bg0': 0,
    'Level1Bg1': 1,
    'Level1Bg2': 2,
    'Level1Bg3': 3,
    'Level1Bg4': 4,
    'Level1Bg5': 5,
    'Level1Bg6': 6,
    'Level2Bg0': 0,
    'Level2Bg1': 1,
    'Level2Bg2': 2,
    'Level2Bg3': 3,
    'Level2Bg4': 4,
    'Level2Bg5': 5,
    'Level2Bg6': 6,
    'Level2Bg7': 7,
    'Level3Bg0': 0,
    'Level3Bg1': 1,
    'Level3Bg2': 2,
    'Level3Bg3': 3,
    'Level3Bg4': 4,
    'Player1': 3,
    'Player1Shot': 2,
    'Player2': 3,
    'Player2Shot': 2,
    'Enemy1': 2,
    'Enemy1Shot': 3,
    'Enemy2': 2,
    'Enemy2Shot': 3,
    'Enemy3': 2,
    'Enemy3Shot': 3,
}

# Entidade que determina a saúde do jogador e do inimigo

ENTITY_HEALTH = {
    'Level1Bg0': 999,
    'Level1Bg1': 999,
    'Level1Bg2': 999,
    'Level1Bg3': 999,
    'Level1Bg4': 999,
    'Level1Bg5': 999,
    'Level1Bg6': 999,
    'Level2Bg0': 999,
    'Level2Bg1': 999,
    'Level2Bg2': 999,
    'Level2Bg3': 999,
    'Level2Bg4': 999,
    'Level2Bg5': 999,
    'Level2Bg6': 999,
    'Level2Bg7': 999,
    'Level3Bg0': 999,
    'Level3Bg1': 999,
    'Level3Bg2': 999,
    'Level3Bg3': 999,
    'Level3Bg4': 999,
    'Player1': 200,
    'Player1Shot': 1,
    'Player2': 200,
    'Player2Shot': 1,
    'Enemy1': 100,
    'Enemy1Shot': 1,
    'Enemy2': 150,
    'Enemy2Shot': 1,
    'Enemy3': 150,
    'Enemy3Shot': 1,
}

# Entidade que determina dano do jogador e do inimigo

ENTITY_DAMAGE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Level1Bg4': 0,
    'Level1Bg5': 0,
    'Level1Bg6': 0,
    'Level2Bg0': 0,
    'Level2Bg1': 0,
    'Level2Bg2': 0,
    'Level2Bg3': 0,
    'Level2Bg4': 0,
    'Level2Bg5': 0,
    'Level2Bg6': 0,
    'Level2Bg7': 0,
    'Level3Bg0': 0,
    'Level3Bg1': 0,
    'Level3Bg2': 0,
    'Level3Bg3': 0,
    'Level3Bg4': 0,
    'Player1': 0,
    'Player1Shot': 50,
    'Player2': 0,
    'Player2Shot': 50,
    'Enemy1': 200,
    'Enemy1Shot': 50,
    'Enemy2': 200,
    'Enemy2Shot': 50,
    'Enemy3': 200,
    'Enemy3Shot': 50,
}

# Entidade que determina ponto que vale o inimigo destruido

ENTITY_SCORE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Level1Bg4': 0,
    'Level1Bg5': 0,
    'Level1Bg6': 0,
    'Level2Bg0': 0,
    'Level2Bg1': 0,
    'Level2Bg2': 0,
    'Level2Bg3': 0,
    'Level2Bg4': 0,
    'Level2Bg5': 0,
    'Level2Bg6': 0,
    'Level2Bg7': 0,
    'Level3Bg0': 0,
    'Level3Bg1': 0,
    'Level3Bg2': 0,
    'Level3Bg3': 0,
    'Level3Bg4': 0,
    'Player1': 0,
    'Player1Shot': 0,
    'Player2': 0,
    'Player2Shot': 0,
    'Enemy1': 100,
    'Enemy1Shot': 0,
    'Enemy2': 125,
    'Enemy2Shot': 0,
    'Enemy3': 150,
    'Enemy3Shot': 0,
}

# Tempo de delay do tiro das naves

ENTITY_SHOT_DELAY = {
    'Player1': 20,
    'Player2': 20,
    'Enemy1': 70,
    'Enemy2': 70,
    'Enemy3': 70,
}

# Menu do jogo

MENU_OPTION = ('Novo Jogo - 1 Jogador',
               'Novo Jogo - 2 Jogadores Cooperativo',
               'Novo Jogo - 2 Jogadores Competitivo',
               'Tela de Pontuação',
               'Sair do Jogo')

# Comandos dos jogadores 1 e 2 com jogador 1 controlando a esquerda do teclado e jogador 2 controlando a direita do teclado

PLAYER_KEY_UP = {'Player1': pygame.K_w,
                 'Player2': pygame.K_UP}
PLAYER_KEY_DOWN = {'Player1': pygame.K_s,
                   'Player2': pygame.K_DOWN}
PLAYER_KEY_LEFT = {'Player1': pygame.K_a,
                   'Player2': pygame.K_LEFT}
PLAYER_KEY_RIGHT = {'Player1': pygame.K_d,
                    'Player2': pygame.K_RIGHT}
PLAYER_KEY_SHOOT = {'Player1': pygame.K_LCTRL,
                    'Player2': pygame.K_RCTRL}

# Tempo de spawn dos inimigos

SPAWN_TIME = 4000

# Tempo que serve de intervalo na redução do contador que será de 100 milisegundos

TIMEOUT_STEP = 100

#Tempo para a fase acabar que será 60 segundos

TIMEOUT_LEVEL = 60000

# WIN_WIDTH e WIN_HEIGHT são constantes que determinam altura e largura da tela e precisam vir antes de SCORE_POS

WIN_WIDTH = 600

WIN_HEIGHT = 400

# SCORE_POS é o posicionamento das informações na tela de pontuação

SCORE_POS = {'Title': (WIN_WIDTH / 2, 52),
             'EnterName': (WIN_WIDTH / 2, 82),
             'Label': (WIN_WIDTH / 2, 92),
             'Name': (WIN_WIDTH / 2, 112),
             0: (WIN_WIDTH / 2, 110),
             1: (WIN_WIDTH / 2, 130),
             2: (WIN_WIDTH / 2, 150),
             3: (WIN_WIDTH / 2, 170),
             4: (WIN_WIDTH / 2, 190),
             5: (WIN_WIDTH / 2, 210),
             6: (WIN_WIDTH / 2, 230),
             7: (WIN_WIDTH / 2, 250),
             8: (WIN_WIDTH / 2, 270),
             9: (WIN_WIDTH / 2, 290),
             }