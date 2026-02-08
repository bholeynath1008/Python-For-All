# Pandas Tutorial for Beginners
## (Python Data Analysis Library)

---

## Table of Contents
1. [Introduction to Pandas](#introduction)
2. [Python vs Pandas: Why Use Pandas?](#comparison)
3. [Pandas Series](#series)
4. [Pandas DataFrame](#dataframe)
5. [DataFrame Operations](#operations)
6. [Combining DataFrames](#combining)

---

## 1. Introduction to Pandas {#introduction}

### What is Pandas?
Pandas is a powerful Python library for data manipulation and analysis. It provides two main data structures: **Series** (1D) and **DataFrame** (2D).

### Why Use Pandas?
- Works seamlessly with tabular data (like Excel spreadsheets, CSV files)
- Powerful data manipulation and cleaning tools
- Built on top of NumPy (fast and efficient)
- Essential for data science, machine learning, and data analysis

### Installation
```python
# Install using pip
pip install pandas

# Import Pandas
import pandas as pd

# Also import NumPy (Pandas works well with NumPy)
import numpy as np
```

---

## 2. Python vs Pandas: Why Use Pandas? {#comparison}

### Example 1: Working with Tabular Data

```python
import pandas as pd

# Using Pure Python (Lists and Dictionaries)
# Imagine you have student data: Name, Age, Grade

students_python = [
    {"Name": "Alice", "Age": 20, "Grade": 85},
    {"Name": "Bob", "Age": 22, "Grade": 90},
    {"Name": "Charlie", "Age": 21, "Grade": 78}
]

# To get all grades - Need a loop!
grades_python = []
for student in students_python:
    grades_python.append(student["Grade"])
print("Python Grades:", grades_python)
# Output: Python Grades: [85, 90, 78]

# To calculate average grade - Need another loop!
total = 0
for grade in grades_python:
    total += grade
average_python = total / len(grades_python)
print("Python Average:", average_python)
# Output: Python Average: 84.33

# Using Pandas (DataFrame)
# Create DataFrame from dictionary
students_pandas = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [20, 22, 21],
    "Grade": [85, 90, 78]
})

# Get all grades - No loop needed!
grades_pandas = students_pandas["Grade"]
print("Pandas Grades:")
print(grades_pandas)
# Output: 
# 0    85
# 1    90
# 2    78
# Name: Grade, dtype: int64

# Calculate average - Built-in function!
average_pandas = students_pandas["Grade"].mean()
print("Pandas Average:", average_pandas)
# Output: Pandas Average: 84.33333333333333
```

**Key Difference**: Pandas has built-in functions for data analysis. Python needs manual loops!

### Example 2: Filtering Data

```python
import pandas as pd

# Using Pure Python (List of Dictionaries)
employees_python = [
    {"Name": "John", "Age": 28, "Salary": 50000},
    {"Name": "Emma", "Age": 32, "Salary": 65000},
    {"Name": "Mike", "Age": 25, "Salary": 45000},
    {"Name": "Sarah", "Age": 35, "Salary": 75000}
]

# Filter employees with salary > 50000 - Need a loop!
high_earners_python = []
for emp in employees_python:
    if emp["Salary"] > 50000:
        high_earners_python.append(emp)
print("Python High Earners:")
for emp in high_earners_python:
    print(f"  {emp['Name']}: ${emp['Salary']}")
# Output:
# Python High Earners:
#   Emma: $65000
#   Sarah: $75000

# Using Pandas (DataFrame)
employees_pandas = pd.DataFrame({
    "Name": ["John", "Emma", "Mike", "Sarah"],
    "Age": [28, 32, 25, 35],
    "Salary": [50000, 65000, 45000, 75000]
})

# Filter employees with salary > 50000 - One line!
high_earners_pandas = employees_pandas[employees_pandas["Salary"] > 50000]
print("Pandas High Earners:")
print(high_earners_pandas)
# Output:
#     Name  Age  Salary
# 1   Emma   32   65000
# 3  Sarah   35   75000
```

**Key Difference**: Pandas filtering is like SQL queries. Python needs manual loops!

### Example 3: Combining Data from Multiple Sources

```python
import pandas as pd

# Using Pure Python (Lists)
# Data from first source
sales_jan = [{"Product": "A", "Sales": 100}, {"Product": "B", "Sales": 150}]
# Data from second source
sales_feb = [{"Product": "A", "Sales": 120}, {"Product": "B", "Sales": 140}]

# Combine manually - Complex!
all_sales_python = []
for item in sales_jan:
    all_sales_python.append({"Product": item["Product"], "Jan": item["Sales"]})

for i, item in enumerate(all_sales_python):
    for feb_item in sales_feb:
        if item["Product"] == feb_item["Product"]:
            all_sales_python[i]["Feb"] = feb_item["Sales"]

print("Python Combined:")
for item in all_sales_python:
    print(f"  Product {item['Product']}: Jan={item['Jan']}, Feb={item['Feb']}")
# Output:
# Python Combined:
#   Product A: Jan=100, Feb=120
#   Product B: Jan=150, Feb=140

# Using Pandas (DataFrames)
sales_jan_df = pd.DataFrame({
    "Product": ["A", "B"],
    "Jan": [100, 150]
})

sales_feb_df = pd.DataFrame({
    "Product": ["A", "B"],
    "Feb": [120, 140]
})

# Combine with merge - One line!
combined_pandas = pd.merge(sales_jan_df, sales_feb_df, on="Product")
print("Pandas Combined:")
print(combined_pandas)
# Output:
#   Product  Jan  Feb
# 0       A  100  120
# 1       B  150  140
```

**Key Difference**: Pandas has powerful merge/join operations. Python requires complex logic!

### Summary: Python vs Pandas

| Task | Python (Lists/Dicts) | Pandas (DataFrame) | Winner |
|------|---------------------|-------------------|---------|
| Store tabular data | List of dictionaries | DataFrame | Pandas ✅ |
| Calculate statistics | Manual loops | Built-in functions (.mean(), .sum()) | Pandas ✅ |
| Filter data | Loop with if statements | Boolean indexing | Pandas ✅ |
| Combine data | Complex manual logic | .merge(), .concat() | Pandas ✅ |
| Handle missing data | Custom code | Built-in handling | Pandas ✅ |
| Read CSV/Excel files | Custom parsing | .read_csv(), .read_excel() | Pandas ✅ |

**Conclusion**: For data analysis and manipulation, Pandas is MUCH easier and faster than pure Python!

---

## 3. Pandas Series {#series}

### What is a Pandas Series?
- **Series** = One-dimensional (1D) array holding data of any type
- Think of it as a **single column** in a spreadsheet
- Like a NumPy array, but with **labels** (index)

### Rule: Series Structure
```
Index    Value
  0  →   10
  1  →   20
  2  →   30
```

### Method 1: Create Series from List

```python
import pandas as pd

# Create list
numbers_list = [10, 20, 30]

# Convert to Series
series_from_list = pd.Series(numbers_list)
print(series_from_list)
# Output:
# 0    10    ← Index 0, Value 10
# 1    20    ← Index 1, Value 20
# 2    30    ← Index 2, Value 30
# dtype: int64

# Check type
print(type(series_from_list))
# Output: <class 'pandas.core.series.Series'>

# Check shape
print(series_from_list.shape)
# Output: (3,)  # 3 elements in 1D
```

### Method 2: Create Series from NumPy Array

```python
import numpy as np
import pandas as pd

# Create NumPy array
numpy_array = np.array([10, 20, 30])

# Convert to Series
series_from_array = pd.Series(numpy_array)
print(series_from_array)
# Output:
# 0    10
# 1    20
# 2    30
# dtype: int32

# Create Series with custom index labels
series_custom_index = pd.Series(numpy_array, index=["first", "second", "third"])
print(series_custom_index)
# Output:
# first     10
# second    20
# third     30
# dtype: int32
```

### Method 3: Create Series from Dictionary

```python
import pandas as pd

# Create dictionary
# Rule: Dictionary keys become index, values become data
data_dict = {'math': 85, 'science': 90, 'english': 78}

# Convert to Series
series_from_dict = pd.Series(data_dict)
print(series_from_dict)
# Output:
# math       85
# science    90
# english    78
# dtype: int64
```

### Rule: Understanding dtype
- `dtype: int64` → Integer numbers (64-bit)
- `dtype: int32` → Integer numbers (32-bit, from NumPy)
- `dtype: float64` → Decimal numbers
- `dtype: object` → Text/strings or mixed types

### Series Operations

```python
grades = pd.Series([85, 90, 78, 92, 88])

# Get statistics
print("Mean:", grades.mean())        # Output: Mean: 86.6
print("Max:", grades.max())          # Output: Max: 92
print("Min:", grades.min())          # Output: Min: 78
print("Sum:", grades.sum())          # Output: Sum: 433
print("Standard Dev:", grades.std()) # Output: Standard Dev: 5.27

# Access by index
print(grades[0])      # Output: 85 (first element)
print(grades[2])      # Output: 78 (third element)

# Filter
high_grades = grades[grades > 85]
print(high_grades)
# Output:
# 1    90
# 3    92
# 4    88
# dtype: int64
```

---

## 4. Pandas DataFrame {#dataframe}

### What is a Pandas DataFrame?
- **DataFrame** = 2-dimensional data structure (table with rows and columns)
- Like a spreadsheet or SQL table
- Most commonly used Pandas object

### Rule: DataFrame Structure
```
        Column1  Column2  Column3
Index0     1        2        3
Index1     4        5        6
```

### Method 1: Create DataFrame from Dictionary

```python
import pandas as pd

# Rule: Dictionary format for DataFrame
# Key = Column name, Value = List of column data

# Example 1: Simple DataFrame
data_dict = {
    'col1': [1, 2], 
    'col2': [3, 4]
}

df = pd.DataFrame(data_dict)
print(df)
# Output:
#    col1  col2
# 0     1     3
# 1     2     4

print(type(df))
# Output: <class 'pandas.core.frame.DataFrame'>

print(df.shape)
# Output: (2, 2)  # 2 rows, 2 columns

# Example 2: Realistic DataFrame
employee_data = {
    'Age': [22, 30, 23, 25, 24],
    'Salary': [28000, 17000, 46000, 42000, 55000],
    'Gender': ["M", "F", "M", "M", "F"]
}

df_employees = pd.DataFrame(employee_data)
print(df_employees)
# Output:
#    Age  Salary Gender
# 0   22   28000      M
# 1   30   17000      F
# 2   23   46000      M
# 3   25   42000      M
# 4   24   55000      F
```

### Method 2: Create DataFrame from Nested List

```python
import pandas as pd

# Rule: Each inner list = one row
data_nested = [[1, 2, 3], 
               [4, 5, 6]]

# Must specify column names
df_from_list = pd.DataFrame(data_nested, columns=["col_a", "col_b", "col_c"])
print(df_from_list)
# Output:
#    col_a  col_b  col_c
# 0      1      2      3
# 1      4      5      6
```

### Method 3: Create DataFrame from 2D NumPy Array

```python
import numpy as np
import pandas as pd

# Create 2D NumPy array
array_2d = np.array([[1, 2, 3], 
                     [4, 5, 6]])

# Convert to DataFrame with custom row and column names
df_from_array = pd.DataFrame(
    array_2d, 
    index=["row_1", "row_2"],           # Row labels
    columns=["col_x", "col_y", "col_z"] # Column labels
)

print(df_from_array)
# Output:
#        col_x  col_y  col_z
# row_1      1      2      3
# row_2      4      5      6
```

### Understanding DataFrame Attributes

```python
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['NYC', 'LA', 'Chicago']
})

# Shape: (rows, columns)
print(df.shape)
# Output: (3, 3)

# Column names
print(df.columns)
# Output: Index(['Name', 'Age', 'City'], dtype='object')

# Row index
print(df.index)
# Output: RangeIndex(start=0, stop=3, step=1)

# Data types of each column
print(df.dtypes)
# Output:
# Name     object   ← Text/string
# Age       int64   ← Integer
# City     object   ← Text/string
# dtype: object

# First few rows
print(df.head())  # Shows first 5 rows by default
# Output: Shows entire DataFrame (only 3 rows)

# Last few rows
print(df.tail(2))  # Shows last 2 rows
# Output:
#       Name  Age     City
# 1      Bob   30       LA
# 2  Charlie   35  Chicago

# Summary statistics
print(df.describe())
# Output:
#              Age
# count   3.000000
# mean   30.000000
# std     5.000000
# min    25.000000
# 25%    27.500000
# 50%    30.000000
# 75%    32.500000
# max    35.000000

# Info about DataFrame
print(df.info())
# Output:
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 3 entries, 0 to 2
# Data columns (total 3 columns):
#  #   Column  Non-Null Count  Dtype 
# ---  ------  --------------  ----- 
#  0   Name    3 non-null      object
#  1   Age     3 non-null      int64 
#  2   City    3 non-null      object
```

---

## 5. DataFrame Operations {#operations}

### A. Setting and Resetting Index

```python
df = pd.DataFrame({
    'Age': [22, 30, 23, 25, 24],
    'Salary': [28000, 17000, 46000, 42000, 55000],
    'Gender': ["M", "F", "M", "M", "F"]
})

print("Original DataFrame:")
print(df)
# Output:
#    Age  Salary Gender
# 0   22   28000      M
# 1   30   17000      F
# 2   23   46000      M
# 3   25   42000      M
# 4   24   55000      F

# Set 'Age' column as index
df_indexed = df.set_index("Age")
print("\nAfter set_index('Age'):")
print(df_indexed)
# Output:
#      Salary Gender
# Age                
# 22    28000      M
# 30    17000      F
# 23    46000      M
# 25    42000      M
# 24    55000      F

# Reset index back to default (0, 1, 2, ...)
df_reset = df_indexed.reset_index()
print("\nAfter reset_index():")
print(df_reset)
# Output:
#    Age  Salary Gender
# 0   22   28000      M
# 1   30   17000      F
# 2   23   46000      M
# 3   25   42000      M
# 4   24   55000      F
```

### B. Dropping Rows

```python
df = pd.DataFrame({
    'Age': [22, 30, 23, 25, 24],
    'Salary': [28000, 17000, 46000, 42000, 55000],
    'Gender': ["M", "F", "M", "M", "F"]
})

# Drop single row by index
# Rule: drop(index=[list of indices])
df_drop_single = df.drop(index=[3])
print("After dropping row at index 3:")
print(df_drop_single)
# Output:
#    Age  Salary Gender
# 0   22   28000      M
# 1   30   17000      F
# 2   23   46000      M
# 4   24   55000      F
# Note: Row at index 3 is removed

# Drop multiple rows by index
df_drop_multiple = df.drop(index=[0, 1, 2])
print("\nAfter dropping rows 0, 1, 2:")
print(df_drop_multiple)
# Output:
#    Age  Salary Gender
# 3   25   42000      M
# 4   24   55000      F
```

### C. Dropping Columns

```python
df = pd.DataFrame({
    'Age': [22, 30, 23, 25, 24],
    'Salary': [28000, 17000, 46000, 42000, 55000],
    'Gender': ["M", "F", "M", "M", "F"]
})

# Drop single column
# Rule: drop(columns=["column_name"])
df_drop_col = df.drop(columns=["Age"])
print("After dropping 'Age' column:")
print(df_drop_col)
# Output:
#    Salary Gender
# 0   28000      M
# 1   17000      F
# 2   46000      M
# 3   42000      M
# 4   55000      F

# Drop multiple columns
df_drop_cols = df.drop(columns=["Age", "Gender"])
print("\nAfter dropping 'Age' and 'Gender' columns:")
print(df_drop_cols)
# Output:
#    Salary
# 0   28000
# 1   17000
# 2   46000
# 3   42000
# 4   55000
```

### D. Sorting DataFrames

```python
df = pd.DataFrame({
    'Age': [22, 30, 23, 25, 24],
    'Salary': [28000, 17000, 46000, 42000, 55000],
    'Gender': ["M", "F", "M", "M", "F"]
})

# Sort by Age in ascending order (smallest to largest)
# Rule: sort_values(by='column_name', ascending=True/False)
df_sorted_asc = df.sort_values(by='Age', ascending=True)
print("Sorted by Age (Ascending):")
print(df_sorted_asc)
# Output:
#    Age  Salary Gender
# 0   22   28000      M  ← Youngest
# 2   23   46000      M
# 4   24   55000      F
# 3   25   42000      M
# 1   30   17000      F  ← Oldest

# Sort by Age in descending order (largest to smallest)
df_sorted_desc = df.sort_values(by='Age', ascending=False)
print("\nSorted by Age (Descending):")
print(df_sorted_desc)
# Output:
#    Age  Salary Gender
# 1   30   17000      F  ← Oldest
# 3   25   42000      M
# 4   24   55000      F
# 2   23   46000      M
# 0   22   28000      M  ← Youngest

# Sort by Salary
df_sorted_salary = df.sort_values(by='Salary', ascending=False)
print("\nSorted by Salary (Descending - Highest first):")
print(df_sorted_salary)
# Output:
#    Age  Salary Gender
# 4   24   55000      F  ← Highest salary
# 2   23   46000      M
# 3   25   42000      M
# 0   22   28000      M
# 1   30   17000      F  ← Lowest salary
```

### E. Accessing Data in DataFrame

```python
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'Salary': [50000, 60000, 70000]
})

# Access single column (returns Series)
ages = df['Age']
print(ages)
# Output:
# 0    25
# 1    30
# 2    35
# Name: Age, dtype: int64

# Access multiple columns (returns DataFrame)
subset = df[['Name', 'Salary']]
print(subset)
# Output:
#       Name  Salary
# 0    Alice   50000
# 1      Bob   60000
# 2  Charlie   70000

# Access rows by index position (.iloc)
# iloc[row_index, column_index]
first_row = df.iloc[0]
print(first_row)
# Output:
# Name      Alice
# Age          25
# Salary    50000
# Name: 0, dtype: object

# Access specific cell
salary_bob = df.iloc[1, 2]  # Row 1, Column 2
print(salary_bob)
# Output: 60000

# Access by label (.loc)
# loc[row_label, column_label]
alice_data = df.loc[0, 'Name']
print(alice_data)
# Output: Alice

# Filter rows
high_earners = df[df['Salary'] > 55000]
print(high_earners)
# Output:
#       Name  Age  Salary
# 1      Bob   30   60000
# 2  Charlie   35   70000
```

---

## 6. Combining DataFrames {#combining}

### Understanding Combine Operations

There are two main ways to combine DataFrames:
1. **Concatenation** (`pd.concat()`) - Stack DataFrames together
2. **Merging** (`pd.merge()`) - Join DataFrames like SQL

### A. Concatenation

Concatenation is like **stacking** DataFrames:
- **axis=0**: Stack vertically (add rows below)
- **axis=1**: Stack horizontally (add columns to the right)

### Example DataFrames for Concatenation

```python
import pandas as pd

# DataFrame 1: City temperatures
df_temp = pd.DataFrame({
    "city": ["mumbai", "delhi", "bangalore", "hyderabad"],
    "temperature": [32, 45, 40, 36]
})
print("Temperature Data:")
print(df_temp)
# Output:
#         city  temperature
# 0     mumbai           32
# 1      delhi           45
# 2  bangalore           40
# 3  hyderabad           36

# DataFrame 2: City humidity
df_humidity = pd.DataFrame({
    "city": ["delhi", "mumbai", "bangalore", "chennai"],
    "humidity": [68, 65, 75, 70]
})
print("\nHumidity Data:")
print(df_humidity)
# Output:
#         city  humidity
# 0      delhi        68
# 1     mumbai        65
# 2  bangalore        75
# 3    chennai        70
```

### Concatenation: axis=1 (Horizontal - Add Columns Side by Side)

```python
# Rule: axis=1 → Stack DataFrames horizontally (side by side)
# Places DataFrames next to each other as additional columns

concat_horizontal = pd.concat([df_temp, df_humidity], axis=1)
print("Concatenate axis=1 (Horizontal - side by side):")
print(concat_horizontal)
# Output:
#         city  temperature       city  humidity
# 0     mumbai           32      delhi        68
# 1      delhi           45     mumbai        65
# 2  bangalore           40  bangalore        75
# 3  hyderabad           36    chennai        70

# Notice: 
# - Both 'city' columns appear (duplicate column names)
# - Rows are matched by INDEX (0→0, 1→1, 2→2, 3→3)
# - NOT matching by city name!
```

### Concatenation: axis=0 (Vertical - Stack Rows on Top)

```python
# Rule: axis=0 → Stack DataFrames vertically (one below the other)
# Adds rows from second DataFrame below first DataFrame

concat_vertical = pd.concat([df_temp, df_humidity], axis=0)
print("Concatenate axis=0 (Vertical - stacked):")
print(concat_vertical)
# Output:
#         city  temperature  humidity
# 0     mumbai         32.0       NaN
# 1      delhi         45.0       NaN
# 2  bangalore         40.0       NaN
# 3  hyderabad         36.0       NaN
# 0      delhi          NaN      68.0
# 1     mumbai          NaN      65.0
# 2  bangalore          NaN      75.0
# 3    chennai          NaN      70.0

# Notice:
# - NaN = Missing value (Not a Number)
# - First 4 rows from df_temp (temperature data, humidity is NaN)
# - Next 4 rows from df_humidity (humidity data, temperature is NaN)
# - Index repeats: 0,1,2,3,0,1,2,3
```

### Concatenation: ignore_index=True

```python
# Rule: ignore_index=True → Create new sequential index (0,1,2,3,...)
# Useful when you don't care about original indices

concat_ignore_index = pd.concat([df_temp, df_humidity], ignore_index=True)
print("Concatenate with ignore_index=True:")
print(concat_ignore_index)
# Output:
#         city  temperature  humidity
# 0     mumbai         32.0       NaN
# 1      delhi         45.0       NaN
# 2  bangalore         40.0       NaN
# 3  hyderabad         36.0       NaN
# 4      delhi          NaN      68.0
# 5     mumbai          NaN      65.0
# 6  bangalore          NaN      75.0
# 7    chennai          NaN      70.0

# Notice:
# - Index is now 0-7 (sequential)
# - No more duplicate indices
```

### B. Merging DataFrames

Merging is like **SQL JOIN** operations - combines DataFrames based on a common column.

### Types of Merges (Joins)

| Merge Type | Description | SQL Equivalent |
|-----------|-------------|----------------|
| **left** | Keep all rows from left DataFrame | LEFT JOIN |
| **right** | Keep all rows from right DataFrame | RIGHT JOIN |
| **inner** | Keep only matching rows (intersection) | INNER JOIN |
| **outer** | Keep all rows from both (union) | FULL OUTER JOIN |

### Left Join

```python
# Rule: LEFT JOIN → Keep ALL rows from left DataFrame
# Add matching data from right DataFrame
# If no match found, fill with NaN

left_join = pd.merge(df_temp, df_humidity, on='city', how='left')
print("LEFT JOIN (keep all from df_temp):")
print(left_join)
# Output:
#         city  temperature  humidity
# 0     mumbai           32      65.0
# 1      delhi           45      68.0
# 2  bangalore           40      75.0
# 3  hyderabad           36       NaN  ← No match in df_humidity

# Explanation:
# - All 4 cities from df_temp are kept
# - mumbai, delhi, bangalore: Found in df_humidity → humidity added
# - hyderabad: NOT found in df_humidity → humidity is NaN
```

### Right Join

```python
# Rule: RIGHT JOIN → Keep ALL rows from right DataFrame
# Add matching data from left DataFrame
# If no match found, fill with NaN

right_join = pd.merge(df_temp, df_humidity, on='city', how='right')
print("RIGHT JOIN (keep all from df_humidity):")
print(right_join)
# Output:
#         city  temperature  humidity
# 0      delhi         45.0        68
# 1     mumbai         32.0        65
# 2  bangalore         40.0        75
# 3    chennai          NaN        70  ← No match in df_temp

# Explanation:
# - All 4 cities from df_humidity are kept
# - delhi, mumbai, bangalore: Found in df_temp → temperature added
# - chennai: NOT found in df_temp → temperature is NaN
```

### Inner Join

```python
# Rule: INNER JOIN → Keep ONLY rows that exist in BOTH DataFrames
# Most restrictive - only matching data

inner_join = pd.merge(df_temp, df_humidity, on='city', how='inner')
print("INNER JOIN (only common cities):")
print(inner_join)
# Output:
#         city  temperature  humidity
# 0     mumbai           32        65
# 1      delhi           45        68
# 2  bangalore           40        75

# Explanation:
# - Only 3 cities appear in BOTH DataFrames
# - hyderabad (only in df_temp) → EXCLUDED
# - chennai (only in df_humidity) → EXCLUDED
# - No NaN values in result!
```

### Outer Join

```python
# Rule: OUTER JOIN → Keep ALL rows from BOTH DataFrames
# Most inclusive - complete data
# Fill with NaN where no match

outer_join = pd.merge(df_temp, df_humidity, on='city', how='outer')
print("OUTER JOIN (all cities from both):")
print(outer_join)
# Output:
#         city  temperature  humidity
# 0     mumbai         32.0      65.0
# 1      delhi         45.0      68.0
# 2  bangalore         40.0      75.0
# 3  hyderabad         36.0       NaN  ← Only in df_temp
# 4    chennai          NaN      70.0  ← Only in df_humidity

# Explanation:
# - ALL 5 unique cities included
# - hyderabad: temperature exists, humidity is NaN
# - chennai: humidity exists, temperature is NaN
# - Common cities: Both values present
```

### Visual Guide: Understanding Joins

```
df_temp cities:        mumbai, delhi, bangalore, hyderabad
df_humidity cities:    delhi, mumbai, bangalore, chennai

Common (in both):      mumbai, delhi, bangalore
Only in df_temp:       hyderabad
Only in df_humidity:   chennai

LEFT JOIN:   mumbai, delhi, bangalore, hyderabad (all from left)
RIGHT JOIN:  delhi, mumbai, bangalore, chennai (all from right)
INNER JOIN:  mumbai, delhi, bangalore (only common)
OUTER JOIN:  mumbai, delhi, bangalore, hyderabad, chennai (all unique)
```

### When to Use Which Join?

| Use Case | Best Join Type | Example |
|----------|---------------|---------|
| Keep all customers, add order data | LEFT | All customers (left), add their orders if exist |
| Keep all orders, add customer details | RIGHT | All orders (right), add customer info if exist |
| Only customers who placed orders | INNER | Customers AND orders must both exist |
| All customers and all orders | OUTER | Complete picture of everything |

---

## Quick Reference Guide

### Series vs DataFrame

| Aspect | Series | DataFrame |
|--------|--------|-----------|
| Dimensions | 1D (single column) | 2D (multiple columns) |
| Structure | Index + Values | Index + Multiple Columns |
| Like... | A single column in Excel | An entire Excel sheet |
| Access by | `series[0]` or `series['label']` | `df['column']` or `df.iloc[row, col]` |

### Common Operations Cheat Sheet

```python
# Creating
series = pd.Series([1, 2, 3])
df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})

# Viewing
df.head()          # First 5 rows
df.tail()          # Last 5 rows
df.shape           # (rows, columns)
df.info()          # Column info
df.describe()      # Statistics

# Selecting
df['col1']         # Single column
df[['col1', 'col2']]  # Multiple columns
df.iloc[0]         # Row by position
df.loc[0, 'col1']  # By label

# Filtering
df[df['col1'] > 5]  # Rows where condition is True

# Modifying
df.set_index('col1')    # Set column as index
df.reset_index()        # Reset to default index
df.drop(index=[0])      # Drop rows
df.drop(columns=['col1'])  # Drop columns
df.sort_values(by='col1')  # Sort by column

# Combining
pd.concat([df1, df2], axis=0)  # Vertical stack
pd.concat([df1, df2], axis=1)  # Horizontal stack
pd.merge(df1, df2, on='key', how='left')   # Left join
pd.merge(df1, df2, on='key', how='right')  # Right join
pd.merge(df1, df2, on='key', how='inner')  # Inner join
pd.merge(df1, df2, on='key', how='outer')  # Outer join

# Statistics
df['col1'].mean()   # Average
df['col1'].sum()    # Sum
df['col1'].min()    # Minimum
df['col1'].max()    # Maximum
df['col1'].std()    # Standard deviation
```

### Common Gotchas for Beginners

1. **Concat vs Merge**
   - `concat()`: Stacks DataFrames (doesn't look at data values)
   - `merge()`: Joins based on common column values (like SQL)

2. **axis Parameter**
   - `axis=0`: Operate along rows (vertically ↓)
   - `axis=1`: Operate along columns (horizontally →)

3. **NaN Values**
   - `NaN` = "Not a Number" = Missing data
   - Common after joins/concatenations
   - Check with: `df.isna()` or `df.isnull()`
   - Fill with: `df.fillna(value)`
   - Drop with: `df.dropna()`

4. **Copy vs View**
   - Always use `.copy()` for independent DataFrame
   - Without copy: Changes affect original!

---

## Practice Exercises

### Beginner Level
1. Create a Series from a list of your favorite numbers
2. Create a DataFrame with 3 columns: Name, Age, City for 5 people
3. Add a new column to the DataFrame
4. Sort the DataFrame by Age

### Intermediate Level
1. Filter the DataFrame to show only people above age 25
2. Create two DataFrames and concatenate them vertically
3. Perform an inner join on two DataFrames
4. Calculate the average of a numeric column

### Advanced Level
1. Create two DataFrames with some overlapping and some unique rows
2. Perform all 4 types of joins (left, right, inner, outer)
3. Handle missing data (NaN) after a join
4. Create a complex filter with multiple conditions

---

## Additional Resources

- Official Pandas Documentation: https://pandas.pydata.org/docs/
- Pandas Cheat Sheet: https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf
- Practice on Kaggle: https://www.kaggle.com/learn/pandas

---

**Happy Learning with Pandas! 🐼**
