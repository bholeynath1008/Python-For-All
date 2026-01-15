# Python Modules & Packages - Complete Guide
A module is **just one Python file** (.py extension) that contains code you want to reuse.
A package is 
# Python Modules & Packages - Quick Reference Guide

## 📝 **Quick Rules to Remember**

1. **One .py file = One module (file)**
   - A single Python file containing code
   - Example: `calculation.py`, `utils.py`

2. **Folder WITH `__init__.py` = Python package**
   - Without `__init__.py` = Just a regular folder (cannot import from it)
   - Use packages to organize large projects

3. **Dot (.) means "go inside" for nested structure:**
   - `package.module` = module inside package
   - `package.subpackage.module` = module inside subpackage

4. **"from X import Y" = Import only Y from X directly**
   - Example: `from calculation import add`
   - Import ONLY 'add' function from calculation module

5. **"import X" = Import entire module X**
   - Example: `import calculation`
   - Must use: `calculation.add()`

6. **"from X import *" = Import ALL public names from X**
   - ⚠️ Use cautiously - can cause naming conflicts!

7. **`__init__.py` in packages can:**
   - Be empty (just marks folder as package)
   - Control what's exported from the package
   - Define package metadata (`__version__`, `__author__`)

8. **Python doesn't need 'export' keyword:**
   - All functions/classes in module are automatically available
   - Use `__all__ = [...]` to control imports with `*`. Define what to exported
   - **see example below**

9. **Import paths:**
   - Same folder: `import module`
   - Subfolder: `from package import module`
   - Nested: `from package.subpackage import module`

10. **In-package imports:**
    - From main package: if you want to import function from that package, you can import directly from package
    - No need to dig into package → module → function
    - Example: `from my_package import function_name`

### `__all__`
---
```python
# ============================================================================
# PYTHON MODULES & PACKAGES - __all__ EXAMPLES
# ============================================================================
# Key Concept: Python doesn't need 'export' keyword
# - All functions/classes in module are automatically available
# - Use `__all__ = [...]` to control imports with `*`
# ============================================================================

# ============================================================================
# EXAMPLE: Package Structure
# ============================================================================
"""
project/
├── main.py
└── calculations/           # Package/Folder
    ├── __init__.py        # Controls package exports
    ├── basic_ops.py       # Module with functions
    └── advanced_ops.py    # Another module
"""

# ============================================================================
# calculations/__init__.py
# ============================================================================
# This file controls what gets exported from the calculations package

# Import specific functions from modules
from .basic_ops import add, multiply
from .advanced_ops import power

# Control what 'from calculations import *' imports
__all__ = ['add', 'multiply', 'power']  # Only these are exported with '*'

# ============================================================================
# calculations/basic_ops.py
# ============================================================================
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b if b != 0 else None

# Module-level __all__ controls 'from basic_ops import *'
__all__ = ['add', 'multiply']  # Only these are exported with '*'

# ============================================================================
# main.py - USAGE EXAMPLES
# ============================================================================

# ----------------------------------------------------------------------------
# METHOD 1: Wildcard import (respects __all__ in __init__.py)
# ----------------------------------------------------------------------------
from calculations import *  # Only imports: add, multiply, power

# ✅ These work (in __all__)
result1 = add(5, 3)        # ✅ add is in __all__
result2 = multiply(4, 2)   # ✅ multiply is in __all__
result3 = power(2, 3)      # ✅ power is in __all__

# ❌ These DON'T work (not in __all__)
# result4 = subtract(5, 3)  # ❌ ERROR: subtract not in __all__
# result5 = divide(10, 2)   # ❌ ERROR: divide not in __all__

# ----------------------------------------------------------------------------
# METHOD 2: Specific import (bypasses __all__)
# ----------------------------------------------------------------------------
# Even if not in __all__, you can still import specifically
from calculations import add           # ✅ Works
from calculations.basic_ops import subtract  # ✅ Works (bypasses __init__.py)

result6 = subtract(10, 4)  # ✅ Now works with specific import

# ----------------------------------------------------------------------------
# METHOD 3: Import entire module
# ----------------------------------------------------------------------------
import calculations.basic_ops

# Access through module name (works regardless of __all__)
result7 = calculations.basic_ops.divide(10, 2)  # ✅ Works

# ============================================================================
# KEY TAKEAWAYS:
# ============================================================================
# 1. __all__ controls ONLY 'from package import *' imports
# 2. Specific imports ALWAYS work: 'from package import specific_function'
# 3. No 'export' keyword needed in Python
# 4. Functions automatically available when module is imported
# ============================================================================

# ============================================================================
# IMPORTANT NOTE:
# The __all__ in __init__.py controls what's available when importing
# directly from the package. The __all__ in individual modules controls
# what's available when importing from that specific module.
# ============================================================================
```

