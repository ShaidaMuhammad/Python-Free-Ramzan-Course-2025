try:
    print(10 / 0)
except ZeroDivisionError as e:
    raise ValueError("Invalid operation") from e