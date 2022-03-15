import pygame
import pygame.image
from pygame.sprite import Group
from sprite import MySprite


class MyGroupSprites(Group):
    def __init__(self):
        super().__init__()
        self.__sprites: list [MySprite] = []
    
    def add(self, *sprites: MySprite):
        for sprite in sprites:
            self.__sprites.append(sprite)
    
    def remove(self, *sprites: MySprite):
        for sprite in sprites:
            self.__sprites.remove(sprite)
    
    def sprites(self) -> 'list[MySprite]':
        return self.__sprites

    def on_collision(self, obj):
        '''Abstract Function\n
        Recebe o objeto com o qual está tocando e executa qualquer ação
        '''
        pass

