from sprite_interface import SpriteInterface


class Sprite(SpriteInterface):
    def __init__(self, image):
        self.__image = image
        self.__position = [0, 0]
        self.__dimension = [0, 0]
        self.__image_scale = [0, 0]
    
    def setup(self, position: int, dimention: int, img_scale: int):
        self.__position = position
        self.__dimension = dimention
        self.__image_scale = img_scale
    
    # Getters
    def getImage(self):
        return self.__image  
    def getPos(self) -> list:
        return self.__position 
    def getDim(self) -> list:
        return self.__dimension
    def getImgScale(self) -> list:
        return self.__image_scale
    
    # Setters
    def setImage(self, img):
        self.__image = img
    def setPos(self, pos: list):
        self.__position = pos  
    def setDim(self, dim: list):
        self.__dimension = dim
    def stImgScale(self, img_scale):
        self.__image_scale = img_scale
