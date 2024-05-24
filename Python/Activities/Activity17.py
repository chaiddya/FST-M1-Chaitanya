# Import pandas
import pandas as pd

# Create a Dictionary that will hold our data
data = {
    "Usernames": ["admin", "Charles", "Deku"],
    "Passwords": ["password", "Charl13", "AllMight"]
}
# Create a DataFrame using that data
df = pd.DataFrame(data)

# Print the DataFrame
print(df)

"""
 Write the DataFrame to a CSV file
 To avoid writing the index numbers to the file as well
 the index property is set to false
"""
df.to_csv("../Inputs/creds.csv", index=False)

# read data from csv
creds = pd.read_csv("../Inputs/creds.csv")
print(creds)

#Print the values only in the Usernames column
print(creds["Usernames"])

#Print the username and password of the second row
print("Username: ", creds["Usernames"][1], "| Password: ", creds["Passwords"][1])

#Sort the Usernames column data in ascending order and print data
print(creds.sort_values("Usernames", ascending=True))

#Sort the Passwords column in descending order and print data
print(creds.sort_values("Passwords", ascending=False))
