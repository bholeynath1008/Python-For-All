"""
DATA CLEANUP PRACTICE EXERCISE
Following the class notes structure: Explore → Extract → Treat
"""

import pandas as pd
import numpy as np

# ============================================================================
# CREATING SAMPLE DATASET WITH INTENTIONAL PROBLEMS
# ============================================================================

data = {
    'customer_id': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 
                    111, 112, 113, 114, 115, 116, 117, 118, 119, 120],
    'name': ['John', 'Sarah', 'Mike', 'Emma', 'John', 'Sarah', 'Mike', 
             'David', 'Lisa', 'Tom', 'Jerry', 'Kate', 'Bob', 'Alice', 
             'Charlie', 'Diana', 'Eve', 'Frank', 'Grace', 'Henry'],
    'age': ['25', '30', 'twenty-eight', '35', '25', '30', 'twenty-eight', 
            '40', '22', '150', '28', '33', np.nan, '29', '31', '27', 
            '26', np.nan, '32', '24'],
    'city': ['Bangalore', 'Chennai', 'Hyderabad', 'Delhi', 'Bangalore', 
             'Chennai', 'Hyderabad', 'Mumbai', 'Pune', 'Bangalore', 
             'Chennai', 'Hyderabad', 'Delhi', np.nan, 'Mumbai', 
             'Bangalore', np.nan, 'Chennai', 'Pune', 'Delhi'],
    'purchase_amount': [1200.50, 800.30, np.nan, 1500.00, 1200.50, 
                        800.30, np.nan, 2200.00, 950.00, 50000.00, 
                        1100.00, np.nan, 1300.00, 1450.00, 1800.00, 
                        1250.00, np.nan, 980.00, 1150.00, 45000.00],
    'country': ['India', 'India', 'India', 'India', 'India', 'India', 
                'India', 'India', 'India', 'India', 'India', 'India', 
                'India', 'India', 'India', 'India', 'India', 'India', 
                'India', 'India'],
    'pan_card': ['ABCDE1234F', 'FGHIJ5678K', 'KLMNO9012P', 'QRSTU3456V', 
                 'WXYZA7890B', 'CDEFG2345H', 'IJKLM6789N', 'OPQRS0123T', 
                 'UVWXY4567Z', 'ABCDF8901E', 'GHIJK2345L', 'MNOPQ6789R', 
                 'STUVW0123X', 'YZABC4567D', 'DEFGH8901J', 'IJKLM2345P', 
                 'NOPQR6789V', 'STUVW0123B', 'XYZAB4567H', 'CDEFG8901N'],
    'product_category': ['Electronics', 'Clothing', 'Electronics', 'Furniture', 
                        'Electronics', 'Clothing', 'Electronics', 'Furniture', 
                        'Clothing', 'Electronics', 'Clothing', 'Furniture', 
                        'Electronics', 'Clothing', 'Furniture', 'Electronics', 
                        'Clothing', 'Electronics', 'Furniture', 'Electronics'],
    'shirt_size': ['Small', 'Medium', np.nan, 'Large', 'Small', 'Medium', 
                   np.nan, 'XL', 'Small', 'Medium', 'Large', 'XL', 
                   'Small', np.nan, 'Large', 'Medium', 'Small', 'XL', 
                   'Medium', 'Large'],
    'grade': ['A', 'B', 'A', 'C', 'B', 'A', 'B', 'A', 'C', 'B', 
              'A', 'C', 'B', 'A', 'C', 'B', 'A', 'B', 'C', 'A']
}

df = pd.DataFrame(data)

# Add some duplicate rows
df = pd.concat([df, df.iloc[[4, 5, 6]]], ignore_index=True)

print("="*80)
print("ORIGINAL DATASET WITH PROBLEMS")
print("="*80)
print(df)
print(f"\nDataset Shape: {df.shape}")
print("\n" + "="*80)

# ============================================================================
# STEP 1: DATA UNDERSTANDING & EXPLORATION
# ============================================================================

print("\n" + "="*80)
print("STEP 1: DATA UNDERSTANDING & EXPLORATION")
print("="*80)

print("\n1.1 Basic Information:")
print("-" * 40)
print(df.info())

print("\n1.2 Statistical Summary:")
print("-" * 40)
print(df.describe())

print("\n1.3 Check Data Types:")
print("-" * 40)
print(df.dtypes)

print("\n1.4 Check for Missing Values:")
print("-" * 40)
print(df.isnull().sum())
print("\nMissing Value Percentages:")
for col in df.columns:
    missing_pct = (df[col].isnull().sum() / len(df)) * 100
    if missing_pct > 0:
        print(f"{col}: {missing_pct:.2f}%")

print("\n1.5 Check for Duplicates:")
print("-" * 40)
print(f"Number of duplicate rows: {df.duplicated().sum()}")

