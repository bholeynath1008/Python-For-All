# **📊 COMPREHENSIVE PANDAS CHEAT SHEET WITH INDEX**

## **📖 TABLE OF CONTENTS**

1. **[Importing Pandas](#1-importing-pandas)**
2. **[Creating Data Structures](#2-creating-data-structures)**
3. **[Viewing/Inspecting Data](#3-viewinginspecting-data)**
4. **[Selecting Data](#4-selecting-data---comprehensive-guide)**
5. **[Data Manipulation](#5-data-manipulation---addingupdatingdeleting)**
   - [Adding Data](#a-addinginserting-data)
   - [Updating Data](#b-updating-data)
   - [Deleting Data](#c-deletingremoving-data)
6. **[Handling Missing Data](#6-handling-missing-data)**
7. **[Data Cleaning](#7-data-cleaning)**
8. **[Data Transformation](#8-data-transformation)**
9. **[Grouping and Aggregation](#9-grouping-and-aggregation)**
10. **[Combining DataFrames](#10-combining-dataframes)**
    - [Merge, Joins, Unions](#combining-dataframes-operations-table)
11. **[Time Series Operations](#11-time-series-operations)**
12. **[Input/Output (I/O)](#12-inputoutput-io)**
13. **[Useful Tips & Tricks](#13-useful-tips--tricks)**
14. **[Common Patterns & Examples](#14-common-patterns--examples)**
15. **[Quick Reference Card](#-quick-reference-card)**

---

## **📌 GLOBAL SAMPLE DATASET**
```python
import pandas as pd
import numpy as np

# Sample DataFrame used throughout this cheat sheet
df = pd.DataFrame({
    'ID': [1, 2, 3, 4, 5, 6],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emma', 'Frank'],
    'Age': [25, 30, 35, 28, 32, 40],
    'Salary': [50000, 60000, 75000, 45000, 55000, 80000],
    'Department': ['HR', 'IT', 'IT', 'HR', 'Finance', 'Finance'],
    'Location': ['NYC', 'LA', 'NYC', 'Chicago', 'LA', 'NYC']
}, index=['emp1', 'emp2', 'emp3', 'emp4', 'emp5', 'emp6'])

print("Sample DataFrame:")
print(df)
"""
        ID     Name  Age  Salary Department  Location
emp1    1    Alice   25   50000         HR       NYC
emp2    2      Bob   30   60000         IT        LA
emp3    3  Charlie   35   75000         IT       NYC
emp4    4    David   28   45000         HR   Chicago
emp5    5     Emma   32   55000   Finance        LA
emp6    6    Frank   40   80000   Finance       NYC
"""
```

## **1. IMPORTING PANDAS**
```python
import pandas as pd  # Standard alias
import numpy as np   # Often used together for numerical operations
```

## **2. CREATING DATA STRUCTURES**

### **Series (1D Labeled Array)**
```python
# Create Series from list
s = pd.Series([1, 3, 5, np.nan, 6, 8], name='my_series')
s = pd.Series([1, 2, 3], index=['a', 'b', 'c'])  # Custom index
s = pd.Series({'a': 1, 'b': 2, 'c': 3})          # From dictionary
```

### **DataFrame (2D Labeled Table - Main Structure)**
```python
# Method 1: From dictionary of lists
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['NYC', 'LA', 'Chicago']
})

# Method 2: From list of dictionaries
data = [{'Name': 'Alice', 'Age': 25}, {'Name': 'Bob', 'Age': 30}]
df = pd.DataFrame(data)

# Method 3: From NumPy array
df = pd.DataFrame(np.random.randn(5, 3), columns=['A', 'B', 'C'])

# Method 4: With date range index
dates = pd.date_range('20230101', periods=6)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=['A', 'B', 'C', 'D'])
```

## **3. VIEWING/INSPECTING DATA**

### **Basic Inspection Methods**
```python
df.head()           # First 5 rows
df.head(3)          # First 3 rows
df.tail()           # Last 5 rows
df.tail(2)          # Last 2 rows
df.shape            # Returns (rows, columns) as tuple
df.shape[0]         # Number of rows only
df.shape[1]         # Number of columns only
len(df)             # Number of rows (alternative)
df.columns          # Column names as Index object
df.columns.tolist() # Column names as list
df.index            # Index/row labels
df.dtypes           # Data type of each column
df.info()           # Concise summary including memory usage
df.describe()       # Statistical summary for numeric columns (count, mean, std, min, 25%, 50%, 75%, max)
df.describe(include='all')  # Include non-numeric columns
```

### **Advanced Inspection Methods**
```python
df['Department'].value_counts()     # Count unique values in a column
df['Department'].value_counts(normalize=True)  # Relative frequencies
df.nunique()                        # Number of unique values per column
df['Department'].nunique()          # Number of unique values in specific column
df.isnull().sum()                   # Count nulls per column
df.notnull().sum()                  # Count non-nulls per column
df.sample(3)                        # Random 3 rows
df.sample(frac=0.5)                 # Random 50% of rows
df.sample(3, random_state=42)       # Reproducible random sampling
df.memory_usage(deep=True)          # Memory usage per column in bytes
```

## **4. SELECTING DATA - COMPREHENSIVE GUIDE**

### **📌 KEY POINTS TO REMEMBER:**
- **Rows are selected using index** (row labels or positions)
- **Columns are selected using column names**
- **Use `iloc` for position-based indexing (integer positions)**
- **Use `loc` for label-based indexing (row/column names)**
- **Single brackets `[]` for column selection, double brackets `[[]]` for multiple columns**

### **A. EXTRACTING VALUES**
```python
# Extract single value
value = df.loc['emp1', 'Salary']    # 50000 (label-based)
value = df.iloc[0, 3]               # 50000 (position-based)
value = df.at['emp1', 'Salary']     # 50000 (fast single cell, label-based)
value = df.iat[0, 3]                # 50000 (fast single cell, position-based)

# Extract column as Series
age_series = df['Age']              # Series of all ages
age_series = df.Age                 # Same using dot notation (if no spaces)

# Extract column as list
age_list = df['Age'].tolist()       # [25, 30, 35, 28, 32, 40]
age_list = df['Age'].values         # numpy array: array([25, 30, 35, 28, 32, 40])

# Extract row as Series
row_series = df.loc['emp1']         # Series for emp1
row_series = df.iloc[0]             # Series for first row

# Extract row as dictionary
row_dict = df.loc['emp1'].to_dict() # {'ID': 1, 'Name': 'Alice', 'Age': 25, ...}

# Extract subset as numpy array
subset_array = df[['Age', 'Salary']].values  # 2D numpy array
subset_array = df.iloc[0:3, 1:4].values      # Specific rows and columns as array
```

### **B. SELECTING COLUMNS**
```python
# Single column (returns Series)
df['Name']                         # Using column name
df.Name                           # Dot notation (only if column name has no spaces/special chars)

# Multiple columns (returns DataFrame)
df[['Name', 'Age']]               # List of column names
df[['Name', 'Age', 'Salary']]     # Multiple columns
```

### **C. SELECTING ROWS**
```python
# Single row by position (iloc)
df.iloc[0]                        # First row (position 0)
df.iloc[2]                        # Third row (position 2)
df.iloc[-1]                       # Last row

# Single row by label (loc)
df.loc['emp1']                    # Row with index label 'emp1'
df.loc['emp3']                    # Row with index label 'emp3'

# Multiple rows by position (iloc)
df.iloc[0:3]                      # Rows 0 to 2 (3 rows) - last excluded
df.iloc[[0, 2, 4]]                # Rows at positions 0, 2, 4
df.iloc[::2]                      # Every 2nd row

# Multiple rows by label (loc)
df.loc['emp1':'emp3']             # Rows 'emp1' to 'emp3' - last INCLUDED
df.loc[['emp1', 'emp3', 'emp5']]  # Specific rows by labels
```

### **D. SELECTING ROWS AND COLUMNS TOGETHER**
```python
# Using iloc (position-based)
df.iloc[0, 1]                     # Single cell: row 0, column 1 → 'Alice'
df.iloc[0:3, 0:2]                 # Rows 0-2, Columns 0-1
df.iloc[[0, 2, 4], [1, 3]]        # Rows 0,2,4 and Columns 1,3
df.iloc[:, [0, 2, 4]]             # All rows, Columns 0,2,4
df.iloc[[0, 2, 4], :]             # Rows 0,2,4, All columns

# Using loc (label-based)
df.loc['emp1', 'Name']            # Single cell: row 'emp1', column 'Name' → 'Alice'
df.loc['emp1':'emp3', 'Name':'Age']  # Row range, Column range
df.loc[['emp1', 'emp3'], ['Name', 'Salary']]  # Specific rows and columns
df.loc[:, ['Name', 'Age', 'Department']]  # All rows, specific columns
df.loc[['emp2', 'emp4', 'emp6'], :]       # Specific rows, all columns
```

### **E. CONDITIONAL SELECTION**
```python
# Single condition
df[df['Age'] > 30]                # Employees older than 30
df[df['Department'] == 'IT']      # Employees in IT department
df[df['Location'].isin(['NYC', 'LA'])]  # Employees in NYC or LA

# Multiple conditions (MUST use parentheses!)
df[(df['Age'] > 30) & (df['Department'] == 'IT')]          # AND condition
df[(df['Age'] < 30) | (df['Salary'] > 70000)]              # OR condition
df[~(df['Department'] == 'HR')]                            # NOT condition
df[(df['Age'] > 25) & (df['Age'] < 35) & (df['Salary'] > 50000)]  # Multiple ANDs

# String methods in conditions
df[df['Name'].str.startswith('A')]       # Names starting with 'A'
df[df['Name'].str.contains('li')]        # Names containing 'li'
df[df['Name'].str.endswith('e')]         # Names ending with 'e'
df[df['Name'].str.len() > 4]             # Names longer than 4 characters

# Query method (alternative syntax)
df.query('Age > 30')
df.query('Department == "IT" and Salary > 65000')
df.query('Age in [25, 30, 35]')
```

## **5. DATA MANIPULATION - ADDING/UPDATING/DELETING**

### **📌 AXIS RULES FOR DROP OPERATIONS:**
- **`axis=0` or `axis='index'` → ROWS** (default)
- **`axis=1` or `axis='columns'` → COLUMNS**
- **`index=` parameter → ROWS**
- **`columns=` parameter → COLUMNS**

### **A. ADDING/INSERTING DATA**

#### **📝 ADDING SINGLE COLUMN**
```python
# Method 1: Direct assignment (most common)
df['Bonus'] = df['Salary'] * 0.10        # 10% bonus for everyone

# Method 2: Using assign (returns new DataFrame)
df = df.assign(Bonus = df['Salary'] * 0.10)

# Method 3: Constant value for all rows
df['Country'] = 'USA'                    # Add column with same value for all rows

# Method 4: Using list/array of values
df['Tax'] = [10000, 12000, 15000, 9000, 11000, 16000]  # Must match row count
```

#### **📝 ADDING MULTIPLE COLUMNS**
```python
# Method 1: Multiple assignments
df['Bonus'] = df['Salary'] * 0.10
df['Tax'] = df['Salary'] * 0.20
df['Net_Salary'] = df['Salary'] - df['Tax']

# Method 2: Using assign with multiple columns
df = df.assign(
    Bonus = df['Salary'] * 0.10,
    Tax = df['Salary'] * 0.20,
    Net_Salary = df['Salary'] * 0.70
)

# Method 3: Add multiple columns from DataFrame
new_columns = pd.DataFrame({
    'Bonus': df['Salary'] * 0.10,
    'Tax': df['Salary'] * 0.20,
    'Net_Salary': df['Salary'] * 0.70
})
df = pd.concat([df, new_columns], axis=1)

# Method 4: Insert columns at specific position
df.insert(2, 'Experience', [3, 5, 7, 2, 4, 10])      # Insert at position 2 (0-based)
df.insert(4, 'Performance', ['A', 'B', 'A', 'C', 'B', 'A'])
```

#### **📝 ADDING SINGLE ROW**
```python
# Method 1: Using loc with new index label (RECOMMENDED)
df.loc['emp7'] = [7, 'Grace', 29, 62000, 'IT', 'Seattle']  # Single row

# Method 2: Using dictionary with loc
df.loc['emp8'] = {'ID': 8, 'Name': 'Henry', 'Age': 27, 
                  'Salary': 48000, 'Department': 'HR', 'Location': 'Boston'}

# Method 3: Using append (DEPRECATED in newer pandas, use concat instead)
# new_row = pd.Series([7, 'Grace', 29, 62000, 'IT', 'Seattle'], index=df.columns)
# df = df.append(new_row, ignore_index=False)

# Method 4: Using concat (BEST for adding to existing DataFrame)
new_row = pd.DataFrame({
    'ID': [7],
    'Name': ['Grace'],
    'Age': [29],
    'Salary': [62000],
    'Department': ['IT'],
    'Location': ['Seattle']
}, index=['emp7'])
df = pd.concat([df, new_row])
```

#### **📝 ADDING MULTIPLE ROWS**
```python
# Method 1: Using loc with multiple index labels
df.loc[['emp8', 'emp9']] = [
    [8, 'Prasad', 28, 40000, 'Gen AI', 'Online'],
    [9, 'Kumar', 32, 45000, 'Gen AI', 'Offline']
]

# Method 2: Using concat (RECOMMENDED)
new_rows = pd.DataFrame({
    'ID': [8, 9],
    'Name': ['Prasad', 'Kumar'],
    'Age': [28, 32],
    'Salary': [40000, 45000],
    'Department': ['Gen AI', 'Gen AI'],
    'Location': ['Online', 'Offline']
}, index=['emp8', 'emp9'])
df = pd.concat([df, new_rows])

# Method 3: Using numpy array with loc (as in your example)
new_data = np.array([
    [8, 'Prasad', 28, 40000, 'Gen AI', 'Online'],
    [9, 'Kumar', 32, 45000, 'Gen AI', 'Offline']
])
df.loc[['emp8', 'emp9']] = new_data

# Method 4: From list of dictionaries
new_rows_list = [
    {'ID': 8, 'Name': 'Prasad', 'Age': 28, 'Salary': 40000, 
     'Department': 'Gen AI', 'Location': 'Online'},
    {'ID': 9, 'Name': 'Kumar', 'Age': 32, 'Salary': 45000, 
     'Department': 'Gen AI', 'Location': 'Offline'}
]
df = pd.concat([df, pd.DataFrame(new_rows_list, index=['emp8', 'emp9'])])
```

#### **⚠️ IMPORTANT RULES FOR ADDING ROWS:**
1. **Column Order Must Match**: When adding rows with lists/arrays, order must match DataFrame columns
2. **Dictionary Keys Must Match**: When using dict, all column names must be provided
3. **Missing Values Become NaN**: If you omit values, they become NaN
4. **Use concat for Multiple Rows**: Most reliable method for adding multiple rows
5. **Index Consistency**: Be careful with index duplicates when adding rows

### **B. UPDATING DATA**

#### **📝 REPLACING VALUES**
```python
# Replace single value
df.replace('NYC', 'New York')                      # Replace all occurrences
df.replace({'NYC': 'New York', 'LA': 'Los Angeles'})  # Multiple replacements
df.replace(['NYC', 'LA'], ['New York', 'Los Angeles'])  # Alternative syntax

# Column-specific replacement
df.replace({'Location': {'NYC': 'New York', 'LA': 'Los Angeles'}})

# Replace with regex
df.replace({'Name': {'^A': 'AA'}}, regex=True)     # Names starting with A → AA

# Replace NaN values
df.replace({np.nan: 0, None: 'Missing'})           # Replace NaN/None

# Replace based on condition
df.loc[df['Age'] < 30, 'Experience'] = 'Junior'    # Conditional update
df.loc[df['Salary'] > 70000, 'Salary'] = 70000     # Cap salary at 70000

# Replace using map
df['Department'] = df['Department'].map({'HR': 'Human Resources', 
                                          'IT': 'Information Technology'})
```

#### **📝 UPDATING SINGLE CELL**
```python
df.loc['emp1', 'Salary'] = 52000           # Update using loc (label-based)
df.iloc[0, 3] = 52000                      # Update using iloc (position-based)
df.at['emp1', 'Salary'] = 52000            # Faster for single cell (label-based)
df.iat[0, 3] = 52000                       # Faster for single cell (position-based)

# Update using column name directly
df.loc[df['Name'] == 'Alice', 'Salary'] = 52000  # Conditional update
```

#### **📝 UPDATING MULTIPLE CELLS**
```python
# Update entire column
df['Salary'] = df['Salary'] * 1.05          # 5% raise for everyone

# Conditional update
df.loc[df['Department'] == 'IT', 'Salary'] = df['Salary'] * 1.10  # 10% raise for IT
df.loc[df['Age'] > 35, 'Bonus'] = 10000     # Higher bonus for older employees

# Update multiple columns
df.loc[df['Location'] == 'NYC', ['Salary', 'Bonus']] = [65000, 5000]

# Using mask
mask = df['Age'] < 25
df.loc[mask, 'Experience'] = 'Junior'
df.loc[~mask, 'Experience'] = 'Senior'

# Update using numpy where
df['Salary_Level'] = np.where(df['Salary'] > 60000, 'High', 'Low')
```

### **C. DELETING/REMOVING DATA**

#### **📝 DROPPING SINGLE ROW**
```python
# Method 1: Using drop with index label
df.drop('emp1')                            # Drop row with label 'emp1'
df.drop(index='emp1')                      # Alternative syntax

# Method 2: Using drop with axis=0
df.drop('emp1', axis=0)                    # Explicit axis specification

# Method 3: By position (using index)
df.drop(df.index[0])                       # Drop first row

# Method 4: Inplace deletion
df.drop('emp1', inplace=True)              # Modify original DataFrame
```

#### **📝 DROPPING MULTIPLE ROWS**
```python
# Method 1: Drop multiple rows by labels
df.drop(['emp1', 'emp3', 'emp5'])          # Drop rows with these labels
df.drop(index=['emp1', 'emp3', 'emp5'])    # Alternative syntax

# Method 2: Drop by position range
df.drop(df.index[1:4])                     # Drop rows 1, 2, 3

# Method 3: Drop by specific positions
df.drop(df.index[[0, 2, 4]])               # Drop rows at positions 0, 2, 4

# Method 4: Conditional deletion
df = df[df['Age'] >= 30]                    # Keep only rows where Age >= 30
df = df[~(df['Department'] == 'HR')]        # Delete rows where Department is HR
df = df.drop(df[df['Salary'] < 50000].index) # Delete rows with Salary < 50000

# Method 5: Drop duplicates
df.drop_duplicates(subset=['Name'])         # Keep first occurrence of each name
df.drop_duplicates(subset=['Department'], keep='last')  # Keep last occurrence
```

#### **📝 DROPPING SINGLE COLUMN**
```python
# Method 1: Using drop with axis=1
df.drop('Salary', axis=1)                   # Drop column 'Salary'
df.drop(columns='Salary')                   # Alternative syntax

# Method 2: Using del keyword
del df['Salary']                            # Inplace deletion (modifies original)

# Method 3: Using pop (removes and returns the column)
salary_column = df.pop('Salary')            # Removes 'Salary' and returns it

# Method 4: By position
df.drop(df.columns[3], axis=1)             # Drop column at position 3
```

#### **📝 DROPPING MULTIPLE COLUMNS**
```python
# Method 1: Drop multiple columns by names
df.drop(['Salary', 'Bonus', 'Tax'], axis=1)  # Drop these columns
df.drop(columns=['Salary', 'Bonus', 'Tax'])  # Alternative syntax

# Method 2: Drop by position range
df.drop(df.columns[2:5], axis=1)            # Drop columns at positions 2, 3, 4

# Method 3: Drop by specific positions
df.drop(df.columns[[1, 3, 5]], axis=1)      # Drop columns at positions 1, 3, 5

# Method 4: Keep only specific columns
df = df[['Name', 'Age', 'Department']]      # Keep only these columns

# Method 5: Drop columns with certain data types
df = df.select_dtypes(exclude=['object'])    # Drop all string columns

# Method 6: Drop columns with too many missing values
df = df.dropna(axis=1, thresh=len(df)*0.7)  # Drop columns with less than 70% non-null values
```

#### **📝 DROPPING ROWS AND COLUMNS SIMULTANEOUSLY**
```python
# Method 1: Chain drop operations
df = df.drop(index=['emp1', 'emp3']).drop(columns=['Bonus', 'Tax'])

# Method 2: Single drop call with both parameters
df = df.drop(index=['emp1', 'emp3'], columns=['Bonus', 'Tax'])

# Method 3: Using loc to select what to keep
df = df.loc[['emp2', 'emp4', 'emp5', 'emp6'], ['Name', 'Age', 'Department']]

# Method 4: Using iloc to select by position
df = df.iloc[1:5, [0, 1, 2, 4]]  # Keep rows 1-4, columns 0,1,2,4
```

### **D. RENAMING**
```python
# Rename columns
df.rename(columns={'Salary': 'Annual_Salary', 'ID': 'Employee_ID'})
df.rename(columns=str.lower)                     # All columns to lowercase
df.rename(columns=lambda x: x.replace(' ', '_')) # Replace spaces with underscores

# Rename rows/index
df.rename(index={'emp1': 'employee_1', 'emp2': 'employee_2'})
df.rename(index=str.upper)                       # All index labels to uppercase

# Rename all columns at once
df.columns = ['emp_id', 'emp_name', 'emp_age', 'emp_salary', 'dept', 'loc']

# Rename all index labels
df.index = ['e1', 'e2', 'e3', 'e4', 'e5', 'e6']
```

### **E. RESETTING INDEX**
```python
df.reset_index()                          # Move index to column, new numeric index
df.reset_index(drop=True)                 # Discard old index completely
df.reset_index(inplace=True)              # Modify in place

df.set_index('Name')                      # Set 'Name' as new index
df.set_index(['Department', 'Name'])      # Multi-level index
```

## **6. HANDLING MISSING DATA**

### **Detecting Missing Values**
```python
df.isnull()        # Boolean DataFrame (True for NaN/None)
df.isna()          # Alias for isnull()
df.notnull()       # Opposite of isnull()
df.notna()         # Alias for notnull()
df.isnull().sum()  # Count missing values per column
df.isnull().sum().sum()  # Total missing values in DataFrame
df.isnull().mean() * 100 # Percentage of missing values per column
```

### **Dealing with Missing Values**
```python
# Dropping missing values
df.dropna()                         # Drop rows with ANY NaN
df.dropna(axis=1)                   # Drop columns with ANY NaN
df.dropna(how='all')                # Drop rows where ALL values are NaN
df.dropna(thresh=3)                 # Keep rows with at least 3 non-NaN values
df.dropna(subset=['Salary', 'Age']) # Only check specific columns for NaN

# Filling missing values
df.fillna(0)                        # Fill all NaN with 0
df.fillna({'Salary': df['Salary'].median(), 'Age': df['Age'].mean()})  # Column-specific
df.fillna(method='ffill')           # Forward fill (carry last observation forward)
df.fillna(method='bfill')           # Backward fill (use next observation)
df.fillna(method='ffill', limit=2)  # Forward fill with limit of 2 consecutive fills
df.interpolate()                    # Interpolate missing values
df.fillna(df.mean())                # Fill with column means
df.fillna(df.mode().iloc[0])        # Fill with most frequent value (mode)

# Replace specific values
df.replace(-999, np.nan)            # Replace -999 with NaN
df.replace([-999, -888], np.nan)    # Replace multiple values with NaN
df.replace({'Male': 'M', 'Female': 'F'})  # Replace using dictionary
```

## **7. DATA CLEANING**

### **Type Conversion**
```python
df['Age'] = df['Age'].astype('int')        # Convert to integer
df['Salary'] = df['Salary'].astype('float') # Convert to float
df['Name'] = df['Name'].astype('str')      # Convert to string
df['ID'] = df['ID'].astype('category')     # Convert to categorical (saves memory)

# Safe conversion with error handling
df['Age'] = pd.to_numeric(df['Age'], errors='coerce')  # Convert to numeric, invalid→NaN
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')  # Convert to datetime

# Convert multiple columns
df[['Age', 'Salary']] = df[['Age', 'Salary']].astype('float')
```

### **String Operations**
```python
df['Name'].str.lower()                     # Convert to lowercase
df['Name'].str.upper()                     # Convert to uppercase
df['Name'].str.title()                     # Title case (first letter of each word)
df['Name'].str.strip()                     # Remove leading/trailing whitespace
df['Name'].str.lstrip()                    # Remove leading whitespace
df['Name'].str.rstrip()                    # Remove trailing whitespace
df['Name'].str.replace(' ', '_')           # Replace spaces with underscores
df['Name'].str.contains('Al')              # Check if contains substring
df['Name'].str.startswith('A')             # Check if starts with
df['Name'].str.endswith('e')               # Check if ends with
df['Name'].str.len()                       # Length of each string
df['Name'].str.split(' ')                  # Split string into list
df['Name'].str.split(' ', expand=True)     # Split into separate columns
df['Name'].str.slice(0, 3)                 # Get first 3 characters
df['Name'].str.find('a')                   # Find position of substring
df['Name'].str.count('a')                  # Count occurrences of substring
df['Name'].str.extract('(\d+)')            # Extract numbers
```

### **Removing Duplicates**
```python
df.drop_duplicates()                       # Remove exact duplicate rows
df.drop_duplicates(subset=['Name', 'Age']) # Remove duplicates based on specific columns
df.drop_duplicates(keep='first')           # Keep first occurrence (default)
df.drop_duplicates(keep='last')            # Keep last occurrence
df.drop_duplicates(keep=False)             # Remove all duplicates (keep none)
df.duplicated()                            # Boolean Series indicating duplicates
df.duplicated(subset=['Name'])             # Check duplicates in specific column
```

## **8. DATA TRANSFORMATION**

### **Applying Functions**
```python
# Apply function to Series
df['Salary'].apply(lambda x: x * 1.1)           # 10% increase
df['Name'].apply(lambda x: x.upper())           # Convert to uppercase
df['Name'].apply(len)                           # Get length of each name

# Apply function to DataFrame (row-wise or column-wise)
df.apply(np.mean, axis=0)                       # Column-wise mean
df.apply(np.mean, axis=1)                       # Row-wise mean
df.apply(lambda x: x.max() - x.min(), axis=0)   # Range per column

# Apply function element-wise
df.applymap(lambda x: len(str(x)))              # Length of string representation
df.applymap(str.upper)                          # Convert all strings to uppercase

# Vectorized operations (FASTER than apply)
df['Double_Salary'] = df['Salary'] * 2
df['Log_Salary'] = np.log(df['Salary'])
df['Normalized'] = (df['Salary'] - df['Salary'].min()) / (df['Salary'].max() - df['Salary'].min())
```

### **Mapping Values**
```python
# Map using dictionary
gender_map = {'M': 'Male', 'F': 'Female'}
df['Gender'] = df['Gender'].map(gender_map)

# Map using function
df['Salary_Level'] = df['Salary'].map(lambda x: 'High' if x > 60000 else 'Low')

# Replace values
df.replace({'NYC': 'New York', 'LA': 'Los Angeles'})
df.replace([25, 30], [26, 31])                    # Replace specific values
df.replace({'Age': {25: 26, 30: 31}})             # Column-specific replacement
```

### **Binning/Discretization**
```python
# Equal-width bins
df['Age_Group'] = pd.cut(df['Age'], bins=3, labels=['Young', 'Middle', 'Senior'])
df['Salary_Bin'] = pd.cut(df['Salary'], bins=[0, 50000, 70000, 100000], 
                          labels=['Low', 'Medium', 'High'])

# Equal-frequency bins (quantiles)
df['Salary_Quartile'] = pd.qcut(df['Salary'], q=4, labels=['Q1', 'Q2', 'Q3', 'Q4'])

# Custom bins with boundaries
bins = [20, 30, 40, 50]
labels = ['20s', '30s', '40s']
df['Age_Decade'] = pd.cut(df['Age'], bins=bins, labels=labels, include_lowest=True)
```

## **9. GROUPING AND AGGREGATION**

### **GroupBy Operations**
```python
# Basic grouping
grouped = df.groupby('Department')                   # Group by single column
grouped = df.groupby(['Department', 'Location'])     # Group by multiple columns

# Aggregation functions
grouped.mean()                                       # Mean per group (average salary per dept)
grouped.sum()                                        # Sum per group (total salary per dept)
grouped.count()                                      # Count per group (non-null)
grouped.size()                                       # Size per group (including nulls)
grouped.min()                                        # Minimum per group (min salary per dept)
grouped.max()                                        # Maximum per group (max salary per dept)
grouped.std()                                        # Standard deviation per group
grouped.var()                                        # Variance per group
grouped.median()                                     # Median per group
grouped.first()                                      # First value per group
grouped.last()                                       # Last value per group

# Multiple aggregations
grouped.agg(['mean', 'sum', 'count'])                # Multiple functions on all columns
grouped.agg({'Salary': ['mean', 'sum'], 'Age': 'median'})  # Column-specific functions

# Named aggregations (pandas 0.25+)
grouped.agg(
    avg_salary=('Salary', 'mean'),
    total_salary=('Salary', 'sum'),
    count_employees=('ID', 'count')
)

# Custom aggregation
grouped.agg({'Salary': lambda x: x.max() - x.min()})  # Range of salaries per group

# Transform (broadcast group results to original shape)
df['Dept_Avg_Salary'] = df.groupby('Department')['Salary'].transform('mean')
```

### **Pivot Tables**
```python
# Basic pivot table
pd.pivot_table(df, values='Salary', index='Department', aggfunc='mean')
"""
               Salary
Department           
Finance       67500.0
HR           47500.0
IT           67500.0
"""

# Multi-dimensional pivot
pd.pivot_table(df, values='Salary', index='Department', columns='Location', 
               aggfunc='mean', fill_value=0, margins=True)

# Multiple aggregation functions
pd.pivot_table(df, values=['Salary', 'Age'], index='Department',
               aggfunc={'Salary': ['mean', 'sum'], 'Age': 'median'})

# Pivot with multiple index/columns
pd.pivot_table(df, values='Salary', index=['Department', 'Location'], 
               columns='Age', aggfunc='mean')
```

## **10. COMBINING DATAFRAMES**

### **📊 COMBINING DATAFRAMES OPERATIONS TABLE**

| **Operation** | **Type** | **Method** | **Description** | **Example** |
|---------------|----------|------------|-----------------|-------------|
| **Union** | Vertical | `pd.concat([df1, df2])` | Stack rows (all columns must match) | Combine datasets from different periods |
| **Concatenation** | Horizontal | `pd.concat([df1, df2], axis=1)` | Stack columns (rows must align) | Add new metrics to existing rows |
| **Inner Join** | Merge | `pd.merge(df1, df2, how='inner')` | Only matching rows from both | Get employees with both personal and salary info |
| **Left Join** | Merge | `pd.merge(df1, df2, how='left')` | All left + matching right | All employees with their department (if exists) |
| **Right Join** | Merge | `pd.merge(df1, df2, how='right')` | All right + matching left | All departments with their employees (if exists) |
| **Outer Join** | Merge | `pd.merge(df1, df2, how='outer')` | All rows from both | Complete employee-department mapping |
| **Index Join** | Join | `df1.join(df2)` | Merge on index | Combine datasets with same index |

### **A. CONCATENATION (UNION)**

```python
# Sample DataFrames for examples
df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
df2 = pd.DataFrame({'A': [5, 6], 'B': [7, 8]})
df3 = pd.DataFrame({'C': [9, 10], 'D': [11, 12]})

# Vertical concatenation (UNION - stack rows)
pd.concat([df1, df2])                       # Stack vertically (axis=0 default)
pd.concat([df1, df2], ignore_index=True)    # Reset index
pd.concat([df1, df2], keys=['df1', 'df2'])  # Add keys for identification
pd.concat([df1, df2], axis=0)               # Explicit axis=0 for rows

# Horizontal concatenation (stack columns)
pd.concat([df1, df3], axis=1)               # Stack horizontally
pd.concat([df1, df3], axis=1, join='inner') # Inner join on index
pd.concat([df1, df3], axis=1, join='outer') # Outer join on index (default)

# Concatenate multiple DataFrames
pd.concat([df1, df2, df3], axis=0)          # Stack all vertically
pd.concat([df1, df2, df3], axis=1)          # Stack all horizontally
```

### **B. MERGE (JOINS)**

```python
# Sample DataFrames for merge examples
employees = pd.DataFrame({
    'Employee_ID': [1, 2, 3, 4],
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Dept_ID': [101, 102, 101, 103]
})

departments = pd.DataFrame({
    'Dept_ID': [101, 102, 104],
    'Dept_Name': ['HR', 'IT', 'Finance'],
    'Location': ['NYC', 'LA', 'Chicago']
})

# INNER JOIN (default) - only matching rows
pd.merge(employees, departments, on='Dept_ID')           # Common column
pd.merge(employees, departments, left_on='Dept_ID', right_on='Dept_ID')  # Same
pd.merge(employees, departments, how='inner')            # Explicit inner join

# LEFT JOIN - all left rows + matching right
pd.merge(employees, departments, on='Dept_ID', how='left')
"""
   Employee_ID     Name  Dept_ID Dept_Name Location
0            1    Alice      101        HR      NYC
1            2      Bob      102        IT       LA
2            3  Charlie      101        HR      NYC
3            4    David      103       NaN      NaN
"""

# RIGHT JOIN - all right rows + matching left
pd.merge(employees, departments, on='Dept_ID', how='right')
"""
   Employee_ID     Name  Dept_ID Dept_Name  Location
0          1.0    Alice      101        HR       NYC
1          2.0      Bob      102        IT        LA
2          NaN      NaN      104   Finance   Chicago
"""

# OUTER JOIN (FULL JOIN) - all rows from both
pd.merge(employees, departments, on='Dept_ID', how='outer')
"""
   Employee_ID     Name  Dept_ID Dept_Name  Location
0          1.0    Alice      101        HR       NYC
1          3.0  Charlie      101        HR       NYC
2          2.0      Bob      102        IT        LA
3          4.0    David      103       NaN       NaN
4          NaN      NaN      104   Finance   Chicago
"""

# Merge with suffixes for overlapping columns
df1 = pd.DataFrame({'ID': [1, 2], 'Value': ['A', 'B']})
df2 = pd.DataFrame({'ID': [1, 2], 'Value': ['X', 'Y']})
pd.merge(df1, df2, on='ID', suffixes=('_left', '_right'))

# Merge on multiple columns
pd.merge(df1, df2, on=['ID', 'Date'])                    # Multiple key columns

# Merge with indicator (shows source of each row)
pd.merge(employees, departments, on='Dept_ID', how='outer', indicator=True)
```

### **C. JOIN (INDEX-BASED MERGE)**

```python
# Set index for join examples
df1 = pd.DataFrame({'A': [1, 2, 3]}, index=['a', 'b', 'c'])
df2 = pd.DataFrame({'B': [4, 5, 6]}, index=['b', 'c', 'd'])

# INNER JOIN on index
df1.join(df2)                                            # Default inner join
df1.join(df2, how='inner')                               # Explicit inner join

# LEFT JOIN on index
df1.join(df2, how='left')
"""
   A    B
a  1  NaN
b  2  4.0
c  3  5.0
"""

# RIGHT JOIN on index
df1.join(df2, how='right')
"""
     A  B
b  2.0  4
c  3.0  5
d  NaN  6
"""

# OUTER JOIN on index
df1.join(df2, how='outer')
"""
     A    B
a  1.0  NaN
b  2.0  4.0
c  3.0  5.0
d  NaN  6.0
"""

# Join on column (not index)
df1.join(df2, on='ID')                                   # Join on column 'ID'

# Join multiple DataFrames
df1.join([df2, df3])                                     # Join multiple
```

### **D. COMPARING DATAFRAMES**

```python
# Check if two DataFrames are equal
df1.equals(df2)                                          # Exact equality

# Find differences
pd.testing.assert_frame_equal(df1, df2)                  # Raises error if not equal

# Compare and show differences
comparison = df1.compare(df2)                            # Shows differences
comparison = df1.compare(df2, align_axis=0)              # Stacked differences
comparison = df1.compare(df2, keep_shape=True)           # Keep original shape
comparison = df1.compare(df2, keep_equal=True)           # Include equal values
```

## **11. TIME SERIES OPERATIONS**

### **Working with Dates**
```python
# Convert to datetime
df['Date'] = pd.to_datetime(df['Date_String'])
df['Date'] = pd.to_datetime(df['Date_String'], format='%Y-%m-%d')  # Specify format

# Extract datetime components
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['Day'] = df['Date'].dt.day
df['Weekday'] = df['Date'].dt.weekday                 # Monday=0, Sunday=6
df['Day_Name'] = df['Date'].dt.day_name()             # Monday, Tuesday, etc.
df['Quarter'] = df['Date'].dt.quarter
df['Week'] = df['Date'].dt.isocalendar().week         # ISO week number
df['Is_Weekend'] = df['Date'].dt.weekday >= 5         # Weekend flag

# Date arithmetic
df['Date'] + pd.Timedelta(days=7)                     # Add 7 days
df['Date'] - pd.Timedelta(hours=12)                   # Subtract 12 hours
df['Days_Since'] = (pd.Timestamp.today() - df['Date']).dt.days  # Days since date

# Date filtering
df[df['Date'] > '2023-01-01']                         # After specific date
df[(df['Date'] >= '2023-01-01') & (df['Date'] <= '2023-12-31')]  # Date range
df[df['Date'].dt.year == 2023]                        # Specific year
df[df['Date'].dt.month.isin([1, 2, 3])]               # First quarter
```

### **Resampling**
```python
# Set date as index
df.set_index('Date', inplace=True)

# Downsampling (higher frequency to lower)
df.resample('M').mean()                               # Monthly mean
df.resample('W').sum()                                # Weekly sum
df.resample('Q').count()                              # Quarterly count
df.resample('Y').last()                               # Year-end values

# Upsampling (lower frequency to higher)
df.resample('D').ffill()                              # Forward fill daily
df.resample('H').bfill()                              # Backward fill hourly
df.resample('6H').interpolate()                       # Interpolate every 6 hours

# Resample with multiple aggregations
df.resample('M').agg({'Sales': 'sum', 'Profit': 'mean'})

# Offset resampling
df.resample('MS').sum()                               # Month start
df.resample('ME').sum()                               # Month end
```

## **12. INPUT/OUTPUT (I/O)**

### **Reading Files**
```python
# CSV files
df = pd.read_csv('data.csv')
df = pd.read_csv('data.csv', sep=',')                 # Specify separator
df = pd.read_csv('data.csv', header=0)                # Specify header row
df = pd.read_csv('data.csv', index_col=0)             # First column as index
df = pd.read_csv('data.csv', usecols=['Name', 'Age']) # Read specific columns
df = pd.read_csv('data.csv', nrows=100)               # Read first 100 rows
df = pd.read_csv('data.csv', na_values=['NA', 'null']) # Custom NA values
df = pd.read_csv('data.csv', dtype={'Age': 'int32', 'Salary': 'float64'}) # Specify dtypes

# Excel files
df = pd.read_excel('data.xlsx', sheet_name='Sheet1')
df = pd.read_excel('data.xlsx', sheet_name=0)         # First sheet
df = pd.read_excel('data.xlsx', sheet_name=None)      # All sheets as dictionary

# JSON files
df = pd.read_json('data.json')
df = pd.read_json('data.json', orient='records')      # Different orientations

# SQL databases
from sqlalchemy import create_engine
engine = create_engine('sqlite:///database.db')
df = pd.read_sql('SELECT * FROM employees', engine)
df = pd.read_sql_table('employees', engine)
df = pd.read_sql_query('SELECT name, age FROM employees WHERE age > 30', engine)

# Other formats
pd.read_html('https://example.com/table.html')        # Read HTML tables
pd.read_clipboard()                                   # Read from clipboard
pd.read_parquet('data.parquet')                       # Parquet format
pd.read_pickle('data.pkl')                            # Pickle format
pd.read_feather('data.feather')                       # Feather format
```

### **Writing Files**
```python
# CSV files
df.to_csv('output.csv')                               # Write to CSV
df.to_csv('output.csv', index=False)                  # Without index
df.to_csv('output.csv', header=False)                 # Without header
df.to_csv('output.csv', columns=['Name', 'Age'])      # Specific columns

# Excel files
df.to_excel('output.xlsx', sheet_name='Data')
df.to_excel('output.xlsx', index=False, na_rep='NULL') # Without index, NULL for NaN

# JSON files
df.to_json('output.json')
df.to_json('output.json', orient='records', indent=2) # Pretty print

# SQL databases
df.to_sql('employees', engine, if_exists='replace')   # Replace table
df.to_sql('employees', engine, if_exists='append')    # Append to table
df.to_sql('employees', engine, if_exists='fail')      # Fail if exists

# Other formats
df.to_parquet('output.parquet')
df.to_pickle('output.pkl')
df.to_feather('output.feather')
df.to_html('output.html')                             # HTML table
df.to_string()                                        # String representation
df.to_latex('output.tex')                             # LaTeX table
```

## **13. USEFUL TIPS & TRICKS**

### **Memory Optimization**
```python
df.info(memory_usage='deep')                          # Detailed memory usage
df.memory_usage(deep=True).sum()                      # Total memory usage

# Downcast numeric columns
df['Age'] = pd.to_numeric(df['Age'], downcast='integer')
df['Salary'] = pd.to_numeric(df['Salary'], downcast='float')

# Use categorical for low-cardinality strings
df['Department'] = df['Department'].astype('category')
df['Location'] = df['Location'].astype('category')

# Use appropriate dtypes
df['ID'] = df['ID'].astype('int32')                   # Use int32 instead of int64
df['Salary'] = df['Salary'].astype('float32')         # Use float32 instead of float64
```

### **Style & Display Options**
```python
# Set display options
pd.set_option('display.max_rows', 100)                # Max rows to show
pd.set_option('display.max_columns', 50)              # Max columns to show
pd.set_option('display.width', 1000)                  # Display width
pd.set_option('display.precision', 2)                 # Decimal precision
pd.set_option('display.float_format', '{:.2f}'.format) # Float formatting
pd.set_option('display.max_colwidth', 50)             # Max column width

# Reset to default
pd.reset_option('display.max_rows')

# Get current option value
pd.get_option('display.max_rows')

# Styling DataFrames
df.style.highlight_max(color='yellow')                # Highlight maximum values
df.style.highlight_min(color='lightgreen')            # Highlight minimum values
df.style.background_gradient(cmap='Blues')            # Color gradient
df.style.bar(subset=['Salary'], color='lightblue')    # Bar charts in cells
df.style.format({'Salary': '${:,.2f}', 'Age': '{:.0f}'}) # Format specific columns

# Context manager for temporary options
with pd.option_context('display.max_rows', 10, 'display.max_columns', 5):
    print(df)
```

### **Performance Optimization**
```python
# Vectorized operations (FAST)
df['New'] = df['A'] + df['B']                         # Vectorized addition
df['New'] = np.log(df['A'])                           # Vectorized log

# Avoid apply when possible (SLOW)
# Slow: df['New'] = df['A'].apply(lambda x: x * 2)
# Fast: df['New'] = df['A'] * 2

# Use built-in methods
# Slow: df['Name'].apply(str.upper)
# Fast: df['Name'].str.upper()

# Use numpy for mathematical operations
# Slow: df['A'].apply(np.sqrt)
# Fast: np.sqrt(df['A'])

# Use query for filtering
# Faster for large DataFrames
df.query('Age > 30 and Salary > 50000')
```

### **Method Chaining**
```python
# Clean method chaining
result = (df
          .query('Age > 25 and Department == "IT"')
          .groupby('Location')
          .agg({'Salary': 'mean', 'Age': 'median'})
          .rename(columns={'Salary': 'Avg_Salary', 'Age': 'Median_Age'})
          .sort_values('Avg_Salary', ascending=False)
          .round(2)
          .head(10))

# Complex transformation pipeline
cleaned_df = (df
              .dropna(subset=['Salary', 'Age'])
              .assign(Salary_Group=lambda x: np.where(x['Salary'] > 60000, 'High', 'Low'),
                      Age_Group=lambda x: pd.cut(x['Age'], bins=[20, 30, 40, 50]))
              .drop_duplicates(subset=['Name', 'Age'])
              .reset_index(drop=True)
              .sort_values(['Department', 'Salary'], ascending=[True, False]))
```

## **14. COMMON PATTERNS & EXAMPLES**

### **Data Cleaning Pipeline**
```python
def clean_dataframe(df):
    """Complete data cleaning pipeline"""
    df_clean = (df
                # Handle missing values
                .dropna(subset=['ID', 'Name'])                    # Critical columns
                .fillna({'Age': df['Age'].median(),
                         'Salary': df['Salary'].mean(),
                         'Department': 'Unknown'})
                
                # Remove duplicates
                .drop_duplicates(subset=['ID'], keep='last')
                
                # Clean strings
                .assign(Name=lambda x: x['Name'].str.strip().str.title(),
                        Department=lambda x: x['Department'].str.upper())
                
                # Fix data types
                .astype({'ID': 'int32', 
                         'Age': 'int32',
                         'Salary': 'float32'})
                
                # Remove outliers
                .query('Age >= 18 and Age <= 70')
                .query('Salary >= 0 and Salary <= 1000000')
                
                # Reset index
                .reset_index(drop=True)
                
                # Sort
                .sort_values(['Department', 'Salary'], ascending=[True, False]))
    
    return df_clean
```

### **Exploratory Data Analysis (EDA)**
```python
def quick_eda(df):
    """Quick exploratory data analysis"""
    print("=" * 50)
    print("EXPLORATORY DATA ANALYSIS")
    print("=" * 50)
    
    # Basic info
    print(f"\n1. DATASET SHAPE: {df.shape[0]} rows × {df.shape[1]} columns")
    
    # Data types
    print(f"\n2. DATA TYPES:")
    print(df.dtypes)
    
    # Missing values
    print(f"\n3. MISSING VALUES:")
    missing = df.isnull().sum()
    missing_pct = (missing / len(df)) * 100
    missing_df = pd.DataFrame({'Missing Count': missing, 
                               'Percentage': missing_pct})
    print(missing_df[missing_df['Missing Count'] > 0])
    
    # Summary statistics
    print(f"\n4. SUMMARY STATISTICS:")
    print(df.describe())
    
    # Unique values
    print(f"\n5. UNIQUE VALUES PER COLUMN:")
    print(df.nunique())
    
    # Sample data
    print(f"\n6. SAMPLE DATA (first 3 rows):")
    print(df.head(3))
    
    # Correlation matrix (for numeric columns)
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    if len(numeric_cols) > 1:
        print(f"\n7. CORRELATION MATRIX:")
        print(df[numeric_cols].corr())
    
    return df
```

### **Common Operations Reference**
```python
# Frequently used patterns
selected = df.loc[condition, ['col1', 'col2']]        # Filter and select
aggregated = df.groupby('group_col')['value_col'].agg(['mean', 'sum'])
pivoted = pd.pivot_table(df, values='val', index='row', columns='col', aggfunc='mean')
merged = pd.merge(df1, df2, on='key', how='left')
concatenated = pd.concat([df1, df2], ignore_index=True)
sorted_df = df.sort_values(['col1', 'col2'], ascending=[True, False])
```

## **📚 QUICK REFERENCE CARD**

### **Most Used Methods**
```
df.head()        - View first 5 rows
df.info()        - DataFrame info (dtypes, memory)
df.describe()    - Statistical summary
df.groupby()     - Group operations
df.merge()       - SQL-like joins
df.concat()      - Concatenate DataFrames
df.drop()        - Delete rows/columns
df.fillna()      - Fill missing values
df.apply()       - Apply function
df.sort_values() - Sort by values
df.pivot_table() - Create pivot table
df.set_index()   - Set index column
df.reset_index() - Reset index
```

### **Selection Cheat Sheet**
```
Single column:       df['col']           → Series
Multiple columns:    df[['col1','col2']] → DataFrame
Row by label:        df.loc['label']     → Series
Row by position:     df.iloc[0]          → Series
Rows by label range: df.loc['a':'c']     → DataFrame (last INCLUDED)
Rows by pos range:   df.iloc[0:3]        → DataFrame (last EXCLUDED)
Single cell label:   df.loc['row','col'] → Scalar
Single cell pos:     df.iloc[0,1]        → Scalar
Conditional:         df[df['col']>val]   → DataFrame
Multiple conditions: df[(c1)&(c2)|(c3)]  → DataFrame
```

### **Axis Parameter Guide**
```
axis=0 or 'index'    → ROWS (vertical)
axis=1 or 'columns'  → COLUMNS (horizontal)

df.drop('row', axis=0)      → Delete row
df.drop('col', axis=1)      → Delete column
df.mean(axis=0)             → Column means
df.mean(axis=1)             → Row means
df.apply(func, axis=0)      → Apply to each column
df.apply(func, axis=1)      → Apply to each row
```

## **⚠️ COMMON PITFALLS & SOLUTIONS**

1. **SettingWithCopyWarning**
   ```python
   # WRONG - Creates warning
   subset = df[df['Age'] > 30]
   subset['New'] = 100  # Warning!
   
   # CORRECT - Use .copy()
   subset = df[df['Age'] > 30].copy()
   subset['New'] = 100  # No warning
   ```

2. **Inplace vs Return New DataFrame**
   ```python
   # Method 1: Inplace modification
   df.drop('col', axis=1, inplace=True)
   
   # Method 2: Return new DataFrame
   df = df.drop('col', axis=1)
   
   # Both achieve same result
   ```

3. **Column Name Issues**
   ```python
   # Spaces in column names
   df['column name']        # Use quotes
   # df.column name         # ERROR - can't use dot notation
   
   # Special characters
   df['col-name']           # Use quotes
   # df.col-name            # ERROR
   ```

4. **Index vs Position Confusion**
   ```python
   # Label-based (loc) includes end
   df.loc['a':'c']  # Includes a, b, c
   
   # Position-based (iloc) excludes end
   df.iloc[0:3]     # Includes 0, 1, 2 (NOT 3)
   ```

## **🎯 PRACTICE RESOURCES**

1. **Kaggle**: Pandas courses and datasets
2. **Pandas Documentation**: Excellent with examples
3. **Real Datasets**: data.gov, Kaggle, UCI Machine Learning Repository
4. **Practice Projects**:
   - Data cleaning: Titanic dataset
   - Analysis: Sales data, COVID-19 data
   - Transformation: Weather data, stock prices

---

**REMEMBER THE BASICS:**
- **Check shape and dtypes** after major operations
- **Use vectorized operations** instead of loops for speed
- **Method chaining** makes code cleaner and more readable
- **Always validate** your data after transformations
- **`.copy()` is your friend** when creating subsets to modify

**Happy Data Wrangling! 🐼**
