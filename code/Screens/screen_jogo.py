from .bases.screen_base import ScreenBase
from Sprites.player_ship import PlayerShip

class ScreenJogo(ScreenBase):
    def setup(self):
        self.get_gSytem().INPUT.add_quit_listener(self.get_gSytem().SCREEN_MANAGER.quit)

        player = PlayerShip()
        player.set_position((300, 500))
        
        
        print('Oi, tudo bem?')

    def leave(self):
        print('Volte logo')