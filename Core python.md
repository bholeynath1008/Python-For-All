
---
# 🐍 Python – Notes 
## 📘 Textbook Study Notes

## 📌 Table of Contents
1. [Python Execution & Development Environment](#chapter-1-python-execution--development-environment)
2. [Python Syntax Fundamentals](#chapter-2-python-syntax-fundamentals)
3. [Data Types in Python](#chapter-3-data-types-in-python)
4. [User-Defined Function](#chapter-4-user-defined-function)

---

## Chapter 1: Python Execution & Development Environment

### Ways to Execute Python Programs
Python programs can be executed using:

1. **Command Prompt (Python Shell)**
2. **Python IDLE**

---

### Integrated Development Environment (IDE)
Popular IDEs for Python development:

- **Jupyter Notebook** (Browser-based interactive shell)
- **Spyder** (Python IDE that comes with **Anaconda**)
-  **Anaconda** (Comes with bundled IDEs and libraries)
- **PyCharm**
- **Visual Studio Code**
- **Google Colab** *(Cloud-based)*

---

### Interpreter vs Compiler
**Compiler:** translates an entire program into machine code at once.

**Interpreter (Python):** Code is run directly by the interpreter at runtime
| Feature | Interpreter | Compiler |
|------|-----------|----------|
| Execution | One statement at a time | Entire program at once |
| Error Handling | Stops at first error | Errors shown after full analysis |
| Debugging | Easier | Harder |
| Memory | No object code (efficient) | Generates object code (needs more memory) |
| Speed | Slower execution | Faster execution |

---

### Advantages of Python
- **Programmer-friendly language**
- **Large ecosystem with rich libraries**
- **Less code with more functionality**
- **Open-source**
- **Interpreted language**
- **No compilation needed**
- **Code executes directly**

---

## Chapter 2: Python Syntax Fundamentals

### Comments in Python

#### Single Line Comment
```python
# This is a comment
````

#### Multi-Line Comments

```python
""" This is a multi-line comment """
''' This is a multi-line comment '''
```

---

### Python Terminology

#### Function

* Reusable block of code
* Performs a specific task
* Defined using parentheses: `function_name()`
* Example: `a()` → `a` is function name
* Built-in functions:

  * `print()`
  * `len()`
  * `type()`

---

#### Keyword

* Reserved words with special meaning
* Cannot be used as variable names
* Examples:

  * `if`, `for`, `while`, `def`, `class`

---

#### Variable

* Named storage location for data
* Can store different data types
* Follows naming rules

```python
var = 10
```

---

#### Attribute

* Property or characteristic of an object
* Accessed using dot notation

```python
np.array()
```

* `array` → attribute of `np` module
* Attributes can be **methods** or **data**

---

### Variables in Python

* Store values in memory
* **Dynamic typing**
* No need to declare data type
* Data type assigned automatically

```python
a = "apple"   # 'a' becomes string automatically
```

---

### Variable Assignments

#### Assigning Different Values to Different Variables

```python
x, y, z = 20, 40, 50
```

* Number of variables must equal number of values
* Each value creates its own object

---

#### Assigning Same Value to Different Variables *(Recommended)*

```python
x = y = z = 20
```

* Only one object created in memory
* All variables point to same memory location

---

#### Assigning Single Value to Single Variable

```python
c = 90
```

* Object `90` created
* Variable `c` references that object

---

#### Assigning Multiple Values to Single Variable

```python
d = 20, 30, 50, 50
type(d)   # <class 'tuple'>
```

* Stored as **tuple** by default

---

### Variable Naming Rules

* Must start with **a–z**, **A–Z**, or `_`
* Cannot start with number
* Can contain alphanumeric characters
* Only special character allowed: `_`
* Case-sensitive (`name ≠ Name`)
* Cannot use keywords

---

### Python Keywords

```python
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await',
 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except',
 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is',
 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return',
 'try', 'while', 'with', 'yield']
```

---

## Chapter 3: Data Types in Python

### Dynamic Typing

==Python assigns data type automatically based on value==
No explicit declaration required.

---

### Fundamental (Primitive) Data Types

#### Integer (`int`)

* Numerical values without decimals
* Examples: `10`, `25`, `600`
* No built-in attributes for modification
* `len()` ❌ not applicable

---

#### Float (`float`)

* Numerical values with decimals
* Examples: `2.5`, `9.0`, `25.5`
* `45.0` is float, not integer
* `len()` ❌ not applicable

---

#### Boolean (`bool`)

* Logical values only
* Values: `True`, `False`
* `len()` ❌ not applicable

---

#### String (`str`)

* Any non-numeric value
* Examples:

  * `"Lord Shiva"`
  * `"Rama"`
  * `"S1232"`
* One object stores multiple characters
* Has built-in methods
* `len()` ✅ applicable

```python
s = "shiva"
s.upper()
len(s)   # 5
```

---

### Methods & Attributes Applicability

| Data Type | Attributes/Methods | len() | Examples                |
| --------- | ------------------ | ----- | ----------------------- |
| int       | ❌                  | ❌     | 10                      |
| float     | ❌                  | ❌     | 2.5                     |
| bool      | ❌                  | ❌     | True                    |
| str       | ✅                  | ✅     | upper(), lower()        |
| list      | ✅                  | ✅     | append(), remove()      |
| tuple     | ✅                  | ✅     | count(), index()        |
| set       | ✅                  | ✅     | union(), intersection() |
| dict      | ✅                  | ✅     | keys(), values()        |

---

### Single vs Multiple Values

* `"shiva rama krishna"` → **Single string**
* `"shiva", "rama", "krishna"` → **Tuple**

---

### Default Tuple Creation

When values are separated by commas, Python creates tuple:

```python
a = 1, 2
b = 1, "shiva"
c = True, 25.4
```

---

### Object Size Concept

* `int`, `float`, `bool` → size = **1 value**
* Size refers to **number of values**, not memory bits
* Strings store multiple characters but form **one object**

---

### Checking Data Type

```python
x = 5
type(x)   # <class 'int'>
```

---

### Advanced (Non-Primitive) Data Types

#### List

* Mutable
* Ordered

```python
[1, 2, 3, "srk"]
```

---

#### Tuple

* Immutable
* Ordered

```python
(1, 2, 3)
```

---

#### Set

* Unordered
* Unique elements

```python
{1, 2, 3}
```

---

#### Dictionary

* Key–Value pairs
* Python 3.7+ maintains insertion order

```python
d = {"name": "John", "age": 25}
len(d)
d.keys()
d["name"]
```

---

### Deleting Objects

```python
del x
del x, y
```

---

### String Storage Notes

* Strings stored in **box** in memory
* Numbers stored directly
* `int` has no size limit
* `len()` not applicable for `int`, `float`, `bool`
* Spaces inside quotes are counted as characters

```python
s1 = "gen-ai"
```

#### Multi-Line String

```python
s4 = '''genai
&
agentic ai'''
```

* All variables stored in **RAM**

---

### Typecasting

#### Integer Conversion

```python
marks = 75
float(marks)
bool(marks)
str(marks)
```

If value is `0`:

```python
bool(0)   # False
```

---

#### Float Conversion

```python
price = 249.99
int(price)
bool(price)
str(price)
```

---

#### Boolean Conversion

```python
is_logged_in = True
int(is_logged_in)
float(is_logged_in)
str(is_logged_in)
```

For `False`:

```python
int(False)
float(False)
str(False)
```

---

#### String Conversion

```python
age = "24"
int(age)
float(age)
bool(age)
```

Empty string:

```python
name = ""
bool(name)   # False
```

<span style="color:red">❌ Invalid Conversion</span>

```python
int("Hello")
```

---

### Single-Line vs Multi-Line Execution

* Single-line → value displayed automatically
* Multi-line → only last line displayed

```python
a = 24
a
b = 30
b
```

To display both:

```python
print(a)
print(b)
```

---

## Chapter 4: User-Defined Function

### Definition

A **user-defined function** is created by the programmer to perform a specific task.

---

### Basic Function Example

```python
def add(a, b):
    return a + b
```

* `def` → function keyword
* `add` → function name
* `a, b` → parameters
* `return` → sends result back

---

### Function Call (Keyword Arguments)

```python
result = add(a=23, b=95)
print(result)
```

**Output**

```
118
```

✔ Values passed using parameter names
✔ Order does not matter

---

> 📝 **Revision Tip:**
> Focus on ==dynamic typing==, ==typecasting rules==, ==tuple creation==, and ==function basics==.

```

---

If you want next:
- 📄 **PDF version**
- 📘 **Chapter-wise exercises**
- 🧠 **Interview Q&A**
- 🗂️ **One-page revision cheatsheet**

Just tell me 👍
```


# Python Indexing & Slicing Notes

## 📌 **Data Types Where Indexing/Slicing Works**
- **Strings**: Sequence of characters
- **Lists**: Ordered collection of items
- **Tuples**: Immutable ordered collection
- **Dictionaries**: Key-value pairs (indexing by key, not position)

## ❌ **Data Types Where Indexing/Slicing is NOT Applicable**
- **int** (stores single value)
- **float** (stores single value)  
- **boolean** (stores single value)
- **Reason**: These store single values, not sequences/collections

---

## 🔢 **Indexing**
- **Purpose**: Extracting a single value/character
- **Syntax**: `variable_name[index]`
- **Examples**:
  ```python
  d = "bholeynath"
  print(d[0])    # 'b'
  print(d[-1])   # 'h' (negative indexing from end)
  print(d[5])    # 'y'
  ```

---

## 🔪 **Slicing**
- **Purpose**: Extracting multiple characters/values
- **For strings**: 1 value = 1 character
- **Pattern extraction**: Follows specific pattern based on step

### **Syntax**:
```python
variable_name[start:end:step]
```

### **Key Rules**:
1. **start index**: Inclusive (includes the character at start position)
2. **end index**: Exclusive (stops BEFORE this position)
3. **step**: Direction and interval
   - **Positive step**: Forward movement (left to right)
   - **Negative step**: Backward movement (right to left)

---

## 📊 **Examples & Patterns**

### **Basic Examples**:
```python
d = "bholeynath"

# Positive step (increment)
print(d[0:3:1])     # "bho" - from index 0 to 2, step 1
print(d[0:3])       # "bho" - step defaults to 1
print(d[:3])        # "bho" - start defaults to 0

# Negative step (decrement)
print(d[7:2:-1])    # "anyeh" - from index 7 down to 3
```

### **Important Cases**:

```python
d = "bholeynath"

# ❌ Empty string cases (direction conflict):
print(d[1:6:-1])    # "" (empty) - start(1) < end(6) but step is negative
print(d[-2:5:1])    # "" (empty) - start(-2=8) > end(5) but step is positive

# ✅ Valid patterns:
print(d[:])         # "bholeynath" - entire string
print(d[:8])        # "bholeyna" - start=0 to index 7
print(d[3:])        # "leynath" - index 3 to end
print(d[0::1])      # "bholeynath" - all characters

# Negative indexing:
print(d[-6:8:1])    # "eyna" - from index 4 to 7
print(d[-4::-1])    # "elyhb" - from index 6 backward to start
```

---

## 🎯 **Practical Extraction Example**

```python
d = "NARgenai001"

# Extract different parts:
institute = d[:3]      # "NAR"
course = d[3:9]        # "genai" (index 3 to 8)
roll_no = d[9:]        # "001" (index 9 to end)

print(f"Institute: {institute}")    # NAR
print(f"Course: {course}")          # genai  
print(f"Roll No: {roll_no}")        # 001
```

### **Alternative extraction using slicing**:
```python
# Extracting "genai" from the string:
data = "NARgenai001"
course = data[3:-3]    # "genai" (from index 3 to index -4)
print(course)          # "genai"
```

---

## 💡 **Key Takeaways**

1. **No errors in slicing** - returns empty string instead of error
2. **Direction matters** - start must be in direction of step relative to end
3. **Default values**:
   - `start` defaults to 0 (if step positive) or -1 (if step negative)
   - `end` defaults to len(string) (if step positive) or before start (if step negative)
   - `step` defaults to 1
4. **Negative indices** count from end (-1 = last character)
5. **Step determines direction**:
   - Positive: Left → Right
   - Negative: Right → Left

---

## 🚨 **Common Pitfalls**
- `"text"[5:2]` returns `""` (empty) - default step=1 can't go backward
- `"text"[2:5:-1]` returns `""` (empty) - direction conflict
- Remember: `end` index is **excluded** from result
- Slicing always returns a new object (original unchanged)










# Python Slicing: Handling Missing Start/End Indices

## 📌 **When Start or End Index is Not Provided**

When you omit the `start` or `end` index in slicing, Python automatically determines them based on:
1. **The sign of the step** (positive or negative)
2. **The direction** of traversal

### **Key Rule**:
> **Missing indices default to extremes based on direction of traversal.**

---

## 🔄 **Two Directions of Traversal**

### **1. POSITIVE STEP (step > 0)**
- **Direction**: Left → Right (forward)
- **Path**: From beginning toward end
- **Missing start**: Defaults to `0` (first character)
- **Missing end**: Defaults to `len(string)` (just past last character)

### **2. NEGATIVE STEP (step < 0)**
- **Direction**: Right → Left (backward)
- **Path**: From end toward beginning
- **Missing start**: Defaults to `-1` (last character)
- **Missing end**: Defaults to `-len(string)-1` (just before first character)

---

## 📊 **Detailed Examples**

```python
text = "Python"

### Case 1: POSITIVE STEP (forward direction)
print("--- POSITIVE STEP (forward) ---")

# Missing start, positive step → starts from 0
print(text[:4])      # "Pyth" (same as text[0:4])
print(text[:4:1])    # "Pyth" (same as text[0:4:1])
print(text[:4:2])    # "Pt" (start=0, end=4, step=2)

# Missing end, positive step → goes to len(text)
print(text[2:])      # "thon" (same as text[2:6])
print(text[2::1])    # "thon" (same as text[2:6:1])
print(text[2::2])    # "to" (start=2, end=6, step=2)

# Both missing, positive step → entire string forward
print(text[:])       # "Python" (same as text[0:6:1])
print(text[::1])     # "Python" (same as text[0:6:1])
print(text[::2])     # "Pto" (start=0, end=6, step=2)

### Case 2: NEGATIVE STEP (backward direction)
print("\n--- NEGATIVE STEP (backward) ---")

# Missing start, negative step → starts from -1 (last)
print(text[::-1])    # "nohtyP" (same as text[-1:-7:-1])
print(text[:2:-1])   # "noht" (start=-1, end=2, step=-1)
# Explanation: starts at last char, moves backward, stops before index 2

# Missing end, negative step → ends just before first (-len-1)
print(text[4::-1])   # "ohtyP" (start=4, end=-7, step=-1)
# Explanation: starts at index 4, moves backward to beginning

print(text[4:1:-1])  # "oht" (explicit start and end)
```

---

## 🎯 **Visual Representation**

```python
text = "Python"
# Index:   0   1   2   3   4   5
#         P   y   t   h   o   n
#        -6  -5  -4  -3  -2  -1

# Positive step paths:
text[::1]   # P → y → t → h → o → n
text[::2]   # P → t → o

# Negative step paths:
text[::-1]  # n → o → h → t → y → P
text[::-2]  # n → h → y
```

---

## 💡 **Practical Examples with Missing Indices**

```python
d = "bholeynath"

print("Original:", d)  # "bholeynath"

### Scenario 1: Extract from beginning to specific point
print(d[:5])     # "bhole" (start=0, end=5, step=1)

### Scenario 2: Extract from specific point to end  
print(d[5:])     # "ynath" (start=5, end=10, step=1)

### Scenario 3: Reverse the entire string
print(d[::-1])   # "htanyelohb" (complete reverse)

### Scenario 4: Reverse from end to specific point
print(d[:4:-1])  # "htanye" (start=-1, end=4, step=-1)
# Explanation: Starts at last 'h', moves backward, stops before 'e' (index 4)

### Scenario 5: Reverse from specific point to beginning
print(d[6::-1])  # "yelohb" (start=6, end=-11, step=-1)
# Explanation: Starts at 'n' (index 6), moves backward to beginning

### Scenario 6: Every other character in reverse
print(d[::-2])   # "hnyhb" (start=-1, end=-11, step=-2)
```

---

## 🚨 **Special Cases & Edge Conditions**

```python
text = "Hello"

# Empty results (valid but empty):
print(text[2:2])      # "" (start=end)
print(text[3:1])      # "" (start>end with positive step)
print(text[1:3:-1])   # "" (start<end with negative step)

# Single character extractions:
print(text[2:3])      # "l" (start=2, end=3)
print(text[-3:-2])    # "l" (same as above)

# Using only step (missing start AND end):
print(text[::])       # "Hello" (all defaults)
print(text[::-1])     # "olleH" (reverse)
```

---

## 🔑 **Memory Aid for Missing Indices**

### **For POSITIVE step (step > 0)**:
```
[:end]      → [0:end:1]
[start:]    → [start:len(text):1]
[::step]    → [0:len(text):step]
```

### **For NEGATIVE step (step < 0)**:
```
[:end:step] → [-1:end:step]  (start at last)
[start::step] → [start:-len(text)-1:step]  (go to before first)
[::-1]      → [-1:-len(text)-1:-1]  (full reverse)
```

---

## ✅ **Quick Reference Table**

| Slice | Step | Missing Start | Missing End | Equivalent To |
|-------|------|---------------|-------------|---------------|
| `[:5]` | +1 | 0 | 5 | `[0:5:1]` |
| `[3:]` | +1 | 3 | len(text) | `[3:len(text):1]` |
| `[::2]` | +2 | 0 | len(text) | `[0:len(text):2]` |
| `[::-1]` | -1 | -1 | -len-1 | `[-1:-len-1:-1]` |
| `[:3:-1]` | -1 | -1 | 3 | `[-1:3:-1]` |
| `[4::-1]` | -1 | 4 | -len-1 | `[4:-len-1:-1]` |

**Remember**: The defaults depend on the **direction** determined by the step!
