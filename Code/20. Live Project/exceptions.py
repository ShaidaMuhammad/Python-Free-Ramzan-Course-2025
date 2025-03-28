class CalculatorError(Exception):
    """Base calculator exception"""
    pass

class DivisionByZeroError(CalculatorError):
    """Raised when attempting division by zero"""
    pass

class InvalidOperationError(CalculatorError):
    """Raised for invalid mathematical operations"""
    pass