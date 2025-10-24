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
print(coffee.loc[coffee["Cups_Sold"] >= 65].sort_values("Cups_Sold", ascending=1))
print("----------------------------------------------")
print(coffee[coffee["Cups_Sold"] >= 65].sort_values("Cups_Sold", ascending=1)) # this will also work
print("----------------------------------------------")
print(coffee[(coffee["Cups_Sold"] >= 65) & (coffee["Product"] == "Latte")])