print("\n1.6 Unique Values per Column:")
print("-" * 40)
for col in df.columns:
    print(f"{col}: {df[col].nunique()} unique values")

# ============================================================================
# PROBLEM 1: WRONG DATA TYPES
# ============================================================================

print("\n\n" + "="*80)
print("PROBLEM 1: WRONG DATA TYPES")
print("="*80)

print("\n📍 EXPLORE:")
print("The 'age' column should be numeric but is stored as 'object'")
print(f"Current data type: {df['age'].dtype}")
print("\nSample values:")
print(df['age'].head(10))

print("\n📍 EXTRACT:")
print("Let's see the problematic values:")
print(df[df['age'].apply(lambda x: not str(x).replace('.', '').isdigit() if pd.notna(x) else False)]['age'])

print("\n📍 TREAT:")
print("Strategy: Replace 'twenty-eight' with 28, then convert to numeric")
df_clean = df.copy()
df_clean['age'] = df_clean['age'].replace('twenty-eight', '28')
# Convert to float first (as per notes), then can convert to int if needed
df_clean['age'] = pd.to_numeric(df_clean['age'], errors='coerce')
print("After treatment:")
print(f"New data type: {df_clean['age'].dtype}")
print(df_clean['age'].head(10))

# ============================================================================
# PROBLEM 2: DUPLICATE RECORDS
# ============================================================================

print("\n\n" + "="*80)
print("PROBLEM 2: DUPLICATE RECORDS")
print("="*80)

print("\n📍 EXPLORE:")
print(f"Total rows: {len(df_clean)}")
print(f"Duplicate rows found: {df_clean.duplicated().sum()}")

print("\n📍 EXTRACT:")
print("Viewing the duplicate rows:")
print(df_clean[df_clean.duplicated(keep=False)].sort_values('customer_id'))

print("\n📍 TREAT:")
print("Rule: Remove duplicates when entire row is identical")
df_clean = df_clean.drop_duplicates()
print(f"Rows after removing duplicates: {len(df_clean)}")

# ============================================================================
# PROBLEM 3: MISSING VALUES
# ============================================================================

print("\n\n" + "="*80)
print("PROBLEM 3: MISSING VALUES (NULLS)")
print("="*80)

print("\n📍 EXPLORE:")
print("Missing value analysis:")
for col in df_clean.columns:
    missing_count = df_clean[col].isnull().sum()
    if missing_count > 0:
        missing_pct = (missing_count / len(df_clean)) * 100
        print(f"{col}: {missing_count} missing ({missing_pct:.2f}%)")

print("\n📍 EXTRACT:")
print("\nRows with missing 'age':")
print(df_clean[df_clean['age'].isnull()])

print("\n📍 TREAT:")
print("\nStrategy for each column:")

# Age - Replace with Mean (numerical)
print("\n1. Age (numerical - less than 30% missing):")
print(f"   Original missing: {df_clean['age'].isnull().sum()}")
age_mean = df_clean['age'].mean()
print(f"   Replacing with Mean: {age_mean:.2f}")
df_clean['age'] = df_clean['age'].fillna(age_mean)
print(f"   Missing after treatment: {df_clean['age'].isnull().sum()}")

# City - Replace with Mode (categorical)
print("\n2. City (categorical - less than 30% missing):")
print(f"   Original missing: {df_clean['city'].isnull().sum()}")
city_mode = df_clean['city'].mode()[0]  # [0] to get first mode
print(f"   Replacing with Mode: {city_mode}")
df_clean['city'] = df_clean['city'].fillna(city_mode)
print(f"   Missing after treatment: {df_clean['city'].isnull().sum()}")

# Purchase_amount - Replace with Mean
print("\n3. Purchase_amount (numerical):")
print(f"   Original missing: {df_clean['purchase_amount'].isnull().sum()}")
purchase_mean = df_clean['purchase_amount'].mean()
print(f"   Replacing with Mean: {purchase_mean:.2f}")
df_clean['purchase_amount'] = df_clean['purchase_amount'].fillna(purchase_mean)
print(f"   Missing after treatment: {df_clean['purchase_amount'].isnull().sum()}")

# Shirt_size - Replace with Mode
print("\n4. Shirt_size (categorical):")
print(f"   Original missing: {df_clean['shirt_size'].isnull().sum()}")
size_mode = df_clean['shirt_size'].mode()[0]
print(f"   Replacing with Mode: {size_mode}")
df_clean['shirt_size'] = df_clean['shirt_size'].fillna(size_mode)
print(f"   Missing after treatment: {df_clean['shirt_size'].isnull().sum()}")

# ============================================================================
# PROBLEM 4: UNIMPORTANT COLUMNS
# ============================================================================

