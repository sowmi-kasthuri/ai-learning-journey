# pandas practicse
import pandas as pd
# print(pd.__version__)
df = pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]], columns = ["A" , "B", "C"])

# print(df)

# Head and tail functions
'''
print(df.head())
print(df.head(2))
print(df.tail(2))
'''
# column & index
'''
print(df.columns)
print (df.index)
print(df.index.tolist())
'''

#Useful info about df
'''
print(df.info())
print(df.describe())
print(df["A"].unique()) # find unqiue values in a row
print(df.nunique()) # find number of unique values
print(df.shape)
'''

# read csv file from /warmup folder
coffee = pd.read_csv("./warmup/coffee.csv")
#print(coffee.head())
'''
print(coffee.loc[[0,1,2,3,4]])
print("------")
print(coffee.loc[0:14])
print("------")
print(coffee.loc[0:])
print("------")
'''
# print specific values
'''
print(coffee.loc[0:14, ["Date" , "Product", "Cups_Sold"]])
print("------")
print(coffee.iloc[0:14, [0,1,2]])
print("------")
'''
# sort
'''
print(coffee.sort_values("Cups_Sold")) # ascending order
print("----------------------------------------------")
print(coffee.sort_values("Cups_Sold", ascending=False)) # descending order
print("----------------------------------------------")
print(coffee.sort_values(["Cups_Sold", "Product"], ascending=[0,1])) # descending order on multiple columns
'''
# filter
'''
print(coffee.loc[coffee["Cups_Sold"] >= 65].sort_values("Cups_Sold", ascending=1))
print("----------------------------------------------")
print(coffee[coffee["Cups_Sold"] >= 65].sort_values("Cups_Sold", ascending=1)) # this will also work
print("----------------------------------------------")
print(coffee[(coffee["Cups_Sold"] >= 65) & (coffee["Product"] == "Latte")])
'''
'''
#1. Load & Inspect
#Load coffee.csv into a DataFrame.
#Print the first 5 rows.
#Print column names and data types.
#Print basic summary statistics for numeric columns.

print(coffee.columns)
print(coffee.dtypes)
print("----------------------------------------------")
print(coffee.info())
'''

# 2. Data Selection
#Print only the Product and Cups_Sold columns for all entries.
# Print all rows where Product is "Latte".
'''
print("----------------------------------------------")
print(coffee.loc[:, ["Product", "Cups_Sold"]])
print(coffee[(coffee["Product"] == "Latte")])
'''

#3. Filtering & Masking
#Find all days where more than 70 cups were sold (any product).
#Show rows where Revenue is between 2000 and 2200.
'''
print("----------------------------------------------")
print(coffee[coffee["Cups_Sold"] > 70])
print(coffee[(coffee["Revenue"] >= 2000) & (coffee["Revenue"] <= 2200)])
'''

#4. Indexing & Slicing
#Print only the data for dates between 2025-10-03 and 2025-10-05 (inclusive).
#Select rows by integer index for the 5th to 10th entries using .iloc.

print(coffee.dtypes)
coffee["Date"] = pd.to_datetime(coffee["Date"])
print(coffee.dtypes)
print(coffee[(coffee["Date"] >= "2025-10-03") & (coffee["Date"] <= "2025-10-05")])
print("----------------------------------------------")
print(coffee.iloc[5:10])