import pandas as pd
import numpy as np
dataset = pd.read_csv('Data_1.csv')
# print(dataset)
mean = np.mean(dataset['Salary'])
# print(mean)
# print(dataset.mean())
# print(dataset.loc[:, 'Age'].mean())
median = np.median(dataset['Age'])
# print(median)
# print(dataset.median())
# print(dataset.mode())
print(dataset.loc[:, 'Country'].mode())
print(dataset['Country'].value_counts())
print(dataset['Purchased'].value_counts())











# import csv
#
# with open('Data_1.csv', mode='r') as csv_file:
#     csv_reader = csv.DictReader(csv_file)
#     line_count = 0
#     for row in csv_reader:
#         if line_count == 0:
#             print(f'Column names are {", ".join(row)}')
#             line_count += 1
#         for n in row:
#             print(row[n])
#         # print(f'\t{row["name"]} works in the {row["department"]} department, and was born in {row["birthday month"]}.')
#         line_count += 1
#     print(f'Processed {line_count} lines.')