### **Example File Structure:**
```
project/
├── calculation.py  ← This is a MODULE
└── main.py
```

### **Inside calculation.py:**
Contains functions and variables that are automatically available for import.

---

## 📚 **Package = Folder of Modules**
A package is a folder containing multiple Python files (modules) + a special `__init__.py` file.

### **Example Package Structure:**
```
math_tools/           ← This is a PACKAGE
├── __init__.py      ← REQUIRED: Makes folder a package
├── calculation.py    ← Module 1
├── geometry.py       ← Module 2
└── statistics.py     ← Module 3
```

---

## 🎯 **Key Concepts Explained**

### **`__all__` Variable**
- Controls what gets imported with `from module import *`
- Defined in modules or `__init__.py` files
- Example: `__all__ = ['add', 'multiply']` means only these functions are exported with `*`

### **Package-Level Imports**
When `__init__.py` is configured, you can import directly from the package:
```python
# With proper __init__.py configuration
from math_tools import add, calculate_area
# Instead of:
# from math_tools.calculation import add
# from math_tools.geometry import calculate_area
```

### **Relative vs Absolute Imports**
- **Absolute**: `from package.module import function`
- **Relative**: `from .module import function` (inside same package)
- **Relative parent**: `from ..other_package import something`

---

## 🔄 **Import Patterns in Action**

### **Importing from Same Directory:**
```
project/
├── main.py
├── helpers.py
└── calculations.py
```
From main.py: `import helpers` or `from calculations import add`

### **Importing from Package:**
```
project/
├── main.py
└── utils/
    ├── __init__.py
    ├── file_handler.py
    └── data_processor.py
```
From main.py: `from utils import process_data` (if exported in `__init__.py`)

### **Importing from Nested Package:**
```
project/
├── main.py
└── services/
    ├── __init__.py
    └── api/
        ├── __init__.py
        └── client.py
```
From main.py: `from services.api.client import APIClient`

## 📌 **Key Terms Defined**

- **Module**: Single Python file (.py) containing code
- **Package**: Folder containing modules and `__init__.py`
- **`__init__.py`**: Special file that makes a folder a Python package
- **`__all__`**: List controlling what gets imported with `from module import *`
- **Import Path**: Python's way of locating modules/packages
- **Namespace**: Container for holding identifiers (function/class names)
- **Public API**: Functions/classes meant for external use
- **Private**: Functions/classes starting with `_` (convention, not enforced)

### **Example File Structure:**
```
project/
├── calculation.py  ← This is a MODULE
└── main.py
```

### **What's inside calculation.py:**
```python
# calculation.py - A simple module
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

# __all__ controls what gets imported with 'from calculation import *'
__all__ = ['add', 'multiply']  # Only these are exported with '*'
```

## 📚 **Package = A Folder of Modules**
A package is **a folder** containing multiple Python files (modules) with a special `__init__.py` file.

### **Example Package Structure:**
```
math_tools/           ← This is a PACKAGE (a folder)
├── __init__.py      ← REQUIRED: Makes this folder a package
├── calculation.py    ← Module 1
├── geometry.py       ← Module 2
└── statistics.py     ← Module 3
```

### **The `__init__.py` File:**
```python
# math_tools/__init__.py
from .calculation import add, subtract
from .geometry import calculate_area
from .statistics import mean, median

# Package metadata
__version__ = "1.0.0"
__author__ = "Your Name"

# Controls 'from math_tools import *'
__all__ = ['add', 'subtract', 'calculate_area', 'mean']
```

## 🧩 **Importing - Different Ways**

### **Method 1: Import Entire Module** 
```python
import calculation  # Import the WHOLE module

# Usage
result = calculation.add(2, 3)
calculation.subtract(5, 2)
calculation.multiply(4, 3)
```

