from sprite import Sprite
from sprite_interface import SpriteInterface

class Block(Sprite):
    def __init__(self, img):
        super().__init__(img)


class BlockGroup(SpriteInterface):
    def __init__(self, columns, rows):
        self.__blockers: list [Block] = [[0] * columns for _ in range(rows)]
        self.__collumns = columns
        self.__rows = rows
    
    def addBlock(self, block: Block, column: int, row: int):
        self.__blockers[row][column] = block
    
    def getBlockers(self) -> list:
        return self.__blockers