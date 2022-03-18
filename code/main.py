# fazer todas as importações necessárias
import pygame
from GameSystem import gSystem
from Interfaces.screen_interface import ScreenInterface
from Screens.screen_jogo import ScreenJogo


def main(*args):
    # Inicializar
    pygame.init()
    gSystem.init(fps=60)

    # Cria uma lista com todas as telas do jogo
    telas_jogo: list[ScreenInterface] = [ScreenJogo('jogo', gSystem)]
    
    for tela in telas_jogo:
        gSystem.SCREEN_MANAGER.add_screen(tela)

    # Chamar o gerenciador de telas
    gSystem.SCREEN_MANAGER.__main__('jogo')

    pygame.quit()
    pass


if __name__ == '__main__':
    main()
