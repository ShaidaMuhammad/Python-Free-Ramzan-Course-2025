def my_function():
    x = 10 
    print(x)

my_function()
# print(x)


y = 20
print("Outside of the function: ", y)
def my_function():
    print("Inside of the function", y)

my_function()

z = 10
def modify_global():
    global z
    z = 20
modify_global()
print(z)