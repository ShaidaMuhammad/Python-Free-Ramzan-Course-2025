from model import CalculatorModel
from exceptions import CalculatorError


class CalculatorController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def handle_input(self, button_text):
        try:
            if button_text == 'C':
                self.model.reset()
            elif button_text in '+-*/':
                self.model.set_operation(button_text)
            elif button_text == '.':
                if '.' not in self.model.current_input:
                    self.model.update_input(button_text)
            elif button_text == '=':
                self.model.calculate()
            else:  # Numeric input
                self.model.update_input(button_text)

            self.view.update_display(self.model.current_input)

        except CalculatorError:
            self.view.show_error("Error")
            self.model.reset()