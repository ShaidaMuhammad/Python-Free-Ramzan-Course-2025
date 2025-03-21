greet = "   pa Khair raghly!"

print(greet.upper())
print(greet.lower())
print(greet.title())

print(greet.capitalize())

print(greet.strip())
print(greet.startswith("p"))
print(greet.startswith(" "))
print(greet.endswith("!"))
print(greet.endswith("raghly!"))

print(greet.replace("Khair", "Kheryat"))

print(greet.split())
print(greet.split("a"))

print(greet.isalpha())
print(greet.isalnum())




words = ["Starry", "Mashy"]
print(" ".join(words))
print("+".join(words))