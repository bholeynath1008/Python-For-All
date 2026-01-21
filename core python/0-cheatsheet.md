# Python Complete Cheat Sheet

## Data Types & Structures

| Type | Syntax | Ordered | Mutable | Duplicates | Key Features |
|------|--------|---------|---------|------------|--------------|
| List | `[]` | Yes | Yes | Yes | `l[0] = 5`, `l.append()`, `l.pop()` |
| Tuple | `()` | Yes | No | Yes | Immutable, faster than lists |
| Set | `{}` | No | Yes | No | Unique, `{1,2,3}`, no indexing |
| Dict | `{:}` | Yes | Yes | Keys: No | `{key: value}`, keys immutable |

```python
# Type Conversion
list(x)    # → List
tuple(x)   # → Tuple
set(x)     # → Set (removes duplicates)
dict(x)    # → Dict (needs pairs like [(k1,v1), (k2,v2)])

# Check type
print(type(x))  # <class 'list'>
```

## Slicing (Creates New Copy)

```python
# Basic syntax: [start:stop:step]
# stop is NOT inclusive
# Defaults: start=0, stop=len(), step=1

l = [1, 2, 3, 4, 5]
l[1:4]      # [2, 3, 4] - index 1 to 3
l[:3]       # [1, 2, 3] - first 3
l[2:]       # [3, 4, 5] - from index 2
l[::2]      # [1, 3, 5] - every 2nd
l[::-1]     # [5, 4, 3, 2, 1] - reverse copy
```

## Reverse Operations

| Method | Mutates Original? | Returns Value | Example |
|--------|-------------------|---------------|---------|
| Slice `[::-1]` | No | New list | `l[::-1]` |
| `.reverse()` | Yes | None | `l.reverse()` |
| `reversed()` | No | Iterator | `list(reversed(l))` |

```python
l = [1, 2, 3, 4]

# 1) Slice (recommended for copy)
rev = l[::-1]  # New list: [4, 3, 2, 1]

# 2) .reverse() (mutates in-place)
l.reverse()    # l becomes [4, 3, 2, 1], returns None

# 3) reversed() function
r = reversed(l)  # Returns iterator
list(r)          # Convert to list: [4, 3, 2, 1]
```

## Mutating vs Non-Mutating Methods

### **LIST METHODS**

**Mutates In-Place (Returns None/None or new value):**
- `.append(x)` - Add to end
- `.extend(iter)` - Add multiple
- `.insert(i, x)` - Insert at index
- `.remove(x)` - Remove first match
- `.pop([i])` - Remove & return at index
- `.clear()` - Remove all
- `.sort()` - Sort in-place (returns None)
- `.reverse()` - Reverse in-place (returns None)

**Returns New Value (Original unchanged):**
- `+` operator - `l1 + l2` (new list)
- `*` operator - `l * 3` (new list)
- Slicing `[:]` - Returns copy
- `.copy()` - Shallow copy
- `sorted()` - Returns sorted list

### **DICTIONARY METHODS**

**Mutates In-Place:**
- `.update(dict2)` - Merge dictionaries
- `.pop(key)` - Remove & return value
- `.popitem()` - Remove & return (key, value)
- `.clear()` - Remove all

**Returns New Value:**
- `.copy()` - Shallow copy
- `.keys()` - View of keys
- `.values()` - View of values
- `.items()` - View of (key, value) pairs
- `.get(key, default)` - Returns value or default

### **SET METHODS**

**Mutates In-Place:**
- `.add(x)` - Add element
- `.remove(x)` - Remove element (KeyError if missing)
- `.discard(x)` - Remove element (no error)
- `.update(set2)` - Add multiple
- `.clear()` - Remove all

**Returns New Value:**
- `.copy()` - Shallow copy
- `.union(set2)` - Returns union
- `.intersection(set2)` - Returns intersection
- `.difference(set2)` - Returns difference

```python
# Check if same memory
l1 = [1, 2, 3]
l2 = l1.copy()
print(id(l1) == id(l2))  # False - different objects

l3 = l1
print(id(l1) == id(l3))  # True - same object
```

## Dictionary Operations

```python
# Dictionary operations
d = {"a": 3, "b": 99, "c": 99}

# Filter by value
filtered = {k: v for k, v in d.items() if v == 99}
# {'b': 99, 'c': 99}

# Get first match
first = next(({k: v} for k, v in d.items() if v == 99), None)

# Update dictionary
d.update({"d": 100})  # Mutates d
d1.update(d2)         # Merge d2 into d1

# Set default value
d.setdefault("e", 0)  # If "e" doesn't exist, set to 0

# Dictionary from two lists
keys = ["a", "b", "c"]
values = [1, 2, 3]
d = dict(zip(keys, values))  # {'a': 1, 'b': 2, 'c': 3}
```

