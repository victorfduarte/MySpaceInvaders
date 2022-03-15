'''
Este é um módulo do GameSystem que trabalha os inputs
'''

import pygame
import pygame.event

class Input:
    '''Classe para fazer funcionar os inputs do jogo. Cria um objeto para ser único em
    todo o jogo. Possui as seguintes funções:\n
    add_keyboard_listener(func: function, k_event: int, code: int = ANY) -> None: Recebe
    uma função e a chama sempre que ocorrer a combinação k_event e code\n
    remove_keyboard_listener(func: function, k_event: int, code: int = ANY) -> None:
    Desfaz a conexão entre a função e a combinação k_event e code\n
    '''
    ANY = 0

    def __init__(self):
        self.__keyboard: dict[tuple[int], list[function]] = {}
        self.__quit: list[function] = []
    

    def add_keyboard_listener(self, func: function, k_event: int, code: int = ANY):
        '''Chama func quando ocorrer o evento k_event com a chave code. Se code for ANY,
        então chama func sempre que ocorrer o evento k_event'''
        if (k_event, code) in self.__keyboard:
            if func not in self.__keyboard[(k_event, code)]:
                self.__keyboard[(k_event, code)].append(func)
        else:
            self.__keyboard[(k_event, code)] = [func]
    
    def remove_keyboard_listener(self, func: function, k_event: int, code: int = ANY):
        '''Remove a ligação entre func para com o par k_event e code\n
        Se a ligação não existir, não faz nada'''
        if (k_event, code) in self.__keyboard:
            if func in self.__keyboard[(k_event, code)]:
                if len(self.__keyboard[(k_event, code)]) == 1:
                    del self.__keyboard[(k_event, code)]
                else:
                    self.__keyboard[(k_event, code)].remove(func)
    

    def add_quit_listener(self, func: function):
        '''Chama func quando ocorrer o evento QUIT'''
        if func not in self.__quit:
            self.__quit.append(func)
    
    def remove_quit_listener(self, func: None):
        '''Remove a ligação entre func para com o evento QUIT\n
        Se a ligação não existir, não faz nada'''
        if func in self.__quit:
            self.__quit.remove(func)
    

    def __listen__(self):
        '''Esta função verifica todos os inputs e chama as funções listadas
        correspondentes\n
        **Esta função faz parte do sistema e não deve ser chamada***
        '''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.__notify_quit__()

            elif event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                self.__notify_keyboard__(event)

    def __notify_keyboard__(self, event: pygame.event.Event):
        '''Esta função verifica todos os inputs de teclado e chama as funções listadas
        correspondentes\n
        **Esta função faz parte do sistema e não deve ser chamada***
        '''
        for ktype, kcode in self.__keyboard.keys():
            if event.type == ktype:
                if kcode == self.ANY:
                    # Notifying
                    for func in self.__keyboard[(ktype, kcode)]:
                        func()
                
                elif kcode == event.key:
                    # Notifying
                    for func in self.__keyboard[(ktype, kcode)]:
                        func()
                    return
    
    def __notify_quit__(self):
        '''Esta função verifica o input de QUIT e chama as funções listadas
        correspondentes\n
        **Esta função faz parte do sistema e não deve ser chamada***
        '''
        for func in self.__quit:
            func()

