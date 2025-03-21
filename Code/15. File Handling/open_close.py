file = open("my_text.txt", "r")
print(file.read())
file.close()

with open("my_text.txt", "r") as f:
    print(f.read())

print("Completed.")