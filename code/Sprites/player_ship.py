
from Sprites.bases.sprite import MySprite
from Sprites.bases.two_directions import TwoDirection


class PlayerShip(MySprite, TwoDirection):
    def __init__(self, initial_lives = 3):
        super().__init__('Player', 'resources/images/ship.png')
        self.twoDirectionsetup(350)
        
        self.__double_shoot = False
        self.__lives = initial_lives


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