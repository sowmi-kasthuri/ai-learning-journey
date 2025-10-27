# Week 2 Detailed Plan
## Python Deep Dive + Data Handling

**Dates:** October 21-27, 2025  
**Goal:** Master exceptions, libraries, data handling (NumPy/Pandas basics)

---

## WEEK 2 OVERVIEW

### Learning Focus:
- Exception handling (try/except)
- Python libraries and modules
- NumPy for arrays and math
- Pandas for data manipulation
- CSV/JSON file handling

### Weekly Goals:
- [✅] CS50 Lectures 3-4 completed
- [✅] Problem Sets 3-4 solved
- [✅] NumPy basics practiced
- [✅] Pandas fundamentals learned
- [ ] 25+ Exercism problems solved
- [ ] 1 data analysis project built
- [✅ ] 7 consecutive days coding 🟩🟩🟩🟩🟩🟩🟩

---

## DAY 6 - MONDAY, OCT 21

### Morning Session (6:00-8:00 AM)

**CS50 Lecture 3: Exceptions** (2 hours)
- **Link:** https://cs50.harvard.edu/python/2022/weeks/3/

**Topics:**
- try and except
- ValueError, KeyError, etc.
- else clause
- finally clause
- raise (creating exceptions)
- Custom exceptions

**Practice:**
```python
# Example: Safe division
def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("Cannot divide by zero")
        return None
    else:
        return result
    finally:
        print("Division attempted")
```

**Create:** `week2/lecture3-examples.py`
- Code all lecture examples
- Try different exception types
- Experiment with try/except/else/finally

### Evening Session (7:00-9:30 PM)

**7:00-7:15 PM: Review** (15 min)
- Re-run morning examples
- Try writing exception handling from memory

**7:15-8:30 PM: Problem Set 3** (75 min)
- **Link:** https://cs50.harvard.edu/python/2022/psets/3/

**Problems:**
1. **Fuel Gauge** - Convert fraction, handle exceptions
2. **Felipe's Taqueria** - Menu with error handling
3. **Grocery List** - Count items with dict
4. **Outdated** - Date format conversion

**8:30-9:15 PM: Exercism** (45 min)
- Do 5 problems focusing on exception handling
- Any unlocked problems are fine
- Focus on clean error handling

**9:15-9:30 PM: Git Push** (15 min)
```bash
git add .
git commit -m "Day 6: Exceptions - Lecture 3 + Problem Set 3"
git push
```

**Day 6 Goals:**
- [✅] Understand try/except/else/finally
- [✅] Handle multiple exception types
- [✅] Problem Set 3 complete
- [✅] 5 Exercism problems solved

---

## DAY 7 - TUESDAY, OCT 22

### Morning Session (6:00-8:00 AM)

**CS50 Lecture 4: Libraries** (2 hours)
- **Link:** https://cs50.harvard.edu/python/2022/weeks/4/

**Topics:**
- import statement
- from keyword
- Python standard library
- random module
- statistics module
- Command-line arguments (sys.argv)
- pip and PyPI
- Custom modules

**Practice:**
```python
import random
import statistics

# Random number
num = random.randint(1, 10)

# Statistics
data = [1, 2, 3, 4, 5]
mean = statistics.mean(data)
```

**Create:** `week2/lecture4-examples.py`

### Evening Session (7:00-9:30 PM)

**7:00-7:15 PM: Review** (15 min)

**7:15-8:30 PM: Problem Set 4** (75 min)
- **Link:** https://cs50.harvard.edu/python/2022/psets/4/

**Problems:**
1. **Emojize** - Use emoji library
2. **Frank, Ian and Glen's Letters** - Use Figlet
3. **Adieu, Adieu** - Use inflect library
4. **Guessing Game** - random numbers
5. **Little Professor** - Math practice game
6. **Bitcoin Price Index** - API requests (if covered)

**Note:** Some need `pip install` - follow instructions!

**8:30-9:15 PM: Exercism** (45 min)
- 5 problems using imports/modules

**9:15-9:30 PM: Git Push**
```bash
git add .
git commit -m "Day 7: Libraries - Lecture 4 + Problem Set 4"
git push
```

