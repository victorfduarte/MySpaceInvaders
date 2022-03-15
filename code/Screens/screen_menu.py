from screen import Screen

class ScreenMenu(Screen):
    def __init__(self, name, inp, collision, timer, display, manager):
        super().__init__(name, inp, collision, timer, display, manager)
    
    def setup(self):
        pass

    def leave(self):
        pass