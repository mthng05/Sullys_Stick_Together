# we use this file to split the dataset into training set and test set in 2020 and 2021
import pandas as pd
import csv  

col_names = ['iso_code','continent','location','date',
             'new_cases','total_deaths',
             'reproduction_rate','tests_per_case',
             'total_vaccinations','people_fully_vaccinated']

continents = ['Asia', 'Europe', 'North America', 'South America', 'Africa', 'Oceania']

# with open('owid-covid-data.csv', 'r') as input_file, open('my_data2020.csv', 'w') as output_file:
with open('owid-covid-data.csv', 'r') as input_file, open('my_data2021.csv', 'w') as output_file:
    #create csv reader and writer objects
    csv_reader = csv.reader(input_file)
    csv_writer = csv.writer(output_file)

    # write the header
    header_row = next(csv_reader)

    # get the indexes of columns to keep
    indexes_to_keep = [i for i, header in enumerate(header_row) if header in col_names]

    # write the header row to the output file
    header_row_to_write = [header_row[i] for i in indexes_to_keep]
    csv_writer.writerow(header_row_to_write)

    # write the rows with only the selected columns
    for row in csv_reader:
        if (row[1] == 'Asia') or (row[1] == 'Europe') or (row[1] == 'North America') or (row[1] == 'South America') or (row[1] == 'Africa') or (row[1] == 'Oceania'):
            new_row = [row[i] for i in indexes_to_keep]
            csv_writer.writerow(new_row)


# df = pd.read_csv('my_data2020.csv')
df = pd.read_csv('my_data2021.csv')

# choose only the data from january 2020 to july 2020
# df = df[(df['date'] >= '2020-01-01') & (df['date'] <= '2020-07-31')]
# choose only the data from february 2021 to october 2021
df = df[(df['date'] >= '2021-02-01') & (df['date'] <= '2021-10-31')]

# df.to_csv('my_data2020.csv', index=False)
df.to_csv('my_data2021.csv', index=False)

# with open('owid-covid-data.csv', 'r') as input_file, open('my_data2020_test.csv', 'w') as output_file:
with open('owid-covid-data.csv', 'r') as input_file, open('my_data2021_test.csv', 'w') as output_file:
    #create csv reader and writer objects
    csv_reader = csv.reader(input_file)
    csv_writer = csv.writer(output_file)

    # write the header
    header_row = next(csv_reader)

    # get the indexes of columns to keep
    indexes_to_keep = [i for i, header in enumerate(header_row) if header in col_names]

    # write the header row to the output file
    header_row_to_write = [header_row[i] for i in indexes_to_keep]
    csv_writer.writerow(header_row_to_write)

    # write the rows with only the selected columns
    for row in csv_reader:
        if (row[1] == 'Asia') or (row[1] == 'Europe') or (row[1] == 'North America') or (row[1] == 'South America') or (row[1] == 'Africa') or (row[1] == 'Oceania'):
            new_row = [row[i] for i in indexes_to_keep]
            csv_writer.writerow(new_row)


# df = pd.read_csv('my_data2020_test.csv')
df = pd.read_csv('my_data2021_test.csv')

# df = df[(df['date'] >= '2020-08-01') & (df['date'] <= '2020-09-30')]
df = df[(df['date'] >= '2021-11-01') & (df['date'] <= '2021-12-31')]

# df.to_csv('my_data2020_test.csv', index=False)
df.to_csv('my_data2021_test.csv', index=False)

# ------------------------------------------
# count total line in owid-covid-data.csv
# with open('owid-covid-data.csv', 'r') as f:
#     reader = csv.reader(f)
#     data = list(reader)
# print(len(data))