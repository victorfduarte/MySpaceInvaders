from .draw_interface import DrawInterface
from .collision_interface import CollisionInterface
from .move_interface import MoveInterface
from .sprite_behavior_interface import SpriteBehaviorInterface


class SpriteInterface(DrawInterface, CollisionInterface, MoveInterface):
    def kill(self):
        '''*Abstract Funcition*\n
        Método a ser executado para destruir um Sprite
        '''
        pass

    def add_behavior(self, behavior: SpriteBehaviorInterface) -> None:
        '''*Abstract Function*\n
        Adiciona um comportamento ao Sprite
        '''
        pass

    def remove_behavior(self, name: str) -> None:
        '''*Abstract Function*\n
        Remove um comportamento do Sprite, com base no nome
        '''
        pass

    def get_name(self):
        '''*Abstract Funcition*\n
        Retorna qual o nome do objeto
        '''
        pass

    def get_angle(self):
        '''*Abstract Funcition*\n
        Retorna o ângulo do objeto em graus
        '''

    def set_dimension(self, dimension: 'tuple[int, int]') -> None:
        '''*Abstract Function*\n
        Seta o a largura e a altura do objeto
        '''
        pass

    def set_angle(self, angle: int):
        '''*Abstract Funcition*\n
        Seta o ângulo do objeto em graus
        '''
        pass