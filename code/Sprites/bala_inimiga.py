from tkinter import Button
from .bases.sprite import MySprite
from.bases.bullet import Bullet

class BalaInimiga(MySprite):
    def __init__(self, pos: 'tuple[int, int]'):
        super().__init__('BalaInimiga', 'resources/images/bala_inimiga.png')
        self.set_position(pos)

        bullet = Bullet(self, 900, -90)
        self.add_behavior(bullet)