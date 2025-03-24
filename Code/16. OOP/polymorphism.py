class Animal:
    def speak(self):
        print("Animal speaks!")  # Default implementation

class Dog(Animal):
    def speak(self):  # Method overriding (polymorphism)
        print("Woof!")  # Dog-specific behavior

class Cat(Animal):
    def speak(self):  # Method overriding (polymorphism)
        print("Meow!")  # Cat-specific behavior


# Using polymorphism
animals = [Dog(), Cat()]  # List of different Animal subtypes
for animal in animals:
    animal.speak()  # Same method, different behaviors
