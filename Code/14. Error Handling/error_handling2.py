try:
    y = int(input("Enter value y: "))
    x = int(input("Enter value x: "))

    print("Y divide by x is:", y / x)
except ZeroDivisionError:
    print("Divide by 0 is impossible.")
except ValueError:
    print("You can only divide numbers by each other.")
else:
    print("Division succesfull.")
finally:
    print("Operations ended.")

print("Program Completed.")