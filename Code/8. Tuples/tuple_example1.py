# Creating List
sports_l = list(("Cricket", "Football", "Table Tennis", "Cricket"))

# Creating Tuple
sports_t = ("Cricket", "Football", "Table Tennis", "Cricket")
# sports_t = tuple(("Cricket", "Football", "Table Tennis", "Cricket"))

# print(sports_l)
# print(type(sports_l))
print(sports_t)
print(type(sports_t))

# Accessing element with positive indexing
print(sports_t[0])

# Accessing element with negative indexing
print(sports_t[-2])


# Slicing of tuples
print(sports_t[:2])
print(sports_t[1:3])
print(sports_t[-3:])

# Lists are mutalble
sports_l[0] = "Wrestling"
print(sports_l)

# Tuples are immutable
# sports_t[0] = "Wrestling"