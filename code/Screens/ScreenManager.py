from Screen import Screen

class ScreenManager:
    '''Esta classe gerenciará as várias telas do jogo'''
    def __init__(self):
        self.__screens: list [Screen] = []
        self.__screen_name: str = ''
    
    def changeScreen(self, name: str):
        self.__screen_name = name
    
    def main(self):
        while True:
            for screen in self.__screens:
                if screen.getName() == self.__screen_name:
                    screen.setup()
                    screen.mainloop()
                    break