# Data Cleaning

## Key Rules to Understand

### 1. **Data Quality Issues**
   - **Wrong Data**: Incorrect values or formats (e.g., "20+" instead of 20)
   - **Wrong Data Type**: Numeric data stored as strings/objects
   - **Duplicates**: Identical rows that need to be removed
   - **Missing Values (NaN)**: Empty cells that need handling
   - **Outliers**: Extreme values that deviate from the normal pattern

### 2. **Missing Values Handling Strategy**
   - **Remove**: Drop rows/columns with missing values
   - **Replace**: Fill missing values with:
     - **Continuous Variables**: Mean or Median
     - **Discrete/Categorical Variables**: Mode (most frequent value)

### 3. **Outlier Detection Methods**
   - **Boxplot**: Visual identification
   - **IQR Method** (Interquartile Range):
     - Lower Limit = Q1 - (1.5 × IQR)
     - Upper Limit = Q3 + (1.5 × IQR)
     - Values outside these limits are outliers

### 4. **3R Technique for Outliers**
   - **Remove**: Delete outlier records
   - **Replace**: Rectify errors or apply winsorization (cap at limits)
   - **Retain**: Keep for separate analysis

### 5. **Best Practices**
   - Always check data types using `.info()`
   - Check for duplicates before analysis
   - Calculate percentage of missing values
   - Visualize outliers before removing
   - Document your cleaning decisions

---

## Python Functions Reference

### **Pandas DataFrame Functions**

| Function | Purpose | Syntax Example |
|----------|---------|----------------|
| `pd.DataFrame()` | Create a DataFrame | `pd.DataFrame({"col": [values]})` |
| `.info()` | Display DataFrame information (types, non-null counts) | `df.info()` |
| `.unique()` | Get unique values in a column | `df["col"].unique()` |
| `.replace()` | Replace values | `df["col"].replace({"old": new}, inplace=True)` |
| `.astype()` | Convert data type | `df["col"].astype('float')` |
| `.duplicated()` | Check for duplicate rows | `df.duplicated()` |
| `.drop_duplicates()` | Remove duplicate rows | `df.drop_duplicates(inplace=True)` |
| `.isnull()` | Check for missing values (returns Boolean) | `df.isnull()` |
| `.sum()` | Sum values (often used with `.isnull()`) | `df.isnull().sum()` |
| `.dropna()` | Remove rows with missing values | `df.dropna()` |
| `.drop()` | Remove rows or columns | `df.drop(columns=["col"])` or `df.drop(index=[0])` |
| `.fillna()` | Fill missing values | `df["col"].fillna(value)` |
| `.mean()` | Calculate mean | `df["col"].mean()` |
| `.median()` | Calculate median | `df["col"].median()` |
| `.mode()` | Calculate mode (most frequent) | `df["col"].mode()[0]` |
| `.quantile()` | Calculate quantile/percentile | `df["col"].quantile(0.25)` |
| `.clip()` | Limit values to a range (winsorization) | `df["col"].clip(lower=min, upper=max)` |
| `len()` | Get length/count of DataFrame | `len(df)` |

### **NumPy Functions**

| Function | Purpose | Syntax Example |
|----------|---------|----------------|
| `np.nan` | Represent missing/null values | `np.nan` |

### **Visualization Functions**

| Function | Purpose | Syntax Example |
|----------|---------|----------------|
| `sns.boxplot()` | Create boxplot to visualize outliers | `sns.boxplot(x=df["col"])` |
| `plt.show()` | Display the plot | `plt.show()` |

### **Parameters to Remember**

| Parameter | Purpose | Used In |
|-----------|---------|---------|
| `inplace=True` | Modify DataFrame directly (no return) | `.replace()`, `.drop_duplicates()` |
| `ignore_index=True` | Reset index after operation | `.drop_duplicates()` |
| `columns=["col"]` | Specify column(s) to drop | `.drop()` |
| `index=[0, 1]` | Specify row index(es) to drop | `.drop()` |
| `lower=value` | Set lower limit | `.clip()` |
| `upper=value` | Set upper limit | `.clip()` |

