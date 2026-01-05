# **🐍 Python – Notes**

## **📌 Table of Contents**

1. [Python Execution & Development Environment](https://file+.vscode-resource.vscode-cdn.net/e%3A/Python%20Django/djangoDRF/python%20Jan1%20notes.md#chapter-1-python-execution--development-environment)
2. [Python Syntax Fundamentals](https://file+.vscode-resource.vscode-cdn.net/e%3A/Python%20Django/djangoDRF/python%20Jan1%20notes.md#chapter-2-python-syntax-fundamentals)
3. [Data Types in Python](https://file+.vscode-resource.vscode-cdn.net/e%3A/Python%20Django/djangoDRF/python%20Jan1%20notes.md#chapter-3-data-types-in-python)
4. [User-Defined Function](https://file+.vscode-resource.vscode-cdn.net/e%3A/Python%20Django/djangoDRF/python%20Jan1%20notes.md#chapter-4-user-defined-function)
5. [String Methods](https://file+.vscode-resource.vscode-cdn.net/e%3A/Python%20Django/djangoDRF/python%20Jan1%20notes.md#chapter-5-string-methods)
6. [Mutable vs Immutable Objects](https://file+.vscode-resource.vscode-cdn.net/e%3A/Python%20Django/djangoDRF/python%20Jan1%20notes.md#chapter-6-mutable-vs-immutable-objects)
7. [Advanced Data Types: Lists, Tuples, Sets, and Dictionaries](https://file+.vscode-resource.vscode-cdn.net/e%3A/Python%20Django/djangoDRF/python%20Jan1%20notes.md#chapter-7-advanced-data-types-lists-tuples-sets-and-dictionaries)

---

## **Chapter 1: Python Execution & Development Environment**

### **Ways to Execute Python Programs**

Python programs can be executed using:

1. **Command Prompt (Python Shell)**
2. **Python IDLE**

---

### **Integrated Development Environment (IDE)**

Popular IDEs for Python development:

- **Jupyter Notebook** (Browser-based interactive shell)
- **Spyder** (Python IDE that comes with **Anaconda**)
- **Anaconda** (Comes with bundled IDEs and libraries)
- **PyCharm**
- **Visual Studio Code**
- **Google Colab** *(Cloud-based)*

---

### **Interpreter vs Compiler**

**Compiler:** translates an entire program into machine code at once.

**Interpreter (Python):** Code is run directly by the interpreter at runtime

| Feature | Interpreter | Compiler |
| --- | --- | --- |
| Execution | One statement at a time | Entire program at once |
| Error Handling | Stops at first error | Errors shown after full analysis |
| Debugging | Easier | Harder |
| Memory | No object code (efficient) | Generates object code (needs more memory) |
| Speed | Slower execution | Faster execution |

---

### **Advantages of Python**

- **Programmer-friendly language**
- **Large ecosystem with rich libraries**
- **Less code with more functionality**
- **Open-source**
- **Interpreted language**
- **No compilation needed**
- **Code executes directly**

---

## **Chapter 2: Python Syntax Fundamentals**

### **Comments in Python**

### **Single Line Comment**

```python
# This is a comment

```

### **Multi-Line Comments**

```python
""" This is a multi-line comment """
''' This is a multi-line comment '''

```

---

### **Python Terminology**

### **Function**

- Reusable block of code
- Performs a specific task
- Defined using parentheses: `function_name()`
- Example: `a()` → `a` is function name
- Built-in functions: `print()`, `len()`, `type()`

---

### **Keyword**

- Reserved words with special meaning, Cannot be used as variable name

```
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await',
 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except',
 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is',
 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return',
 'try', 'while', 'with', 'yield']

```

---

### **Variable**

- Named storage location for data
- Can store different data types
- Follows naming rules

```python
var = 10

```

---

### **Attribute**

- Property or characteristic of an object
- Accessed using dot notation

```python
np.array()

```

- `array` → attribute of `np` module
- Attributes can be **methods** or **data**

---

### **Variables in Python**

- Store values in memory
- **Dynamic typing**
- No need to declare data type
- Data type assigned automatically

```python
a = "apple"   # 'a' becomes string automatically

```

---

### **Variable Assignments**

### **Assigning Different Values to Different Variables**

```python
x, y, z = 20, 40, 50

```

- Number of variables must equal number of values
- Each value creates its own object

---

### **Assigning Same Value to Different Variables *(Recommended)***

```python
x = y = z = 20

```

- Only one object created in memory
- All variables point to same memory location

---

### **Assigning Single Value to Single Variable**

```python
c = 90

```

- Object `90` created
- Variable `c` references that object

---

### **Assigning Multiple Values to Single Variable**

```python
d = 20, 30, 50, 50

type(d)   # <class 'tuple'>

```

- Stored as **tuple** by default

---

### **Variable Naming Rules**

- Must start with **a–z**, **A–Z**, or `_`
- Cannot start with number
- Can contain alphanumeric characters
- Only special character allowed: `_`
- Case-sensitive (`name ≠ Name`)
- Cannot use keywords

---

## **Chapter 3: Data Types in Python**

### **Dynamic Typing**

*Notes*: Python assigns data type automatically based on value

No explicit declaration required.

---

### **Fundamental (Primitive) Data Types**

### **Integer (`int`)**

- Numerical values without decimals
- Examples: `10`, `25`, `600`
- No built-in attributes for modification
- `len()` ❌ not applicable

---

### **Float (`float`)**

- Numerical values with decimals
- Examples: `2.5`, `9.0`, `25.5`
- `45.0` is float, not integer
- `len()` ❌ not applicable

---

### **Boolean (`bool`)**

- Logical values only
- Values: `True`, `False`
- `len()` ❌ not applicable

---

### **String (`str`)**

- Any non-numeric value
- Examples:
- `"Lord Shiva"`
- `"Rama"`
- `"S1232"`
- One object stores multiple characters
- Has built-in methods
- `len()` ✅ applicable

```python
s = "shiva"

s.upper()

len(s)   # 5

```

---

### **Methods & Attributes Applicability**

| Data Type | Attributes/Methods | len() | Examples                |

| --------- | ------------------ | ----- | ----------------------- |

| int       | ❌                  | ❌     | 10                      |

| float     | ❌                  | ❌     | 2.5                     |

| bool      | ❌                  | ❌     | True                    |

| str       | ✅                  | ✅     | upper(), lower()        |

| list      | ✅                  | ✅     | append(), remove()      |

| tuple     | ✅                  | ✅     | count(), index()        |

| set       | ✅                  | ✅     | union(), intersection() |

| dict      | ✅                  | ✅     | keys(), values()        |

---

? Attributes means here:

### **Single vs Multiple Values**

- `"shiva rama krishna"` → **Single string**
- `"shiva", "rama", "krishna"` → **Tuple**

---

### **Default Tuple Creation**

When values are separated by commas, Python creates tuple:

```python
a = 1, 2
b = 1, "shiva"
c = True, 25.4
```

---

### **Object Size Concept**

- `int`, `float`, `bool` → size = **1 value**
- Size refers to **number of values**, not memory bits
- Strings store multiple characters but form **one object**

---

### **Checking Data Type**

```python
x = 5
type(x)   # <class 'int'>

```

---

### **Advanced (Non-Primitive) Data Types**

### **List**

- Mutable
- Ordered

```python
[1, 2, 3, "srk"]
```

---

### **Tuple**

- Immutable
- Ordered

```python
(1, 2, 3)

```

---

### **Set**

- Unordered
- Unique elements

```python
{1, 2, 3}

```

---

### **Dictionary**

- Key–Value pairs
- Python 3.7+ maintains insertion order

```python
d = {"name": "John", "age": 25}

len(d)

d.keys()

d["name"]

```

---

### **Deleting Objects**

```python
del x

del x, y

```

---

### **String Storage Notes**

- Strings stored in **box** in memory
- Numbers stored directly
- `int` has no size limit
- `len()` not applicable for `int`, `float`, `bool`
- Spaces inside quotes are counted as characters

```python
s1 = "gen-ai"

```

### **Multi-Line String**

```python
s4 = '''genai

&

agentic ai'''

```

- All variables stored in **RAM**

---

### **Typecasting**

### **Integer Conversion**

```python
marks = 75
float(marks)
bool(marks)
str(marks)

```

If value is `0`:

```python
bool(0)   # False

```

---

### **Float Conversion**

```python
price = 249.99
int(price)
bool(price)
str(price)
```

---

### **Boolean Conversion**

```python
is_logged_in = True
int(is_logged_in)
float(is_logged_in)
str(is_logged_in)

```

For `False`:

```python
int(False)
float(False)
str(False)

```

---

### **String Conversion**

```python
age = "24"
int(age)
float(age)
bool(age)

```

Empty string:

```python
name = ""
bool(name)   # False

```

❌ Invalid Conversion

```python
int("Hello") # String cannont be cast to int, typecasting error:
```

---

### **Single-Line vs Multi-Line Execution**

- Single-line → value displayed automatically
- Multi-line → only last line displayed

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

## **Python Indexing & Slicing**

### **Data Types Where Indexing/Slicing Works**

- **Strings**: Sequence of characters
- **Lists**: Ordered collection of items
- **Tuples**: Immutable ordered collection
- **Dictionaries**: Key-value pairs (indexing by key, not position)

### **❌ Data Types Where Indexing/Slicing is NOT Applicable**

- **int** (stores single value)
- **float** (stores single value)
- **boolean** (stores single value)
- **Reason**: These store single values, not sequences/collections

---

### **Indexing**

- **Purpose**: Extracting a single value/character
- **Syntax**: `variable_name[index]`
- **Examples**:

```
  d = "bholeynath"
  print(d[0])    # 'b'
  print(d[-1])   # 'h' (negative indexing from end)
  print(d[5])    # 'y'
```

---

## **🔪 Slicing**

- **Purpose**: Extracting multiple characters/values
- **For strings**: 1 value = 1 character
- **Pattern extraction**: Follows specific pattern based on step

### **Python String Slicing**

**Basic Syntax:**

```python
string[start:end:step]
```

- **start**: Starting index (inclusive)
- **end**: Ending index (exclusive)
- **step**: Direction & increment value

## **🎯 Core Rules**

### **1. Default Values**

- **Positive step [:n:1] or [n::1]** (forward):
    - Missing `start` → defaults to `0`
    - Missing `end` → defaults to `len(string)`
    - Missing `step` → defaults to `1`
- **Negative step [:n:-1] or [n::-1]** (backward):
    - Missing `start` → defaults to `len(string)-1`
    - Missing `end` → defaults to `0`

**Step Determines Direction:**

```python
text = "ABCDE"

# Positive step (1): A → B → C → D → E
print(text[::1])   # "ABCDE"

# Negative step (-1): E → D → C → B → A
print(text[::-1])  # "EDCBA"

# Step 2: Every other character
print(text[::2])   # "ACE"

text = "Python"

# ✅ Valid: Start < End with Positive Step
text[0:3:1]    # "Pyt"

# ✅ Valid: Start > End with Negative Step
text[3:0:-1]   # "hty"

# ❌ Empty: Direction Conflict (returns empty string)
text[0:3:-1]   # ""
text[3:0:1]    # ""

```

**Indexing Types**

```python
d = "bholeynath"
# Positive: 0   1   2   3   4   5   6   7   8   9
#           b   h   o   l   e   y   n   a   t   h
# Negative: -10 -9  -8  -7  -6  -5  -4  -3  -2  -1

```

## **📊 Common Operations**

### **Extraction Examples**

```python
d = "bholeynath"

# Forward slicing
print(d[0:3:1])     # "bho"
print(d[:3])        # "bho" (same as above)
print(d[4:])        # "eynath" (from index 4 to end)

# Backward slicing
print(d[7:2:-1])    # "anyeh" (indices 7 down to 3)
print(d[::-1])      # "htanyelohb" (full reverse)
s = "abcd"
s[::-1]
# Equivalent to:
s[3:0:-1]  # 'dcba' ✅ includes index 0
```

### **Practical Application**

```python
data = "NARgenai001"

# Extract components
institute = data[:3]      # "NAR"
course = data[3:8]        # "genai"
roll_no = data[8:]        # "001"

# Alternative using negative indices
course = data[3:-3]       # "genai"

```

## **Key Behaviors**

1. No Errors in Slicing, Always returns a string (empty if invalid)
2. New Object Creation, slicing creates a new string and original remains unchanged

## **⚡ Memory Aids**

### **Quick Reference Table**

| Pattern | Step | Start Default | End Default | Example |
| --- | --- | --- | --- | --- |
| `[:n]` | `+1` | `0` | `n` | `"Hello"[:3] → "Hel"` |
| `[n:]` | `+1` | `n` | `len(str)` | `"Hello"[2:] → "llo"` |
| `[::k]` | `+k` | `0` | `len(str)` | `"Hello"[::2] → "Hlo"` |
| `[::-1]` | `-1` | `len(str) - 1` | `0` | `"Hello"[::-1] → "olleH"` |
| `[:n:-1]` | `-1` | `len(str) - 1` | `n` | `"Hello"[:2:-1] → "ol"` |
| `[n::-1]` | `-1` | `n` | `0` | `"Hello"[3::-1] → "lleH"` |

| Slice Pattern | Step | Equivalent To | Result |
| --- | --- | --- | --- |
| `[:n]` | +1 | `[0:n:1]` | First n characters |
| `[n:]` | +1 | `[n:len(s):1]` | From n to end |
| `[::-1]` | -1 | `[-1:-len-1:-1]` | Full reverse |
| `[m:n:-1]` | -1 | From m backward to n+1 | Reverse slice |

### **Direction Rules**

```
Positive Step (+): Start should be LEFT of End
Negative Step (-): Start should be RIGHT of End

```

## **💡 Pro Tips**

### **1. Slice Examples**

```python
text = "Hello"
 #1. Reverse slicing (negative step)
reverse = text[::-1]  # "olleH"
text[4:-1:-1]    # 'olleH'  (same as text[::-1])
text[::-2]       # 'olH'   indexes: 4 → 2 → 0

# 2. Forward slicing (positive step)
text[1:4]        # 'ell'   start=1, end=4, step=1
text[:3]         # 'Hel'   missing start → 0
text[2:]         # 'llo'   missing end → len(text)
text[:]          # 'Hello' missing start & end
# Step = +2
text[::2]        # 'Hlo'   indexes: 0 → 2 → 4
text[1:5:2]      # 'el'    indexes: 1 → 3

# 3. Slicing Negative step (backward flow (text.len-1 -> 0))
- If end is missing it is 0 index default, and it is Included.
text[:2:-1]      # 'ol'    indexes: 4 → 3 missing start ->text.len-1 (4)
text[3:0:-1]     # 'lle'   index 0 is EXCLUDED because end is always excluded

# Empty: Direction Conflict (returns empty string)
text[0:3:-1]     # ''  ❌ backward step but start < end
text[3:0:1]      # ''  ❌ forward step but start > end

s = "abcd"
s[::-1]
# Equivalent to:
s[3:0:-1]  # 'dcba' ✅ includes index 0

```

### **2. Extract Every Nth Character**

```python
text = "ABCDEFGH"
print(text[::2])   # "ACEG" (every 2nd)
print(text[1::2])  # "BDFH" (starting from index 1)

```

## **Chapter 5: String Methods**

Strings in Python are immutable sequences of characters. Methods return new strings (original unchanged). Common methods operate on case, whitespace, searching, and validation.

### **Case Conversion Methods**

```python
s = " S12@. . aV "
print(s.upper())    # " S12@. . AV " (all uppercase)
print(s.lower())    # " s12@. . av " (all lowercase)
print(s.swapcase()) # " s12@. . Av " (swap case)
print(s.capitalize())  # " S12@. . av " (first char uppercase, rest lowercase)
print(s.title())    # "  S12@. . Av " (each word's first char uppercase)

```

### **Whitespace Removal Methods**

```python
s = " S12@. . aV "
print(s.lstrip())   # "S12@. . aV " (remove leading whitespace)
print(s.rstrip())   # " S12@. . aV" (remove trailing whitespace)
print(s.strip())    # "S12@. . aV" (remove both leading and trailing)

```

### **Searching and Counting Methods**

```python
s = " S12@. . aV "
print(s.count('a')) # 1 (count occurrences)
print(s.index('a')) # 10 (index of first occurrence; raises ValueError if not found)
print(s.find('a'))  # 10 (index of first occurrence; returns -1 if not found)
print(s.find('z'))  # -1 (no error, unlike index())

```

### **Splitting and Joining Methods**

- **split()**: Splits string into list of substrings (default by whitespace).

```python
s = "siva rama krishna"
print(s.split())    # ['siva', 'rama', 'krishna']

```

- **join()**: Joins iterable of strings with self as separator.

```python
print("".join(["siva", "rama"]))  # "sivarama"
print(" ".join(["siva", "rama"])) # "siva rama"

```

### **Prefix/Suffix and Replacement Methods**

```python
s = "Python"
print(s.startswith("Py"))  # True
print(s.endswith("on"))    # True

s = "AP40BG1993"
print(s.removeprefix("AP40"))  # "BG1993" (remove starting prefix)
print(s.removesuffix("1993"))  # "AP40BG" (remove ending suffix)

print(s.replace("BG", "XX"))   # "AP40XX1993" (replace all occurrences)

```

### **Validation Methods (Return Boolean)**

| Method | Description | Example (`s = "abc123"`) | Result |
| --- | --- | --- | --- |
| `isalpha()` | All characters alphabetic | `s.isalpha()` | False |
| `isdigit()` | All characters digits | `s.isdigit()` | False |
| `isspace()` | All characters whitespace | `" ".isspace()` | True |
| `islower()` | All cased characters lowercase | `s.islower()` | True |
| `isupper()` | All cased characters uppercase | `"ABC".isupper()` | True |
| `isalnum()` | All characters alphanumeric | `s.isalnum()` | True |
| `istitle()` | Title-cased (first char of words uppercase) | `"Siva Rama".istitle()` | True |

**Note**: Empty string returns `False` for most validation methods.

### **String Basics Recap**

- **Single-Line String**: `s = "hello"`
- **Multi-Line String**: `s = '''multi\nline'''` or `s = """multi\nline"""`
- **Length**: `len(s)` (counts characters, including spaces).
- **Concatenation**: `s1 + s2` or `s1 * 3` (repeats).
- **Type Casting**: `str(123)` → `"123"`; `int("123")` → `123`.
- **Indexing/Slicing**: As in Chapter 3 (e.g., `s[0]`, `s[1:3]`).
- **Attributes**: Strings have methods (as above); no direct data attributes.

**Example Extraction**:

```python
s = "AP40BG1993"
last_four = s[-4:]      # "1993" (slicing)
prefix_removed = s.removeprefix("AP40")  # "BG1993"

```

**Difference: String vs Tuple**:

- `a = "siva rama"` → Single string object (one value, len=9).
- `b = "siva", "rama"` → Tuple of two strings (multiple values, len=2).

---

## **Chapter 6: Mutable vs Immutable Objects**

Python objects are either **mutable** (changeable in-place) or **immutable** (unchangeable; modifications create new objects).

### **Key Differences**

| Aspect | Mutable Objects | Immutable Objects |
| --- | --- | --- |
| **Definition** | Can modify values in same object | Cannot modify; new object created |
| **Examples** | List, Set, Dict | int, float, bool, str, tuple |
| **Memory** | Same ID after modification | New ID after modification |
| **Pros** | Efficient for changes | Safer (thread-safe), hashable |
| **Cons** | Risk of unintended changes | Overhead for frequent changes |

### **Memory Address Check (Using `id()`)**

```python
# Immutable Example (int)
a = 10
print(id(a))  # e.g., 1407123456 (memory address)
a = 12        # New object created; old discarded
print(id(a))  # Different address

# Mutable Example (list)
l = [1, 2, 3]
print(id(l))  # e.g., 1407123456
l.append(4)   # Same object modified
print(id(l))  # Same address

```

**Modification Rules**:

- **Immutable**: Reassign to store changes (e.g., `s = s.upper()`).
- **Mutable**: Modify directly (e.g., `l.append(4)`). Avoid `l = l.append()` (returns None, causes error).

**Copying**:

- **Shallow Copy**: Copies object but shares nested references (e.g., `l2 = l.copy()` or `l2 = l[:]`). Different IDs, but changes in nested mutables affect both.
- **Deep Copy**: Fully independent copy (use `copy.deepcopy(l)` from `import copy`). For basics, `copy()` suffices.

```python
l1 = [1, 2, 3]
l2 = l1        # Shallow reference (same ID)
l2.append(4)   # Affects l1 too
print(id(l1) == id(l2))  # True

l2 = l1.copy() # Shallow copy (different ID)
l2.append(5)   # Doesn't affect l1
print(id(l1) == id(l2))  # False

```

**Note**: Small ints (-5 to 256) are cached (same ID for same value).

---

## **Chapter 7: Advanced Data Types: Lists, Tuples, Sets, and Dictionaries**

Python Collection Types:

| Feature | **List [ ]** | **Tuple ( )** | **Set {}** |
| --- | --- | --- | --- |
| **Empty creation** | `l = [] 
 l = list()` | `t = () 
t = tuple()` | `s = set()` |
| **Print empty** | `[]` | `()` | `set()` |
| **With values** | `[v1, v2, v3, ...]` | `(v1, v2, v3, ...)` | `{v1, v2, v3, ...}` |
| **Allowed value types** | All data types | All data types | Only immutable types`int, float, bool, str, tuple` |
| **Order preserved** | ✅ Yes | ✅ Yes | ❌ No |
| **Indexing** | ✅ Yes | ✅ Yes | ❌ No |
| **Slicing** | ✅ Yes | ✅ Yes | ❌ No |
| **Duplicates allowed** | ✅ Yes | ✅ Yes | ❌ No |
| **Mutable / Immutable** | **Mutable** | **Immutable** | **Mutable** |
| **Replace element** | ✅ Yes`l[i] = value` | ❌ No | ❌ No |
| **Add element** | ✅ Yes`append()insert()extend()` | ❌ No | ✅ Yes`add()update()` |
| **Remove element** | ✅ Yes`remove()pop()clear()` | ❌ No | ✅ Yes`remove()discard()pop()` |
| **Modification allowed** | Add / Replace / Remove | ❌ Not allowed | Add / Remove |
| **Extract / Select** | Indexing & slicing | Indexing & slicing | ❌ Not possible |

### 

**Notes**:

- List/Tuple: Use `[]` vs `()`.
- Set: No curly braces for empty; rejects mutables (unhashable means mutable, e.g., lists/sets as elements—hash must be fixed for fast lookups).
- # {} is empty dict, not set
- Dict: Key-value pairs; keys must be immutable/hashable.

### **Lists (Mutable, Ordered Collection)**

### **Creation**

```python
l = [1, 2, "three"]  # Mixed types OK

```

### **Extract/Select**

- Indexing/Slicing: `l[0]`, `l[-1]`, `l[1:3]`.
- Example: `l = [10, 2, 30]` → `l[-1]` → `30`.

### **Modify (Add/Replace/Remove)**

- **Add**:
    
    ```python
    l.append(25)          # Single value (end)
    l.extend([30, 45])    # Multiple (end)
    l.insert(3, 23)       # Single at index 3
    # Multiple at positions: Use loop or multiple inserts
    
    ```
    
- **Replace**: Extract then assign: `l[-1] = 50`.
- **Remove**:
    
    ```python
    l.remove(23)    # First occurrence (ValueError if missing)
    l.pop(1)        # By index (removes/returns; default last)
    l.clear()       # Empty list
    del l[0]        # By index
    del l           # Delete entire list
    
    ```
    
- **Concatenation**: `l1 + l2` (new list); `l1.extend(l2)` (modifies l1).

### **Additional Methods**

```python
l.count(10)     # Occurrences
l.index(5)      # First index (ValueError if missing)
l.reverse()     # In-place reverse
l.sort()        # Ascending (in-place; errors on mixed types)
l.sort(reverse=True)  # Descending
l.copy()        # Shallow copy

```

**Example**:

```python
l = [15, 5, 6, 3, 8, 33, 11]
l.insert(3, 23)       # [15, 5, 6, 23, 3, 8, 33, 11]
l.extend([40, 50])    # Adds to end

```

### **Tuples (Immutable, Ordered Collection)**

### **Creation**

```python
t = (1, 2, "three")  # Or `1, 2, "three"`

```

### **Extract/Select**

Same as lists: Indexing/Slicing (e.g., `t[2]` → `"three"`).

### **Modify**

Immutable—no add/replace/remove. Use for fixed data.

### **Methods**

Only two:

```python
t.count(1)      # Occurrences
t.index(2)      # First index (ValueError if missing)

```

**Uses**:

- Lock data (no accidental changes).
- Faster iteration/loops than lists.

**Example**:

```python
t = (10, 5, 20, 19)
print(t[2])     # 20
# t[2] = 90     # Error: Cannot modify

```

### **Sets (Mutable, Unordered, Unique Elements)**

### **Creation**

```python
s = {1, 2, 3}  # Auto-removes duplicates
# Cannot add mutables: { [1,2] } → TypeError (unhashable)
# Booleans as ints: {0, False} → {False} (0 == False); {1, True} → {1}

```

### **Extract/Select**

No indexing/slicing (unordered). Use `in` or convert: `list(s)[0]`.

### **Modify (Add/Remove)**

- **Add**:
    
    ```python
    s.add(25)             # Single
    s.update([30, 45])    # Multiple
    
    ```
    
- **Remove**:
    
    ```python
    s.remove(3)     # Raises KeyError if missing
    s.discard(4)    # No error if missing
    s.clear()       # Empty
    del s           # Delete entire
    
    ```
    

### **Set Operations (Advantages: Fast lookups, no duplicates)**

```python
A = {1, 2, 3}
B = {3, 4, 5}

A.union(B)              # {1,2,3,4,5} (or A \| B)
A.intersection(B)       # {3} (or A & B)
A - B                   # {1,2} (A only)
B - A                   # {4,5} (B only)
A.symmetric_difference(B)  # {1,2,4,5} (non-common)
A.isdisjoint(B)         # False (have common)
A.issubset(B)           # False
B.issuperset(A)         # True (A subset of B)
s.copy()                # Shallow copy

```

**Example**:

```python
s1 = {1, 2, 3, 4}
s2 = {5, 6, 7}
print(s1.isdisjoint(s2))  # True

```

### **Dictionaries (Mutable, Ordered Key-Value Pairs)**

### **Creation**

```python
d = {"name": "Siva", "age": 25}  # Keys immutable/unique

```

### **Extract/Select**

`d["name"]` or `d.get("age")` (no KeyError if missing).

### **Modify**

- Add/Replace: `d["city"] = "Delhi"`
- Remove: `del d["age"]` or `d.pop("name")`
- `d.clear()`, `del d`

### **Methods**

`d.keys()`, `d.values()`, `d.items()`, `len(d)`.

**Note**: Brief—focus on keys as unique identifiers.

### **Type Casting Between Types**

```python
l = [1, 2, 3, 4]
t = tuple(l)        # (1, 2, 3, 4)
s = set(l)          # {1, 2, 3, 4}

# Merge lists without duplicates
l1 = [1, 2, 3]
l2 = [2, 3, 4]
unique = list(set(l1) | set(l2))  # [1, 2, 3, 4] (or set(l1 + l2))

```

**Avoid**: `l1.extend(l2)` (keeps duplicates); `l1 + l2` (concatenates with duplicates).
