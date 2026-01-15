# Perfect Notes: Understanding `if __name__ == "__main__":` in Python

## Why This Matters
In Python, you often see this at the bottom of files:
```python
if __name__ == "__main__":
    # code here
```
This guard allows the **same file** to serve **two roles**:
- A **reusable module** (imported safely without side effects).
- A **standalone script** (runs extra code only when executed directly).

It prevents bugs and makes your code professional and maintainable.

## 1. Key Terms
- **Script**: A Python file you run directly with `python filename.py`. This is the "main program".
- **Module**: A `.py` file containing reusable code (functions, classes, variables) that you import into other files.
- **__name__**: A special built-in variable Python automatically creates for **every** Python file.
  - Python sets its value **before** your code runs.
  - **When you run the file directly**: `__name__ = "__main__"` (a special string created by Python).
  - **When you import the file**: `__name__ = "module_name"` (the filename without `.py`).

## Summary Table

| Situation                          | Example Scenario                                                                 | __name__ Value                  | Top-Level Code Runs?                  | Main Guard Block Runs? | Outcome / Why It Matters                                                                                   |
|------------------------------------|----------------------------------------------------------------------------------|---------------------------------|---------------------------------------|------------------------|-----------------------------------------------------------------------------------------------------------|
| **Running directly**               | `python demo.py`                                                                 | "__main__" (set by Python)      | Yes                                   | Yes                    | Full execution: definitions + test/demo code.<br>Perfect for standalone scripts, testing, quick runs.     |
| **Importing as module**            | `import demo` in another file                                                    | "demo" (filename without .py)   | Yes (definitions only)                | No                     | Safe reuse: functions/classes available, no side effects.<br>Avoids bugs when building larger programs.   |
| **No guard (bad practice)**        | Direct calls/prints at top level (no `if`)                                        | Doesn't matter                  | Yes (everything runs on load)         | N/A                    | Unwanted actions on import → bugs, slow imports, errors.<br>Example: accidental server start on import.  |

Python decides the value based on **how** the file is used — you don't set it yourself.

## 2. Demo: Seeing __name__ in Action
Create `mymodule.py`:
```python
print("File is loading...")
print(f"__name__ is: '{__name__}'")

if __name__ == "__main__":
    print("→ Running as main script!")
else:
    print("→ Imported as module!")
```

**Case 1: Run directly**
```bash
python mymodule.py
```
**Output:**
```
File is loading...
__name__ is: '__main__'
→ Running as main script!
```

**Case 2: Import it**
Create `test.py`:
```python
import mymodule
print("Back in test.py")
```
Run:
```bash
python test.py
```
**Output:**
```
File is loading...
__name__ is: 'mymodule'
→ Imported as module!
Back in test.py
```

## 3. What Runs When?
- **Top-level code** (anything not inside a function/class) **always** runs when the file loads — whether run directly or imported.
- Code **inside** `if __name__ == "__main__":` runs **only** when the file is run directly.

## 4. The Problem It Solves
Without the guard, code meant for "testing/run directly" runs every time the file is imported → bugs, unwanted output, slow imports.

**Bad Example (`bad.py` – no guard):**
```python
def greet():
    print("Hello!")

print("Loading module...")
greet()  # Runs immediately!
```

Import it:
```python
import bad
```
**Output (unwanted!):**
```
Loading module...
Hello!
```

**Good Example (`good.py` – with guard):**
```python
def greet():
    print("Hello!")

print("Loading module...")

if __name__ == "__main__":
    greet()  # Only when run directly
```

- Run directly → "Hello!" prints.
- Import → only "Loading module..." prints. Safe!

## 5. Real-World Uses
Put inside the guard:
- Test/demo code
- Calling a `main()` function
- Handling command-line arguments (`sys.argv`)
- Running examples or quick scripts

Example:
```python
if __name__ == "__main__":
    import sys
    print("Arguments:", sys.argv)
    greet("World")
```

## 6. Golden File Structure (Best Practice)
```python
# 1. Imports
import os
import sys
# (standard library → third-party → your own)

# 2. Constants / globals
API_KEY = "secret"
DEBUG = True

# 3. Definitions (functions, classes)
def greet(name):
    print(f"Hello, {name}!")

class Calculator:
    def add(self, a, b):
        return a + b

# Optional: define main() for clarity
def main():
    greet("World")
    calc = Calculator()
    print(calc.add(2, 3))

# 4. Main guard
if __name__ == "__main__":
    main()  # or put code directly here
```
