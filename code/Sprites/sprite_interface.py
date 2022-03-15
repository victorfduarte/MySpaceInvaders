'''
A interface a ser utilizada por Sprites e Grupos de Sprites
'''


class SpriteInterface:
    def kill(self):
        '''Abstract Function\n
        Função para destruir o objeto
        '''
        pass

    def draw(self, screen):
        '''Abstract Function\n
        Desenha o objeto na tela
        '''
        pass

    def on_collision(self, obj) -> None:
        '''Abstract Function\n
        Recebe o objeto com o qual está tocando e executa qualquer ação
        '''
        pass