from sprite import Sprite


class Bullet(Sprite):
    def __init__(self, img, direction: int, speed: int):
        super().__init__(img)
        self.__direction = direction
        self.__speed = speed
    
    def check_limits(self, screen) -> bool:
        '''Verifica se a bala já saiu da tela\n
        Retorna True se ainda estiver dentro e False se não'''
        pass

    def update_pos(self, delta: float):
        '''Atualiza a posição da bala\n
        Recebe um valor delta para fazer a correção do tempo
        '''
        (x, y) = self.getPos()
        y += self.__speed * self.__direction * delta
        self.setPos([x, y])


    # Getters
    def getDirection(self) -> int:
        return self.__direction
    def getSpeed(self) -> int:
        return self.__speed

    # Setters
    def setDirection(self, direction: int):
        self.__direction = direction
    def setSpeed(self, speed: int):
        self.__speed = speed