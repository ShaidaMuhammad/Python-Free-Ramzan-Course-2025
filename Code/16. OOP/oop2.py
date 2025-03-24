class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name} \t Age: {self.age}")

obj1 = Student("Ali", 17)
obj2 = Student("Khan", 30)

obj1.display_info()
obj2.display_info()

print(obj1.name)