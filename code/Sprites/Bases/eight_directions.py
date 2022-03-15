from ...GameSystem import gSystem
from sprite import MySprite
import pygame as pg

class EightDirection(MySprite):
    def __init__(self, speed, num_directions: int = 8, axel_opt = 'x',
    angle: bool = False):
        '''Recebe a velocidade, em px/ms, o número de direções, (2, 4, 8), o eixo,
        opcional (caso o número de direções seja 2, define se é no eixo X ou Y), e
        se deve rotacionar a imagem ou não 
        '''
        super().__init__()
        self.__directions = num_directions
        self.__axel_opt = axel_opt
        self.__angle = angle
        self.__speed: int = speed

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
        self.__direction = [self.STOPED, self.STOPED]

        if self.__directions == 2:
            self.__set_two_directions__()

        elif self.__directions == 4:
            self.__set_four_directions__()

        elif self.__directions == 8:
            self.__set_eight_directions__()

    
    def __set_two_directions__(self):
        if self.__axel_opt == 'x':
            gSystem.INPUT.add_keyboard_listener(self.__move_right__,
                                                pg.KEYDOWN, self.__right_key)
            gSystem.INPUT.add_keyboard_listener(self.__move_left__,
                                                pg.KEYDOWN, self.__left_key)

            gSystem.INPUT.add_keyboard_listener(self.__stop_x_move__,
                                                pg.KEYUP, self.__right_key)
            gSystem.INPUT.add_keyboard_listener(self.__stop_x_move__,
                                                pg.KEYUP, self.__left_key)
        
        elif self.__axel_opt == 'y':
            gSystem.INPUT.add_keyboard_listener(self.__move_up__,
                                                pg.KEYDOWN, self.__up_key)
            gSystem.INPUT.add_keyboard_listener(self.__move_down__,
                                                pg.KEYDOWN, self.__down_key)

            gSystem.INPUT.add_keyboard_listener(self.__stop_y_move__,
                                                pg.KEYUP, self.__up_key)
            gSystem.INPUT.add_keyboard_listener(self.__stop_y_move__,
                                                pg.KEYUP, self.__down_key)

    def __set_four_eight_directions__(self):
        gSystem.INPUT.add_keyboard_listener(self.__move_right__,
                                            pg.KEYDOWN, self.__right_key)
        gSystem.INPUT.add_keyboard_listener(self.__move_left__,
                                            pg.KEYDOWN, self.__left_key)
        gSystem.INPUT.add_keyboard_listener(self.__move_up__,
                                            pg.KEYDOWN, self.__up_key)
        gSystem.INPUT.add_keyboard_listener(self.__move_down__,
                                            pg.KEYDOWN, self.__down_key)

        gSystem.INPUT.add_keyboard_listener(self.__stop_x_move__,
                                            pg.KEYUP, self.__right_key)
        gSystem.INPUT.add_keyboard_listener(self.__stop_x_move__,
                                            pg.KEYUP, self.__left_key)
        gSystem.INPUT.add_keyboard_listener(self.__stop_y_move__,
                                            pg.KEYUP, self.__up_key)
        gSystem.INPUT.add_keyboard_listener(self.__stop_y_move__,
                                            pg.KEYUP, self.__down_key)
    

    def __move__(self, delta):
        if self.__direction[0] == self.RIGHT:
            (x, y) = self.getPos()
            x += self.__speed * delta
            self.setPos((x, y))
            
            if self.__directions == 4:
                self.__direction[1] = self.STOPED

        elif self.__direction[0] == self.LEFT:
            (x, y) = self.getPos()
            x -= self.__speed * delta
            self.setPos((x, y))
            
            if self.__directions == 4:
                self.__direction[1] = self.STOPED

        elif self.__direction[1] == self.UP:
            (x, y) = self.getPos()
            y -= self.__speed * delta
            self.setPos((x, y))

            if self.__directions == 4:
                self.__direction[0] = self.STOPED

        elif self.__direction[1] == self.DOWN:
            (x, y) = self.getPos()
            y += self.__speed * delta
            self.setPos((x, y))

            if self.__directions == 4:
                self.__direction[0] = self.STOPED


    def __move_right__(self):
        self.__direction[0] = self.RIGHT
        gSystem.TIMER.add_everytime_clock(self.__move__)

    def __move_left__(self):
        self.__direction[0] = self.LEFT
        gSystem.TIMER.add_everytime_clock(self.__move__)

    def __move_up__(self):
        self.__direction[1] = self.UP
        gSystem.TIMER.add_everytime_clock(self.__move__)

    def __move_down__(self):
        self.__direction[1] = self.DOWN
        gSystem.TIMER.add_everytime_clock(self.__move__)


    def __stop_x_move__(self):
        self.__direction[0] = self.STOPED
        gSystem.TIMER.remove_clock(self.__move__)
    
    def __stop_y_move__(self):
        self.__direction[1] = self.STOPED
        gSystem.TIMER.remove_clock(self.__move__)