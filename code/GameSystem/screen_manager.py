from ..Screens.screen import Screen

class ScreenManager:
    '''Classe para fazer funcionar as telas do jogo. Cria um objeto para ser único em
    todo o jogo. Possui as seguintes funções:\n
    setScreen(name: str) -> None: Seta qual a tela atual do jogo\n    
    quit() -> None: Fecha o jogo\n
    add_screen(screen: Screen) -> None: Adiciona uma nova tela ao jogo\n
    remove_screen(screen: Screen) -> None: Remove a tela do jogo
    '''

    def __init__(self):
        self.__screens: list [Screen] = []
        self.__screen_name: str = ''
        self.__on = True
    

    def setScreen(self, name: str):
        '''Seta qual a tela atual do jogo'''
        self.__screen_name = name
    
    def quit(self):
        '''Fecha o jogo'''
        self.__on = False
    

    def add_screen(self, screen: Screen):
        self.__screens.append(screen)
    
    def remove_screen(self, screen: Screen):
        self.__screens.remove(screen)
    

    def __main__(self):
        while self.__on:
            for screen in self.__screens:
                if screen.getName() == self.__screen_name:
                    screen.__mainloop__()
                    break