## String Operations

```python
# Splitting & Joining
s = "siva rama krishna"
words = s.split()          # ['siva', 'rama', 'krishna']
joined = " ".join(words)   # "siva rama krishna"

# String methods (return new strings)
"hello".upper()      # "HELLO"
"HELLO".lower()      # "hello"
"hello".capitalize() # "Hello"
"hello world".title() # "Hello World"
"  hello  ".strip()  # "hello" - remove whitespace

# Check methods (return boolean)
"abc123".isalnum()   # True - letters or numbers
"abc".isalpha()      # True - letters only
"123".isdigit()      # True - digits only
"   ".isspace()      # True - whitespace only
"hello".islower()    # True
"HELLO".isupper()    # True
"Hello World".istitle() # True

# String formatting
name = "Alice"
age = 25
# f-string (Python 3.6+)
print(f"{name} is {age} years old")
# format() method
print("{} is {} years old".format(name, age))
# Old style
print("%s is %d years old" % (name, age))
```

## Input & Formatting

```python
# Input
name = input("Enter name: ")          # String input
age = int(input("Enter age: "))       # Convert to int
num = float(input("Enter number: "))  # Convert to float

# Dangerous but powerful (evaluates Python code)
result = eval(input("Enter expression: "))  # e.g., "2+3*4"

# Multiple values
print("Hello", "World", sep=" | ")   # "Hello | World"
print("Hello", "World", end="!\n")   # "Hello World!" with newline
x, y, z = 10, 20, 30                # Multiple assignment
```

## Common Operations

```python
# Check existence
item in list            # Returns True/False
key in dict             # Checks for key
item in set             # Fast membership test
substring in string     # Check substring

# Count and index
t = (1, 2, 3, 2, 1)
t.count(2)              # 2 - occurrences
t.index(3)              # 2 - first index
# For lists:
l = [1, 2, 3, 2, 1]
l.index(2)              # 1 - first occurrence

# Tuple unpacking
a, b, c = (1, 2, 3)     # a=1, b=2, c=3
a, *rest = (1, 2, 3, 4) # a=1, rest=[2,3,4]
*a, b = (1, 2, 3, 4)    # a=[1,2,3], b=4

# Variable naming rules
# Allowed: letters, digits, underscore (_)
# Must start with letter or underscore
# Case-sensitive: name ≠ Name
# No keywords: if, for, while, etc.
```

## Loops with All Data Structures

### **BASIC LOOP TYPES**
```python
# For loop
for i in range(5):            # 0 to 4
    print(i)

# While loop
count = 0
while count < 5:
    print(count)
    count += 1
```

### **LOOPING THROUGH LISTS**
```python
fruits = ["apple", "banana", "cherry"]
# Basic
for fruit in fruits:
    print(fruit)
# With index
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")
# Backwards
for fruit in reversed(fruits):
    print(fruit)
# List comprehension
[upper for fruit in fruits]  # ['APPLE', 'BANANA', 'CHERRY']
```

### **LOOPING THROUGH TUPLES**
```python
colors = ("red", "green", "blue")
for color in colors:
    print(color)
# Tuple unpacking in loop
coords = [(1, 2), (3, 4)]
for x, y in coords:
    print(f"x={x}, y={y}")
```

### **LOOPING THROUGH SETS**
```python
unique = {1, 2, 3, 4}
for num in unique:           # No guaranteed order
    print(num)
for num in sorted(unique):   # Always sorted
    print(num)
# Set comprehension
{sq for num in unique}       # {1, 4, 9, 16}
```

### **LOOPING THROUGH DICTIONARIES**
```python
person = {"name": "Alice", "age": 25}
# Keys
for key in person:
    print(key)
# Values
for value in person.values():
    print(value)
# Items (key-value pairs)
for key, value in person.items():
    print(f"{key}: {value}")
# Dict comprehension
{k.upper(): v for k, v in person.items()}
```

### **LOOP CONTROL**
```python
# Break and Continue
for i in range(10):
    if i == 3:
        continue  # Skip 3
    if i == 7:
        break     # Stop at 7
    print(i)

# Else with loops (runs if no break)
for i in range(5):
    if i == 10:  # Never true
        break
else:
    print("Loop completed without break")

# Nested loops
matrix = [[1, 2], [3, 4]]
for row in matrix:
    for num in row:
        print(num)
```

