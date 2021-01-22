from ui import UI
from converter import Converter


class App:
    def __init__(self):
        self.ui = UI(Converter())
        self.ui.draw_screen()

    # PUBLIC METHODS
    def start(self):
        self.ui.mainloop()
