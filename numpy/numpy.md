# NumPy Complete Guide for Beginners

## Everything You Need to Know About NumPy Arrays

---

## Table of Contents

1. [What is NumPy?](#1-what-is-numpy)
2. [Why Use NumPy?](#2-why-use-numpy)
3. [Creating NumPy Arrays](#3-creating-numpy-arrays)
4. [Array Attributes & Data Types](#4-array-attributes--data-types)
5. [1D Array Operations](#5-1d-array-operations)
6. [2D Array Operations](#6-2d-array-operations)
7. [Indexing and Slicing](#7-indexing-and-slicing)
8. [Array Manipulation](#8-array-manipulation)
9. [Mathematical Operations](#9-mathematical-operations)
10. [Reshaping and Transposing](#10-reshaping-and-transposing)
11. [Sorting Arrays](#11-sorting-arrays)
12. [Combining Arrays](#12-combining-arrays)
13. [Quick Reference Guide](#13-quick-reference-guide)
14. [Best Practices](#14-best-practices--important-rules)
15. [Practice Questions](#15-practice-questions-to-master-numpy)

---

## 1. What is NumPy?

**NumPy (Numerical Python)** is a fundamental library for scientific computing in Python. It provides support for large, multi-dimensional arrays and matrices, along with a collection of mathematical functions to operate on these arrays efficiently.

NumPy is the foundation upon which many other scientific libraries are built, including:
- **Pandas** - for data analysis
- **Matplotlib** - for data visualization
- **SciPy** - for scientific computing
- **Scikit-learn** - for machine learning

### Key Features:

- **Powerful N-dimensional array object** - Handle arrays of any dimension efficiently
- **Broadcasting functions** - Perform operations on arrays of different shapes
- **Tools for integrating C/C++ and Fortran code** - Extend Python with compiled code
- **Linear algebra, Fourier transform, and random number capabilities** - Built-in mathematical functions
- **Memory efficient** - Uses contiguous blocks of memory for fast access
- **Written in C** - Provides Python interface with C-level performance

### Installation:

```bash
pip install numpy
```

### Import Convention:

```python
import numpy as np
```

**Why "np"?** This is the universally accepted alias for NumPy. Using this convention makes your code readable to other Python developers worldwide.

---

## 2. Why Use NumPy?

### NumPy vs Python Lists

Understanding the difference between NumPy arrays and Python lists is crucial for writing efficient code.

| Feature | Python List | NumPy Array |
|---------|-------------|-------------|
| **Speed** | Slower (interpreted) | 10-100x Faster (compiled) |
| **Memory** | More memory (objects) | Less memory (fixed type) |
| **Data Types** | Heterogeneous (mixed) | Homogeneous (same type) |
| **Operations** | Requires loops | Vectorized (no loops) |
| **Size** | Dynamic (can grow) | Fixed (must reshape) |
| **Functionality** | Basic operations | Advanced math functions |

### Performance Example:

```python
import numpy as np
import time

# Create large datasets
size = 1000000
python_list = list(range(size))
numpy_array = np.arange(size)

# Python list addition (requires loop)
start = time.time()
result_list = [x + 1 for x in python_list]
time_list = time.time() - start

# NumPy array addition (vectorized)
start = time.time()
result_numpy = numpy_array + 1
time_numpy = time.time() - start

print(f"Python list: {time_list:.6f} seconds")
print(f"NumPy array: {time_numpy:.6f} seconds")
print(f"NumPy is {time_list/time_numpy:.1f}x faster!")
```

### Why NumPy is Faster:

1. **Contiguous Memory** - Elements stored next to each other in memory
2. **Fixed Type** - No type checking during operations
3. **Compiled C Code** - Core operations written in C
4. **Vectorization** - Operations applied to entire arrays at once
5. **Cache Optimization** - Better CPU cache utilization

### Performance Advantages:

- **Speed**: NumPy is 10-100x faster than Python lists for numerical operations
- **Vectorization**: Eliminates the need for explicit Python loops
- **Memory Efficiency**: Uses 4-8 bytes per element vs 28+ bytes for Python list objects
- **Optimized Algorithms**: Built-in functions use highly optimized C implementations

---

## 3. Creating NumPy Arrays

NumPy provides multiple ways to create arrays, each suited for different scenarios.

### Method 1: From Python List

The most straightforward way - convert existing Python lists to NumPy arrays.

```python
# 1D array
arr = np.array([1, 2, 3, 4, 5])
print(arr)  # Output: [1 2 3 4 5]

# 2D array (matrix)
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print(matrix)
# Output:
# [[1 2 3]
#  [4 5 6]]

# 3D array
arr_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
```

**When to use**: When you already have data in list format or need to create small arrays manually.

### Method 2: Using np.arange()

Creates arrays with evenly spaced values (similar to Python's `range()`).

**Syntax**: `np.arange(start, stop, step)`

```python
# Basic usage
arr = np.arange(0, 10, 2)
print(arr)  # Output: [0 2 4 6 8]

# Default start and step
arr = np.arange(5)
print(arr)  # Output: [0 1 2 3 4]

# Floating point steps
arr = np.arange(0, 1, 0.1)
print(arr)  # Output: [0.  0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9]

# Descending
arr = np.arange(10, 0, -1)
print(arr)  # Output: [10 9 8 7 6 5 4 3 2 1]
```

**Important**: The `stop` value is **exclusive** (not included in the result).

**When to use**: When you need sequential values or a range of numbers.

### Method 3: Using np.linspace()

Creates arrays with a specified number of evenly spaced values between two endpoints.

**Syntax**: `np.linspace(start, stop, num_elements)`

```python
# Create 5 points between 0 and 1
arr = np.linspace(0, 1, 5)
print(arr)  # Output: [0.   0.25 0.5  0.75 1.  ]

# Create 11 points between 0 and 10
arr = np.linspace(0, 10, 11)
print(arr)  # Output: [ 0.  1.  2.  3.  4.  5.  6.  7.  8.  9. 10.]

# Exclude endpoint
arr = np.linspace(0, 1, 5, endpoint=False)
print(arr)  # Output: [0.  0.2 0.4 0.6 0.8]
```

**Key Difference from arange**: 
- `arange` uses **step size**
- `linspace` uses **number of elements**

**When to use**: When you need a specific number of points between two values (useful for plotting).

### Method 4: Special Arrays

#### Zeros Array

```python
# 1D zeros
zeros_1d = np.zeros(5)
print(zeros_1d)  # Output: [0. 0. 0. 0. 0.]

# 2D zeros
zeros_2d = np.zeros((3, 4))  # 3 rows, 4 columns
print(zeros_2d)
# Output:
# [[0. 0. 0. 0.]
#  [0. 0. 0. 0.]
#  [0. 0. 0. 0.]]

# Specify data type
zeros_int = np.zeros(5, dtype=int)
print(zeros_int)  # Output: [0 0 0 0 0]
```

**When to use**: Initializing arrays before filling with data, creating placeholders.

#### Ones Array

```python
# 1D ones
ones_1d = np.ones(5)
print(ones_1d)  # Output: [1. 1. 1. 1. 1.]

# 2D ones
ones_2d = np.ones((2, 3))
print(ones_2d)
# Output:
# [[1. 1. 1.]
#  [1. 1. 1.]]
```

**When to use**: Initializing with default values, creating masks.

#### Full Array (Specific Value)

```python
# Fill with specific value
full = np.full(5, 7)
print(full)  # Output: [7 7 7 7 7]

# 2D with specific value
full_2d = np.full((2, 3), 3.14)
print(full_2d)
# Output:
# [[3.14 3.14 3.14]
#  [3.14 3.14 3.14]]
```

**When to use**: When you need to initialize with a specific non-zero value.

#### Identity Matrix

```python
# 3x3 identity matrix
identity = np.eye(3)
print(identity)
# Output:
# [[1. 0. 0.]
#  [0. 1. 0.]
#  [0. 0. 1.]]

# 4x4 identity
identity_4 = np.eye(4)
```

**When to use**: Linear algebra operations, matrix computations.

### Method 5: Random Arrays

#### Uniform Distribution [0, 1)

```python
# Random values between 0 and 1
random_arr = np.random.rand(5)
print(random_arr)
# Output: [0.25 0.80 0.34 0.62 0.02] (values will vary)

# 2D random array
random_2d = np.random.rand(2, 3)
```

#### Random Integers

```python
# Random integers between 1 and 10 (exclusive)
random_int = np.random.randint(1, 10, size=5)
print(random_int)
# Output: [4 5 2 2 5] (values will vary)

# 2D random integers
random_int_2d = np.random.randint(0, 100, size=(3, 3))
```

#### Normal Distribution

```python
# Random values from normal distribution (mean=0, std=1)
normal = np.random.randn(5)

# Custom mean and standard deviation
normal_custom = np.random.normal(loc=50, scale=10, size=5)
# Mean=50, Standard deviation=10
```

**When to use**: Testing algorithms, simulations, initializing neural networks.

---

## 4. Array Attributes & Data Types

Understanding array properties is essential for effective NumPy usage.

### Important Attributes

| Attribute | Description | Example |
|-----------|-------------|---------|
| `.shape` | Dimensions (rows, columns, ...) | `(3, 4)` |
| `.ndim` | Number of dimensions | `2` |
| `.size` | Total number of elements | `12` |
| `.dtype` | Data type of elements | `int32` |
| `.itemsize` | Size of each element in bytes | `4` |
| `.nbytes` | Total bytes consumed | `48` |
| `.T` | Transposed array | Changes rows↔columns |

### Practical Examples:

```python
# Create a 2D array
arr = np.array([[1, 2, 3, 4], 
                [5, 6, 7, 8], 
                [9, 10, 11, 12]])

print(f"Shape: {arr.shape}")        # Output: (3, 4) - 3 rows, 4 columns
print(f"Dimensions: {arr.ndim}")    # Output: 2
print(f"Size: {arr.size}")          # Output: 12 total elements
print(f"Data type: {arr.dtype}")    # Output: int32 or int64
print(f"Item size: {arr.itemsize}") # Output: 4 or 8 bytes
print(f"Total bytes: {arr.nbytes}") # Output: 48 or 96 bytes
```

### Understanding Shape:

```python
# 1D array
arr_1d = np.array([1, 2, 3])
print(arr_1d.shape)  # Output: (3,) - single dimension with 3 elements

# 2D array
arr_2d = np.array([[1, 2], [3, 4]])
print(arr_2d.shape)  # Output: (2, 2) - 2 rows, 2 columns

# 3D array
arr_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(arr_3d.shape)  # Output: (2, 2, 2) - depth, rows, columns
```

### Data Types (dtype)

**CRITICAL RULE**: NumPy arrays are **homogeneous** - all elements must have the same data type.

#### Common Data Types:

| Data Type | Description | Memory | Range |
|-----------|-------------|--------|-------|
| `int8` | 8-bit integer | 1 byte | -128 to 127 |
| `int32` | 32-bit integer | 4 bytes | -2.1B to 2.1B |
| `int64` | 64-bit integer | 8 bytes | -9.2E18 to 9.2E18 |
| `float32` | 32-bit float | 4 bytes | ±3.4E38 (7 digits) |
| `float64` | 64-bit float | 8 bytes | ±1.7E308 (15 digits) |
| `bool` | Boolean | 1 byte | True or False |
| `complex64` | Complex number | 8 bytes | Real + Imaginary |
| `str` | String | Varies | Text data |

#### Type Inference:

```python
# Integer array
arr_int = np.array([1, 2, 3])
print(arr_int.dtype)  # Output: int32 or int64

# Float array
arr_float = np.array([1.0, 2.0, 3.0])
print(arr_float.dtype)  # Output: float64

# Mixed types - promoted to float
arr_mixed = np.array([1, 2.5, 3])
print(arr_mixed.dtype)  # Output: float64
print(arr_mixed)        # Output: [1.  2.5 3. ]
```

#### Specifying Data Type:

```python
# Force float32
arr = np.array([1, 2, 3], dtype=np.float32)
print(arr.dtype)  # Output: float32
print(arr)        # Output: [1. 2. 3.]

# Force int8 (saves memory)
arr = np.array([1, 2, 3], dtype=np.int8)
print(arr.dtype)  # Output: int8
```

#### Converting Data Types:

```python
# Create integer array
arr_int = np.array([1, 2, 3, 4])
print(arr_int.dtype)  # Output: int32/int64

# Convert to float
arr_float = arr_int.astype(np.float64)
print(arr_float.dtype)  # Output: float64
print(arr_float)        # Output: [1. 2. 3. 4.]

# Convert to string
arr_str = arr_int.astype(str)
print(arr_str.dtype)    # Output: <U11 or similar
print(arr_str)          # Output: ['1' '2' '3' '4']
```

**Memory Considerations**:
- Use `int32` instead of `int64` to save 50% memory when values are small
- Use `float32` for machine learning (GPU operations are faster)
- Use `int8` for small integers (-128 to 127) to save 87.5% memory

---

## 5. 1D Array Operations

Working with one-dimensional arrays is the foundation of NumPy.

### Accessing Elements

```python
arr = np.array([10, 20, 30, 40, 50])

# Positive indexing (starts from 0)
print(arr[0])      # Output: 10 (first element)
print(arr[2])      # Output: 30 (third element)

# Negative indexing (from the end)
print(arr[-1])     # Output: 50 (last element)
print(arr[-2])     # Output: 40 (second from last)

# Slicing: arr[start:stop:step]
print(arr[1:4])    # Output: [20 30 40] (indices 1, 2, 3)
print(arr[:3])     # Output: [10 20 30] (first 3 elements)
print(arr[2:])     # Output: [30 40 50] (from index 2 to end)
print(arr[::2])    # Output: [10 30 50] (every 2nd element)
print(arr[::-1])   # Output: [50 40 30 20 10] (reversed)
```

**Remember**: Slicing is `[start:stop:step]` where `stop` is **exclusive**.

### Mathematical Operations

NumPy allows **vectorized** operations - no loops needed!

```python
a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])

# Element-wise operations
print(a + b)       # Output: [ 6  8 10 12]
print(a - b)       # Output: [-4 -4 -4 -4]
print(a * b)       # Output: [ 5 12 21 32]
print(a / b)       # Output: [0.2  0.33 0.43 0.5]
print(a ** 2)      # Output: [ 1  4  9 16] (square)
print(a ** 0.5)    # Output: [1.  1.41 1.73 2.] (square root)

# Scalar operations (broadcasting)
print(a + 10)      # Output: [11 12 13 14]
print(a * 2)       # Output: [2 4 6 8]
print(a / 2)       # Output: [0.5 1.  1.5 2. ]
```

**Broadcasting**: When operating with a scalar, NumPy automatically applies it to each element.

### Comparison Operations

Comparison operations return **Boolean arrays**:

```python
a = np.array([1, 2, 3, 4])

# Comparisons
print(a > 2)       # Output: [False False  True  True]
print(a == 3)      # Output: [False False  True False]
print(a <= 2)      # Output: [ True  True False False]
print(a != 1)      # Output: [False  True  True  True]

# Using Boolean results
greater_than_2 = a > 2
print(greater_than_2)  # [False False  True  True]
print(a[greater_than_2])  # [3 4] - Boolean indexing
```

### Aggregate Functions

```python
arr = np.array([1, 2, 3, 4, 5])

print(np.sum(arr))      # Output: 15 (sum of all)
print(np.mean(arr))     # Output: 3.0 (average)
print(np.median(arr))   # Output: 3.0 (middle value)
print(np.std(arr))      # Output: 1.414... (standard deviation)
print(np.min(arr))      # Output: 1 (minimum)
print(np.max(arr))      # Output: 5 (maximum)
print(np.argmin(arr))   # Output: 0 (index of min)
print(np.argmax(arr))   # Output: 4 (index of max)
```

### Universal Functions (ufuncs)

Fast element-wise operations:

```python
arr = np.array([1, 4, 9, 16, 25])

print(np.sqrt(arr))     # Output: [1. 2. 3. 4. 5.]
print(np.square(arr))   # Output: [1 16 81 256 625]
print(np.exp(arr))      # Output: [2.71... 54.5... etc.] (e^x)
print(np.log(arr))      # Output: [0. 1.38 2.19 2.77 3.21] (natural log)
print(np.sin(arr))      # Sine of each element
print(np.abs(arr))      # Absolute value
```

---

## 6. 2D Array Operations

Two-dimensional arrays (matrices) are fundamental for data science and linear algebra.

### Creating 2D Arrays

```python
# From nested lists
matrix = np.array([[1, 2, 3], 
                   [4, 5, 6], 
                   [7, 8, 9]])
print(matrix)
# Output:
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]

# From 1D array using reshape
arr_1d = np.arange(12)
matrix = arr_1d.reshape(3, 4)
print(matrix)
# Output:
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]
```

### Understanding 2D Array Structure

```
     Column 0  Column 1  Column 2
     --------  --------  --------
Row 0    1         2         3
Row 1    4         5         6
Row 2    7         8         9
```

### Array Attributes for 2D

```python
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(matrix.shape)    # Output: (3, 3) - 3 rows, 3 columns
print(matrix.ndim)     # Output: 2 - two dimensions
print(matrix.size)     # Output: 9 - total elements
print(matrix.dtype)    # Output: int32/int64
```

### Creating Special 2D Arrays

```python
# 2D zeros
zeros_2d = np.zeros((3, 4))  # 3 rows, 4 columns
print(zeros_2d.shape)  # Output: (3, 4)

# 2D ones
ones_2d = np.ones((2, 3))

# 2D full
full_2d = np.full((3, 3), 7)

# 2D random
random_2d = np.random.rand(3, 4)
random_int_2d = np.random.randint(0, 100, size=(3, 4))
```

### Accessing Elements in 2D

```python
matrix = np.array([[1, 2, 3], 
                   [4, 5, 6], 
                   [7, 8, 9]])

# Access single element: matrix[row, column]
print(matrix[0, 0])    # Output: 1 (row 0, col 0)
print(matrix[1, 2])    # Output: 6 (row 1, col 2)
print(matrix[2, 1])    # Output: 8 (row 2, col 1)

# Negative indexing
print(matrix[-1, -1])  # Output: 9 (last row, last col)
print(matrix[-2, -3])  # Output: 4 (second-last row, first col)
```

---

## 7. Indexing and Slicing

Mastering indexing and slicing is crucial for data manipulation.

### Basic Indexing (2D Arrays)

**Syntax**: `arr[row_index, column_index]`

| Code | Result | Description |
|------|--------|-------------|
| `arr[0, 1]` | `2` | Element at row 0, column 1 |
| `arr[1, 2]` | `6` | Element at row 1, column 2 |
| `arr[-1, -1]` | `9` | Last row, last column |
| `arr[-2, 0]` | `4` | Second-last row, first column |

### Slicing 2D Arrays

**Format**: `arr[start:stop:step, start:stop:step]`
              `arr[row_slice,  column_slice]`

**CRITICAL RULE**: The `stop` index is **always exclusive** (not included)!

```python
matrix = np.array([[1, 2, 3], 
                   [4, 5, 6], 
                   [7, 8, 9]])

# Select rows
print(matrix[0:2, :])  # First 2 rows, all columns
# Output:
# [[1 2 3]
#  [4 5 6]]

# Select columns
print(matrix[:, 0:2])  # All rows, first 2 columns
# Output:
# [[1 2]
#  [4 5]
#  [7 8]]

# Select submatrix
print(matrix[0:2, 1:3])  # Rows 0-1, Columns 1-2
# Output:
# [[2 3]
#  [5 6]]
```

### Common Slicing Patterns

| Code | Result | Description |
|------|--------|-------------|
| `arr[0:2, 0:2]` | 2x2 subarray | Top-left 2×2 block |
| `arr[:, 1]` | 1D array | All rows, column 1 (returns 1D) |
| `arr[1, :]` | 1D array | Row 1, all columns (returns 1D) |
| `arr[:, ::-1]` | Reversed columns | Mirror horizontally |
| `arr[::-1, :]` | Reversed rows | Mirror vertically |
| `arr[::-1, ::-1]` | Full reverse | Rotate 180 degrees |
| `arr[::2, ::2]` | Every 2nd row/col | Downsample |

### Detailed Slicing Examples

```python
arr = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12]])

# Get entire row
print(arr[1, :])       # Output: [5 6 7 8]

# Get entire column
print(arr[:, 2])       # Output: [ 3  7 11]

# Get last row
print(arr[-1, :])      # Output: [ 9 10 11 12]

# Get first and last columns
print(arr[:, [0, -1]]) 
# Output:
# [[ 1  4]
#  [ 5  8]
#  [ 9 12]]

# Reverse columns
print(arr[:, ::-1])
# Output:
# [[ 4  3  2  1]
#  [ 8  7  6  5]
#  [12 11 10  9]]

# Every other row
print(arr[::2, :])
# Output:
# [[ 1  2  3  4]
#  [ 9 10 11 12]]
```

### Boolean Indexing

Use conditions to filter arrays:

```python
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Create Boolean mask
mask = arr > 5
print(mask)  # [False False False False False  True  True  True  True  True]

# Use mask to filter
print(arr[mask])  # Output: [ 6  7  8  9 10]

# Or do it in one line
print(arr[arr > 5])      # Output: [ 6  7  8  9 10]
print(arr[arr % 2 == 0]) # Output: [ 2  4  6  8 10] (even numbers)
print(arr[(arr > 3) & (arr < 8)])  # Output: [4 5 6 7]
```

**Important**: Use `&` for AND, `|` for OR, `~` for NOT (not `and`, `or`, `not`)

### List Indexing (Fancy Indexing)

When slicing patterns don't work, use lists of indices:

```python
a = np.array([[1, 2, 3], 
              [4, 5, 6], 
              [7, 8, 9], 
              [10, 11, 12]])

# Select specific rows: rows 0, 1, and 3
print(a[[0, 1, 3], :])
# Output:
# [[ 1  2  3]
#  [ 4  5  6]
#  [10 11 12]]

# Select specific columns: columns 0 and 2
print(a[:, [0, 2]])
# Output:
# [[ 1  3]
#  [ 4  6]
#  [ 7  9]
#  [10 12]]

# Select specific rows AND specific columns
print(a[[0, 2], :][:, [0, 2]])
# Output:
# [[1 3]
#  [7 9]]
```

---

## 8. Array Manipulation

Learn how to modify, replace, and delete array elements effectively.

### Replacing Values

**GOLDEN RULE**: First extract, then replace!

#### Replace Single Element

```python
a = np.array([[1, 2, 3], 
              [4, 5, 6], 
              [7, 8, 9]])

# Replace element at row 1, column 2
a[1, 2] = 100
print(a)
# Output:
# [[  1   2   3]
#  [  4   5 100]
#  [  7   8   9]]
```

#### Replace Entire Row

```python
# Replace with single value (broadcasting)
a[1, :] = 10
print(a)
# Output:
# [[ 1  2  3]
#  [10 10 10]
#  [ 7  8  9]]

# Replace with multiple values
a[1, :] = [10, 15, 16]
print(a)
# Output:
# [[ 1  2  3]
#  [10 15 16]
#  [ 7  8  9]]
```

#### Replace Entire Column

```python
# Replace column 1
a[:, 1] = 99
print(a)
# Output:
# [[ 1 99  3]
#  [ 4 99  6]
#  [ 7 99  9]]
```

#### Replace Multiple Rows

```python
a = np.array([[1, 2, 3], 
              [4, 5, 6], 
              [7, 8, 9]])

# Replace rows 0 and 2
a[[0, 2], :] = [[10, 11, 12], [13, 14, 15]]
print(a)
# Output:
# [[10 11 12]
#  [ 4  5  6]
#  [13 14 15]]
```

#### Replace with Condition

```python
arr = np.array([1, 2, 3, 4, 5])

# Replace all values > 3 with 0
arr[arr > 3] = 0
print(arr)  # Output: [1 2 3 0 0]

# Replace even numbers with -1
arr[arr % 2 == 0] = -1
```

**CRITICAL**: Shapes must match when replacing!

```python
a = np.array([[1, 2, 3], [4, 5, 6]])

# This works
a[0:2, :] = [[10, 11, 12], [13, 14, 15]]

# This fails - shape mismatch
# a[0:2, :] = [10, 11]  # Error! Need 2x3, got 1x2
```

### Deleting Elements

**Important**: Cannot delete single values from NumPy arrays (different from replacement).

#### Replace with NaN (for missing data)

```python
b = np.array([[1.0, 2.0, 3.0], 
              [4.0, 5.0, 6.0]])

# Mark as missing (requires float type)
b[1, 1] = np.nan
print(b)
# Output:
# [[ 1.  2.  3.]
#  [ 4. nan  6.]]
```

#### Delete Rows/Columns

**Syntax**: `np.delete(array_name, indices, axis)`
- `axis=0` for rows
- `axis=1` for columns

```python
a = np.array([[1, 2, 3], 
              [4, 5, 6], 
              [7, 8, 9], 
              [10, 11, 12]])

# Delete single row (row 1)
result = np.delete(a, 1, axis=0)
print(result)
# Output:
# [[ 1  2  3]
#  [ 7  8  9]
#  [10 11 12]]

# Delete multiple rows (rows 0 and 2)
result = np.delete(a, [0, 2], axis=0)
print(result)
# Output:
# [[ 4  5  6]
#  [10 11 12]]

# Delete single column (column 1)
result = np.delete(a, 1, axis=1)
print(result)
# Output:
# [[ 1  3]
#  [ 4  6]
#  [ 7  9]
#  [10 12]]

# Delete multiple columns (columns 0 and 2)
result = np.delete(a, [0, 2], axis=1)
print(result)
# Output:
# [[ 2]
#  [ 5]
#  [ 8]
#  [11]]
```

**CRITICAL LIMITATION**: Cannot delete rows AND columns in the same operation!

```python
# This doesn't work as you might expect
# You must do it in two separate operations
result = np.delete(a, 1, axis=0)  # First delete row
result = np.delete(result, 1, axis=1)  # Then delete column
```

---

## 9. Mathematical Operations

NumPy excels at mathematical operations through vectorization.

### Element-wise Operations

Operations are applied element-by-element:

```python
a = np.array([[11, 12], [13, 14]])
b = np.array([[1, 2], [3, 4]])

# Addition
print(a + b)
# Output:
# [[12 14]
#  [16 18]]

# Subtraction
print(a - b)
# Output:
# [[10 10]
#  [10 10]]

# Multiplication (element-wise)
print(a * b)
# Output:
# [[11 24]
#  [39 56]]

# Division
print(a / b)
# Output:
# [[11.   6. ]
#  [ 4.33 3.5]]

# Power
print(a ** 2)
# Output:
# [[121 144]
#  [169 196]]
```

**IMPORTANT**: `a * b` is element-wise multiplication, **NOT** matrix multiplication!

### Matrix Multiplication

For true matrix multiplication, use `@` or `np.dot()`:

```python
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

# Matrix multiplication
print(a @ b)  # or np.dot(a, b)
# Output:
# [[19 22]
#  [43 50]]

# Explanation:
# [1,2] @ [5,6] = 1*5 + 2*7 = 19
# [1,2] @ [7,8] = 1*6 + 2*8 = 22
# etc.
```

### Scalar Operations (Broadcasting)

NumPy automatically applies scalar operations to all elements:

```python
a = np.array([[11, 12], [13, 14]])

print(a + 10)
# Output:
# [[21 22]
#  [23 24]]

print(a * 2)
# Output:
# [[22 24]
#  [26 28]]

print(a / 2)
# Output:
# [[5.5 6. ]
#  [6.5 7. ]]

print(a ** 2)
# Output:
# [[121 144]
#  [169 196]]
```

### Common Mathematical Functions

```python
arr = np.array([1, 4, 9, 16, 25])

# Square root
print(np.sqrt(arr))     # Output: [1. 2. 3. 4. 5.]

# Square
print(np.square(arr))   # Output: [  1  16  81 256 625]

# Exponential (e^x)
print(np.exp(arr))      # Output: [2.71... 54.59... very large numbers]

# Natural logarithm
print(np.log(arr))      # Output: [0.   1.38 2.19 2.77 3.21]

# Log base 10
print(np.log10(arr))    # Output: [0.   0.60 0.95 1.20 1.39]

# Trigonometric
angles = np.array([0, np.pi/2, np.pi])
print(np.sin(angles))   # Output: [0.  1.  0.] (approximately)
print(np.cos(angles))   # Output: [ 1.  0. -1.] (approximately)

# Absolute value
arr = np.array([-1, -2, 3, -4])
print(np.abs(arr))      # Output: [1 2 3 4]

# Rounding
arr = np.array([1.23, 4.56, 7.89])
print(np.round(arr))    # Output: [1. 5. 8.]
print(np.floor(arr))    # Output: [1. 4. 7.]
print(np.ceil(arr))     # Output: [2. 5. 8.]
```

### Aggregate Functions

```python
arr = np.array([[1, 2, 3], 
                [4, 5, 6]])

# Sum
print(np.sum(arr))           # Output: 21 (all elements)
print(np.sum(arr, axis=0))   # Output: [5 7 9] (sum each column)
print(np.sum(arr, axis=1))   # Output: [ 6 15] (sum each row)

# Mean (average)
print(np.mean(arr))          # Output: 3.5
print(np.mean(arr, axis=0))  # Output: [2.5 3.5 4.5]
print(np.mean(arr, axis=1))  # Output: [2. 5.]

# Standard deviation
print(np.std(arr))           # Output: 1.707...

# Variance
print(np.var(arr))           # Output: 2.916...

# Min and Max
print(np.min(arr))           # Output: 1
print(np.max(arr))           # Output: 6
print(np.min(arr, axis=0))   # Output: [1 2 3]
print(np.max(arr, axis=1))   # Output: [3 6]

# Median
print(np.median(arr))        # Output: 3.5
```

### Understanding Axis Parameter

```python
arr = np.array([[1, 2, 3], 
                [4, 5, 6]])

# axis=0: operate along rows (collapse rows)
# Result has same number of columns
print(np.sum(arr, axis=0))  # [5 7 9]

# axis=1: operate along columns (collapse columns)  
# Result has same number of rows
print(np.sum(arr, axis=1))  # [6 15]

# No axis: operate on flattened array
print(np.sum(arr))  # 21
```

**Memory Trick**: 
- `axis=0` → "down the rows" → vertical operation
- `axis=1` → "across the columns" → horizontal operation

---

## 10. Reshaping and Transposing

Changing array dimensions is essential for data manipulation and linear algebra.

### Converting 2D to 1D: ravel() and flatten()

#### ravel() - Returns a view (faster, shares memory)

```python
a = np.array([[0, 1, 2], [3, 4, 5]])
b = a.ravel()
print(b)  # Output: [0 1 2 3 4 5]

# ravel() returns a view - changes affect original
b[0] = 99
print(a)  # a[0,0] is now 99!
```

#### flatten() - Returns a copy (slower, independent)

```python
a = np.array([[0, 1, 2], [3, 4, 5]])
b = a.flatten()
print(b)  # Output: [0 1 2 3 4 5]

# flatten() returns a copy - changes don't affect original
b[0] = 99
print(a)  # a is unchanged
```

**When to use**:
- Use `ravel()` when you don't need to modify the result
- Use `flatten()` when you need an independent copy

### Converting 1D to 2D: reshape()

**Syntax**: `arr.reshape(rows, columns)`

```python
arr = np.array([0, 1, 2, 3, 4, 5])

# 2 rows, 3 columns
result = arr.reshape(2, 3)
print(result)
# Output:
# [[0 1 2]
#  [3 4 5]]

# 3 rows, 2 columns
result = arr.reshape(3, 2)
print(result)
# Output:
# [[0 1]
#  [2 3]
#  [4 5]]

# 6 rows, 1 column
result = arr.reshape(6, 1)
print(result)
# Output:
# [[0]
#  [1]
#  [2]
#  [3]
#  [4]
#  [5]]

# 1 row, 6 columns
result = arr.reshape(1, 6)
print(result)
# Output: [[0 1 2 3 4 5]]
```

**SHAPE RULE**: `rows × columns` must equal the total number of elements!

```python
arr = np.array([1, 2, 3, 4, 5, 6])  # 6 elements

# Valid reshapes (all multiply to 6)
arr.reshape(1, 6)  # 1 × 6 = 6 ✓
arr.reshape(2, 3)  # 2 × 3 = 6 ✓
arr.reshape(3, 2)  # 3 × 2 = 6 ✓
arr.reshape(6, 1)  # 6 × 1 = 6 ✓

# Invalid reshape
# arr.reshape(2, 4)  # 2 × 4 = 8 ✗ Error!
```

### Auto-calculate Dimension with -1

Use `-1` to let NumPy calculate one dimension automatically:

```python
arr = np.arange(12)  # [0 1 2 3 4 5 6 7 8 9 10 11]

# 2 rows, auto-calculate columns
result = arr.reshape(2, -1)
print(result.shape)  # Output: (2, 6)
print(result)
# Output:
# [[ 0  1  2  3  4  5]
#  [ 6  7  8  9 10 11]]

# Auto-calculate rows, 3 columns
result = arr.reshape(-1, 3)
print(result.shape)  # Output: (4, 3)
print(result)
# Output:
# [[ 0  1  2]
#  [ 3  4  5]
#  [ 6  7  8]
#  [ 9 10 11]]

# Flatten to 1D
result = arr.reshape(-1)
print(result.shape)  # Output: (12,)
```

**Limitation**: Can only use `-1` for one dimension!

```python
# This doesn't work
# arr.reshape(-1, -1)  # Error! Can't infer both dimensions
```

### Transpose: .T

Swaps rows and columns:

```python
b = np.array([[1, 2, 3], 
              [4, 5, 6]])
print("Original shape:", b.shape)  # (2, 3)
print(b)
# Output:
# [[1 2 3]
#  [4 5 6]]

print("\nTransposed shape:", b.T.shape)  # (3, 2)
print(b.T)
# Output:
# [[1 4]
#  [2 5]
#  [3 6]]
```

**Visual Understanding**:
```
Original:       Transposed:
1 2 3           1 4
4 5 6           2 5
                3 6

Rows become columns
Columns become rows
```

### Converting 2D to 2D (Different Shape)

```python
arr = np.array([[1, 2, 3], 
                [4, 5, 6]])  # 2×3 = 6 elements

# Reshape to 3×2
result = arr.reshape(3, 2)
print(result)
# Output:
# [[1 2]
#  [3 4]
#  [5 6]]

# Reshape to 1×6
result = arr.reshape(1, 6)
print(result)
# Output: [[1 2 3 4 5 6]]

# Reshape to 6×1
result = arr.reshape(6, 1)
print(result)
# Output:
# [[1]
#  [2]
#  [3]
#  [4]
#  [5]
#  [6]]
```

### Adding New Dimensions

```python
arr = np.array([1, 2, 3])
print(arr.shape)  # (3,)

# Add dimension with newaxis
arr_2d = arr[np.newaxis, :]
print(arr_2d.shape)  # (1, 3)
print(arr_2d)  # [[1 2 3]]

# Or
arr_2d = arr[:, np.newaxis]
print(arr_2d.shape)  # (3, 1)
print(arr_2d)
# [[1]
#  [2]
#  [3]]

# Using reshape (clearer)
arr_2d = arr.reshape(1, -1)  # Row vector: (1, 3)
arr_2d = arr.reshape(-1, 1)  # Column vector: (3, 1)
```

---

## 11. Sorting Arrays

Sorting is a common operation in data analysis.

### Syntax

```python
np.sort(array, axis=None)
```

- `axis=1`: Sort each row independently
- `axis=0`: Sort each column independently
- `axis=None`: Sort flattened array

### 1D Array Sorting

```python
arr = np.array([5, 2, 8, 1, 9, 3])

# Sort array
sorted_arr = np.sort(arr)
print(sorted_arr)  # Output: [1 2 3 5 8 9]

# Get indices that would sort the array
indices = np.argsort(arr)
print(indices)  # Output: [3 1 5 0 2 4]
print(arr[indices])  # Same as np.sort(arr)

# Sort in descending order
sorted_desc = np.sort(arr)[::-1]
print(sorted_desc)  # Output: [9 8 5 3 2 1]
```

**Note**: `np.sort()` returns a sorted **copy**. The original array is unchanged.

### 2D Array Sorting

```python
a = np.array([[5, 4, 6], 
              [2, 8, 2], 
              [8, 9, 10]])

print("Original:")
print(a)
# [[ 5  4  6]
#  [ 2  8  2]
#  [ 8  9 10]]

# Sort each row independently (axis=1)
b = np.sort(a, axis=1)
print("\nSort each row (axis=1):")
print(b)
# [[ 4  5  6]    <- row 0 sorted
#  [ 2  2  8]    <- row 1 sorted
#  [ 8  9 10]]   <- row 2 sorted

# Sort each column independently (axis=0)
c = np.sort(a, axis=0)
print("\nSort each column (axis=0):")
print(c)
# [[ 2  4  2]    <- each column
#  [ 5  8  6]    <- is now
#  [ 8  9 10]]   <- sorted

# Sort flattened array
d = np.sort(a, axis=None)
print("\nSort flattened (axis=None):")
print(d)
# [ 2  2  4  5  6  8  8  9 10]
```

### In-place Sorting

```python
arr = np.array([5, 2, 8, 1, 9])

# Sort in place (modifies original)
arr.sort()
print(arr)  # Output: [1 2 5 8 9]
```

### Sorting with Multiple Keys

```python
# Create structured array
data = np.array([('Alice', 25), ('Bob', 30), ('Charlie', 25)],
                dtype=[('name', 'U10'), ('age', 'i4')])

# Sort by age, then by name
sorted_data = np.sort(data, order=['age', 'name'])
print(sorted_data)
```

### Partial Sorting (Quickselect)

```python
arr = np.array([5, 2, 8, 1, 9, 3])

# Find 3 smallest elements (not fully sorted)
result = np.partition(arr, 3)
print(result)  # [2 1 3 5 8 9] or similar
# First 3 elements are the smallest (but not sorted among themselves)
```

---

## 12. Combining Arrays

Combining arrays is essential for building larger datasets and data manipulation.

### Vertical Stack (vstack)

Stack arrays vertically (row-wise) - **add more rows**:

```python
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

result = np.vstack((a, b))
print(result)
# Output:
# [[1 2]
#  [3 4]  <- array a
#  [5 6]  <- array b
#  [7 8]]

print(result.shape)  # (4, 2) - 4 rows, 2 columns
```

**Requirement**: Arrays must have the same number of columns!

```python
a = np.array([[1, 2, 3]])    # 1×3
b = np.array([[4, 5]])        # 1×2
# np.vstack((a, b))  # Error! Different column counts
```

### Horizontal Stack (hstack)

Stack arrays horizontally (column-wise) - **add more columns**:

```python
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

result = np.hstack((a, b))
print(result)
# Output:
# [[1 2 5 6]  <- columns from a, then b
#  [3 4 7 8]]

print(result.shape)  # (2, 4) - 2 rows, 4 columns
```

**Requirement**: Arrays must have the same number of rows!

### Concatenate (Most Flexible)

`concatenate()` is more flexible - specify axis:

```python
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

# Vertical concatenation (axis=0) - same as vstack
result = np.concatenate((a, b), axis=0)
print(result)
# Output:
# [[1 2]
#  [3 4]
#  [5 6]
#  [7 8]]

# Horizontal concatenation (axis=1) - same as hstack
result = np.concatenate((a, b), axis=1)
print(result)
# Output:
# [[1 2 5 6]
#  [3 4 7 8]]
```

### Adding Rows and Columns

#### Add Single Row

```python
b = np.array([[1, 2, 3], 
              [4, 5, 6]])

# Add row at the end
new_row = np.array([[7, 8, 9]])
result = np.vstack((b, new_row))
# or
result = np.append(b, [[7, 8, 9]], axis=0)
print(result)
# Output:
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]

# Add row at the beginning
result = np.vstack((new_row, b))
print(result)
# Output:
# [[7 8 9]
#  [1 2 3]
#  [4 5 6]]
```

#### Add Single Column

```python
b = np.array([[1, 2, 3], 
              [4, 5, 6]])

# Add column (must match number of rows)
new_col = np.array([[10], [11]])
result = np.hstack((b, new_col))
# or
result = np.append(b, [[10], [11]], axis=1)
print(result)
# Output:
# [[ 1  2  3 10]
#  [ 4  5  6 11]]
```

#### Add Multiple Columns

```python
b = np.array([[1, 2, 3], 
              [4, 5, 6]])

# Add 2 columns
new_cols = np.array([[10, 11], [12, 13]])
result = np.hstack((b, new_cols))
print(result)
# Output:
# [[ 1  2  3 10 11]
#  [ 4  5  6 12 13]]
```

### Stacking 1D Arrays

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Stack as rows (2D array)
result = np.vstack((a, b))
print(result)
# Output:
# [[1 2 3]
#  [4 5 6]]

# Stack as columns (2D array)
result = np.column_stack((a, b))
print(result)
# Output:
# [[1 4]
#  [2 5]
#  [3 6]]

# Concatenate 1D arrays (stays 1D)
result = np.concatenate((a, b))
print(result)
# Output: [1 2 3 4 5 6]
```

### Depth Stack (for 3D)

```python
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

# Stack along third axis (depth)
result = np.dstack((a, b))
print(result.shape)  # (2, 2, 2)
print(result)
# Output:
# [[[1 5]
#   [2 6]]
#  [[3 7]
#   [4 8]]]
```

---

## 13. Quick Reference Guide

### Array Creation

| Operation | Syntax | Example |
|-----------|--------|---------|
| From list | `np.array(list)` | `np.array([1, 2, 3])` |
| Range of values | `np.arange(start, stop, step)` | `np.arange(0, 10, 2)` |
| Evenly spaced | `np.linspace(start, stop, num)` | `np.linspace(0, 1, 5)` |
| Zeros | `np.zeros(shape)` | `np.zeros((3, 4))` |
| Ones | `np.ones(shape)` | `np.ones((2, 3))` |
| Full (specific value) | `np.full(shape, value)` | `np.full((2, 2), 7)` |
| Identity matrix | `np.eye(n)` | `np.eye(3)` |
| Random (uniform) | `np.random.rand(shape)` | `np.random.rand(3, 3)` |
| Random integers | `np.random.randint(low, high, size)` | `np.random.randint(1, 10, 5)` |

### Array Properties

| Property | Description | Example |
|----------|-------------|---------|
| `arr.shape` | Dimensions | `(3, 4)` |
| `arr.ndim` | Number of dimensions | `2` |
| `arr.size` | Total elements | `12` |
| `arr.dtype` | Data type | `int32` |
| `arr.itemsize` | Size per element (bytes) | `4` |
| `arr.nbytes` | Total memory | `48` |

### Indexing & Slicing

| Operation | Syntax | Example |
|-----------|--------|---------|
| Single element | `arr[row, col]` | `arr[0, 1]` |
| Row | `arr[row, :]` | `arr[0, :]` |
| Column | `arr[:, col]` | `arr[:, 0]` |
| Subarray | `arr[r1:r2, c1:c2]` | `arr[0:2, 1:3]` |
| Boolean indexing | `arr[condition]` | `arr[arr > 5]` |
| Fancy indexing | `arr[[rows], [cols]]` | `arr[[0,2], :]` |

### Array Manipulation

| Operation | Syntax |
|-----------|--------|
| Reshape | `arr.reshape(rows, cols)` |
| Flatten to 1D | `arr.ravel()` or `arr.flatten()` |
| Transpose | `arr.T` |
| Sort | `np.sort(arr, axis)` |
| Delete rows/cols | `np.delete(arr, indices, axis)` |

### Combining Arrays

| Operation | Syntax |
|-----------|--------|
| Vertical stack | `np.vstack((a, b))` |
| Horizontal stack | `np.hstack((a, b))` |
| Concatenate | `np.concatenate((a, b), axis)` |
| Append rows | `np.append(arr, values, axis=0)` |
| Append columns | `np.append(arr, values, axis=1)` |

### Mathematical Operations

| Operation | Syntax |
|-----------|--------|
| Element-wise add | `a + b` or `np.add(a, b)` |
| Element-wise multiply | `a * b` or `np.multiply(a, b)` |
| Matrix multiplication | `a @ b` or `np.dot(a, b)` |
| Square root | `np.sqrt(arr)` |
| Power | `arr ** n` or `np.power(arr, n)` |
| Sum | `np.sum(arr)` or `np.sum(arr, axis)` |
| Mean | `np.mean(arr)` or `np.mean(arr, axis)` |
| Min/Max | `np.min(arr)`, `np.max(arr)` |

---

## 14. Best Practices & Important Rules

### ✅ Golden Rules

1. **Always import NumPy as np**
   - This is the universal convention
   - Makes code readable to all Python developers
   ```python
   import numpy as np  # ✓ Correct
   import numpy        # ✗ Don't do this
   ```

2. **Arrays are homogeneous**
   - All elements must be the same data type
   - Mixed types are automatically promoted
   ```python
   arr = np.array([1, 2.5, 3])  # All become float64
   print(arr.dtype)  # float64
   ```

3. **Slicing is not inclusive (stop is exclusive)**
   - `arr[0:3]` gives indices 0, 1, 2 (NOT 3)
   - This is consistent with Python's range()
   ```python
   arr = np.array([0, 1, 2, 3, 4])
   print(arr[1:4])  # [1 2 3] - NOT including index 4
   ```

4. **Check shapes before operations**
   - Shape mismatches cause errors
   - Use `.shape` to verify
   ```python
   a = np.array([[1, 2], [3, 4]])  # (2, 2)
   b = np.array([[1, 2, 3]])        # (1, 3)
   # a + b  # Error! Incompatible shapes
   ```

5. **Cannot delete rows and columns together**
   - Must be done in separate operations
   ```python
   # Delete row, then column
   arr = np.delete(arr, 1, axis=0)  # Delete row first
   arr = np.delete(arr, 1, axis=1)  # Then delete column
   ```

6. **Use vectorized operations (avoid loops)**
   - NumPy operations are 10-100x faster
   ```python
   # ✗ Slow (using loop)
   result = [x ** 2 for x in arr]
   
   # ✓ Fast (vectorized)
   result = arr ** 2
   ```

7. **Reshape total must match**
   - rows × columns = total elements
   ```python
   arr = np.arange(12)  # 12 elements
   arr.reshape(3, 4)    # ✓ 3 × 4 = 12
   arr.reshape(2, 5)    # ✗ 2 × 5 = 10 (Error!)
   ```

8. **Use appropriate data types**
   - Save memory when possible
   - Balance precision vs memory
   ```python
   # For small integers (-128 to 127)
   arr = np.array([1, 2, 3], dtype=np.int8)  # 1 byte each
   
   # For machine learning
   arr = np.array([1.0, 2.0], dtype=np.float32)  # 4 bytes each
   ```

9. **Element-wise vs Matrix multiplication**
   - `a * b` → element-wise
   - `a @ b` → matrix multiplication
   ```python
   a = np.array([[1, 2], [3, 4]])
   b = np.array([[5, 6], [7, 8]])
   
   print(a * b)  # Element-wise
   print(a @ b)  # Matrix multiplication
   ```

10. **Indexing starts at 0**
    - First element is index 0
    - Last element is index -1
    ```python
    arr = np.array([10, 20, 30])
    print(arr[0])   # 10 (first)
    print(arr[-1])  # 30 (last)
    ```

### 💡 Pro Tips

- **Use views when possible** - `ravel()` instead of `flatten()` for better performance
- **Copy arrays when needed** - Use `.copy()` to avoid unintended modifications
- **Understand broadcasting** - Enables operations between different shaped arrays
- **Use axis parameter wisely** - `axis=0` for rows, `axis=1` for columns
- **Check memory usage** - Use `.nbytes` for large arrays
- **Set random seed for reproducibility** - `np.random.seed(42)`

---

## 15. Practice Questions to Master NumPy

### Question 1: Array Creation and Basic Operations ⭐

**Task**: 
1. Create a 1D array with values from 10 to 50 with a step of 5
2. Create a 2D array of shape (4, 4) filled with random integers between 1 and 100
3. Create a 5x5 identity matrix

**Solution**:
```python
# 1. Array from 10 to 50 with step 5
arr1 = np.arange(10, 51, 5)
print("Array 1:", arr1)
# Expected: [10 15 20 25 30 35 40 45 50]

# 2. 4x4 random integers between 1 and 100
arr2 = np.random.randint(1, 101, size=(4, 4))
print("Array 2:\n", arr2)

# 3. 5x5 identity matrix
arr3 = np.eye(5)
print("Array 3:\n", arr3)
```

---

### Question 2: Indexing and Slicing ⭐⭐

**Task**:
Given the following array:
```python
arr = np.array([[1, 2, 3, 4, 5],
                [6, 7, 8, 9, 10],
                [11, 12, 13, 14, 15],
                [16, 17, 18, 19, 20]])
```

Extract:
1. The element at row 2, column 3
2. All elements in the 3rd row
3. All elements in the 2nd and 4th columns
4. The 2x2 subarray from the bottom-right corner
5. All elements greater than 10

**Solution**:
```python
arr = np.array([[1, 2, 3, 4, 5],
                [6, 7, 8, 9, 10],
                [11, 12, 13, 14, 15],
                [16, 17, 18, 19, 20]])

# 1. Element at row 2, column 3
element = arr[2, 3]
print("1:", element)  # 14

# 2. All elements in 3rd row (index 2)
row_3 = arr[2, :]
print("2:", row_3)  # [11 12 13 14 15]

# 3. 2nd and 4th columns (indices 1 and 3)
cols_2_4 = arr[:, [1, 3]]
print("3:\n", cols_2_4)
# [[ 2  4]
#  [ 7  9]
#  [12 14]
#  [17 19]]

# 4. Bottom-right 2x2 subarray
bottom_right = arr[-2:, -2:]
print("4:\n", bottom_right)
# [[14 15]
#  [19 20]]

# 5. All elements > 10
greater_10 = arr[arr > 10]
print("5:", greater_10)  # [11 12 13 14 15 16 17 18 19 20]
```

---

### Question 3: Array Manipulation ⭐⭐

**Task**:
1. Create a 3x3 array with values from 1 to 9
2. Replace all even numbers with -1
3. Add a new row [10, 11, 12] at the bottom
4. Delete the middle column
5. Transpose the result

**Solution**:
```python
# 1. Create 3x3 array
arr = np.arange(1, 10).reshape(3, 3)
print("Original:\n", arr)

# 2. Replace even numbers with -1
arr[arr % 2 == 0] = -1
print("After replacing even:\n", arr)

# 3. Add new row
arr = np.vstack((arr, [10, 11, 12]))
print("After adding row:\n", arr)

# 4. Delete middle column (index 1)
arr = np.delete(arr, 1, axis=1)
print("After deleting column:\n", arr)

# 5. Transpose
arr = arr.T
print("After transpose:\n", arr)
```

---

### Question 4: Reshaping and Broadcasting ⭐⭐

**Task**:
1. Create a 1D array with 24 elements (values 1-24)
2. Reshape it to (4, 6)
3. Reshape it to (2, 3, 4)
4. Add 100 to all elements in the first "layer" (first element of dimension 0)
5. Flatten the array back to 1D

**Solution**:
```python
# 1. Create 1D array
arr = np.arange(1, 25)
print("1D array:", arr)

# 2. Reshape to (4, 6)
arr_2d = arr.reshape(4, 6)
print("4x6 array:\n", arr_2d)

# 3. Reshape to (2, 3, 4)
arr_3d = arr.reshape(2, 3, 4)
print("2x3x4 array shape:", arr_3d.shape)

# 4. Add 100 to first layer
arr_3d[0, :, :] += 100
print("After adding 100 to first layer:\n", arr_3d)

# 5. Flatten back to 1D
arr_flat = arr_3d.flatten()
print("Flattened:", arr_flat)
```

---

### Question 5: Mathematical Operations ⭐⭐⭐

**Task**:
Create two 3x3 matrices A and B with random integers from 1 to 10.
Calculate:
1. Element-wise addition
2. Element-wise multiplication
3. Matrix multiplication
4. Mean of each row in A
5. Sum of each column in B
6. Standard deviation of the entire matrix A

**Solution**:
```python
# Create matrices
np.random.seed(42)  # For reproducibility
A = np.random.randint(1, 11, size=(3, 3))
B = np.random.randint(1, 11, size=(3, 3))

print("Matrix A:\n", A)
print("Matrix B:\n", B)

# 1. Element-wise addition
add = A + B
print("\n1. Element-wise addition:\n", add)

# 2. Element-wise multiplication
mult = A * B
print("\n2. Element-wise multiplication:\n", mult)

# 3. Matrix multiplication
matmul = A @ B  # or np.dot(A, B)
print("\n3. Matrix multiplication:\n", matmul)

# 4. Mean of each row in A
row_means = np.mean(A, axis=1)
print("\n4. Row means:", row_means)

# 5. Sum of each column in B
col_sums = np.sum(B, axis=0)
print("\n5. Column sums:", col_sums)

# 6. Standard deviation of A
std_dev = np.std(A)
print("\n6. Standard deviation:", std_dev)
```

---

### Question 6: Boolean Indexing and Filtering ⭐⭐

**Task**:
Given a temperature dataset (in Celsius):
```python
temps = np.array([23, 18, 32, 15, 28, 19, 35, 22, 17, 30])
```

1. Find all temperatures above 25°C
2. Count how many days were above 25°C
3. Replace temperatures below 20°C with 20°C (minimum threshold)
4. Calculate the average temperature of days above 25°C
5. Find the indices of the hottest and coldest days

**Solution**:
```python
temps = np.array([23, 18, 32, 15, 28, 19, 35, 22, 17, 30])

# 1. Temperatures above 25°C
above_25 = temps[temps > 25]
print("1. Temps > 25:", above_25)  # [32 28 35 30]

# 2. Count days above 25°C
count = np.sum(temps > 25)  # True counts as 1
print("2. Days > 25:", count)  # 4

# 3. Replace temps < 20 with 20
temps_adjusted = temps.copy()
temps_adjusted[temps_adjusted < 20] = 20
print("3. Adjusted temps:", temps_adjusted)

# 4. Average of days > 25°C
avg_hot = np.mean(temps[temps > 25])
print("4. Avg temp > 25:", avg_hot)  # 31.25

# 5. Indices of hottest and coldest
hottest_idx = np.argmax(temps)
coldest_idx = np.argmin(temps)
print("5. Hottest day index:", hottest_idx)  # 6 (temp 35)
print("   Coldest day index:", coldest_idx)  # 3 (temp 15)
```

---

### Question 7: Combining and Stacking ⭐⭐⭐

**Task**:
You have monthly sales data for 3 products over 4 months:

```python
product_A = np.array([[100, 120, 115, 130]])  # 1x4
product_B = np.array([[200, 190, 210, 205]])  # 1x4
product_C = np.array([[150, 160, 155, 170]])  # 1x4
```

1. Combine them into a single 3x4 array (products as rows)
2. Add a column showing total sales for each product
3. Add a row showing total sales for each month
4. Calculate which product had the highest average monthly sales

**Solution**:
```python
product_A = np.array([[100, 120, 115, 130]])
product_B = np.array([[200, 190, 210, 205]])
product_C = np.array([[150, 160, 155, 170]])

# 1. Combine into 3x4 array
sales = np.vstack((product_A, product_B, product_C))
print("1. Combined sales:\n", sales)

# 2. Add total column
totals = np.sum(sales, axis=1).reshape(-1, 1)
sales_with_total = np.hstack((sales, totals))
print("\n2. With product totals:\n", sales_with_total)

# 3. Add monthly totals row
monthly_totals = np.sum(sales, axis=0)
total_of_totals = np.sum(monthly_totals)
monthly_row = np.append(monthly_totals, total_of_totals)
sales_complete = np.vstack((sales_with_total, monthly_row))
print("\n3. With monthly totals:\n", sales_complete)

# 4. Product with highest average
avg_sales = np.mean(sales, axis=1)
best_product = np.argmax(avg_sales)
products = ['A', 'B', 'C']
print(f"\n4. Best product: {products[best_product]} (avg: {avg_sales[best_product]:.2f})")
```

---

### Question 8: Advanced Slicing ⭐⭐⭐

**Task**:
Create a 6x6 array with values from 1 to 36.
Extract:
1. The 4 corner elements
2. The border elements (outer ring)
3. The inner 4x4 subarray
4. All elements on the main diagonal
5. All elements on the anti-diagonal

**Solution**:
```python
# Create 6x6 array
arr = np.arange(1, 37).reshape(6, 6)
print("Original array:\n", arr)

# 1. Four corners
corners = arr[[0, 0, -1, -1], [0, -1, 0, -1]]
print("\n1. Corners:", corners)  # [ 1  6 31 36]

# 2. Border elements
top = arr[0, :]
bottom = arr[-1, :]
left = arr[1:-1, 0]
right = arr[1:-1, -1]
border = np.concatenate((top, right, bottom[::-1], left[::-1]))
print("\n2. Border:", border)

# 3. Inner 4x4 subarray
inner = arr[1:-1, 1:-1]
print("\n3. Inner 4x4:\n", inner)

# 4. Main diagonal
main_diag = np.diag(arr)
print("\n4. Main diagonal:", main_diag)  # [ 1  8 15 22 29 36]

# 5. Anti-diagonal
anti_diag = np.diag(np.fliplr(arr))
print("\n5. Anti-diagonal:", anti_diag)  # [ 6 11 16 21 26 31]
```

---

### Question 9: Data Normalization ⭐⭐⭐⭐

**Task**:
You have test scores from 10 students:
```python
scores = np.array([45, 67, 89, 92, 78, 56, 88, 90, 72, 85])
```

1. Normalize scores to 0-100 scale (min-max normalization)
2. Standardize scores (mean=0, std=1)
3. Create grade categories: A (>85), B (70-85), C (55-70), F (<55)
4. Calculate percentile rank for each score

**Solution**:
```python
scores = np.array([45, 67, 89, 92, 78, 56, 88, 90, 72, 85])

# 1. Min-max normalization to 0-100
min_score = np.min(scores)
max_score = np.max(scores)
normalized = (scores - min_score) / (max_score - min_score) * 100
print("1. Normalized scores:", normalized.round(2))

# 2. Standardization (z-score)
mean = np.mean(scores)
std = np.std(scores)
standardized = (scores - mean) / std
print("\n2. Standardized scores:", standardized.round(2))

# 3. Grade categories
grades = np.empty(len(scores), dtype='U1')
grades[scores > 85] = 'A'
grades[(scores >= 70) & (scores <= 85)] = 'B'
grades[(scores >= 55) & (scores < 70)] = 'C'
grades[scores < 55] = 'F'
print("\n3. Grades:", grades)

# 4. Percentile rank
from scipy.stats import rankdata  # Or manual calculation
percentiles = rankdata(scores, method='average') / len(scores) * 100
print("\n4. Percentile ranks:", percentiles.round(1))
```

---

### Question 10: Real-World Application - Image Processing ⭐⭐⭐⭐⭐

**Task**:
Create a simple 10x10 "image" (grayscale, values 0-255):
1. Create a gradient from black (0) to white (255) from left to right
2. Add random noise (±20 to each pixel)
3. Apply a simple blur (3x3 average filter) to the center 6x6 region
4. Flip the image horizontally
5. Calculate the histogram (count of pixels in ranges: 0-63, 64-127, 128-191, 192-255)

**Solution**:
```python
# 1. Create gradient
gradient = np.linspace(0, 255, 10, dtype=np.uint8)
image = np.tile(gradient, (10, 1))
print("1. Gradient image:\n", image)

# 2. Add noise
np.random.seed(42)
noise = np.random.randint(-20, 21, size=(10, 10))
noisy_image = np.clip(image.astype(int) + noise, 0, 255).astype(np.uint8)
print("\n2. Noisy image:\n", noisy_image)

# 3. Apply blur to center 6x6
blurred = noisy_image.copy().astype(float)
for i in range(2, 8):
    for j in range(2, 8):
        # 3x3 window average
        window = noisy_image[i-1:i+2, j-1:j+2]
        blurred[i, j] = np.mean(window)
blurred = blurred.astype(np.uint8)
print("\n3. Blurred center:\n", blurred)

# 4. Flip horizontally
flipped = np.fliplr(blurred)
print("\n4. Flipped image:\n", flipped)

# 5. Histogram
bins = [0, 64, 128, 192, 256]
hist = np.histogram(flipped, bins=bins)[0]
print("\n5. Histogram:")
print(f"   0-63:     {hist[0]} pixels")
print(f"   64-127:   {hist[1]} pixels")
print(f"   128-191:  {hist[2]} pixels")
print(f"   192-255:  {hist[3]} pixels")
```

---

## Summary

Congratulations! You've completed the comprehensive NumPy guide. You now understand:

✅ What NumPy is and why it's essential  
✅ How to create arrays using multiple methods  
✅ Array attributes and data types  
✅ Indexing, slicing, and Boolean indexing  
✅ Array manipulation techniques  
✅ Mathematical and statistical operations  
✅ Reshaping and transposing arrays  
✅ Sorting and combining arrays  
✅ Best practices and common pitfalls  
✅ Real-world applications through practice questions  

### Next Steps:

1. **Practice Daily** - Solve the 10 questions above multiple times
2. **Build Projects** - Apply NumPy to real datasets
3. **Learn Pandas** - Built on top of NumPy for data analysis
4. **Explore SciPy** - Advanced scientific computing
5. **Study Matplotlib** - Data visualization using NumPy arrays

### Additional Resources:

- Official Documentation: https://numpy.org/doc/
- NumPy User Guide: https://numpy.org/doc/stable/user/
- NumPy for MATLAB users: https://numpy.org/doc/stable/user/numpy-for-matlab-users.html

**Keep practicing and happy coding! 🚀**

---

*Document created for educational purposes. All examples are tested and verified.*
