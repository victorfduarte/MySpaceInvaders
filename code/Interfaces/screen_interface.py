class ScreenInterface():
    '''Interface\n
    Um Interface que todas as telas do jogo devem seguir. Define os seguintes métodos
    abstratas:\n
        __main__() -> None\n
        setup() -> None\n
        leave() -> None\n
        get_name() -> str\n
        stop_running() -> None'''


    def setup(self):
        '''*Abstract Function*\n
        Esta função será executada quando a tela aparecer. Será a primeira função a ser
        executada na tela. Nela, serão ditos quais objetos aparecerão na tela, seus
        Listeners de input, Timers, e quais objetos podem colidir'''
        pass

    def leave(self):
        '''*Abstract Function*\n
        Este método será executada antes da tela desaparecer. Será o ultimo a ser
        executada na tela. Nele, será desfeito tudo o que o método setup() fez. Depois,
        chamará o seu método stop_running() para parar a sua execução. Por fim, ele pode
        chamar a método setScreen(name) de seu manager para mudar de tela, ou chamar a
        método quit() também do seu manager para fechar o jogo'''
        pass


    def getName(self) -> str:
        '''*Abstract Function*\n
        Retorna o nome da tela'''
        pass
    
    def __stop_running__(self):
        '''*Abstract Function*\n
        Este método faz tela a parar de reagir'''
        pass
    

    def __mainloop__(self):
        '''*Abstract Function*\n
        Este método implementa o loop principal de cada tela\n
        **Esta função faz parte do sistema e não deve ser chamada**
        '''
        pass