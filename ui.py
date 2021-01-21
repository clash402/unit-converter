from tkinter import *


class UI(Tk):
    def __init__(self):
        super().__init__()

        self.minsize(300, 200)
        self.config(padx=16, pady=16)
        self.title("Miles-to-Km Converter")

    # PUBLIC METHODS
    def draw_user_input(self):
        user_input = Entry(width=6)
        user_input.grid(column=1, row=0)
        user_input.focus()
        return user_input

    def draw_unit_1_label(self):
        unit_1_label = Label(text="miles", font=("Arial", 16))
        unit_1_label.grid(column=2, row=0)

    def draw_equals_label(self):
        equals_label = Label(text="is equal to", font=("Arial", 16))
        equals_label.grid(column=0, row=1)

    def draw_result_label(self):
        result_label = Label(text="0", font=("Arial", 16))
        result_label.grid(column=1, row=1)
        return result_label

    def draw_unit_2_label(self):
        unit_2_label = Label(text="km", font=("Arial", 16))
        unit_2_label.grid(column=2, row=1)

    def draw_calculate_button(self, clicked, user_input, result_label):
        calculate_button = Button(
            text="Calculate", command=lambda: clicked(
                user_input,
                result_label
            )
        )
        calculate_button.grid(column=1, row=2)

    def calculate_button_clicked(self, user_input, result_label):
        unit_1 = float(user_input.get())
        unit_2 = round(unit_1 * 1.609, 2)
        result_label.config(text=f"{unit_2}")
