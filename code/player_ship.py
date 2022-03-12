from ship import Ship
from bullet import Bullet


class PlayerShip(Ship):
    def __init__(self, image, bullet: Bullet, initial_lives = 3):
        super().__init__(image, bullet)
        self.__double_shoot = False
        self.__lives = initial_lives
    
    def check_inputs(self, code) -> None:
        '''Chamada sempre que uma tecla é pressionada. Faz a validação e determina qual
        operação do jogador de ser chamada'''
        pass

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