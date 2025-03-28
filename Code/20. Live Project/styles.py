class CalculatorStyles:
    WINDOW_TITLE = "Professional Calculator"
    WINDOW_SIZE = "300x450"
    RESIZABLE = False

    # Colors
    BG_COLOR = "#f0f0f0"
    DISPLAY_BG = "#ffffff"
    BUTTON_BG = "#E0E0E0"
    OPERATOR_BG = "#FF9800"
    EQUAL_BG = "#4CAF50"
    TEXT_COLOR = "#333333"
    EQUAL_TEXT = "#ffffff"
    
    # Font sizes (will be initialized after root exists)
    DISPLAY_FONT_SIZE = 20
    BUTTON_FONT_SIZE = 15
    
    # Layout
    BUTTON_LAYOUT = [
        ('7', '8', '9', '/'),
        ('4', '5', '6', '*'),
        ('1', '2', '3', '-'),
        ('0', '.', 'C', '+'),
        ('=',)
    ]