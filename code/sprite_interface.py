'''
A interface a ser utilizada por Sprites e Grupos de Sprites
'''

class SpriteInterface:
    def kill(self):
        '''Abstract Function\n
        Função para destruir o objeto'''
        pass

    def draw(self, screen):
        '''Abstract Function\n
        Desenha o objeto na tela'''
        pass
    
    def check_collision_with(self, obj) -> bool:
        '''Detecta se há colisão entre self e obj e retorna True se sim\n
        Se houver, chama a função touched(obj) de ambos.
        Caso self seja um grupo, chama a touched(obj) do grupo e a do item do grupo.
        Esta função deve ser estendida para funcionar. Por enquanto, somente chama os
        métodos touched(obj) de self e obj'''
        # A ser implementada posteriormente
        self.touched(obj)
        obj.touched(self)
    
    def touched(self, obj) -> None:
        '''Abstract Function\n
        Recebe o objeto com o qual está tocando e executa qualquer ação'''
        pass