### **Method 2: Import Specific Functions Only**
```python
from calculation import add, subtract  # Import ONLY these 2

# Usage - Use them directly (no module prefix needed)
result = add(2, 3)
difference = subtract(5, 2)
# multiply(4, 3) ← ERROR: Not imported!
```

### **Method 3: Import Everything (Use Caution)**
```python
from calculation import *  # Import ALL functions (controlled by __all__)

# Usage
add(2, 3)
# subtract()  ← ERROR if not in __all__
multiply(4, 3)
```

## 📁 **Importing from Different Locations**

### **Case 1: Same Folder**
```
project/
├── main.py
└── calculation.py  ← Same level
```
```python
import calculation
result = calculation.add(2, 3)
```

### **Case 2: Subfolder (Package)**
```
project/
├── main.py
└── utils/           ← Package
    ├── __init__.py
    └── calculation.py
```
```python
# Different import styles:
import utils.calculation
result = utils.calculation.add(2, 3)

from utils import calculation
result = calculation.add(2, 3)

from utils.calculation import add
result = add(2, 3)
```

### **Case 3: Nested Subfolders**
```
project/
├── main.py
└── math/           ← Main package
    ├── __init__.py
    └── operations/  ← Sub-package
        ├── __init__.py
        └── calculation.py
```
```python
from math.operations.calculation import add
result = add(2, 3)
```

## 🏷️ **Better Naming Practices**

### **Module Names:**
```python
# GOOD module names (clear, lowercase, underscores):
- calculation.py
- math_operations.py
- data_processor.py
- file_handler.py

# BAD module names:
- calc.py (too short/unclear)
- MyModule.py (uppercase)
- 123utils.py (starts with number)
```

### **Function Names in Modules:**
```python
# calculation.py - GOOD naming:
def add_numbers(a, b):
    return a + b

def calculate_average(numbers):
    return sum(numbers) / len(numbers)

def validate_input(user_input):
    return user_input.isdigit()

# calculation.py - BAD naming:
def s():  # Too short
    pass

def DoCalc():  # Inconsistent casing
    pass
```

## 🔄 **Common Import Patterns**

### **Pattern 1: Module Aliasing**
```python
import calculation as calc  # Short alias
result = calc.add_numbers(5, 3)
```

### **Pattern 2: Selective Import with Aliases**
```python
from calculation import add_numbers as add, multiply_numbers as mul
result = add(5, 3)
product = mul(4, 2)
```

### **Pattern 3: Package-Level Imports**
```python
# In utils/__init__.py
from .calculation import add_numbers
from .geometry import calculate_area

# In main.py
from utils import add_numbers  # Direct import from package
area = calculate_area(5)  # Works if exported in __init__.py
```

### **Pattern 4: Conditional Import**
```python
try:
    import numpy as np
    HAS_NUMPY = True
except ImportError:
    HAS_NUMPY = False
    print("NumPy not installed, using fallback")
```

## 🎯 **Key Differences**

| | **Module** | **Package** |
|--|------------|-------------|
| **What is it?** | Single .py file | Folder with modules |
| **Special File** | None needed | Needs `__init__.py` |
| **Import Syntax** | `import module` | `import package.module` |
| **Export Control** | `__all__` list | `__init__.py` + `__all__` |
| **Example** | `calculation.py` | `math_tools/` |

## 💡 **Best Practices**

1. **Use descriptive names:** `data_cleaner.py` not `dc.py`
2. **Import only what you need:** Avoid `from module import *`
3. **Group related functions:** One module per logical group
4. **Use packages for large projects:** Organize modules in folders
5. **Keep imports at top:** Put all imports at beginning of file
6. **Use `__all__` for clarity:** Define public API explicitly
7. **Start private names with underscore:** `_internal_function()`
8. **Document your modules:** Add docstrings at the top
9. **Handle import errors gracefully:** Use try-except for optional imports
10. **Keep `__init__.py` clean:** Only export what users need

## 🔧 **Complete Import Examples**

```python
# Module in same folder:
import calculation
result = calculation.add(2, 3)

# Specific function from module:
from calculation import add
result = add(2, 3)

# Module inside package:
import math_package.calculation
result = math_package.calculation.add(2, 3)

# Cleaner package import:
from math_package import calculation
result = calculation.add(2, 3)

# Direct import from configured package (requires __init__.py setup):
from math_package import add  # Only works if __init__.py exports 'add'
result = add(2, 3)
```