### **LOOP WITH BUILT-IN FUNCTIONS**
```python
# zip() - multiple sequences
names = ["Alice", "Bob"]
ages = [25, 30]
for name, age in zip(names, ages):
    print(f"{name}: {age}")

# enumerate() - with index
for i, name in enumerate(names):
    print(f"{i}: {name}")

# filter() - filtered items
nums = [1, 2, 3, 4, 5]
for even in filter(lambda x: x % 2 == 0, nums):
    print(even)

# map() - transformed items
for sq in map(lambda x: x**2, nums):
    print(sq)
```

## Copying Objects

```python
import copy

# Shallow copy (different object, shared nested references)
l1 = [1, 2, [3, 4]]
l2 = l1.copy()          # or l2 = l1[:]
l2[0] = 99              # Only l2 changes
l2[2][0] = 88           # Both l1 and l2 change!

# Deep copy (completely independent)
l3 = copy.deepcopy(l1)
l3[2][0] = 77           # Only l3 changes

# Copy dictionary
d1 = {"a": [1, 2]}
d2 = d1.copy()          # Shallow copy
d3 = copy.deepcopy(d1)  # Deep copy
```

## Quick Reference: Object vs Function

- `object.name()` → **Method** (function bound to object)
- `object.name` → **Attribute** (variable bound to object)
- `name(object)` → **Function** (standalone function)

```python
# Examples:
l = [1, 2, 3]
l.append(4)    # Method - object.method()
len(l)         # Function - function(object)
l.sort()       # Method that mutates in-place (returns None)
sorted(l)      # Function that returns new list
l.__len__()    # Method equivalent to len(l)
```

## Memory Check Pattern

```python
def check_mutation(original, result):
    """Quick check if operation mutates or creates new"""
    print(f"Same object? {original is result}")
    print(f"Original ID: {id(original)}")
    print(f"Result ID: {id(result)}")
    print(f"Original after: {original}")

# Example:
l = [1, 2, 3]
result = l[::-1]  # Slice creates new
check_mutation(l, result)
```

## Comprehension Quick Reference

```python
# List comprehension
[x*2 for x in range(5)]                    # [0, 2, 4, 6, 8]
[x for x in range(10) if x % 2 == 0]       # [0, 2, 4, 6, 8]

# Dictionary comprehension
{x: x*2 for x in range(5)}                 # {0: 0, 1: 2, 2: 4, 3: 6, 4: 8}
{k.upper(): v for k, v in {"a": 1}.items()} # {'A': 1}

# Set comprehension
{x*2 for x in range(5)}                    # {0, 2, 4, 6, 8}

# Generator expression (memory efficient)
(x*2 for x in range(1000000))              # Doesn't create list
```

## Useful Built-in Functions

```python
# Type and value checks
type(x)           # Returns type of x
isinstance(x, int) # Check if x is int or subclass
len(x)            # Length of sequence
abs(-5)           # 5
round(3.14159, 2) # 3.14

# Min/Max/Sum
min([1, 2, 3])    # 1
max([1, 2, 3])    # 3
sum([1, 2, 3])    # 6

# Range
range(5)          # 0,1,2,3,4
range(1, 5)       # 1,2,3,4
range(1, 10, 2)   # 1,3,5,7,9

# Sorting
sorted([3,1,2])   # [1,2,3] - returns new list
sorted([3,1,2], reverse=True)  # [3,2,1]
```

## Error Handling

```python
try:
    x = 1 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
except Exception as e:
    print(f"Other error: {e}")
else:
    print("No errors occurred")
finally:
    print("This always runs")
```

## Common Patterns

```python
# Swap values
a, b = 1, 2
a, b = b, a  # a=2, b=1

# Flatten list of lists
matrix = [[1, 2], [3, 4]]
flat = [item for row in matrix for item in row]  # [1, 2, 3, 4]

# Group elements by criteria
from collections import defaultdict
data = [("a", 1), ("b", 2), ("a", 3)]
grouped = defaultdict(list)
for key, value in data:
    grouped[key].append(value)
# {'a': [1, 3], 'b': [2]}

# Find most common elements
from collections import Counter
nums = [1, 2, 2, 3, 3, 3]
counter = Counter(nums)
print(counter.most_common(1))  # [(3, 3)]
```
