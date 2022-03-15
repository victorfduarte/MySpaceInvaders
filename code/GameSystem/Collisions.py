'''
Este é o módulo do GameSystem que trabalha as colisões entre objetos
'''

from ..Sprites.sprite import MySprite
from ..Sprites.group_sprites import MyGroupSprites
import pygame

class Collisions:
    '''Classe para fazer funcionar os tempos do jogo. Cria um objeto para ser único em
    todo o jogo. Possui as seguintes funções:\n
    add_sprite(sprite: MySprite) -> None: Adiciona o sprite à lista de sprites a serem
    renderizados\n
    remove_sprite(sprite: MySprite) -> None: Remove o sprite da lista de sprites a serem
    renderizados\n
    add_group_sprites(group: MyGroupSprite) -> None: Adiciona o grupo de sprites à lista
    de grupo de sprites a serem renderizados\n
    remove_group_sprites(sprite: MyGroupSprite) -> None: Remove o grupo de sprites de
    lista de grupo de sprites a serem renderizados\n
    '''
    def __init__(self):
        self.__sprites: list[MySprite] = []
        self.__groups: list[MyGroupSprites] = [] 


    def add_sprite(self, sprite: MySprite):
        if sprite not in self.__sprites:
            self.__sprites.append(sprite)
    
    def remove_sprite(self, sprite: MySprite):
        if sprite in self.__sprites:
            self.__sprites.remove(sprite)
    
    def add_group_sprites(self, group: MyGroupSprites):
        if group not in self.__groups:
            self.__groups.append(group)
    
    def remove_group_sprites(self, group: MyGroupSprites):
        if group in self.__groups:
            self.__groups.remove(group)


    def __sprites__(self):
        '''Verifica se há colisão entre os Sprites cadastrados\n
        Se houver, chama a função on_collision() de cada um\n
        **Esta função faz parte do sistema e não deve ser chamada**
        '''
        for idx1 in range(len(self.__sprites)):
            for idx2 in range(idx1+1, len(self.__sprites)):
                if self.__collison__(self.__sprites[idx1], self.__sprites[idx2]):
                    self.__sprites[idx1].on_collision(self.__sprites[idx2])
                    self.__sprites[idx2].on_collision(self.__sprites[idx1])
        pass

    def __groups__(self):
        '''Vefifica se há colisão entre os Sprites dos Grupos de Sprites cadastrados
        Se houver, chama a função on_collision() de cada Sprite e do Grupo\n
        **Esta função faz parte do sistema e não deve ser chamada**
        '''
        for idx1 in range(len(self.__groups)):
            for idx2 in range(idx1+1, len(self.__groups)):
                gp_collision = False
                for sprite1 in self.__groups[idx1].sprites():
                    for sprite2 in self.__groups[idx2].sprites():
                        if self.collison(sprite1, sprite2):
                            sprite1.on_collision(sprite2)
                            sprite2.on_collision(sprite1)
                            gp_collision = True
                if gp_collision:
                    self.__groups[idx1].on_collision(self.__groups[idx2])
                    self.__groups[idx2].on_collision(self.__groups[idx1])

    def __sprite_groups__(self):
        '''Verifica se há colisão entre Sprites com Grupos de Sprites\n
        Se houver, chama a função on_collision() de cada Sprite\n
        **Esta função faz parte do sistema e não deve ser chamada**
        '''
        for sprite1 in self.__sprites:
            for group in self.__groups:
                gp_collision = False
                for sprite2 in group.sprites():
                    if self.collison(sprite1, sprite2):
                        sprite1.on_collision(sprite2)
                        sprite2.on_collision(sprite1)
                        gp_collision = True
                if gp_collision:
                    group.on_collision(sprite1)

    def __collison__(self, obj1: MySprite, obj2: MySprite) -> bool:
        '''Verifica se dois Sprites estão se colidindo\n
        **Esta função faz parte do sistema e não deve ser chamada**
        '''
        if self.axes_collision(obj1.rect.x, obj1.rect.width,
        obj2.rect.x, obj2.rect.width):
            return self.axes_collision(obj1.rect.y, obj1.rect.height,
            obj2.rect.y, obj2.rect.height)
        return False

    def __axes_collision__(self, pt1: int, d1: int, pt2: int, d2: int) -> bool:
        '''Verifica colisão em uma única dimensão\n
        **Esta função faz parte do sistema e não deve ser chamada**
        '''
        if pt1 < d2:
            if pt2 < (pt1 + d1):
                return True
            return False

        elif pt1 < (pt2 + d2):
            return True
