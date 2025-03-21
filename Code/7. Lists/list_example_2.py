sports = ["Cricket", "Football", "Vollyball"]

print(sports)

sports.append("Batmintin")
sports.append("Table Tennis")
print(sports)

sports.insert(1, "Hockey")
print(sports)

sports.append("Cricket")
print(sports)

sports.remove("Cricket")
print("Item removed: ", sports)

sports.pop(2)
print("Vollyball poped: ", sports)