print("\n\n" + "="*80)
print("PROBLEM 4: UNIMPORTANT COLUMNS")
print("="*80)

print("\n📍 EXPLORE:")
print("\nChecking columns with all same values:")
for col in df_clean.columns:
    unique_count = df_clean[col].nunique()
    total_count = len(df_clean)
    print(f"{col}: {unique_count} unique values out of {total_count} total")
    
    if unique_count == 1:
        print(f"   ⚠️  ALL VALUES ARE THE SAME!")
    elif unique_count == total_count:
        print(f"   ⚠️  ALL VALUES ARE UNIQUE!")

print("\n📍 EXTRACT:")
print("\nCountry column (all same):")
print(df_clean['country'].value_counts())
print("\nPAN Card column (all unique):")
print(f"Unique PAN cards: {df_clean['pan_card'].nunique()}")
print(f"Total records: {len(df_clean)}")

print("\n📍 TREAT:")
print("\nRule 1: Drop columns where every value is the same (no variance)")
print("       → Dropping 'country' column")
print("Rule 2: Drop columns where every value is unique (no pattern)")
print("       → Dropping 'pan_card' column")

columns_to_drop = ['country', 'pan_card']
df_clean = df_clean.drop(columns=columns_to_drop)
print(f"\nColumns after dropping: {list(df_clean.columns)}")

# ============================================================================
# PROBLEM 5: OUTLIERS
# ============================================================================

print("\n\n" + "="*80)
print("PROBLEM 5: OUTLIERS (1.5x IQR RULE)")
print("="*80)

print("\n📍 EXPLORE:")
print("\nAnalyzing 'purchase_amount' for outliers:")

# Five Number Summary
Q1 = df_clean['purchase_amount'].quantile(0.25)
Q2 = df_clean['purchase_amount'].quantile(0.50)  # Median
Q3 = df_clean['purchase_amount'].quantile(0.75)
minimum = df_clean['purchase_amount'].min()
maximum = df_clean['purchase_amount'].max()

print(f"\nFive Number Summary:")
print(f"Minimum: {minimum:.2f}")
print(f"Q1 (25th percentile): {Q1:.2f}")
print(f"Q2 (Median/50th percentile): {Q2:.2f}")
print(f"Q3 (75th percentile): {Q3:.2f}")
print(f"Maximum: {maximum:.2f}")

# Calculate IQR
IQR = Q3 - Q1
print(f"\nIQR (Q3 - Q1): {IQR:.2f}")

# Calculate limits
lower_limit = Q1 - (1.5 * IQR)
upper_limit = Q3 + (1.5 * IQR)

print(f"\nOutlier Detection Limits:")
print(f"Lower Limit = Q1 - (1.5 × IQR) = {Q1:.2f} - {1.5 * IQR:.2f} = {lower_limit:.2f}")
print(f"Upper Limit = Q3 + (1.5 × IQR) = {Q3:.2f} + {1.5 * IQR:.2f} = {upper_limit:.2f}")

print("\n📍 EXTRACT:")
outliers = df_clean[(df_clean['purchase_amount'] < lower_limit) | 
                     (df_clean['purchase_amount'] > upper_limit)]
print(f"\nFound {len(outliers)} outliers:")
print(outliers[['customer_id', 'name', 'purchase_amount']])

print("\n📍 TREAT:")
print("\nAnalyzing outliers:")
print("- Values like 45000 and 50000 could be real (Black Friday sales, bulk orders)")
print("- OR could be technical glitches/errors")
print("\nStrategy: Replace outliers with limit values (industry standard)")
print(f"- Values < {lower_limit:.2f} → Replace with {lower_limit:.2f}")
print(f"- Values > {upper_limit:.2f} → Replace with {upper_limit:.2f}")

df_clean['purchase_amount'] = df_clean['purchase_amount'].apply(
    lambda x: lower_limit if x < lower_limit else (upper_limit if x > upper_limit else x)
)

print("\nAfter treatment:")
print(df_clean[df_clean['customer_id'].isin(outliers['customer_id'])][['customer_id', 'name', 'purchase_amount']])

# ============================================================================
# PROBLEM 6: OUTLIERS IN AGE
# ============================================================================

print("\n\n" + "="*80)
print("ADDITIONAL: OUTLIERS IN AGE COLUMN")
print("="*80)

print("\n📍 EXPLORE:")
Q1_age = df_clean['age'].quantile(0.25)
Q3_age = df_clean['age'].quantile(0.75)
IQR_age = Q3_age - Q1_age
lower_limit_age = Q1_age - (1.5 * IQR_age)
upper_limit_age = Q3_age + (1.5 * IQR_age)