---

## Bad data could be:

1. Wrong data
2. Data in wrong format
3. Duplicates
4. Empty cells/missing values
5. Outliers

---

## Import Libraries

```python
import numpy as np
import pandas as pd
```

---

## Create Sample DataFrame

```python
df = pd.DataFrame({"Age": [15, 18, "18", 19.4, "20+"],
                   "Gender": ["male", "female", "female", "female", "male"]})
df
```

**Output:**
```
   Age  Gender
0   15    male
1   18  female
2   18  female
3 19.4  female
4  20+    male
```

---

## Check DataFrame Info

```python
df.info()
```

**Output:**
```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 5 entries, 0 to 4
Data columns (total 2 columns):
 #   Column   Non-Null Count  Dtype 
---  ------   --------------  ----- 
 0   Age      5 non-null      object
 1   Gender   5 non-null      object
dtypes: object(2)
memory usage: 212.0+ bytes
```

---

## Check Unique Values

```python
df["Age"].unique()
```

**Output:**
```
array([15, 18, '18', 19.4, '20+'], dtype=object)
```

---

## 1. Wrong Data

**Solution:** Replace

```python
df["Age"].replace({"20+": 20}, inplace=True)
df
```

**Output:**
```
   Age  Gender
0   15    male
1   18  female
2   18  female
3 19.4  female
4   20    male
```

---

## 2. Wrong Data Type

**Solution:** Convert the datatype

```python
df["Age"] = df["Age"].astype('float')
df
```

**Output:**
```
    Age  Gender
0  15.0    male
1  18.0  female
2  18.0  female
3  19.4  female
4  20.0    male
```

---

## 3. Duplicates

**Solution:** Remove

### Check for duplicated records

```python
# to check the duplicated records
df.duplicated()
```

**Output:**
```
0    False
1    False
2     True
3    False
4    False
dtype: bool
```

### Count total duplicates

```python
# total no. of duplicates in given data
df.duplicated().sum()
```

**Output:** `1`

### Extract duplicate records

```python
# to extract duplicate records
df[df.duplicated()]
```

**Output:**
```
    Age  Gender
2  18.0  female
```

### Extract non-duplicated records

```python
# to extract non duplicated records
df[~df.duplicated()]
```

**Output:**
```
    Age  Gender
0  15.0    male
1  18.0  female
3  19.4  female
4  20.0    male
```

### Remove duplicates

```python
# to remove the duplictes
df.drop_duplicates(inplace=True, ignore_index=True)
df
```

**Output:**
```
    Age  Gender
0  15.0    male
1  18.0  female
2  19.4  female
3  20.0    male
```

---

## Missing Values

**Solution:** Either remove or replace

### Create DataFrame with Missing Values

```python
df = pd.DataFrame({"Age": [15, np.nan, 24, 19, 20, 22],
                   "Gender": ["male", np.nan, "female", "female", "male", np.nan]})
df
```

**Output:**
```
    Age  Gender
0  15.0    male
1   NaN     NaN
2  24.0  female
3  19.0  female
4  20.0    male
5  22.0     NaN
```

### Check for missing values

```python
# to check the missing values records
df.isnull()
```

**Output:**
```
     Age  Gender
0  False   False
1   True    True
2  False   False
3  False   False
4  False   False
5  False    True
```

### Count total missing values

```python
# to check total missing values
df.isnull().sum()
```

**Output:**
```
Age       1
Gender    2
dtype: int64
```

### Check percentage of missing values

```python
# to check percentage of missing values in each variable
df.isnull().sum() / len(df) * 100
```

**Output:**
```
Age       16.666667
Gender    33.333333
dtype: float64
```

---

## Option 1. Remove the rows that contain missing values

```python
df2 = df.dropna()
df2
```

**Output:**
```
    Age  Gender
0  15.0    male
2  24.0  female
3  19.0  female
4  20.0    male
```

### Remove specific column

```python
df1 = df.drop(columns=["Gender"])
df1
```

