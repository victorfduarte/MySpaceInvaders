from .bases.screen_base import ScreenBase

class ScreenJogo(ScreenBase):
    def setup(self):
        self.get_gSytem().INPUT.add_quit_listener(self.get_gSytem().SCREEN_MANAGER.quit)
        print('Oi, tudo bem?')

    def leave(self):
        print('Volte logo')