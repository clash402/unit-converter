from unit_converter.ui.ui import UI
from unit_converter.converter import Converter


class App:
    def __init__(self):
        self.ui = UI(Converter())

    # PUBLIC METHODS
    def start(self):
        self.ui.mainloop()