**Output:**
```
    Age
0  15.0
1   NaN
2  24.0
3  19.0
4  20.0
5  22.0
```

---

## Option 2: Replace the nan values

- Fill with value
- Continous Variables ---> Replace with either Mean or Median
- Discrete Variables ---> Replace with Mode

### Fill with a value

```python
# to fill with a value
df["Age"].fillna(20)
```

**Output:**
```
0    15.0
1    20.0
2    24.0
3    19.0
4    20.0
5    22.0
Name: Age, dtype: float64
```

### Fill with mean

```python
# to fill with mean
df['Age'].fillna(df["Age"].mean())
```

**Output:**
```
0    15.0
1    20.0
2    24.0
3    19.0
4    20.0
5    22.0
Name: Age, dtype: float64
```

### Fill with median

```python
# to fill with median
df["Age"].fillna(df["Age"].median())
```

**Output:**
```
0    15.0
1    20.0
2    24.0
3    19.0
4    20.0
5    22.0
Name: Age, dtype: float64
```

### Fill with mode

```python
# to fill with mode
df["Gender"].fillna(df["Gender"].mode()[0])
```

**Output:**
```
0      male
1    female
2    female
3    female
4      male
5    female
Name: Gender, dtype: object
```

---

## Outliers

```python
df = pd.DataFrame({"marks": [10, 11, 12, 25, 25, 27, 31, 33, 34, 34, 36, 36, 43, 50, 59]})
df
```

**Output:**
```
    marks
0      10
1      11
2      12
3      25
4      25
5      27
6      31
7      33
8      34
9      34
10     36
11     36
12     43
13     50
14     59
```

---

## Various ways of finding the outlier

### 1. Boxplot

**Identifying Outliers based on boxplot**

```python
import matplotlib.pyplot as plt
import seaborn as sns

sns.boxplot(x=df["marks"])
plt.show()
```

**Identifying Outliers based on IQR**

### Calculate Q1, Q3, and IQR

```python
# calculate Q1
Q1 = df["marks"].quantile(0.25)
print("Q1:", Q1)

# calculate Q3
Q3 = df["marks"].quantile(0.75)
print("Q3:", Q3)

# calculate IQR
IQR = Q3 - Q1
print("IQR:", IQR)

# calculate lower limit of outlier
lower_limit = Q1 - (IQR * 1.5)
print("lower limit:", lower_limit)

# calculate upper limit of outlier
upper_limit = Q3 + (IQR * 1.5)
print("upper limit:", upper_limit)
```

**Output:**
```
Q1: 25.0
Q3: 36.0
IQR: 11.0
lower limit: 8.5
upper limit: 52.5
```

---

## Outliers Data

```python
df[(df["marks"] < lower_limit) | (df["marks"] > upper_limit)]
```

**Output:**
```
    marks
14     59
```

---

## Solution: 3R Technique

1. **Remove** (remove the outliers from our dataset)
2. **Replace the ouliers**
   - Rectify or Replace --> (data entry error) ---> Ask and confirm it from the Data Engineering team,
   - Replace with upper limit & lower limit based on IQR
3. **Retain** (consider for analysis) ---> Treat them separately

---

## Remove

```python
df.drop(index=[14])
```

**Output:**
```
    marks
0      10
1      11
2      12
3      25
4      25
5      27
6      31
7      33
8      34
9      34
10     36
11     36
12     43
13     50
```

---

## Replace

- based on confirmation from data engineer team / based on research / based on domain expertise

**Replace based on statistics**

- **winsorization** - replacing the outliers statiscally with lower_linit & upper_limit values

```python
df['marks'] = df['marks'].clip(lower=8.5, upper=52.5)
df
```

**Output:**
```
    marks
0    10.0
1    11.0
2    12.0
3    25.0
4    25.0
5    27.0
6    31.0
7    33.0
8    34.0
9    34.0
10   36.0
11   36.0
12   43.0
13   50.0
14   52.5
```

```python
sns.boxplot(x=df["marks"])
plt.show()
```
