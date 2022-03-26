import pygame
import pygame.time


class Timer:
    '''Classe para fazer funcionar os tempos do jogo. Cria um objeto para ser único em
    todo o jogo. Possui as seguintes funções:\n
    add_clock(func: function, time: int) -> None: Recebe uma função e a chama sempre
    que se passar o tempo em time\n
    add_clock_once(func: function, time: int) -> None: Recebe uma função e a chama
    uma vez depois de se passar o tempo em time\n
    add_everytime_clock(func: function) -> None: Recebe uma função e a chama a todo
    momento\n
    remove_clock(func: function) -> None: Desfaz a ligação de func com o tempo\n
    '''

    def __init__(self):
        self.__objs_update: FunctionList = FunctionList()
        self.__clocks_once: dict[Clock, FunctionList] = {}
        self.__clocks: dict[Clock, FunctionList] = {}
    

    def add_clock(self, time: int, *func: 'function'):
        '''Chama a(s) função(s) a cada time ms'''
        clock = Clock(time)
        if clock not in self.__clocks.keys():
            self.__clocks[clock] = FunctionList(*func)
        else:
            self.__clocks[clock].add_function(*func)
    
    def add_clock_once(self, time: int, *func: 'function'):
        clock = Clock(time)
        if clock not in self.__clocks_once.keys():
            self.__clocks_once[clock] = FunctionList(*func)
        else:
            self.__clocks_once[clock].add_function(*func)

    def add_everytime_clock(self, *func: 'function'):
        '''Chama a função a todo o momento'''
        self.__objs_update.add_function(*func)
    
    def remove_clock(self, *func: 'function'):
        '''Remove a função da lista'''
        self.__objs_update.remove_function(*func)

        for funcs in self.__clocks.values():
            funcs.remove_function(*func)
        
        for funcs in self.__clocks_once.values():
            funcs.remove_function(*func)
    

    def __update__(self, delta: float):
        '''Chama as funções que devem ser chamadas a todo momento e as funções que são
        executadas de tempos em tempos\n
        **Esta função faz parte do sistema e não deve ser chamada***'''

        for func in self.__objs_update.getFuncs():
            func(delta)
        
        for clock, funcs in self.__clocks.items():
            if clock.check(delta):
                for func in funcs.getFuncs():
                    func(delta)

        clocks: list[Clock] = []
        for clock, funcs in self.__clocks_once.items():
            if clock.check(delta):
                clocks.append(clock)
                for func in funcs.getFuncs():
                    func(delta)
        
        for clock in clocks:
            self.__clocks_once.pop(clock)



class Clock:
    def __init__(self, time: int):
        self.__time = time
        self.__ref_time = 0
    

    def check(self, delta: float) -> bool:
        '''Checa quanto tempo já se passou e retorna True se for igual à propriedade
        time
        '''
        now = self.__ref_time + delta * 1000
        self.set_ref(now)

        if now >= self.__time:
            self.set_ref(0)
            return True
        return False

    def set_ref(self, time=0):
        '''Reseta o tempo de referência'''
        self.__ref_time = time

    def getTime(self) -> int:
        return self.__time



class FunctionList:
    def __init__(self, *func: 'function'):
        self.__funcs: list[function] = list(func)

    def add_function(self, *func: 'function'):
        for f in func:
            if f not in self.__funcs:
                self.__funcs.append(f)

    def remove_function(self, *func: 'function'):
        for f in func:
            if f in self.__funcs:
                self.__funcs.remove(f)

    def getFuncs(self) -> 'list[function]':
        return self.__funcs