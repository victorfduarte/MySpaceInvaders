'''
Este é o módulo do GameSystem que trabalha as colisões entre objetos
'''

from Interfaces.collision_interface import CollisionInterface

class Collisions:
    '''Classe para fazer funcionar os tempos do jogo. Cria um objeto para ser único em
    todo o jogo. Possui as seguintes funções:\n
    add_object(obj: CollisionInterface) -> None: Adiciona o objeto à lista de objetos que
    podem se colidir\n
    remove_object(obj: CollisionInterface) -> None: Remove o objeto da lista de objetos
    que podem se colidir\n
    '''
    def __init__(self):
        self.__objects: list[CollisionInterface] = []


    def add_object(self, obj: CollisionInterface):
        for content in obj.get_collision_content():
            if content not in self.__objects:
                self.__objects.append(content)
    
    def remove_object(self, obj: CollisionInterface):
        for content in obj.get_collision_content():
            if content in self.__objects:
                self.__objects.remove(content)


    def __check__(self):
        '''Verifica se há colisão entre os objetos cadastrados\n
        Se houver, chama a função on_collision() de cada um\n
        **Esta função faz parte do sistema e não deve ser chamada**
        '''
        for idx1 in range(len(self.__objects)):
            for idx2 in range(idx1+1, len(self.__objects)):
                if self.__collison__(self.__objects[idx1], self.__objects[idx2]):
                    self.__objects[idx1].on_collision(self.__objects[idx2])
                    self.__objects[idx2].on_collision(self.__objects[idx1])


    def __collison__(self, obj1: CollisionInterface, obj2: CollisionInterface) -> bool:
        '''Verifica se dois objetos estão se colidindo\n
        **Esta função faz parte do sistema e não deve ser chamada**
        '''
        (x1, y1) = obj1.get_position()
        (w1, h1) = obj1.get_dimension()
        (x2, y2) = obj2.get_position()
        (w2, h2) = obj2.get_dimension()

        if self.__axes_collision__(x1, w1, x2, w2):
            return self.__axes_collision__(y1, h1, y2, h2)
        return False

    def __axes_collision__(self, pt1: int, d1: int, pt2: int, d2: int) -> bool:
        '''Verifica colisão em uma única dimensão\n
        **Esta função faz parte do sistema e não deve ser chamada**
        '''
        if pt1 < d2:
            if pt2 < (pt1 + d1):
                return True
            return False

        elif pt1 < (pt2 + d2):
            return True
