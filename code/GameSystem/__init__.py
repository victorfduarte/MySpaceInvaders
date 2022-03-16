from .input import Input
from .collisions import Collisions
from .timer import Timer
from .display import Display
from .screen_manager import ScreenManager

class GSystem:
    def __init__(self):
        self.INPUT: Input = None
        self.COLLISIONS: Collisions = None
        self.TIMER: Timer = None
        self.DISPLAY: Display = None
        self.SCREEN_MANAGER: ScreenManager = None
        

    def init(self, width = 800, height = 600):
        '''Inicializa o sistema configurando a largura e altura da tela e o nome da
        primeira tela a aparecer no jogo
        '''

        self.INPUT = Input()
        self.COLLISIONS = Collisions()
        self.TIMER = Timer()
        self.DISPLAY = Display()
        self.SCREEN_MANAGER = ScreenManager(self)

        self.DISPLAY.__setup__(width, height)


gSystem = GSystem()