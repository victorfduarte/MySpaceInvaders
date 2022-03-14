'''
Este é um módulo do GameSystem que trabalha os inputs
'''


class Input:
    ANY = 0

    def __init__(self, pg):
        self.__pg = pg  # Uma referência para o framework Pygame
        self.__keyboard = {}


    def listen_keyboard(self):
        '''Esta função verifica todos os inputs de teclado e chama as funções listadas
        correspondentes'''
        for event in self.__pg.event.get():
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
    

    def add_keyboard_listener(self, func: None, k_event: int, code: int = ANY):
        if (k_event, code) in self.__keyboard:
            if func not in self.__keyboard[(k_event, code)]:
                self.__keyboard[(k_event, code)].append(func)
        else:
            self.__keyboard[(k_event, code)] = [func]
    
    
    def remove_keyboard_listener(self, func: None, k_event: int, code: int = ANY):
        if (k_event, code) in self.__keyboard:
            if func in self.__keyboard[(k_event, code)]:
                if len(self.__keyboard[(k_event, code)]) == 1:
                    del self.__keyboard[(k_event, code)]
                else:
                    self.__keyboard[(k_event, code)].remove(func)

