import pygame
import pygame.image
from Interfaces.collision_interface import CollisionInterface
from Interfaces.draw_interface import DrawInterface


class MySprite(DrawInterface, CollisionInterface):
    def __init__(self, name: str, image_path: str):
        self.name = name
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.__image_scale = [0, 0]
    

    def get_draw_content(self) -> 'list[DrawInterface]':
        '''Retorna a sua lista dos objetos a serem desenhados na tela\n
        MySprite é um objeto simples, então retorna uma lista consigo mesmo
        '''
        return [self]
    
    def get_collision_content(self) -> 'list[CollisionInterface]':
        '''Retorna o conteúdo para verificar a colisão\n
        MySprite é um objeto simples, então retorna uma lista consigo mesmo
        '''
        return [self]
    

    # Getters
    def get_image(self) -> pygame.Surface:
        return self.image  

    def get_position(self) -> 'tuple[int, int]':
        return (self.rect.x, self.rect.y)

    def get_dimension(self) -> 'tuple[int, int]':
        return (self.rect.width, self.rect.height)

    def get_img_scale(self) -> list:
        return self.__image_scale
    
    
    # Setters
    def set_image(self, img: pygame.Surface):
        self.image = img

    def set_position(self, pos: 'tuple[int, int]'):
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def get_dimension(self, dim: 'tuple[int, int]'):
        self.rect.width = dim[0]
        self.rect.height = dim[1]

    def set_img_scale(self, img_scale):
        self.__image_scale = img_scale
