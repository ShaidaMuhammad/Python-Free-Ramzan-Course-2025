age = int(input("Please Enter your age: "))
country = input("Please tell me your country: ")

if age > 18:
    if country == "USA":
        print("You are eligible to vote in the USA.")
    else:
        print("You are not eligible to Vote in the USA.")
else:
    print("You are not eligible to vote.")
