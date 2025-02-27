import csv

# Open the file in write mode to write data
with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "City"])
    writer.writerow(["John", 25, "New York"])
    writer.writerow(["Sarah", 28, "Chicago"])

# Open the file in read mode to read data
with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)