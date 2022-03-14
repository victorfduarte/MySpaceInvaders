'''
Este é o módulo do GameSystem que trabalha as colisões entre objetos
'''


from tokenize import group


class Collisions:
    def __init__(self, pg):
        self.__pg = pg  # Uma referência para o framework Pygame
    

    def sprites(self, sprites: list):
        '''Recebe uma lista de Sprites e verifica se há colisão entre eles\n
        Se houver, chama a função on_collision() de cada um'''
        for idx1 in range(len(sprites)):
            for idx2 in range(idx1+1, len(sprites)):
                if self.collison(sprites[idx1], sprites[idx2]):
                    sprites[idx1].on_collision(sprites[idx2])
                    sprites[idx2].on_collision(sprites[idx1])
        pass


    def groups(self, groups: list):
        '''Recebe uma lista de Grupos de Sprite e vefifica se há colisão
        entre os itens dos grupos\n
        Se houver, chama a função on_collision() de cada Sprite e do Grupo'''
        for idx1 in range(len(groups)):
            for idx2 in range(idx1+1, len(groups)):
                gp_collision = False
                for sprite1 in groups[idx1].getChildren():
                    for sprite2 in groups[idx2].getChildren():
                        if self.collison(sprite1, sprite2):
                            sprite1.on_collision(sprite2)
                            sprite2.on_collision(sprite1)
                            gp_collision = True
                if gp_collision:
                    groups[idx1].on_collision(groups[idx2])
                    groups[idx2].on_collision(groups[idx1])




    def sprite_groups(self, sprites: list, groups: list):
        '''Recebe uma lista de Sprites e uma de Grupos e verifica se há colisão entre
        Sprites com Grupos de Sprites\n'''
        pass


    def collison(self, obj1, obj2) -> bool:
        if self.axes_collision(obj1.x, obj1.width, obj2.x, obj2.width):
            return self.axes_collision(obj1.y, obj1.height, obj2.y, obj2.height)
        return False
    

    def axes_collision(self, point1, dist1, point2, dist2) -> bool:
        if point1 < point2:
            if point2 < (point1 + dist1):
                return True
            return False

        elif point1 < (point2 + dist2):
            return True
