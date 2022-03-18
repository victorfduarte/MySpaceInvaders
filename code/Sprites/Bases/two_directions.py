from GameSystem import gSystem
import pygame as pg
from Interfaces.sprite_behavior_interface import SpriteBehaviorInterface
from Interfaces.sprite_interface import SpriteInterface


class TwoDirection(SpriteBehaviorInterface):
    def __init__(self, parent: SpriteInterface, speed: int, axel = 'x'):
        '''Recebe a velocidade, em px/s, o eixo, (X ou Y), e se deve rotacionar a
        imagem ou não 
        '''
        self.__name = 'TwoDirections'
        self.__parent = parent
        self.__axel = axel
        self.__speed = speed
        self.__x, self.__y = parent.get_position()

        # Constantes que definem direção
        self.RIGHT = 2
        self.LEFT = 4
        self.UP = 1
        self.DOWN = 3
        self.STOPED = 0

        # Teclas de Direção
        self.__right_key = pg.K_RIGHT
        self.__left_key = pg.K_LEFT
        self.__up_key = pg.K_UP
        self.__down_key = pg.K_DOWN

        # Define qual a direção atual do personagem em x e y, ou e está parado
        self.__direction = self.STOPED

        if self.__axel == 'x':
            gSystem.INPUT.add_keyboard_listener(self.__move_right__,
                                                pg.KEYDOWN, self.__right_key)
            gSystem.INPUT.add_keyboard_listener(self.__move_left__,
                                                pg.KEYDOWN, self.__left_key)

            gSystem.INPUT.add_keyboard_listener(self.__stop_move__,
                                                pg.KEYUP, self.__right_key)
            gSystem.INPUT.add_keyboard_listener(self.__stop_move__,
                                                pg.KEYUP, self.__left_key)
        
        elif self.__axel == 'y':
            gSystem.INPUT.add_keyboard_listener(self.__move_up__,
                                                pg.KEYDOWN, self.__up_key)
            gSystem.INPUT.add_keyboard_listener(self.__move_down__,
                                                pg.KEYDOWN, self.__down_key)

            gSystem.INPUT.add_keyboard_listener(self.__stop_move__,
                                                pg.KEYUP, self.__up_key)
            gSystem.INPUT.add_keyboard_listener(self.__stop_move__,
                                                pg.KEYUP, self.__down_key)
    
    
    def get_name(self) -> str:
        return self.__name
    

    def kill(self) -> None:
        if self.__axel == 'x':
            gSystem.INPUT.remove_keyboard_listener(self.__move_right__,
                                                pg.KEYDOWN, self.__right_key)
            gSystem.INPUT.remove_keyboard_listener(self.__move_left__,
                                                pg.KEYDOWN, self.__left_key)

            gSystem.INPUT.remove_keyboard_listener(self.__stop_move__,
                                                pg.KEYUP, self.__right_key)
            gSystem.INPUT.remove_keyboard_listener(self.__stop_move__,
                                                pg.KEYUP, self.__left_key)
        
        elif self.__axel == 'y':
            gSystem.INPUT.remove_keyboard_listener(self.__move_up__,
                                                pg.KEYDOWN, self.__up_key)
            gSystem.INPUT.remove_keyboard_listener(self.__move_down__,
                                                pg.KEYDOWN, self.__down_key)

            gSystem.INPUT.remove_keyboard_listener(self.__stop_move__,
                                                pg.KEYUP, self.__up_key)
            gSystem.INPUT.remove_keyboard_listener(self.__stop_move__,
                                                pg.KEYUP, self.__down_key)
    

    def __move__(self, delta):
        deslocamento = self.__speed * delta

        if self.__direction == self.RIGHT:
            self.__x += deslocamento
            self.__parent.set_position((self.__x, self.__y))

        elif self.__direction == self.LEFT:
            self.__x -= deslocamento
            self.__parent.set_position((self.__x, self.__y))

        elif self.__direction == self.UP:
            self.__y -= deslocamento
            self.__parent.set_position((self.__x, self.__y))

        elif self.__direction == self.DOWN:
            self.__y += deslocamento
            self.__parent.set_position((self.__x, self.__y))


    def __move_right__(self):
        self.__direction = self.RIGHT
        self.__x, self.__y = self.__parent.get_position()
        gSystem.TIMER.add_everytime_clock(self.__move__)

    def __move_left__(self):
        self.__direction = self.LEFT
        self.__x, self.__y = self.__parent.get_position()
        gSystem.TIMER.add_everytime_clock(self.__move__)

    def __move_up__(self):
        self.__direction = self.UP
        self.__x, self.__y = self.__parent.get_position()
        gSystem.TIMER.add_everytime_clock(self.__move__)

    def __move_down__(self):
        self.__direction = self.DOWN
        self.__x, self.__y = self.__parent.get_position()
        gSystem.TIMER.add_everytime_clock(self.__move__)

    def __stop_move__(self):
        self.__direction = self.STOPED
        gSystem.TIMER.remove_clock(self.__move__)