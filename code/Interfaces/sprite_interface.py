from .draw_interface import DrawInterface
from .collision_interface import CollisionInterface
from .move_interface import MoveInterface
from .sprite_behavior_interface import SpriteBehaviorInterface


class SpriteInterface(DrawInterface, CollisionInterface, MoveInterface):
    def kill(self):
        '''*Abstract Funcition*\n
        Método a ser executado para destruir um Sprite'''
        pass

    def add_behavior(self, behavior: SpriteBehaviorInterface) -> None:
        '''*Abstract Function*\n
        Adiciona um comportamento ao Sprite'''
        pass

    def remove_behavior(self, name: str) -> None:
        '''*Abstract Function*\n
        Remove um comportamento do Sprite, com base no nome'''
        pass