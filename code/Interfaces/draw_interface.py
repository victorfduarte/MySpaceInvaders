'''
A interface que possibilita os objetos poderem ser desenhados
'''

from pygame import Surface

class DrawInterface:
    def get_children(self) -> 'list[DrawInterface]':
        '''*Abstract Function*\n
        Retorna a sua lista dos objetos a serem desenhados na tela\n
        Caso o objeto seja simples, retorna uma lista contendo ele mesmo. Caso o objeto
        seja um grupo de outros objetos, deve chamar este mesmo método de todos os seus
        componentes e juntar os resultados todos em uma única lista
        '''
        pass

    def get_content(self) -> Surface:
        '''*Abstract Function*\n
        Retorna o conteúdo do objeto a ser desenhado na tela
        '''
        pass

    def get_position(self) -> 'tuple[int, int]':
        '''*Abstract Function*\n
        Retorna a posição X, Y do objeto
        '''
        pass