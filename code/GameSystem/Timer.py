import pygame
import pygame.time


class Timer:
    '''Classe para fazer funcionar os tempos do jogo. Cria um objeto para ser único em
    todo o jogo. Possui as seguintes funções:\n
    add_clock(func: function, time: int) -> None: Recebe uma função e a chama sempre que
    se passar o tempo em time\n
    add_everytime_clock(func: function) -> None: Recebe uma função e a chama a todo
    momento\n
    remove_clock(func: function) -> None: Desfaz a ligação de func com o tempo\n
    '''

    def __init__(self):
        self.__objs_update: list[function] = []
        self.__clocks: dict[Clock, list[function]]= {}
        self.DELTA = pygame.time.get_ticks()
    

    def add_clock(self, time: int, func: 'function'):
        '''Chama a função a cada time ms'''
        for clock in self.__clocks.keys():
            if clock.getTime() == time:
                self.__clocks[clock].append(func)
                break
        else:
            clock = Clock(self.__pg, time)
            self.__clocks[clock] = [func]

    def add_everytime_clock(self, func: 'function'):
        '''Chama a função a todo o momento'''
        if func not in self.__objs_update:
            self.__objs_update.append(func)
    
    def remove_clock(self, func: 'function'):
        '''Remove a função da lista'''
        if func in self.__objs_update:
            self.__objs_update.remove(func)

        for funcs in self.__clocks.values():
            if func in funcs:
                funcs.remove(func)
    

    def __update__(self):
        '''Chama as funções que devem ser chamadas a todo momento e as funções que são
        executadas de tempos em tempos\n
        **Esta função faz parte do sistema e não deve ser chamada***'''
        self.DELTA = pygame.time.get_ticks() - self.DELTA

        for func in self.__objs_update:
            func(self.DELTA)
        
        for clock, funcs in self.__clocks.items():
            if clock.check():
                for func in funcs:
                    func(self.DELTA)


class Clock:
    def __init__(self, time):
        self.__time = time
        self.__ref_time = 0
    

    def reset(self, time=0):
        '''Reseta o tempo de referência'''
        if time:
            self.__ref_time = time
        else:
            self.__ref_time = pygame.time.get_ticks()
    
    def check(self) -> bool:
        '''Checa quanto tempo já se passou e retorna True se for igual à propriedade time'''
        now = pygame.time.get_ticks()
        if now - self.__ref_time >= self.__time:
            self.reset(now)
            return True
        return False
    

    def getTime(self) -> int:
        return self.__time

    def setTime(self, time: int):
        self.__time = time