**Day 7 Goals:**
- [✅] Understand import and modules
- [✅] Use random, statistics libraries
- [✅] Install packages with pip
- [✅] Problem Set 4 complete

---

## DAY 8 - WEDNESDAY, OCT 23

### Morning Session (6:00-8:00 AM)

**NumPy Basics** (2 hours)

**Resources:**
- NumPy Quickstart: https://numpy.org/doc/stable/user/quickstart.html
- Real Python NumPy: https://realpython.com/numpy-tutorial/

**Topics:**
- Arrays vs lists
- Creating arrays
- Array operations
- Indexing and slicing
- Basic math operations

**Practice:**
```python
import numpy as np

# Create array
arr = np.array([1, 2, 3, 4, 5])

# Operations
print(arr * 2)  # [2, 4, 6, 8, 10]
print(arr.mean())  # 3.0
print(arr.sum())  # 15

# 2D array
matrix = np.array([[1, 2], [3, 4]])
print(matrix.shape)  # (2, 2)
```

**Create:** `week2/numpy-practice.py`
- Try array creation
- Math operations
- Indexing/slicing

### Evening Session (7:00-9:30 PM)

**7:00-8:00 PM: NumPy Exercises** (60 min)
- Create arrays different ways
- Practice math operations
- Work with 2D arrays
- Solve 3-5 simple NumPy problems online

**8:00-9:00 PM: Exercism** (60 min)
- 5 problems (any unlocked)

**9:00-9:30 PM: Git Push + Reflection**
```bash
git add .
git commit -m "Day 8: NumPy basics and practice"
git push
```

**Day 8 Goals:**
- [✅] Understand NumPy arrays
- [✅] Do basic array operations
- [✅] Know when to use NumPy vs lists

---

## DAY 9 - THURSDAY, OCT 24

### Morning Session (6:00-8:00 AM)

**Pandas Basics** (2 hours)

**Resources:**
- Pandas Getting Started: https://pandas.pydata.org/docs/getting_started/intro_tutorials/
- Kaggle Pandas: https://www.kaggle.com/learn/pandas

**Topics:**
- DataFrames and Series
- Reading CSV files
- Selecting data
- Filtering rows
- Basic operations

**Practice:**
```python
import pandas as pd

# Create DataFrame
data = {
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35],
    'city': ['Chennai', 'Mumbai', 'Delhi']
}
df = pd.DataFrame(data)

# Operations
print(df.head())
print(df['age'].mean())
print(df[df['age'] > 28])
```

**Create:** `week2/pandas-practice.py`
- Create DataFrames
- Read sample CSV
- Filter and select data

### Evening Session (7:00-9:30 PM)

**7:00-8:30 PM: Pandas Practice** (90 min)
- Download sample CSV (use Kaggle datasets)
- Read it with pandas
- Practice filtering, selecting
- Calculate statistics
- Export results

**8:30-9:15 PM: Exercism** (45 min)
- 5 problems

**9:15-9:30 PM: Git Push**
```bash
git add .
git commit -m "Day 9: Pandas basics and CSV handling"
git push
```

**Day 9 Goals:**
- [✅] Read/write CSV files
- [✅] Filter DataFrame rows
- [✅] Calculate basic statistics
- [✅] Understand DataFrame structure

---

## DAY 10 - FRIDAY, OCT 25

### Morning Session (6:00-8:00 AM)

**Data Cleaning Practice** (2 hours)

**Focus:**
- Handling missing data
- Data type conversions
- String cleaning
- Removing duplicates

**Practice:**
```python
import pandas as pd

# Read messy data
df = pd.read_csv('messy_data.csv')

# Clean it
df = df.drop_duplicates()
df = df.dropna()  # Remove missing values
df['column'] = df['column'].str.strip()  # Clean strings
```

**Create:** `week2/data-cleaning-practice.py`

### Evening Session (7:00-9:30 PM)

**7:00-8:00 PM: Mini Data Project** (60 min)
- Find a simple dataset (Kaggle)
- Clean it
- Answer 3-5 questions about it
- Create simple analysis

**8:00-9:00 PM: Exercism** (60 min)
- 5 problems

