from screen import Screen

class ScreenManager:
    '''Esta classe gerenciará as várias telas do jogo'''

    def __init__(self):
        self.__screens: list [Screen] = []
        self.__screen_name: str = ''
        self.__on = True
    

    def changeScreen(self, name: str):
        self.__screen_name = name
    
    def quit(self):
        self.__on = False
    

    def addScreen(self, screen: Screen):
        self.__screens.append(screen)
    
    def removeScreen(self, screen: Screen):
        self.__screens.remove(screen)
    

    def __main__(self):
        while self.__on:
            for screen in self.__screens:
                if screen.getName() == self.__screen_name:
                    screen.setup()
                    screen.__mainloop__()
                    break