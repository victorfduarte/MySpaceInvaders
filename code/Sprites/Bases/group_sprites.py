import pygame
import pygame.image
from .sprite import MySprite
from Interfaces.draw_interface import DrawInterface
from Interfaces.collision_interface import CollisionInterface


class MyGroupSprites(DrawInterface, CollisionInterface):
    def __init__(self):
        super().__init__()
        self.__sprites: list [MySprite] = []
    

    def add(self, *sprites: MySprite):
        for sprite in sprites:
            self.__sprites.append(sprite)
    
    def remove(self, *sprites: MySprite):
        for sprite in sprites:
            self.__sprites.remove(sprite)


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

