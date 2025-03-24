class Animal:
    def speak(self):
        print("Animal speaks!")

class Dog(Animal):
    def bark(self):
        print("Woof!")
        super().speak()

my_dog = Dog()
my_dog.speak()  # Output: Animal speaks!
my_dog.bark()   # Output: Woof!
