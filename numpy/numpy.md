# NumPy Tutorial for Beginners
## (Numerical Python)

---

## Table of Contents
1. [Introduction to NumPy](#introduction)
2. [NumPy Arrays Basics](#arrays-basics)
3. [Creating 1D Arrays](#creating-1d-arrays)
4. [Accessing and Modifying Arrays](#accessing-modifying)
5. [Array Operations](#operations)
6. [2D Arrays](#2d-arrays)
7. [Array Manipulation](#manipulation)
8. [Matrix Operations](#matrix-operations)

---

## 1. Introduction to NumPy {#introduction}

### What is NumPy?
NumPy is a Python library for numerical computing that provides powerful array objects and mathematical functions.

### Why Use NumPy?
- Faster than Python lists for numerical operations
- Provides multi-dimensional arrays
- Rich collection of mathematical functions
- Foundation for data science libraries (Pandas, SciPy, etc.)

### Installation
```python
# Install using pip
pip install numpy

# Import NumPy
import numpy as np
```

---

## 2. NumPy Arrays Basics {#arrays-basics}

### Rule: Regular Python vs NumPy Array
- **Python variable**: Just stores a single value
- **NumPy array**: Stores multiple values efficiently

### ⚠️ IMPORTANT RULE: What Can Be Converted to NumPy Arrays?
- ✅ **Lists**: `np.array([1, 2, 3])` - WORKS
- ✅ **Tuples**: `np.array((1, 2, 3))` - WORKS
- ✅ **Nested lists/tuples**: `np.array([[1, 2], [3, 4]])` - WORKS
- ❌ **Single numbers**: `np.array(45)` - Creates 0-D array (usually not intended)
- ❌ **Strings**: `np.array("hello")` - Creates array of single string (usually not intended)
- ❌ **Dictionaries**: `np.array({1: 2})` - GIVES ERROR
- ❌ **Sets**: `np.array({1, 2, 3})` - GIVES ERROR

**Best Practice**: Always use lists `[]` or tuples `()` to create NumPy arrays!

### Example: Creating Your First Array

```python
import numpy as np

# Regular Python integer
num = 45
print(num)
print(type(num))
# Output: 45
# Output: <class 'int'>

# ❌ AVOID: Converting single number (creates 0-D array)
# This is technically valid but rarely what you want
scalar_array = np.array(num)
print(type(scalar_array))
# Output: <class 'numpy.ndarray'>
print(scalar_array.ndim)
# Output: 0  # Zero-dimensional array!

# ✅ CORRECT: Use list or tuple to create array
number_list = [45]
proper_array = np.array(number_list)
print(proper_array)
# Output: [45]
print(proper_array.ndim)
# Output: 1  # One-dimensional array
```

### Example: 1D Array from List

```python
# ✅ Create array from Python list
numbers_list = [10, 20, 30]
arr_from_list = np.array(numbers_list)
print(arr_from_list)
# Output: [10 20 30]

# Check number of dimensions
print(arr_from_list.ndim)
# Output: 1

# Check shape (size of each dimension)
print(arr_from_list.shape)
# Output: (3,)  # means 3 elements in one dimension
```

### Example: 1D Array from Tuple

```python
# ✅ Create array from Python tuple
numbers_tuple = (100, 200, 300)
arr_from_tuple = np.array(numbers_tuple)
print(arr_from_tuple)
# Output: [100 200 300]

# Check number of dimensions
print(arr_from_tuple.ndim)
# Output: 1

# Check shape (size of each dimension)
print(arr_from_tuple.shape)
# Output: (3,)  # means 3 elements in one dimension
```

### Rule: Understanding Dimensions
- **ndim**: Number of dimensions (axes)
  - 1D array: ndim = 1 (like a list)
  - 2D array: ndim = 2 (like a table/matrix)
  - 3D array: ndim = 3 (like a cube)
- **shape**: Size of each dimension as a tuple
  - (3,) means 3 elements in 1D
  - (2, 3) means 2 rows, 3 columns in 2D

### Example: 2D Array

```python
# ✅ CORRECT: Use nested list (double brackets for 2D)
matrix_list = [[10, 20, 30]]
arr_2d = np.array(matrix_list)
print(arr_2d)
# Output: [[10 20 30]]

print(arr_2d.ndim)
# Output: 2

print(arr_2d.shape)
# Output: (1, 3)  # 1 row, 3 columns

# ✅ CORRECT: Create 2D array from nested tuple
matrix_tuple = ((5, 15, 25),)
arr_2d_tuple = np.array(matrix_tuple)
print(arr_2d_tuple)
# Output: [[5 15 25]]

print(arr_2d_tuple.shape)
# Output: (1, 3)  # 1 row, 3 columns
```

---

## 3. Creating 1D Arrays {#creating-1d-arrays}

### Rule: Common Array Creation Functions

| Function | Purpose | Example |
|----------|---------|---------|
| `np.array()` | Convert list to array | `np.array([1,2,3])` |
| `np.arange()` | Create range of values | `np.arange(0, 10, 2)` |
| `np.zeros()` | Create array of zeros | `np.zeros(5)` |
| `np.ones()` | Create array of ones | `np.ones(5)` |
| `np.linspace()` | Create evenly spaced values | `np.linspace(0, 1, 5)` |
| `np.random.randint()` | Random integers | `np.random.randint(0, 100, 5)` |

### Examples:

```python
# 1. arange - like Python range()
sequence_arr = np.arange(1, 10)
print(sequence_arr)
# Output: [1 2 3 4 5 6 7 8 9]

# Rule: arange(start, stop, step)
# - start: included
# - stop: excluded
# - step: increment (default 1)

# 2. zeros - array filled with zeros
zeros_arr = np.zeros(5)
print(zeros_arr)
# Output: [0. 0. 0. 0. 0.]

# 3. ones - array filled with ones
ones_arr = np.ones(5)
print(ones_arr)
# Output: [1. 1. 1. 1. 1.]

# 4. linspace - evenly spaced numbers
# Rule: linspace(start, stop, num_of_samples)
# Both start and stop are INCLUDED
evenly_spaced = np.linspace(0, 1, 5)
print(evenly_spaced)
# Output: [0.   0.25 0.5  0.75 1.  ]

# 5. Random integers
# Rule: randint(start, end, num_of_samples)
# start is included, end is excluded
random_numbers = np.random.randint(1, 1000, 5)
print(random_numbers)
# Output: [14 387 268 307 884] (your numbers will differ)
```

---

## 4. Accessing and Modifying Arrays {#accessing-modifying}

### Rule: Indexing Starts at 0
- First element: index 0
- Last element: index -1
- Second-to-last: index -2

### A. Accessing Single Values

```python
prices = np.arange(10, 51, 10)
print(prices)
# Output: [10 20 30 40 50]

# Access first element
print(prices[0])
# Output: 10

# Access last element
print(prices[-1])
# Output: 50
```

### B. Slicing Arrays

```python
# Rule: array[start:stop:step]
# start: included
# stop: excluded
# step: increment (default 1)

# Get elements from index 1 to 4 (exclusive)
print(prices[1:4])
# Output: [20 30 40]

# Get every 2nd element from index 0 to 5
print(prices[0:5:2])
# Output: [10 30 50]

# Reverse slicing
print(prices[-1:-4:-1])
# Output: [50 40 30]
```

### C. Fancy Indexing

```python
# Rule: Access multiple specific elements using a list of indices
# Syntax: array[[index1, index2, index3]]

print(prices[[0, 3, 2, 4]])
# Output: [10 40 30 50]
```

### D. Boolean Indexing (Filtering)

```python
# Rule: Use conditions to filter arrays
numbers = np.array([45, 46, 47])

# Get only even numbers
even_nums = numbers[numbers % 2 == 0]
print(even_nums)
# Output: [46]

# Get numbers greater than 45
greater_than_45 = numbers[numbers > 45]
print(greater_than_45)
# Output: [46 47]
```

### E. Adding Values

```python
# Rule: np.append() returns NEW array (doesn't modify original)
scores = np.array([45, 46, 47])

# Add single value
scores_with_new = np.append(scores, 110)
print(scores_with_new)
# Output: [45 46 47 110]

# Add multiple values
scores_extended = np.append(scores, [140, 120, 130])
print(scores_extended)
# Output: [45 46 47 140 120 130]
```

### F. Modifying Values

```python
grades = np.array([85, 90, 78])

# Replace single value
grades[1] = 95
print(grades)
# Output: [85 95 78]

# Replace multiple values with one value
grades[[1, 2]] = 80
print(grades)
# Output: [85 80 80]

# Replace multiple values with multiple values
grades[[0, 2]] = [88, 92]
print(grades)
# Output: [88 80 92]
```

### G. Deleting Values

```python
# Rule: np.delete(array, index/indices)
# Returns NEW array

temperatures = np.array([20, 25, 30, 35])

# Delete single value
temp_reduced = np.delete(temperatures, 1)
print(temp_reduced)
# Output: [20 30 35]

# Delete multiple values
temp_minimal = np.delete(temperatures, [1, 2])
print(temp_minimal)
# Output: [20 35]
```

### H. Copying Arrays

```python
# Rule: ALWAYS use .copy() to create independent copy
# Without copy(), changes affect original array

original = np.array([1, 2, 3])

# ❌ WRONG - creates reference, not copy
reference = original
reference[0] = 100
print(original)  # Changed!
# Output: [100 2 3]

# ✅ CORRECT - creates independent copy
original = np.array([1, 2, 3])
independent_copy = original.copy()
independent_copy[0] = 100
print(original)  # Not changed
# Output: [1 2 3]
print(independent_copy)
# Output: [100 2 3]
```

### I. Sorting Arrays

```python
# Rule: np.sort() returns sorted array, doesn't modify original
unsorted = np.array([64, 25, 12, 22, 11])

sorted_arr = np.sort(unsorted)
print(sorted_arr)
# Output: [11 12 22 25 64]
```

---

## 5. Array Operations {#operations}

### Rule: Operations Work Element-wise
- Arrays must have compatible shapes
- Operation applies to corresponding elements

### A. Arithmetic Operations

```python
arr1 = np.array([10, 20, 30, 40])
arr2 = np.array([5, 10, 15, 20])

# Addition
sum_result = arr1 + arr2
print(sum_result)
# Output: [15 30 45 60]

# Subtraction
diff_result = arr1 - arr2
print(diff_result)
# Output: [5 10 15 20]

# Multiplication (element-wise)
product_result = arr1 * arr2
print(product_result)
# Output: [50 200 450 800]

# Division
division_result = arr1 / arr2
print(division_result)
# Output: [2. 2. 2. 2.]

# Power
squared = arr1 ** 2
print(squared)
# Output: [100 400 900 1600]
```

### B. Comparison Operations

```python
# Rule: Returns boolean array
values1 = np.array([10, 20, 30, 40])
values2 = np.array([15, 15, 30, 35])

# Element-wise comparison
less_than = values1 < values2
print(less_than)
# Output: [True False False False]

greater_than = values1 > values2
print(greater_than)
# Output: [False True False True]

equal_to = values1 == values2
print(equal_to)
# Output: [False False True False]

# Check if entire arrays are equal
values3 = np.array([10, 20, 30, 40])
are_equal = np.array_equal(values1, values3)
print(are_equal)
# Output: True
```

### C. Mathematical Functions

```python
nums = np.array([1, 4, 9, 16])

# Exponential
exp_result = np.exp(nums)
print(exp_result)
# Output: [2.718  54.598  8103.084  8886110.521]

# Square root
sqrt_result = np.sqrt(nums)
print(sqrt_result)
# Output: [1. 2. 3. 4.]

# Logarithm (natural log)
log_result = np.log(nums)
print(log_result)
# Output: [0.  1.386  2.197  2.773]

# Trigonometric
angles = np.array([0, 30, 45, 60, 90])
sin_values = np.sin(np.radians(angles))  # Convert degrees to radians
print(sin_values)
# Output: [0.  0.5  0.707  0.866  1.]
```

### D. Aggregate Functions

```python
data = np.array([10, 20, 30, 40, 50])

# Sum of all elements
total = np.sum(data)
print(total)
# Output: 150

# Mean (average)
average = np.mean(data)
print(average)
# Output: 30.0

# Median
median = np.median(data)
print(median)
# Output: 30.0

# Standard deviation
std_dev = np.std(data)
print(std_dev)
# Output: 14.142

# Minimum and maximum
minimum = np.min(data)
print(minimum)
# Output: 10

maximum = np.max(data)
print(maximum)
# Output: 50

# Index of minimum and maximum
min_index = np.argmin(data)
print(min_index)
# Output: 0

max_index = np.argmax(data)
print(max_index)
# Output: 4
```

---

## 6. 2D Arrays (Matrices) {#2d-arrays}

### Rule: 2D Array Structure
- Rows: First dimension (axis 0)
- Columns: Second dimension (axis 1)
- Shape: (rows, columns)

### A. Creating 2D Arrays

```python
# Method 1: From nested list
matrix = np.array([[100, 200, 300, 400], 
                   [500, 600, 700, 800]])
print(matrix)
# Output: [[100 200 300 400]
#          [500 600 700 800]]

print(matrix.ndim)
# Output: 2

print(matrix.shape)
# Output: (2, 4)  # 2 rows, 4 columns
```

### B. Special 2D Arrays

```python
# Zeros matrix
zeros_matrix = np.zeros((3, 3))
print(zeros_matrix)
# Output: [[0. 0. 0.]
#          [0. 0. 0.]
#          [0. 0. 0.]]

# Ones matrix
ones_matrix = np.ones((3, 3))
print(ones_matrix)
# Output: [[1. 1. 1.]
#          [1. 1. 1.]
#          [1. 1. 1.]]

# Identity matrix (diagonal of 1s)
identity_matrix = np.eye(3, 3)
print(identity_matrix)
# Output: [[1. 0. 0.]
#          [0. 1. 0.]
#          [0. 0. 1.]]

# Diagonal matrix
diagonal_matrix = np.diag([5, 10, 15])
print(diagonal_matrix)
# Output: [[5  0  0]
#          [0 10  0]
#          [0  0 15]]

# Extract diagonal from existing matrix
sample_matrix = np.array([[1, 2, 3], 
                          [4, 5, 6]])
diagonal_elements = np.diag(sample_matrix)
print(diagonal_elements)
# Output: [1 5]  # main diagonal elements
```

### C. Indexing 2D Arrays

```python
sales_data = np.array([[10, 20, 50], 
                       [30, 40, 60],
                       [20, 80, 90]])
print(sales_data)
# Output: [[10 20 50]
#          [30 40 60]
#          [20 80 90]]

# Rule: array[row, column]

# Access entire first row
first_row = sales_data[0]
print(first_row)
# Output: [10 20 50]

# Access specific element (row 2, column 2)
element = sales_data[2, 2]
print(element)
# Output: 90

# Access element (row 1, column 0)
element2 = sales_data[1, 0]
print(element2)
# Output: 30

# Slice rows
rows_1_to_2 = sales_data[1:3]
print(rows_1_to_2)
# Output: [[30 40 60]
#          [20 80 90]]

# Slice specific row and columns
row0_cols = sales_data[0, 1:3]
print(row0_cols)
# Output: [20 50]

# Access all rows, specific column
column_1 = sales_data[:, 1]
print(column_1)
# Output: [20 40 80]

# Access specific rows, all columns
first_two_rows = sales_data[0:2, :]
print(first_two_rows)
# Output: [[10 20 50]
#          [30 40 60]]
```

---

## 7. Array Manipulation {#manipulation}

### A. Flattening (2D to 1D)

```python
# Rule: .ravel() converts any array to 1D
grid = np.array([[10, 20, 30], 
                 [40, 50, 60]])

flattened = grid.ravel()
print(flattened)
# Output: [10 20 30 40 50 60]
```

### B. Reshaping

```python
# Rule: reshape(rows, columns)
# Total elements must match: rows × columns = total elements

sequence = np.arange(6)
print(sequence)
# Output: [0 1 2 3 4 5]

print(sequence.shape)
# Output: (6,)

# Reshape to 2×3
matrix_2x3 = sequence.reshape(2, 3)
print(matrix_2x3)
# Output: [[0 1 2]
#          [3 4 5]]

# Reshape to 3×2
matrix_3x2 = sequence.reshape(3, 2)
print(matrix_3x2)
# Output: [[0 1]
#          [2 3]
#          [4 5]]

# Check shape
data = np.array([[100, 200, 300], 
                 [400, 500, 600]])
print(data.shape)
# Output: (2, 3)

# Reshape
reshaped_data = data.reshape(3, 2)
print(reshaped_data)
# Output: [[100 200]
#          [300 400]
#          [500 600]]
```

### C. Transpose

```python
# Rule: .T swaps rows and columns
# (rows, columns) becomes (columns, rows)

original = np.array([[1, 2, 3], 
                     [4, 5, 6]])
print(original.shape)
# Output: (2, 3)

transposed = original.T
print(transposed)
# Output: [[1 4]
#          [2 5]
#          [3 6]]

print(transposed.shape)
# Output: (3, 2)
```

---

## 8. Matrix Operations {#matrix-operations}

### A. Element-wise Operations

```python
# Rule: Same as 1D arrays, but on 2D
matrix_a = np.array([[1, 2], 
                     [3, 4]])
matrix_b = np.array([[10, 20], 
                     [30, 40]])

# Addition
sum_matrices = matrix_a + matrix_b
print(sum_matrices)
# Output: [[11 22]
#          [33 44]]

# Subtraction
diff_matrices = matrix_b - matrix_a
print(diff_matrices)
# Output: [[9 18]
#          [27 36]]

# Element-wise multiplication (NOT matrix multiplication)
element_product = matrix_a * matrix_b
print(element_product)
# Output: [[10 40]
#          [90 160]]
```

### B. Matrix Multiplication

```python
# Rule: Use np.matmul() or @ operator
# Shapes must be compatible: (m, n) × (n, p) = (m, p)

mat1 = np.array([[1, 2], 
                 [3, 4]])
mat2 = np.array([[5, 6], 
                 [7, 8]])

# Method 1: np.matmul()
result_matmul = np.matmul(mat1, mat2)
print(result_matmul)
# Output: [[19 22]
#          [43 50]]

# Method 2: @ operator
result_at = mat1 @ mat2
print(result_at)
# Output: [[19 22]
#          [43 50]]
```

### C. Concatenation

```python
block_a = np.array([[1, 2], 
                    [3, 4]])
block_b = np.array([[5, 6], 
                    [7, 8]])

# Rule: axis=0 stacks vertically (adds rows)
# Rule: axis=1 stacks horizontally (adds columns)

# Vertical stack (axis=0) - stack rows
vertical_concat = np.concatenate((block_a, block_b), axis=0)
print(vertical_concat)
# Output: [[1 2]
#          [3 4]
#          [5 6]
#          [7 8]]

# Alternative: np.vstack()
vertical_stack = np.vstack((block_a, block_b))
print(vertical_stack)
# Output: [[1 2]
#          [3 4]
#          [5 6]
#          [7 8]]

# Horizontal stack (axis=1) - stack columns
horizontal_concat = np.concatenate((block_a, block_b), axis=1)
print(horizontal_concat)
# Output: [[1 2 5 6]
#          [3 4 7 8]]

# Alternative: np.hstack()
horizontal_stack = np.hstack((block_a, block_b))
print(horizontal_stack)
# Output: [[1 2 5 6]
#          [3 4 7 8]]
```

---

## Quick Reference: Key Rules to Remember

### 1. **Array Creation**
- Use `np.array()` to convert lists
- Use `np.arange(start, stop, step)` for ranges (stop excluded)
- Use `np.linspace(start, stop, n)` for n evenly spaced values (both included)

### 2. **Indexing**
- Indexing starts at 0
- Negative indices count from the end (-1 is last)
- Slicing: `[start:stop:step]` (stop excluded)

### 3. **Dimensions**
- `ndim`: number of dimensions
- `shape`: tuple of dimension sizes
- 1D: `(n,)`, 2D: `(rows, cols)`

### 4. **Modifying Arrays**
- Most operations return NEW arrays
- Use `.copy()` for independent copies
- `np.append()`, `np.delete()` don't modify original

### 5. **Operations**
- Arithmetic operations are element-wise
- Use `np.matmul()` or `@` for matrix multiplication
- Arrays must have compatible shapes

### 6. **Axis Parameter**
- `axis=0`: operate along rows (vertically)
- `axis=1`: operate along columns (horizontally)

### 7. **Common Functions**
- Aggregation: `sum()`, `mean()`, `min()`, `max()`
- Math: `sqrt()`, `exp()`, `log()`, `sin()`, `cos()`
- Shape: `reshape()`, `ravel()`, `.T` (transpose)

---

## Practice Exercises

### Beginner Level
1. Create an array of numbers from 0 to 9
2. Create a 3×3 matrix of ones
3. Access the middle element of `[1, 2, 3, 4, 5]`
4. Get all even numbers from an array

### Intermediate Level
1. Reshape array `[1,2,3,4,5,6]` into 2×3 matrix
2. Add two 2×2 matrices together
3. Find the mean of each row in a matrix
4. Concatenate two arrays vertically

### Advanced Level
1. Multiply two matrices using matrix multiplication
2. Create a 5×5 identity matrix
3. Extract diagonal elements from a matrix
4. Filter a 2D array based on conditions

---

## Additional Resources

- Official NumPy Documentation: https://numpy.org/doc/
- NumPy Quickstart Tutorial: https://numpy.org/doc/stable/user/quickstart.html
- Practice on platforms like HackerRank, LeetCode, or Kaggle

---

**Happy Learning! 🎓**
