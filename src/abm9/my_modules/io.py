import csv


def read_data(f):
    # Read input data
    f = open(f, newline='')
    data = []
    for line in csv.reader(f, quoting=csv.QUOTE_NONNUMERIC):
        row = []
        for value in line:
            row.append(value)
            #print(value)
        data.append(row)
    f.close()
    
    n_rows=len(row)
    n_cols=len(data)
    return data,n_rows, n_cols

def write_data(address,data):
    f = open(address, 'w', newline='')
    writer = csv.writer(f, delimiter=',')
    for row in data:
        writer.writerow(row) # List of values.
    f.close()