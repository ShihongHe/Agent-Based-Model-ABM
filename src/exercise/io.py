# Create something to write
a = []
for i in range(10):
    a.append("Coding is fun!");
# Open a file for writing
f = open("a.out", 'w')
# Write lines to the file
for line in a:
    f.write(line)
# Close the file
f.close()

with open("data.txt") as f:
    data = []
    for line in f:
        parsed_line = str.split(line,",")
        data_line = []
        for word in parsed_line:
            data_line.append(str(word))
        data.append(data_line)
print(data)

import csv
f = open('data.csv',newline='')
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
for row in reader: # A list of rows
    for value in row: # A list of value
        print(value) # Floats
f.close()



data=["111","222","333"]
f = open('data.csv', 'a', newline='')
writer = csv.writer(f, delimiter=' ')
for row in data:
    writer.writerow(row) # List of values.
f.close()






