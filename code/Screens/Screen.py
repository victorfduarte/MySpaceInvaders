from ..GameSystem.input import Input
from ..GameSystem.collisions import Collisions
from ..GameSystem.timer import Timer
from ..GameSystem.display import Display
from screen_manager import ScreenManager


class Screen:
    '''Abstract Class\n
    Todas as telas do jogo herdaram dessa classe. Cada tela implementará as seguintes
    funções abstratas:\n
        setup() -> None\n
        leave() -> None\n
    Possui também as seguintes funções:\n
        get_name() -> str\n
        stop_running() -> None'''
    
    def __init__(self, name: str, inp: Input, collision: Collisions, timer: Timer,
    display: Display, manager: ScreenManager):
        self.__name = name
        self.__input = inp
        self.__collision = collision
        self.__timer = timer
        self.__display = display
        self.__running = False
        self.__manager = manager
    
    def setup(self):
        '''*Abstract Function*\n
        Esta função será executada quando a tela aparecer. Será a primeira função a ser
        executada na tela. Nela, serão ditos quais objetos aparecerão na tela, seus
        Listeners de input, Timers, e quais objetos podem colidir'''
        pass

    def leave(self):
        '''*Abstract Function*\n
        Esta função será executada antes da tela desaparecer. Será a ultima função a ser
        executada na tela. Nela, será desfeito tudo o que a função setup() fez. Depois,
        chamará o seu método stopRunning() para parar a sua execução. Por fim, ela pode
        chamar a método changeScreen(name) de seu manager para mudar de tela, ou chamar a
        método quit() também do seu manager para fechar o jogo'''
        pass

    def getName(self) -> str:
        return self.__name
    
    def stop_running(self):
        '''Esta função faz a parar de reagir'''
        self.__running = False
    

    def __mainloop__(self):
        '''Este método implementa o loop principal de cada tela
        **Esta função faz parte do sistema e não deve ser chamada**
        '''
        self.__running = True
        
        while self.__running:
            # Inputs
            self.__input.__listen_keyboard__()
            # Colisões
            self.__collision.__sprites__()
            self.__collision.__groups__()
            self.__collision.__sprite_groups__()
            # Timer
            self.__timer.__update__()
            # Update Display
            self.__display.__drawAll__()
            self.__display.__update__()