class NegativeAgeError(Exception):
    def __init__(self, message="Age can not be negative!"):
        self.message = message
        super().__init__(self.message)

age = -5
if age < 0:
    raise NegativeAgeError("Negative age is not possible")
