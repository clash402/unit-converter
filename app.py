from ui import UI


class App:
    def __init__(self):
        self.ui = UI()
        self.ui.draw_unit_1_label()
        self.ui.draw_unit_2_label()
        self.ui.draw_equals_label()
        self.ui.draw_calculate_button(
            self.ui.calculate_button_clicked,
            self.ui.draw_user_input(),
            self.ui.draw_result_label()
        )

    # PUBLIC METHODS
    def start(self):
        self.ui.mainloop()
