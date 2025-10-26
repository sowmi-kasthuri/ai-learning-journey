# 🐼 Pandas Quick Sheet — Covers 80% of Practical Use

> **Goal:** A concise, hands-on reference to cover the Pandas operations you’ll use most often in AIML engineering.

---

## 📦 Setup
```python
import pandas as pd
import numpy as np

📥 Load and Save Data
Load from common file formats

df = pd.read_csv('data.csv')
df = pd.read_excel('data.xlsx')
df = pd.read_json('data.json')

Save DataFrames back to files
df.to_csv('output.csv', index=False)
df.to_excel('output.xlsx', index=False)
df.to_parquet('output.parquet')  # Faster + compressed

👀 Explore Data
Inspect structure and summary info

df.head()          # first 5 rows
df.tail(3)         # last 3 rows
df.shape           # (rows, columns)
df.info()          # data types, non-null counts
df.describe()      # summary stats (mean, std, etc.)
df.columns         # list of column names
df.dtypes          # column data types
df['col'].unique() # unique values
df['col'].value_counts()  # frequency counts


🎯 Select and Filter Rows / Columns
Column selection

df['col']                     # single column
df[['col1', 'col2']]          # multiple columns

Row access by position or label
df.iloc[0]                    # first row (by position)
df.loc[0, 'col']              # row 0, specific column

Conditional filtering
df.loc[df['age'] > 30]
df.loc[(df['age'] > 30) & (df['city'] == 'NY')]
df.query('age > 30 and city == "NY"')  # cleaner syntax


🧩 Modify Columns
Create, rename, drop, change types

df['new'] = df['a'] + df['b']                     # add new column
df.rename(columns={'old': 'new'}, inplace=True)
df.drop(columns=['unwanted'], inplace=True)
df['col'] = df['col'].astype('category')          # change data type
df['col'] = df['col'].fillna(0)                   # fill missing
df['col'] = df['col'].replace({'old': 'new'})     # replace values

🧼 Clean Data
Handle missing values and duplicates

df.isnull().sum()         # count missing per column
df.dropna(inplace=True)   # drop rows with NaNs
df.fillna(0, inplace=True)
df.duplicated().sum()     # count duplicates
df.drop_duplicates(inplace=True)

🔢 Sorting and Indexing
Sort and manage indices

df.sort_values('col', ascending=False)
df.reset_index(drop=True, inplace=True)
df.set_index('id', inplace=True)

📊 Aggregation and Grouping
Group and summarize

df.groupby('category')['sales'].sum()
df.groupby('category')[['sales', 'profit']].agg(['mean', 'sum'])
df.pivot_table(values='sales', index='region', columns='year', aggfunc='sum')

🔗 Merge, Join, Combine
Combine multiple DataFrames

pd.concat([df1, df2])                    # stack vertically
pd.concat([df1, df2], axis=1)            # side-by-side
pd.merge(df1, df2, on='id')              # inner join
pd.merge(df1, df2, on='id', how='left')  # left join

🧮 Apply Functions
Apply transformations to columns or rows

df['new'] = df['col'].apply(lambda x: x * 2)
df.apply(np.sum, axis=0)  # sum by column
df.apply(np.sum, axis=1)  # sum by row

🕵️‍♀️ Handy Utilities
Quick insights and diagnostics

df.sample(5)                # random sample
df.nunique()                # unique counts per column
df.memory_usage(deep=True)  # memory footprint
df.corr(numeric_only=True)  # correlation matrix

⚡ Performance Tips
Keep your workflow efficient

# Prefer Parquet over CSV for large files
df.to_parquet('data.parquet')

# Define dtypes upfront to save memory
df = pd.read_csv('data.csv', dtype={'id': 'int32', 'category': 'category'})

# Avoid loops and .apply() for speed; use vectorized ops
df['x'] = df['a'] + df['b']

🧠 Remember
    Pandas is in-memory — optimize for available RAM.
    Think vectorized, not iterative.
    You don’t need every function; just master these workflows.

🏁 Once fluent here, you’re 80–90% ready for any data-cleaning or feature-prep task in ML pipelines.

---
Type        |  Typical Uses in Pandas                                               
------------+-----------------------------------------------------------------------
List        |  Selecting multiple columns, dropping columns, assigning new col/index
Dictionary  |  Mapping values, renaming columns, replacing, groupby aggregation     
Tuple       |  MultiIndex, advanced slicing/indexing, hierarchical data             
Scalar      |  Assigning a constant value to an entire column                       
Set         |  Membership tests with.isin()                                         

Rule of Thumb:

Scalar: Use to assign a single value to a DataFrame column or Series.
List: Use for ordered selection or when acting on multiple items.
Dictionary: Use for mapping old values/names to new ones, or for aggregation/grouping.
Tuple: Use for hierarchical/multi-level indexing or slicing.
Set: Use for checking if an element is in a group with .isin().