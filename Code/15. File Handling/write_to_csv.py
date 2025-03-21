import csv

with open("data.csv", "a", newline="\n") as file:
    writer = csv.writer(file)
    writer.writerow(["Muhammad", 62, "SA"])
