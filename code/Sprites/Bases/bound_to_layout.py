from GameSystem import gSystem
from Interfaces.sprite_behavior_interface import SpriteBehaviorInterface
from Interfaces.sprite_interface import SpriteInterface

class BoundToLayout(SpriteBehaviorInterface):
    def __init__(self, parent: SpriteInterface):
        self.__parent = parent

        self.__display_width = gSystem.DISPLAY.getWidth()
        self.__display_height = gSystem.DISPLAY.getHeight()
    
    def position_outside_layout(self, pos: 'tuple[int, int]', *args) -> bool:
        (x, y) = pos
        width, height = self.__parent.get_dimension()

        if x < 0:
            return True
        elif x + width > self.__display_width:
            return True
        
        if y < 0:
            return True
        elif y + height > self.__display_height:
            return True
        
        return False
    

    def correct_position(self, pos: 'tuple[int, int]', *args) -> 'tuple[int, int]':
        (x, y) = pos
        width, height = self.__parent.get_dimension()

        if x < 0:
            x = 0
        elif x + width > self.__display_width:
            x = self.__display_width - width
        
        if y < 0:
            y = 0
        elif y + height > self.__display_height:
            y = self.__display_height - height
        
        return (x, y)
