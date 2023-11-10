import csv, os.path as path

filtered_rows = []
filter_year = 2022

csv_path = path.join('Resources', 'Crime_Data_from_2020_to_Present.csv')

with open(csv_path) as csv_file:

    csv_read = csv.reader(csv_file)
    # remove header from csv (file has already been checked to confirm header exists)
    csv_header = next(csv_read)
    print(csv_header)

    

        