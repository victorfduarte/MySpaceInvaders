from sprite_interface import SpriteInterface
from enemy_ship import EnemyShip

class EnemiesGroup(SpriteInterface):
    def __init__(self, columns, rows):
        self.__enemies: list [EnemyShip] = [[0] * columns for _ in range(rows)]
        self.__columns = columns
        self.__rows = rows 
    
    def addChild(self, enemy: EnemyShip, column: int, row: int):
        self.__enemies[row][column] = enemy

    def getChildren(self) -> list:
        return self.__enemies
    
