from ship import Ship
from bullet import Bullet

class EnemyShip(Ship):
    def __init__(self, image, bullet: Bullet):
        super().__init__(image, bullet)
        self.__images = [image]
        self.__index_image = 0
    
    def addImage(self, img):
        self.__images.append(img)
    
    def update_image(self):
        '''Atualiza a imagem do inimigo'''
        self.updateIndexImage()
        self.setImage(self.__images[self.__index_image])
        pass


    # Getters
    def getImages(self) -> list:
        return self.__images
    def getIndexImage(self) -> int:
        return self.__index_image

    # Setters
    def setImages(self, imgs: list):
        self.__images = imgs
    def updateIndexImage(self):
        '''Incrementa o index_image e reinicia se necessário'''
        if self.__index_image == len(self.__images) - 1:
            self.__index_image = 0
        else:
            self.__index_image += 1