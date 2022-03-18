import pygame
import pygame.image
from .sprite import MySprite
from Interfaces.draw_interface import DrawInterface
from Interfaces.collision_interface import CollisionInterface
from Interfaces.sprite_interface import SpriteInterface


class MyGroupSprites(SpriteInterface):
    def __init__(self):
        super().__init__()
        self.__sprites: list [MySprite] = []
        self.__rect = pygame.Rect(0, 0, 0, 0)
    

    def add(self, *sprites: MySprite):
        for sprite in sprites:
            if sprite not in self.__sprites:
                self.__sprites.append(sprite)
                
        x, y, *dim = self.__calculate_rect__()
        self.set_position((x, y))
        self.set_dimension(dim)
    
    def remove(self, *sprites: MySprite):
        for sprite in sprites:
            if sprite not in self.__sprites:
                self.__sprites.remove(sprite)

        x, y, *dim = self.__calculate_rect__()
        self.set_position((x, y))
        self.set_dimension(dim)
    

    def __calculate_rect__(self) -> 'tuple[int, int, int, int]':
        '''Calcula X, Y, Width e Height do grupo'''
        x, y = self.__sprites[0].get_position()
        width, height = self.__sprites[0].get_dimension()

        if len(self.__sprites):
            for sprite in self.__sprites:
                sx, sy = sprite.get_position()
                swidth, sheight = sprite.get_dimension()

                if sx < x:
                    x = sx
                if sy < y:
                    y = sy
                if sx + swidth > x + width:
                    width = sx + swidth - x
                if sy + sheight > y + height:
                    height = sy + sheight - y

            return (x, y, width, height)
        else:
            return (0, 0, 0, 0)



    def get_draw_content(self) -> 'list[DrawInterface]':
        '''Retorna a sua lista dos objetos a serem desenhados na tela\n
        MyGroupSpritse é um objeto composto, então retorna uma lista contento a junção
        dos retornos da função get_draw_content() de seus componentes
        '''
        children: list[DrawInterface] = []

        for item in self.__sprites:
            children.extend(item.get_draw_content())
        
        return children

    def get_collision_content(self) -> 'list[CollisionInterface]':
        '''Retorna o conteúdo para verificar a colisão\n
        MyGroupSpritse é um objeto composto, então retorna uma lista contento a junção
        dos retornos da função get_collision_content() de seus componentes
        '''
        children: list[CollisionInterface] = []

        for item in self.__sprites:
            children.extend(item.get_collision_content())
        
        return children

