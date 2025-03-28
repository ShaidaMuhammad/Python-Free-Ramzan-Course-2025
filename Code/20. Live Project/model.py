from exceptions import DivisionByZeroError, InvalidOperationError


class CalculatorModel:
    def __init__(self):
        self.reset()
    
    def reset(self):
        self.current_input = "0"
        self.stored_value = None
        self.operation = None
        self.reset_input = False
    
    def update_input(self, value):
        if self.current_input == "0" or self.reset_input:
            self.current_input = value
            self.reset_input = False
        else:
            self.current_input += value
    
    def set_operation(self, operation):
        if self.operation and not self.reset_input:
            self.calculate()
        self.stored_value = float(self.current_input)
        self.operation = operation
        self.reset_input = True
    
    def calculate(self):
        if not self.operation or self.stored_value is None:
            return
        
        try:
            current_value = float(self.current_input)
            
            if self.operation == '+':
                result = self.stored_value + current_value
            elif self.operation == '-':
                result = self.stored_value - current_value
            elif self.operation == '*':
                result = self.stored_value * current_value
            elif self.operation == '/':
                if current_value == 0:
                    raise DivisionByZeroError()
                result = self.stored_value / current_value
            else:
                raise InvalidOperationError()
            
            # Clean up .0 from integer results
            self.current_input = str(int(result) if result.is_integer() else result)
            self.operation = None
            self.stored_value = None
            self.reset_input = True
            
        except (DivisionByZeroError, InvalidOperationError):
            self.reset()
            raise