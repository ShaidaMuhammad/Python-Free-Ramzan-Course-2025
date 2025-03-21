def greet(name, message):
    print(f"{message}, {name}!")

greet("Ali", "Starry Mashy")
greet(name="Ali", message="Starry Mashy")
greet(message="Starry Mashy", name="Ali")

x = lambda name, message: print(f"{message}, {name}!")
x("Ali", "Pa Khair Raaghly!")