**9:00-9:30 PM: Git Push + Week 2 Summary**
```bash
git add .
git commit -m "Day 10: Data cleaning + mini analysis project"
git push
```

**Day 10 Goals:**
- [✅] Clean messy data
- [✅] Handle missing values
- [✅] Perform basic analysis
- [✅] Export clean data

---

## WEEKEND - DAYS 11-12 (OCT 26-27)

### Saturday - Day 11

**Morning (9:00 AM-12:00 PM):**

**Project Planning** (1 hour)
- Choose data project idea:
  1. **CSV Data Analyzer** - Read CSV, generate statistics, export report
  2. **Data Cleaner Tool** - Clean messy CSV files automatically
  3. **Simple Data Dashboard** - Read data, show insights

**Project Building** (2 hours)
- Set up project structure
- Write main functions
- Implement core logic

**Afternoon (2:00-5:00 PM):**
- Complete project features
- Test with different datasets
- Add error handling
- Document code

**Evening:**
- 5 Exercism problems
- Git push

### Sunday - Day 12

**Morning (9:00 AM-12:00 PM):**
- Polish project
- Add README.md
- Test edge cases
- Final touches

**Afternoon (2:00-4:00 PM):**
- Deploy/organize project in GitHub
- Write project documentation
- Create sample output

**Evening (7:00-8:00 PM):**
- Week 2 reflection
- Plan Week 3
- Celebrate! 🎉

---

## WEEK 2 PROJECT IDEAS

### Project 1: CSV Data Analyzer
**Features:**
- Read any CSV file
- Show column statistics (mean, median, mode)
- Count missing values
- Export summary report
- Handle errors gracefully

### Project 2: Data Cleaner
**Features:**
- Remove duplicates
- Fill/remove missing values
- Clean string columns
- Convert data types
- Export cleaned CSV

### Project 3: Sales Data Dashboard (Simple)
**Features:**
- Read sales CSV
- Calculate total sales
- Find best/worst products
- Show monthly trends
- Export report

---

## WEEK 2 SUCCESS METRICS

By Sunday, Oct 27:

**Learning:**
- [✅] Exceptions mastered
- [✅] Can use Python libraries
- [✅] NumPy basics solid
- [✅] Pandas fundamentals clear
- [✅] Can read/clean CSV data

**Output:**
- [✅] Lectures 3-4 ✅
- [✅] Problem Sets 3-4 ✅
- [✅] 25+ Exercism problems ✅
- [❌] 1 data project built - Couldnt do.  Got bogged down on Pandas
- [✅] 7 consecutive coding days 🟩×7

**GitHub:**
- [✅] week2/ folder organized
- [✅] All code committed
- [❌] Project with README - Got tied down on Pandas
- [✅] 12/70 green squares total

---

## RESOURCES

**CS50 Python:**
- Lecture 3: https://cs50.harvard.edu/python/2022/weeks/3/
- Lecture 4: https://cs50.harvard.edu/python/2022/weeks/4/

**NumPy:**
- Official tutorial: https://numpy.org/doc/stable/user/quickstart.html
- Real Python: https://realpython.com/numpy-tutorial/

**Pandas:**
- 10 min intro: https://pandas.pydata.org/docs/user_guide/10min.html
- Kaggle course: https://www.kaggle.com/learn/pandas

**Datasets:**
- Kaggle: https://www.kaggle.com/datasets
- (Choose small, simple CSV files)

**Exercism:**
- Python track: https://exercism.org/tracks/python

---

## TIPS FOR WEEK 2

1. **Exception handling** - Use it everywhere, makes code robust
2. **Libraries** - Don't memorize, learn to read docs
3. **NumPy** - Think in arrays, not loops
4. **Pandas** - Most powerful for data work
5. **Practice daily** - Consistency > intensity

---

## WEEK 2 vs WEEK 1

**Week 1:** Python basics (functions, conditionals, loops)  
**Week 2:** Python tools (exceptions, libraries, data handling)

**After Week 2, you'll have:**
- Solid Python foundation ✅
- Can handle real data ✅
- Ready for APIs (Week 3) ✅
- Ready for AI (Week 5+) ✅

---

**LET'S CRUSH WEEK 2!** 🔥💪🚀