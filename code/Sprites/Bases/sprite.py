from GameSystem import gSystem
import pygame.image
import pygame.transform
from pygame import Surface
from Interfaces.collision_interface import CollisionInterface
from Interfaces.draw_interface import DrawInterface
from Interfaces.sprite_interface import SpriteInterface
from Interfaces.sprite_behavior_interface import SpriteBehaviorInterface


class MySprite(SpriteInterface):
    def __init__(self, name: str, image_path: str):
        self.__name = name

        self.__behaviors: list[SpriteBehaviorInterface] = []
        self.__draw_content: list[DrawInterface] = [self]
        self.__collision_content: list[CollisionInterface] = [self]

        self.__image_base = pygame.image.load(image_path)
        self.__image = self.__image_base
        self.__rect = self.__image.get_rect()
        self.__image_scale = [0, 0]
        self.__angle = 0

        gSystem.DISPLAY.add_object(self)
        gSystem.COLLISIONS.add_object(self)
    

    def on_collision(self, obj: 'CollisionInterface', *args) -> None:
        '''*Abstract Function*\n
        Método que é chamado toda vez que o objeto se colide. Recebe como argumento o
        objeto com o qual a colisão ocorreu
        '''
        pass

    def move(self, pos: 'tuple[int, int]', *args) -> None:
        '''Move o objeto para a posição especificada. Pode implementar verificações que
        permitam ou não a movimentação. Vem com uma implementação padrão que somente
        chama o método set_position(pos), porém pode ser reimplementado'''
        self.set_position(pos)
    

    # Sprite Interface
    def kill(self, *args):
        '''Método a ser executado para destruir um Sprite'''
        gSystem.DISPLAY.remove_object(self)
        gSystem.COLLISIONS.remove_object(self)
        for behavior in self.__behaviors:
            behavior.kill()

    def add_behavior(self, behavior: SpriteBehaviorInterface) -> None:
        '''Adiciona um comportamento ao Sprite'''
        if behavior not in self.__behaviors:
            self.__behaviors.append(behavior)

    def remove_behavior(self, name: str) -> None:
        '''Remove um comportamento do Sprite, com base no nome'''
        for behavior in self.__behaviors:
            if behavior.get_name() == name:
                behavior.kill()
                self.__behaviors.remove(behavior)


    # Draw (Getter, Setter)
    def get_draw_content(self) -> 'list[DrawInterface]':
        '''Retorna a sua lista dos objetos a serem desenhados na tela\n
        Caso o objeto seja simples, retorna uma lista contendo ele mesmo. Caso o objeto
        seja um grupo de outros objetos, deve chamar este mesmo método de todos os seus
        componentes e juntar os resultados todos em uma única lista
        '''
        return self.__draw_content

    def set_draw_content(self, content: 'list[DrawInterface]'):
        '''Seta a sua lista dos objetos a serem desenhados na tela\n
        '''
        self.__draw_content = content


    # Collision (Getter, Setter)
    def get_collision_content(self) -> 'list[CollisionInterface]':
        '''Retorna o conteúdo para verificar a colisão\n
        Caso o objeto seja simples, retorna uma lista contendo ele mesmo. Caso o objeto
        seja um grupo de outros objetos, deve chamar este mesmo método de todos os seus
        componentes e juntar os resultados todos em uma única lista
        '''
        return self.__collision_content

    def set_collision_content(self, content: 'list[CollisionInterface]') -> None:
        '''Seta o conteúdo para verificar a colisão\n
        '''
        self.__collision_content = content
        

    # Getters
    def get_name(self):
        '''Retorna qual o nome do objeto'''
        return self.__name

    def get_position(self) -> 'tuple[float, float]':
        '''Retorna a posição X, Y do objeto
        '''
        return (self.__rect.x, self.__rect.y)

    def get_dimension(self) -> 'tuple[int, int]':
        '''Retorna a largura e a altura do objeto
        '''
        return (self.__rect.width, self.__rect.height)

    def get_image(self) -> Surface:
        '''Retorna o conteúdo do objeto a ser desenhado na tela
        '''
        return self.__image_base
    
    def get_angle(self):
        '''Retorna o ângulo do objeto emg graus'''
        return self.__angle


    # Setters
    def set_position(self, pos: 'tuple[int, int]') -> None:
        '''Seta a posição X, Y do objeto
        '''
        self.__rect.x, self.__rect.y = pos
    
    def set_dimension(self, dimension: 'tuple[int, int]') -> None:
        '''Seta o a largura e a altura do objeto
        '''
        self.__rect.width, self.__rect.height = dimension

    def set_image(self, img: Surface) -> None:
        '''Seta o conteúdo do objeto a ser desenhado na tela
        '''
        self.__image = pygame.transform.rotate(self.__image_base, self.__angle)
    
    def set_angle(self, angle: int):
        '''Seta o ângulo do objeto em graus'''
        self.__angle = angle
        self.__image = pygame.transform.rotate(self.__image_base, angle)

