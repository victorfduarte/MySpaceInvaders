'''
A interface que possibilita os objetos poderem ser desenhados
'''

from pygame import Surface

class DrawInterface:
    def get_draw_content(self) -> 'list[DrawInterface]':
        '''*Abstract Function*\n
        Retorna a sua lista dos objetos a serem desenhados na tela\n
        Caso o objeto seja simples, retorna uma lista contendo ele mesmo. Caso o objeto
        seja um grupo de outros objetos, deve chamar este mesmo método de todos os seus
        componentes e juntar os resultados todos em uma única lista
        '''
        pass

    def set_draw_content(self, content: 'list[DrawInterface]'):
        '''*Abstract Function*\n
        Seta a sua lista dos objetos a serem desenhados na tela\n
        '''
        pass

    def get_position(self) -> 'tuple[int, int]':
        '''*Abstract Function*\n
        Retorna a posição X, Y do objeto
        '''
        pass

    def get_dimension(self) -> 'tuple[int, int]':
        '''*Abstract Function*\n
        Retorna a largura e a altura do objeto
        '''
        pass

    def get_image(self) -> Surface:
        '''*Abstract Function*\n
        Retorna o conteúdo do objeto a ser desenhado na tela
        '''
        pass

    def set_image(self, img: Surface) -> None:
        '''*Abstract Function*\n
        Seta o conteúdo do objeto a ser desenhado na tela
        '''
        pass