import tkinter as tk
from tkinter import font as tkfont
from styles import CalculatorStyles


class CalculatorView:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.styles = CalculatorStyles()

        # Initialize fonts after root exists
        self.display_font = tkfont.Font(size=self.styles.DISPLAY_FONT_SIZE)
        self.button_font = tkfont.Font(size=self.styles.BUTTON_FONT_SIZE)

        self._setup_window()
        self._create_display()
        self._create_buttons()

    def _setup_window(self):
        self.root.title(self.styles.WINDOW_TITLE)
        self.root.geometry(self.styles.WINDOW_SIZE)
        self.root.resizable(self.styles.RESIZABLE, self.styles.RESIZABLE)
        self.root.config(bg=self.styles.BG_COLOR)

    def _create_display(self):
        self.display_var = tk.StringVar()
        self.display_var.set("0")

        self.display = tk.Label(
            self.root,
            textvariable=self.display_var,
            anchor="e",
            padx=10,
            font=self.display_font,
            bg=self.styles.DISPLAY_BG,
            relief="sunken"
        )
        self.display.pack(fill="x", padx=10, pady=10, ipady=10)

    def _create_buttons(self):
        for row in self.styles.BUTTON_LAYOUT:
            frame = tk.Frame(self.root, bg=self.styles.BG_COLOR)
            frame.pack(fill="x", padx=5, pady=2)
            
            for btn_text in row:
                self._create_button(frame, btn_text)
    
    def _create_button(self, parent, text):
        if text == '=':
            bg = self.styles.EQUAL_BG
            fg = self.styles.EQUAL_TEXT
            command = lambda: self.controller.handle_input(text)
        elif text in '+-*/':
            bg = self.styles.OPERATOR_BG
            fg = self.styles.TEXT_COLOR
            command = lambda: self.controller.handle_input(text)
        else:
            bg = self.styles.BUTTON_BG
            fg = self.styles.TEXT_COLOR
            command = lambda: self.controller.handle_input(text)
        
        btn = tk.Button(
            parent,
            text=text,
            command=command,
            font=self.button_font,
            bg=bg,
            fg=fg,
            relief="raised",
            bd=1
        )
        btn.pack(side="left", expand=True, fill="x", ipady=10)
    
    def update_display(self, value):
        self.display_var.set(value)
    
    def show_error(self, message):
        self.display_var.set(message)