# Table of Contents
* [Business Rules for Data Exploration and Cleaning](#business-rules-for-data-exploration-and-cleaning)
* [Quick Reference: All Methods Used(data exploration, data cleaning, panda tips)](#quick-reference-all-methods-used)
* [Remember These Tips](#remember-these-tips)

# Business Rules for Data Exploration and Cleaning
## For coding follow quick reference below: 
### Theoretical Understanding
Data exploration and cleaning are crucial steps in the data science pipeline:

1. **Data Exploration:** Understanding the structure, quality, and anomalies in your dataset

2. **Data Cleaning:** Fixing identified issues to ensure data quality

3. **Process:** `Observe` → `Extract` → `Clean` (repeat as needed) or `Explore` → `Clean` → `Validate`
During data exploration and cleaning, we often encounter issues such as missing values, wrong data types, invalid values, or duplicates.
For **every data quality issue**, we must consciously choose **one and only one** of the following strategies:

> **Replace · Remove · Retain**

The choice depends on:

* Business requirements
* Nature of the data
* Percentage of data affected
* Availability of correct data

---

## 1. Replace

Replacement is chosen when data is important and cannot be discarded.

### 1.1 Replace with Original Data (Best Option)

* Contact the **backend / source system team** to retrieve the correct values.
* This is the **most accurate and preferred solution**, especially when data correctness is critical.

**Example:**
If a student’s age is incorrectly stored as `"srk"` but the backend confirms the correct age is `25`, replace it with the actual value.

---

### 1.2 Replace Statistically

Used when original data is not immediately available.

* **Numerical columns:**
  Replace with **mean or median** (median preferred if data is skewed).
* **Categorical columns:**
  Replace with **mode** (most frequent value).

This approach assumes missing or invalid values follow the same distribution as valid data.

---

### 1.3 Replace Logically (Domain Knowledge)

Use **business logic or common sense** to infer values.

**Examples:**

* Sequential IDs → fill missing value with the next logical number
* Age cannot be negative → replace with a reasonable age
* Salary cannot be zero for a full-time employee → replace using business rules

---

## 2. Remove

* Remove records **only when the wrong or missing data is less than 5%** of the dataset.
* This avoids significant data loss while maintaining data quality.

**Rule of thumb:**

> If bad data < 5% → Remove
> If bad data ≥ 5% → Replace

---

## 3. Retain

* Keep data **as it is** when:

  * The issue is not critical
  * The data can still be used safely
  * Cleaning may introduce bias or incorrect assumptions

---
# **Beginner-Friendly Data Exploration & Cleaning Guide**

## **What is Data Exploration & Cleaning?**
Think of it like cleaning your room:
- **Exploration** = Looking around to see what's messy
- **Cleaning** = Actually putting things in their right place
- **Process** = `Look` → `Find problems` → `Fix them` → `Check again`

## **Common Problems You'll Find**
1. **Missing Values** → Empty cells in your spreadsheet
2. **Wrong Types** → Numbers stored as text, dates stored wrong
3. **Invalid Values** → Age = 150 years, Name = "12345"
4. **Duplicates** → Same person listed twice

---

## **The 3R Rule: How to Fix Problems**
For every problem, choose **ONE**:

### **1. Replace** 
When data is important and you can't delete it.

**3 Ways to Replace:**
```python
# 1. Replace with original (best) → Get correct value from source
# 2. Replace with average → Use mean/median for numbers
# 3. Replace with logic → Age can't be negative, make it reasonable
```

### **2. Remove** 
Delete bad data **only if less than 5%** of your data is bad.

**Rule of thumb:**
- Bad data < 5% → Remove
- Bad data ≥ 5% → Replace

### **3. Retain** 
Leave it as-is when:
- Problem isn't serious
- Fixing might make things worse
- You can still use the data safely

---

## **Let's Practice with Example Data**

### **Sample Dataset (Messy Version)**
```python
import pandas as pd

# Create example student data with problems
data = {
    'student_id': [1, 2, 3, 4, 5, 1],  # ID 1 appears twice!
    'name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve', 'Alice'],
    'age': [20, '21', 'twenty-two', 23, 24, 20],  # Mix of types
    'grade': ['A', 'B', 'C', None, 'A', 'A'],  # One missing grade
    'attendance': [95, 92, '88%', 94, 91, 95]  # Percent sign in some
}

df = pd.DataFrame(data)
print("=== OUR MESSY DATASET ===")
print(df)
print("\nShape (rows, columns):", df.shape)
```

**What's wrong here?**
1. student_id 1 is duplicated (row 0 and row 5)
2. age has mixed types: numbers and text
3. One grade is missing (None)
4. attendance has '%' sign in one value

---

## **Step-by-Step Cleaning Process**

### **Step 1: Look at Your Data**
```python
# Method 1: See first few rows
print("First 3 rows:")
print(df.head(3))

# Method 2: Check data types
print("\nData types:")
print(df.dtypes)

# Method 3: Check for missing values
print("\nMissing values in each column:")
print(df.isnull().sum())

# Method 4: See all unique values in a column
print("\nAll unique ages:")
print(df['age'].unique())
```

### **Step 2: Fix Duplicates**
```python
# Find duplicate student IDs
print("Duplicate student IDs:")
duplicate_ids = df[df.duplicated(subset=['student_id'], keep=False)]
print(duplicate_ids)

# Remove duplicates (keep first, remove others)
df_clean = df.drop_duplicates(subset=['student_id'], keep='first')
print(f"\nRemoved {len(df) - len(df_clean)} duplicate(s)")
```

### **Step 3: Fix Wrong Data Types**
```python
# Fix age column (convert text to numbers)
df_clean['age'] = pd.to_numeric(df_clean['age'], errors='coerce')
print("Age after conversion:")
print(df_clean['age'])

# Fix attendance (remove % and convert to number)
df_clean['attendance'] = df_clean['attendance'].astype(str).str.replace('%', '')
df_clean['attendance'] = pd.to_numeric(df_clean['attendance'], errors='coerce')
```

### **Step 4: Handle Missing Values**
```python
# Check what's still missing
print("\nMissing values after fixing types:")
print(df_clean.isnull().sum())

# Replace missing grade with most common grade
most_common_grade = df_clean['grade'].mode()[0]
df_clean['grade'] = df_clean['grade'].fillna(most_common_grade)
print(f"\nFilled missing grade with: {most_common_grade}")
```

### **Step 5: Check Final Result**
```python
print("\n=== FINAL CLEANED DATA ===")
print(df_clean)
print("\nData types now:")
print(df_clean.dtypes)
print("\nMissing values now:")
print(df_clean.isnull().sum())
print("\nShape now:", df_clean.shape)
```

---

## Quick Reference: All Methods Used

### **EXPLORATION METHODS (Looking at Data)**
```python
# 1. See basic info
df.shape                 # Shows (rows, columns)
df.head()               # First 5 rows
df.tail()               # Last 5 rows

# 2. Check data types
df.dtypes               # Type of each column
df.info()               # More detailed info

# 3. Find missing values
df.isnull()             # True/False for each cell
df.isnull().sum()       # Count missing per column
df.isnull().sum().sum() # Total missing values

# 4. Check unique values
df['column'].unique()           # All unique values
df['column'].nunique()          # Count of unique values
df['column'].value_counts()     # Count each value

# 5. Find duplicates
df.duplicated()                         # Find duplicate rows
df.duplicated(subset=['col1', 'col2'])  # Find duplicates in specific columns
df['column'].duplicated().sum()         # Count duplicates in a column
```

### **CLEANING METHODS (Fixing Data)**
```python
# 1. Fix data types
df['column'] = pd.to_numeric(df['column'], errors='coerce')  # Text to number
df['column'] = pd.to_datetime(df['column'])                   # Text to date
df['column'] = df['column'].astype('category')                # To category type

# 2. Handle missing values
df['column'].fillna(value)           # Fill with specific value
df['column'].fillna(df['column'].mean())   # Fill with average
df['column'].fillna(df['column'].median()) # Fill with middle value
df['column'].fillna(df['column'].mode()[0]) # Fill with most common
df.dropna()                           # Remove rows with any missing
df.dropna(subset=['column'])         # Remove rows missing specific column

# 3. Remove duplicates
df.drop_duplicates()                          # Remove exact duplicate rows
df.drop_duplicates(subset=['column'])        # Remove duplicates in column
df.drop_duplicates(subset=['col1', 'col2'])  # Remove duplicates in multiple columns

# 4. Replace wrong values
df['column'].replace('wrong', 'correct')      # Replace one value
df['column'].replace(['bad1', 'bad2'], 'good') # Replace multiple values

# 5. String operations (for text columns)
df['column'].str.replace('old', 'new')   # Replace text
df['column'].str.strip()                 # Remove spaces from start/end
df['column'].str.lower()                 # Convert to lowercase
```

### **USEFUL PANDAS TRICKS**
```python
# Copy data (always do this before cleaning!)
df_copy = df.copy()

# Reset index after cleaning
df = df.reset_index(drop=True)

# Rename columns
df = df.rename(columns={'old_name': 'new_name'})

# Select specific columns
df[['col1', 'col2']]  # Just these two columns

# Filter rows
df[df['age'] > 18]           # Age greater than 18
df[df['name'].str.contains('A')]  # Names containing 'A'

# Calculate basic statistics
df.describe()  # Shows count, mean, min, max for numeric columns
```

---

## **Simple Cleaning Checklist**

### **Before Cleaning:**
1. ✅ Make a copy of original data
2. ✅ Check data types with `df.dtypes`
3. ✅ Look for missing values with `df.isnull().sum()`
4. ✅ Check for duplicates with `df.duplicated().sum()`

### **Common Fixes:**
1. **Text where numbers should be** → Use `pd.to_numeric()`
2. **Dates stored as text** → Use `pd.to_datetime()`
3. **Missing values** → Use `fillna()` or `dropna()`
4. **Duplicates** → Use `drop_duplicates()`
5. **Wrong values** → Use `replace()`

### **After Cleaning:**
1. ✅ Check data types again
2. ✅ Check missing values again
3. ✅ Look at first few rows
4. ✅ Save cleaned data to new file

---

## **Example: Complete Cleaning Script**
```python
import pandas as pd

def clean_data(df):
    """Simple cleaning function for beginners"""
    
    # Step 0: Make a copy
    df_clean = df.copy()
    
    # Step 1: Remove duplicates
    df_clean = df_clean.drop_duplicates()
    
    # Step 2: Fix data types
    # Convert all numeric columns
    for col in ['age', 'score', 'attendance']:
        if col in df_clean.columns:
            df_clean[col] = pd.to_numeric(df_clean[col], errors='coerce')
    
    # Step 3: Fill missing values
    # Fill numbers with median
    for col in df_clean.select_dtypes(include=['number']).columns:
        df_clean[col] = df_clean[col].fillna(df_clean[col].median())
    
    # Fill text with "Unknown"
    for col in df_clean.select_dtypes(include=['object']).columns:
        df_clean[col] = df_clean[col].fillna('Unknown')
    
    return df_clean

# Use it like this:
cleaned_df = clean_data(df)
print("Original rows:", len(df))
print("Cleaned rows:", len(cleaned_df))
```

---

## **Remember These Tips**
1. **Always backup** your original data
2. **Check after each step** - don't do all cleaning at once
3. **Think before removing** - is 5% really okay to delete?
4. **When in doubt, ask** - someone might know the correct value
5. **Document changes** - write down what you fixed

## **Common Mistakes to Avoid:**
```python
# ❌ WRONG - Modifying original data
df = df.drop_duplicates()  # Can't undo!

# ✅ RIGHT - Work on copy
df_clean = df.copy()
df_clean = df_clean.drop_duplicates()

# ❌ WRONG - Converting without checking
df['age'] = pd.to_numeric(df['age'])

# ✅ RIGHT - Check what will become NaN
print("Problematic values:", df[~df['age'].str.isnumeric()]['age'].unique())
df['age'] = pd.to_numeric(df['age'], errors='coerce')
```

**Pro Tip:** Start with these basics, and you'll be cleaning data like a pro in no time! 🚀
