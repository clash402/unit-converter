from ui import UI


class App:
    def __init__(self):
        self.ui = UI()
        self.ui.draw_screen()

    # PUBLIC METHODS
    def start(self):
        self.ui.mainloop()
