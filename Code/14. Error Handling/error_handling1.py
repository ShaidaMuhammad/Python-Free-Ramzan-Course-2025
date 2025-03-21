try:
    y = int(input("Enter value y: "))
    x = int(input("Enter value x: "))

    print("Y divide by x is:", y / x)
except ZeroDivisionError as e:
    print("Divide by 0 is impossible.", e)
except ValueError:
    print("You can only divide numbers by each other.")

print("Program Completed.")
