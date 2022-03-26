from .bases.sprite import MySprite
from .bases.bullet import Bullet

class Bala(MySprite):
    def __init__(self, pos: 'tuple[int, int]'):
        super().__init__('BalaPersonagem', 'resources/images/laser.png')
        self.set_position(pos)

        bullet = Bullet(self, 900, 90)
        self.add_behavior(bullet)
