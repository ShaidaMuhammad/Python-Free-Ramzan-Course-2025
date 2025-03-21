with open("my_text.txt", "r") as f:
    lines = f.readlines()
    print(lines[2])
    print(lines[-1])