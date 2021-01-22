from tkinter import *


class UI(Tk):
    def __init__(self, converter):
        super().__init__()

        self.FONT = ("Arial", 16)

        self.converter = converter

        self.minsize(300, 200)
        self.config(padx=16, pady=16)
        self.title("Miles-to-Km Converter")

        self.user_input = self._draw_user_input()
        self.result_label = self._draw_result_label()

    # PRIVATE METHODS
    def _draw_user_input(self):
        user_input = Entry(width=6)
        user_input.grid(column=1, row=0)
        user_input.focus()
        return user_input

    def _draw_result_label(self):
        result_label = Label(text="0", font=self.FONT)
        result_label.grid(column=1, row=1)
        return result_label

    def _draw_unit_label(self, text, pos):
        unit_label = Label(text=text, font=self.FONT)
        unit_label.grid(column=pos[0], row=pos[1])

    def _draw_equals_label(self):
        equals_label = Label(text="is equal to", font=self.FONT)
        equals_label.grid(column=0, row=1)

    def _draw_calculate_button(self, _calculate_button_clicked):
        calculate_button = Button(text="Calculate", command=_calculate_button_clicked)
        calculate_button.grid(column=1, row=2)

    def _update_result_label(self, new_value):
        self.result_label.config(text=f"{new_value}")

    # EVENTS
    def _calculate_button_clicked(self):
        new_units = self.converter.convert_miles_to_km(self.user_input)
        self._update_result_label(new_units)

    # PUBLIC METHODS
    def draw_screen(self):
        self._draw_unit_label("miles", (2, 0))
        self._draw_unit_label("km", (2, 1))
        self._draw_equals_label()
        self._draw_calculate_button(self._calculate_button_clicked)
