# Import pandas
import pandas
from pandas import ExcelWriter

# Create a dictionary that will be used to create the DataFrame
data = {
    'FirstName':["Satvik", "Avinash", "Lahri"],
    'LastName':["Shah", "Kati", "Rath"],
    'Email':["satshah@example.com", "avinashK@example.com", "lahri.rath@example.com"],
    'PhoneNumber':["4537829158", "4892184058", "4528727830"]
}

# Create the DataFrame that will be written to the excel file
dataframe = pandas.DataFrame(data)

# Print the dataframe
print(dataframe)

# Write the dataframe to a Excel file
writer = ExcelWriter('../Inputs/sample.xlsx')
dataframe.to_excel(writer, 'Sheet1', index = False)

# Commit data to the Excel file
writer._save()

# Read data from Excel sheet
users = pandas.read_excel('../Inputs/sample.xlsx')

# Print the dataframe
print(users)

# Print the number of rows and columns
print("====================================")
print("Number of rows:", users.shape[0])
print("Number of columns:", users.shape[1])

# Print the data in the emails column only
print("====================================")
print("Emails:")
print(users['Email'])

# Sort the data based on FirstName in ascending order and print the data
print("====================================")
print("Sorted data:")
print(users.sort_values('FirstName'))

