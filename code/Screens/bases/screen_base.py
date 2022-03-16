import pygame.time
from GameSystem import GSystem
from Interfaces.screen_interface import ScreenInterface

class ScreenBase(ScreenInterface):
    '''Base Class\n
    Todas as telas do jogo herdaram dessa classe. Ela implementa a interface
    ScreenInterface. Cada tela terá de implementarar os seguintes métodos abstratos:\n
        setup() -> None\n
        leave() -> None\n
    
    Ela disponibiliza também, os seguintes métodos:\n
        get_name() -> str\n
        get_gSystem() -> GSystem
    '''
    
    def __init__(self, name: str, game_system: GSystem):
        self.__name = name
        self.__game_system = game_system
        self.__running = False
    

    def get_gSytem(self) -> GSystem:
        return self.__game_system

    def getName(self) -> str:
        '''Retorna o nome da tela'''
        return self.__name
    
    def __stop_running__(self):
        '''Este método faz a tela parar de reagir'''
        self.__running = False
    

    def __mainloop__(self):
        '''Este método implementa o loop principal de cada tela\n
        **Esta função faz parte do sistema e não deve ser chamada**
        '''
        self.setup()

        clock = pygame.time.Clock()
        framerate = self.__game_system.DISPLAY.getFramerate()
        self.__running = True

        
        while self.__running:
            dt = clock.tick(framerate)
            # Inputs
            self.__game_system.INPUT.__listen__()
            # Colisões
            self.__game_system.COLLISIONS.__check__()
            # Timer
            self.__game_system.TIMER.__update__(dt)
            # Update Display
            self.__game_system.DISPLAY.__update__()
            # Mantem o Framerate