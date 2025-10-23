# numpy basics practise - video by Keith Galli.
# https://www.youtube.com/watch?v=QUT1VHiLmmI
import numpy as np
#print(f"Numpy version is : {np.__version__}")

'''
# 1D array
a = np.array([10,20,30])
print(f"the array is {a}")
print(f"Dimension of {a} is {a.ndim}")

# 2D array
b = np.array([[5,6,7],[8,9,10]])
print(f"the array is {b}")
print(f"Dimension of {b} is {b.ndim}")

# 3D array
c = np.array([[1,1,1],[1,1,1],[1,1,1]])
print(f"the array is {c}")
'''

'''
# Create ana 1D array of 5 random numbers between 0 and 1.
random_arr = np.random.randint(0, 10, size=5)
print(random_arr)
'''

'''
# 2D array (say, 3 rows and 3 columns) with random integers.
random_matrix = np.random.randint(0, 10, size=(3,3))
print(random_matrix)
'''

'''
# 2D array (say, 3 rows and 3 columns) with random floats.
random_matrix = np.random.rand(3,3) # automatically generates random floats between 1 and 0
print(random_matrix)
'''
'''
# 2D array (say, 3 rows and 3 columns) with random floats.
random_matrix = np.random.rand(3,3) * 50 # generates random floats between 0 and 50
print(random_matrix)
random_matrix = np.round(random_matrix,2) # restricting to 2 decimal points
print(random_matrix)
'''
'''
a = np.array([10,20,30], dtype='int16')
b = np.array([[5,6,7],[8,9,10]])
c =  np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
print(a)
print(b)

print(f"Shape of a : {a.shape}") # to get shape
print(f"Shape of b : {b.shape}")
print(f"Size of a : {a.size}") # to get size
print(f"Size of b : {b.size}")
print(f"ItemSize of a : {a.itemsize}") # to get itemsize (bytestorage)
print(f"ItemSize of b : {b.itemsize}")
print(f"Dtype of a is :{a.dtype}") # dtype
print(f"Dtype of b is :{b.dtype}") # dtype

print(c)
print(f"The item in c[2,4] is {c[1,3]}") # specific item in an array.  python uses 0 index
print(f"The item in c[2,4] is {c[1,-4]}") # same as above but negative index.
print(f"The items in row 2 of c are {c[1, :]}") # get a specific row items.  again index 0
print(f"The items in column 2 of c are {c[:, 1]}") # get a specific column items.  again index 0
print(f"Elements in row 2 of c; step by 2 : {c[1, 1:6:2]}") # print row 2 items 2,4,6 i.e. 9,11,13
'''
'''
arr_a = np.array([3,6,9,12])
arr_b = np.array([1,2,3,4])

arr_add = arr_a + arr_b
print(arr_add)

arr_sub = arr_a - arr_b
print(arr_sub)

arr_prod = arr_a * arr_b
print(arr_prod)

arr_div = arr_a / arr_b
print(arr_div)
'''


'''
arr_c = np.array([10,20,30,40,40])
arr_mean = arr_c.mean().astype(int)
arr_sum = arr_c.sum().astype(int)
print(arr_mean,arr_sum,arr_c.shape)
'''

'''
arr = np.array([10, 20, 30, 40, 50])
#print(arr[1:4:1])
#print(arr[3:])

mat = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(mat[1, :])
print(mat[:, 2])

arr2 = np.array([1, 2, 3, 4, 5, 6])
arr2_2x3 = arr2.reshape(2,3)
print(arr2)
print(arr2_2x3)
'''


'''
Create a NumPy array for daily temperatures: [20][22][21][19][23][25][22].
Print average, maximum, and minimum temperature for the week.


temp = np.array([20,22,21,19,23,25,22])
temp_max = temp.max()
temp_min = temp.min()
temp_mean = int(temp.mean())
print(temp_mean, temp_max, temp_min)
'''

'''
Sales Data Matrix:

Create a 2D NumPy array for sales data:
[[12][18][11], [16][22][19], [14][17][15], [20][25][22]]

Tasks:
Print sales for the second day.
Print total sales for product 3 (third column) across all days.

sales = np.array([[12, 18, 11], [16, 22, 19], [14, 17, 15], [20, 25, 22]])
print(sales)
print(sales[1, :])
print(sales[:, 2])
print(f"Total Sales of day 3 : {sales[:, 2].sum()}")

'''

'''
Filter High Temperatures
Using your temp array from earlier ([20][22][21][19][23][25][22]):

Create a new array containing only the temperatures greater than 22.
Print this filtered array.

temp = np.array([20, 22, 21, 19, 23, 25, 22])
temp1 = temp[temp > 22]
print(temp1)
'''

'''
Your sales matrix from earlier:

sales = np.array([[12, 18, 11],
                  [16, 22, 19],
                  [14, 17, 15],
                  [20, 25, 22]])
Tasks:
Reshape it to shape (2, 6)
Print the reshaped matrix
Print the sum of all sales (all numbers in the reshaped array)

sales = np.array([[12, 18, 11], [16, 22, 19], [14, 17, 15], [20, 25, 22]])
sales_2x6 = sales.reshape(2,6)
sales_sum = sales_2x6.sum()

print(sales)
print("      ")
print(sales_2x6)
print("      ")
print(sales_sum)

'''

'''
Problem 5: Dice Simulation

Task:
Simulate rolling a six-sided die 10 times (random integers 1–6).
Print the resulting array.
Print the number of times you rolled a “6”.


dice = np.random.randint(1,7, size=10)
print(dice)
print("      ")

six_count = (dice == 6).sum()
print(six_count)
'''

'''
Problem 6: Slicing Practice
Using your temperatures array (temp = np.array([20][22][21][19][23][25][22])):
Print the temperatures for days 2 to 5 (inclusive).
'''
temp = np.array([20, 22, 21, 19, 23, 25, 22])
print(temp[1:6:1])