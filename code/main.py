# fazer todas as importações necessárias
import pygame
from GameSystem import gSystem
from Screens.screen import Screen
from Screens.screen_jogo import ScreenJogo



def main(*args):
    # Inicializar
    pygame.init()
    gSystem.init(first_screen='jogo')

    # Cria uma lista com todas as telas do jogo
    telas_jogo: list[Screen] = [ScreenJogo('jogo', gSystem)]
    
    for tela in telas_jogo:
        gSystem.SCREEN_MANAGER.add_screen(tela)

    # Chamar o gerenciador de telas
    gSystem.SCREEN_MANAGER.__main__()
    pass



if __name__ == '__main__':
    print(__name__)
    print(__package__)
    main()