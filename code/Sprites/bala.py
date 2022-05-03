from .bases.sprite import MySprite
from .bases.bullet import Bullet

class Bala(MySprite):
    def __init__(self, pos: 'tuple[int, int]'):
        super().__init__('BalaPersonagem', 'resources/images/bala.png')
        self.set_position(pos)

        bullet = Bullet(self, 450, 90) # Velocidade: 900
        self.add_behavior(bullet)
