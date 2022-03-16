from Interfaces.screen_interface import ScreenInterface

class ScreenManager:
    '''Classe para fazer funcionar as telas do jogo. Cria um objeto para ser único em
    todo o jogo. Possui as seguintes funções:\n
    setScreen(name: str) -> None: Seta qual a tela atual do jogo\n    
    quit() -> None: Fecha o jogo\n
    add_screen(screen: Screen) -> None: Adiciona uma nova tela ao jogo\n
    remove_screen(screen: Screen) -> None: Remove a tela do jogo
    '''

    def __init__(self, parent):
        self.parent = parent
        self.__screens: list [ScreenInterface] = []
        self.__screen_name: str = ''
        self.__current_screen: ScreenInterface = None
        self.__on = True    

    def setScreen(self, name: str):
        '''Seta qual a tela atual do jogo'''
        self.__current_screen.leave()
        self.__screen_name = name
        self.__current_screen.__stop_running__()

        for screen in self.__screens:
            if screen.getName() == self.__screen_name:
                self.__current_screen = screen
                break
        else:
            self.quit()

    
    def quit(self):
        '''Fecha o jogo'''
        self.__current_screen.__stop_running__()
        self.__on = False
        self.__current_screen.leave()
    

    def add_screen(self, screen: ScreenInterface):
        self.__screens.append(screen)
    
    def remove_screen(self, screen: ScreenInterface):
        self.__screens.remove(screen)
    

    def __main__(self, first_screen = 'menu'):
        '''Verifica qual a tela atual e chama o seu mainloop\n
        **Esta função faz parte do sistema e não deve ser chamada**
        '''
        self.__screen_name = first_screen

        for screen in self.__screens:
            if screen.getName() == self.__screen_name:
                self.__current_screen = screen
                break
        else:
            return

        while self.__on:
            self.__current_screen.__mainloop__()