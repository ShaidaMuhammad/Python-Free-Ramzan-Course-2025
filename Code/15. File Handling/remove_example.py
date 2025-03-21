import os

try:
    os.remove("test.txt")
    # alternative method
    os.unlink("test.txt")
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied!")
else:
    print("File succesfully deleted.")
finally:
    print("Operation Completed.")


# Alternative method to delete file safely
if os.path.exists("test.txt"):
    os.remove("example.txt")
    print("File deleted.")
else:
    print("File does not exist.")
