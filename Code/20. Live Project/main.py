import tkinter as tk
from model import CalculatorModel
from view import CalculatorView
from controller import CalculatorController


def main():
    root = tk.Tk()

    # Initialize MVC components
    model = CalculatorModel()
    controller = CalculatorController(model, None)  # View will be set later
    view = CalculatorView(root, controller)
    controller.view = view  # Complete the circular reference

    root.mainloop()

if __name__ == "__main__":
    main()