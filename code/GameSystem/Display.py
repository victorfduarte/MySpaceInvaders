'''
Este é o módulo do GameSystem que trabalha as colisões entre objetos
'''

from Interfaces.draw_interface import DrawInterface

import pygame
import pygame.display
import pygame.time

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
        self.__objects: list[DrawInterface] = []
        self.__framerate = 0
    

    def add_object(self, obj: DrawInterface):
        '''Recebe um objeto a ser desenhado na tela'''
        for child in obj.get_draw_content():
            if child not in self.__objects:
                self.__objects.append(obj)
    
    def remove_object(self, obj: DrawInterface):
        '''Deixa de desenhar o objeto na tela'''
        for child in obj.get_draw_content:
            if child in self.__objects:
                self.__objects.remove(obj)


    def getWidth(self) -> int:
        return self.__width
    
    def getHeight(self) -> int:
        return self.__height
    
    def getFramerate(self) -> int:
        return self.__framerate
    

    def __setup__(self, width: int, height: int, fps: int):
        '''Inicializa a tela com o tamanho especificado. Executa o comando
        pygame.display.set_mode()\n
        **Esta função faz parte do sistema e não deve ser chamada**
        '''
        self.__display = pygame.display.set_mode((width, height))
        self.__width = width
        self.__height = height
        self.__framerate = fps
    

    def __clear__(self):
        '''Limpa a tela, possibilitando ser redesenhada\n
        **Esta função faz parte do sistema e não deve ser chamada**
        '''
        self.__display.fill((0, 0, 0))

    def __drawAll__(self):
        '''Desenha os sprites cadastrados na tela\n
        **Esta função faz parte do sistema e não deve ser chamada**
        '''
        for obj in self.__objects:
            self.__display.blit(obj.get_image(), obj.get_position())

    def __update__(self):
        '''Atualiza a tela, desenhando tudo o que deve aparecer\n
        **Esta função faz parte do sistema e não deve ser chamada**
        '''
        self.__clear__()
        self.__drawAll__()
        pygame.display.update()