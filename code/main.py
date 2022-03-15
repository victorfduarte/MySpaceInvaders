# fazer todas as importações necessárias
from turtle import Screen
import pygame
from GameSystem.input import Input
from GameSystem.collisions import Collisions
from GameSystem.timer import Timer
from GameSystem.display import Display
from Screens.screen_manager import ScreenManager
# from Screens.screen_jogo import 


def main(*args):
    # Inicializar
    pygame.init()

    # Instanciar os objetos de Input, Colisão, Tempo e Saída
    input_obj = Input()
    collsion = Collisions()
    timer = Timer()
    display = Display()

    # Criar as telas e o gerenciador
    screen_manager = ScreenManager()
    # menu_screen = 

    # Chamar o gerenciador de telas
    screen_manager.__main__()
    pass



if __name__ == '__main__':
    print(__name__)
    print(__package__)
    main()