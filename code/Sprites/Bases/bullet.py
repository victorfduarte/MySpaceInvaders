from GameSystem import gSystem
from math import cos, sin, degrees, radians
from Interfaces.sprite_behavior_interface import SpriteBehaviorInterface
from Interfaces.sprite_interface import SpriteInterface


class Bullet(SpriteBehaviorInterface):
    def __init__(self, parent: SpriteInterface, speed: int, direction: int):
        '''Recebe o Sprite pai, a velocidade em px/s e a direção em graus'''
        self.__name = 'Bullet'
        self.__parent = parent
        self.__direction = direction
        self.__speed = speed

        self.__parent.set_angle(direction)

        self.__x, self.__y = parent.get_position()
        self.__width, self.__height = parent.get_dimension()
        self.__display_width = gSystem.DISPLAY.getWidth()
        self.__display_height = gSystem.DISPLAY.getHeight()

        self.__sin = sin(radians(direction))
        self.__cos = cos(radians(direction))

        gSystem.TIMER.add_everytime_clock(self.__move__)
    

    def kill(self) -> None:
        '''Desfaz o comportamento'''
        gSystem.TIMER.remove_clock(self.__move__)
        pass


    def __move__(self, delta):
        '''Atualiza a posição da bala\n
        Recebe um valor delta para fazer a correção do tempo
        '''
        self.__check_limits__()

        desy = - (self.__speed * self.__sin * delta)
        desx = self.__speed * self.__cos * delta

        self.__x += desx
        self.__y += desy
        self.__parent.move((self.__x, self.__y))


    def __check_limits__(self) -> bool:
        '''Verifica se a bala já saiu da tela\n
        Retorna True se ainda estiver dentro e False se não'''
        if self.__x > self.__display_width:
            self.__parent.kill()
        
        elif self.__x + self.__width <= 0:
            self.__parent.kill()

        elif self.__y > self.__display_height:
            self.__parent.kill()
        
        elif self.__y + self.__height <= 0:
            self.__parent.kill()


    # Getters
    def get_name(self) -> str:
        '''Retorna o nome do comportamento'''
        return self.__name

    def getDirection(self) -> int:
        return self.__direction

    def getSpeed(self) -> int:
        return self.__speed


    # Setters
    def setSpeed(self, speed: int):
        self.__speed = speed