from sprite_interface import SpriteInterface
from enemy_ship import EnemyShip

class EnemiesGroup(SpriteInterface):
    def __init__(self, columns, rows):
        self.enemies: list [EnemyShip] = []
        self.columns = columns
        self.rows = rows 