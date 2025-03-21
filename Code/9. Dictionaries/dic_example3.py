student_info = {"Name": "Ali", "Age": 17, "GPA": 3.9}
print(student_info)
del student_info["Age"]
print(student_info)
deleted = student_info.pop("GPA")
print(student_info)
print("Deleted: ", deleted)

# Clear/Delete all elements from dictionary
student_info.clear()
print(student_info)