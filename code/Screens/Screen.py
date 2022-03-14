class Screen:
    '''Abstract Class\n
    Todas as telas do jogo herdaram dessa classe. Cada tela implementará o seu próprio
    setup() e on_exit()'''
    
    def __init__(self, name: str, inp, collision, timer, display, manager):
        self.__name = name
        self.__input = inp
        self.__collision = collision
        self.__timer = timer
        self.__display = display
        self.__running = False
        self.__manager = manager
    
    def setup(self):
        '''Abstract Function\n
        Esta função será executada quando a tela aparecer. Será a primeira função a ser
        executada na tela'''
        pass

    def leave(self):
        '''Abstract Fucntion\n
        Esta função será executada antes da tela desaparecer. Será a ultima função a ser
        executada na tela, com o propósito de deixar a tela em um estado nulo'''
        pass
    
    def mainloop(self):
        '''Este método implementa o loop principal de cada tela.'''
        self.__running = True
        
        while self.__running:
            # Inputs
            self.__input.loop()
            # Colisões
            self.__collision.loop()
            # Timer
            self.__timer.loop()
            # Update Display
            self.__display.loop()


    def getName(self) -> str:
        return self.__name
    
    def setRunning(self, state: bool):
        self.__running = state