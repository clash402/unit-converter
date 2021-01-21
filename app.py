from ui import UI


class App:
    def __init__(self):
        self._draw_screen()

    # PRIVATE METHODS
    def _draw_screen(self):
        self.ui = UI()
        self.ui.draw_unit_label("miles", (2, 0))
        self.ui.draw_unit_label("km", (2, 1))
        self.ui.draw_equals_label()
        self.ui.draw_calculate_button(
            self.ui.calculate_button_clicked,
            self.ui.draw_user_input(),
            self.ui.draw_result_label()
        )

    # PUBLIC METHODS
    def start(self):
        self.ui.mainloop()
