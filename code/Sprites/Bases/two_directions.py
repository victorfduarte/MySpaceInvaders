from GameSystem import gSystem
from Interfaces.move_interface import MoveInterface
from Interfaces.draw_interface import DrawInterface
import pygame as pg
import pygame.transform

class TwoDirection(MoveInterface, DrawInterface):
    def twoDirectionsetup(self, speed: int, axel = 'x', angle: bool = False):
        '''Recebe a velocidade, em px/s, o eixo, (X ou Y), e se deve rotacionar a
        imagem ou não 
        '''
        self.image_base = self.get_image()
        self.__axel = axel
        self.__angle_enable = angle
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
    

    def __move__(self, delta):
        if self.__direction == self.RIGHT:
            (x, y) = self.get_position()
            x += self.__speed / 1000 * delta
            self.set_position((x, y))

        elif self.__direction == self.LEFT:
            (x, y) = self.get_position()
            x -= self.__speed / 1000 * delta
            self.set_position((x, y))

        elif self.__direction == self.UP:
            (x, y) = self.get_position()
            y -= self.__speed / 1000 * delta
            self.set_position((x, y))

        elif self.__direction == self.DOWN:
            (x, y) = self.get_position()
            y += self.__speed / 1000 * delta
            self.set_position((x, y))


    def __move_right__(self):
        self.__direction = self.RIGHT
        gSystem.TIMER.add_everytime_clock(self.__move__)
        if self.__angle_enable:
            self.set_image(pygame.transform.rotate(self.image_base, -90))

    def __move_left__(self):
        self.__direction = self.LEFT
        gSystem.TIMER.add_everytime_clock(self.__move__)
        if self.__angle_enable:
            self.set_image(pygame.transform.rotate(self.image_base, 90))

    def __move_up__(self):
        self.__direction = self.UP
        gSystem.TIMER.add_everytime_clock(self.__move__)
        if self.__angle_enable:
            self.set_image(pygame.transform.rotate(self.image_base, 0))

    def __move_down__(self):
        self.__direction = self.DOWN
        gSystem.TIMER.add_everytime_clock(self.__move__)
        if self.__angle_enable:
            self.set_image(pygame.transform.rotate(self.image_base, 180))

    def __stop_move__(self):
        self.__direction = self.STOPED
        gSystem.TIMER.remove_clock(self.__move__)