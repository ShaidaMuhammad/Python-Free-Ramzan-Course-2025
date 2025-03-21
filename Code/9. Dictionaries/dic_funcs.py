student_info = {"Name": "Ali", "Age": 17, "GPA": 3.9}
print(student_info)

# Print a list of keys of dictionary
print(student_info.keys())

# Print a list of values of dictionary
print(student_info.values())

# Get list of tuples from dictionary key-value pairs
print(student_info.items())

for key, val in student_info.items():
    print(f"Key: {key}, Value: {val}")