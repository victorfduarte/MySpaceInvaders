'''
A interface que possibilita os objetos poderem ser colididos
'''

class CollisionInterface:
    def get_collision_content(self) -> 'list[CollisionInterface]':
        '''*Abstract Function*\n
        Retorna o conteúdo para verificar a colisão\n
        Caso o objeto seja simples, retorna uma lista contendo ele mesmo. Caso o objeto
        seja um grupo de outros objetos, deve chamar este mesmo método de todos os seus
        componentes e juntar os resultados todos em uma única lista
        '''
        pass

    def set_collision_content(self, content: 'list[CollisionInterface]') -> None:
        '''*Abstract Function*\n
        Seta o conteúdo para verificar a colisão\n
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

    def on_collision(self, obj: 'CollisionInterface') -> None:
        '''*Abstract Function*\n
        Método que é chamado toda vez que o objeto se colide. Recebe como argumento o
        objeto com o qual a colisão ocorreu
        '''
        pass