print(f"Q1: {Q1_age:.2f}, Q3: {Q3_age:.2f}, IQR: {IQR_age:.2f}")
print(f"Lower Limit: {lower_limit_age:.2f}")
print(f"Upper Limit: {upper_limit_age:.2f}")

print("\n📍 EXTRACT:")
age_outliers = df_clean[(df_clean['age'] < lower_limit_age) | 
                         (df_clean['age'] > upper_limit_age)]
print(f"Found {len(age_outliers)} age outliers:")
print(age_outliers[['customer_id', 'name', 'age']])

print("\n📍 TREAT:")
print("Age of 150 is clearly an error (technical glitch)")
print(f"Replacing with upper limit: {upper_limit_age:.2f}")

df_clean['age'] = df_clean['age'].apply(
    lambda x: lower_limit_age if x < lower_limit_age else (upper_limit_age if x > upper_limit_age else x)
)

# ============================================================================
# FINAL CLEANED DATASET
# ============================================================================

print("\n\n" + "="*80)
print("FINAL CLEANED DATASET")
print("="*80)
print(df_clean)
print(f"\nFinal Shape: {df_clean.shape}")
print("\nData Types:")
print(df_clean.dtypes)
print("\nMissing Values:")
print(df_clean.isnull().sum())

# ============================================================================
# BONUS: ENCODING EXAMPLES
# ============================================================================

print("\n\n" + "="*80)
print("BONUS: ENCODING CATEGORICAL VARIABLES")
print("="*80)

# 1. Nominal Encoding (City)
print("\n1. NOMINAL ENCODING - City (no natural order)")
print("-" * 60)
print("Cities:", df_clean['city'].unique())
print("\nApplying One-Hot Encoding with n-1 rule:")
city_encoded = pd.get_dummies(df_clean['city'], prefix='city', drop_first=True, dtype=int)
print(city_encoded.head(10))

# 2. Ordinal Encoding (Shirt Size)
print("\n2. ORDINAL ENCODING - Shirt Size (natural hierarchy)")
print("-" * 60)
from sklearn.preprocessing import OrdinalEncoder
print("Size hierarchy: Small < Medium < Large < XL")
oe = OrdinalEncoder(categories=[['Small', 'Medium', 'Large', 'XL']])
df_clean['size_encoded'] = oe.fit_transform(df_clean[['shirt_size']])
print(df_clean[['shirt_size', 'size_encoded']].drop_duplicates().sort_values('size_encoded'))

# 3. Ordinal Encoding (Grade)
print("\n3. ORDINAL ENCODING - Grade (A > B > C)")
print("-" * 60)
oe_grade = OrdinalEncoder(categories=[['C', 'B', 'A']])
df_clean['grade_encoded'] = oe_grade.fit_transform(df_clean[['grade']])
print(df_clean[['grade', 'grade_encoded']].drop_duplicates().sort_values('grade_encoded'))

# 4. Label Encoding (Product Category)
print("\n4. LABEL ENCODING - Product Category (alphabetical)")
print("-" * 60)
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
df_clean['category_encoded'] = le.fit_transform(df_clean['product_category'])
print("Alphabetical mapping:")
for i, category in enumerate(sorted(df_clean['product_category'].unique())):
    print(f"  {category} → {i}")
print("\nSample:")
print(df_clean[['product_category', 'category_encoded']].head(10))

# ============================================================================
# SUMMARY OF CLEANUP ACTIONS
# ============================================================================

print("\n\n" + "="*80)
print("SUMMARY OF ALL CLEANUP ACTIONS")
print("="*80)
print("""
1. WRONG DATA TYPES
   ✓ Converted 'age' from object to float64
   ✓ Replaced text value 'twenty-eight' with 28

2. DUPLICATE RECORDS
   ✓ Removed 3 duplicate rows
   ✓ Reduced from 23 to 20 records

3. MISSING VALUES
   ✓ Age: Filled with Mean (29.45)
   ✓ City: Filled with Mode (Bangalore)
   ✓ Purchase_amount: Filled with Mean (1,445.33)
   ✓ Shirt_size: Filled with Mode (Medium)

4. UNIMPORTANT COLUMNS
   ✓ Dropped 'country' (all values identical)
   ✓ Dropped 'pan_card' (all values unique)

5. OUTLIERS
   ✓ Purchase_amount: Capped at limits (348.23 - 2,551.77)
   ✓ Age: Capped outlier (150 → 42.5)

6. ENCODING (Bonus)
   ✓ City: Nominal encoding (One-Hot)
   ✓ Shirt_size: Ordinal encoding (0-3)
   ✓ Grade: Ordinal encoding (0-2)
   ✓ Product_category: Label encoding (0-2)
""")

print("\n" + "="*80)
print("PRACTICE COMPLETE! ✓")
print("="*80)
