from sprite import Sprite
from bullet import Bullet

class Ship(Sprite):
    def __init__(self, image, bullet: Bullet):
        super().__init__(image)
        self.__bullet = bullet

    def mover(self, x, y):
        '''Move a quantidade de pixels especificada em x e y'''
        pos = self.getPos()
        self.setPos([pos[0] + x, pos[1] + y])
    
    def atirar() -> Bullet:
        '''Abstract Function\n
        Faz a nave atirar e retorna o(s) objeto(s) criados'''
        pass
    

    # Getters
    def getBullet(self) -> Bullet:
        return self.__bullet

    # Setters
    def setBullet(self, bullet: Bullet):
        self.__bullet = bullet