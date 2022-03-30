from GameSystem import gSystem
import pygame as pg
from .bases.sprite import MySprite
from .bases.two_directions import TwoDirection
from.bases.bound_to_layout import BoundToLayout
from .bala import Bala


class PlayerShip(MySprite):
    def __init__(self, pos: 'tuple[int, int]', initial_lives = 3):
        super().__init__('Player', 'resources/images/nave.png')
        self.set_position(pos)

        # Comportamentos
        self.twod_irection = TwoDirection(self, 300, 'x')
        self.bound_to_layout = BoundToLayout(self)

        self.add_behavior(self.twod_irection)
        self.add_behavior(self.bound_to_layout)

        # Propiedades
        self.__double_shoot = True
        self.__lives = initial_lives
        self.can_shoot = True

        self.point1 = (24, -5)
        self.point2 = (6, 13)
        self.point3 = (42, 13)

        # Eventos
        gSystem.INPUT.add_keyboard_listener(self.atirar, pg.KEYDOWN, pg.K_SPACE)
    

    def move(self, pos: 'tuple[int, int]') -> None:
        if not self.bound_to_layout.position_outside_layout(pos):
            self.set_position(pos)
        else:
            self.set_position(self.bound_to_layout.correct_position(pos))


    def atirar(self):
        if self.can_shoot:
            x, y = self.get_position()

            if not self.__double_shoot:
                balax = self.point1[0] + x
                balay = self.point1[1] + y

                Bala((balax, balay))
                print('Atirando')
            
            else:
                bala1x = self.point2[0] + x
                bala1y = self.point2[1] + y
                bala2x = self.point3[0] + x
                bala2y = self.point3[1] + y

                Bala((bala1x, bala1y))
                Bala((bala2x, bala2y))

                print('Atirando Duplo')


            self.can_shoot = False

            gSystem.TIMER.add_clock_once(400, self.enable_shoot)
    

    def enable_shoot(self, delta):
        self.can_shoot = True


    def decrementar_vida(self) -> bool:
        '''Decrementa o número de vidas e retorna False se o número de vidas for zero'''
        if self.__lives:
            self.__lives -= 1
            return True
        return False
    
    
    # Getters
    def getDoubleShoot(self) -> bool:
        return self.__double_shoot
    def getLives(self) -> int:
        return self.__lives
    
    # Setters
    def setDoubleShoot(self, ds: bool):
        self.__double_shoot = ds
    def setLives(self, lives: int):
        self.__lives = lives
