student_data = ('Ali', 17, 3.9, True)

for std in student_data:
    print(std)

print("####################################")

for i, std in enumerate(student_data):
    print(f"Iteration: {i + 1}, Details: {std}")
