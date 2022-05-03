from .bases.sprite import MySprite
from .bala_inimiga import BalaInimiga

class EnemyShip(MySprite):
    def __init__(self, position: 'tuple[int, int]', img_path: str):
        super().__init__('Enemy', img_path)
        
        # Comportamentos
        # Animação

        # Propriedades
        self.point1 = ()


    def atirar(self):
        x, y = self.get_position()
        
        balax = x + self.point1[0]
        balay = y + self.point1[1]

        BalaInimiga((balax, balay))
    