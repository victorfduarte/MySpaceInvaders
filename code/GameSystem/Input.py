'''
Este é um módulo do GameSystem que trabalha os inputs
'''

import pygame


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
        self.__keyboard: dict[tuple[int], list] = {}
    

    def add_keyboard_listener(self, func: None, k_event: int, code: int = ANY):
        '''Chama func quando ocorrer o evento k_event com a chave code. Se code for ANY,
        então chama func sempre que ocorrer o evento k_event'''
        if (k_event, code) in self.__keyboard:
            if func not in self.__keyboard[(k_event, code)]:
                self.__keyboard[(k_event, code)].append(func)
        else:
            self.__keyboard[(k_event, code)] = [func]
    
    def remove_keyboard_listener(self, func: None, k_event: int, code: int = ANY):
        '''Remove a ligação entre func para com o par k_event e code'''
        if (k_event, code) in self.__keyboard:
            if func in self.__keyboard[(k_event, code)]:
                if len(self.__keyboard[(k_event, code)]) == 1:
                    del self.__keyboard[(k_event, code)]
                else:
                    self.__keyboard[(k_event, code)].remove(func)


    def __listen_keyboard__(self):
        '''Esta função verifica todos os inputs de teclado e chama as funções listadas
        correspondentes\n
        **Esta função faz parte do sistema e não deve ser chamada***'''
        for event in pygame.event.get():
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

