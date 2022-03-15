import pygame
import pygame.image
from pygame.sprite import Sprite
from sprite_interface import SpriteInterface

class MySprite(Sprite, SpriteInterface):
    def __init__(self, name, image_path: str):
        super().__init__()
        self.name = name
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.__image_scale = [0, 0]
    
    def setup(self, position: 'list[int]', dimention: 'list[int]', img_scale: int):
        self.rect.x = position[0]
        self.rect.y = position[1]
        self.rect.width = dimention[0]
        self.rect.height = dimention[1]
        self.__image_scale = img_scale
    

    # Getters
    def getImage(self) -> pygame.Surface:
        return self.image  

    def getPos(self) -> 'tuple[int]':
        return (self.rect.x, self.rect.y)

    def getDim(self) -> 'tuple[int]':
        return (self.rect.width, self.rect.height)

    def getImgScale(self) -> list:
        return self.__image_scale
    
    
    # Setters
    def setImage(self, img_path: str):
        self.image = pygame.image.load(img_path)

    def setPos(self, pos: 'tuple[int, int]'):
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def setDim(self, dim: 'tuple[int, int]'):
        self.rect.width = dim[0]
        self.rect.height = dim[1]

    def stImgScale(self, img_scale):
        self.__image_scale = img_scale
