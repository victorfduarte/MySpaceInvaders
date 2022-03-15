'''
Este é o módulo do GameSystem que trabalha as colisões entre objetos
'''

from ..Sprites.Bases.group_sprites import MyGroupSprites
from ..Sprites.Bases.sprite import MySprite

import pygame
import pygame.display

class Display:
    '''Classe para fazer funcionar a tela do jogo. Cria um objeto para ser único em
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
        self.__width = 0
        self.__height = 0
        self.__display: pygame.Surface = None
        self.__sprites: list[MySprite] = []
        self.__group_sprites: list[MyGroupSprites] = []
    

    def add_sprite(self, sprite: MySprite):
        if sprite not in self.__sprites:
            self.__sprites.append(sprite)
    
    def remove_sprite(self, sprite: MySprite):
        if sprite in self.__sprites:
            self.__sprites.remove(sprite)
    
    def add_group_sprites(self, group):
        if group not in self.__group_sprites:
            self.__group_sprites.append(group)
    
    def remove_group_sprites(self, group):
        if group in self.__group_sprites:
            self.__group_sprites.remove(group)
    

    def getWidth(self) -> int:
        return self.__width
    
    def getHeight(self) -> int:
        return self.__height
    

    def __setup__(self, width: int, height: int):
        '''Inicializa a tela com o tamanho especificado. Executa o comando
        pygame.display.set_mode()\n
        **Esta função faz parte do sistema e não deve ser chamada**
        '''
        self.__display = pygame.display.set_mode((width, height))
        self.__width = width
        self.__height = height

    def __drawAll__(self):
        '''Desenha os sprites cadastrados na tela\n
        **Esta função faz parte do sistema e não deve ser chamada**
        '''
        for sprite in self.__sprites:
            self.__display.blit(sprite.getImage(), sprite.getPos())
        
        for group in self.__group_sprites:
            for sprite in group.sprites():
                self.__display.blit(sprite.getImage(), sprite.getPos())

    def __update__(self):
        '''Atualiza a tela, desenhando tudo o que deve aparecer\n
        **Esta função faz parte do sistema e não deve ser chamada**
        '''
        pygame.display.update()