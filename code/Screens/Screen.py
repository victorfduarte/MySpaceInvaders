from ..GameSystem import GSystem

class Screen:
    '''Abstract Class\n
    Todas as telas do jogo herdaram dessa classe. Cada tela implementará as seguintes
    funções abstratas:\n
        setup() -> None\n
        leave() -> None\n
    Possui também as seguintes funções:\n
        get_name() -> str\n
        stop_running() -> None'''
    
    def __init__(self, name: str, game_system: GSystem):
        self.__name = name
        self.__game_system = game_system
        self.__running = False
    
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
        chamará o seu método stop_running() para parar a sua execução. Por fim, ela pode
        chamar a método setScreen(name) de seu manager para mudar de tela, ou chamar a
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

        self.setup()

        self.__running = True
        
        while self.__running:
            # Inputs
            self.__game_system.INPUT.__listen__()
            # Colisões
            self.__game_system.COLLISIONS.__sprites__()
            self.__game_system.COLLISIONS.__groups__()
            self.__game_system.COLLISIONS.__sprite_groups__()
            # Timer
            self.__game_system.TIMER.__update__()
            # Update Display
            self.__game_system.DISPLAY.__drawAll__()
            self.__game_system.DISPLAY.__update__()