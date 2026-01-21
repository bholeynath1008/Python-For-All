# Python Control Flow - Complete Study Guide

### **INDEX**

- [1. Introduction to Control Flow](#1-introduction-to-control-flow)
  - [1.1 What is Control Flow?](#11-what-is-control-flow)
  - [1.2 Types of Control Structures](#12-types-of-control-structures)
  - [1.3 Conditional Operators in Control Flow](#13-conditional-operators-in-control-flow)
- [2. Conditional Statements](#2-conditional-statements)
  - [2.1 Simple IF Statement](#21-simple-if-statement)
  - [2.2 IF-ELSE Statement](#22-if-else-statement)
  - [2.3 IF-ELIF Statement](#23-if-elif-statement)
  - [2.4 IF-ELIF-ELSE Statement](#24-if-elif-else-statement)
  - [2.5 Nested IF Statement](#25-nested-if-statement)
- [3. Loops (Iterations)](#3-loops-iterations)
  - [3.1 FOR Loop](#31-for-loop)
  - [3.2 WHILE Loop](#32-while-loop)
  - [3.3 Nested Loops](#33-nested-loops)
  - [3.4 Loop Control Statements](#34-loop-control-statements)
- [4. Use Cases & When to Use](#4-use-cases--when-to-use)
  - [4.1 Conditional Statements Use Cases](#41-conditional-statements-use-cases)
  - [4.2 Loop Use Cases](#42-loop-use-cases)
  - [4.3 Real-World Scenarios](#43-real-world-scenarios)
  - [4.4 Best Practices](#44-best-practices)
- [Summary Cheat Sheet](#summary-cheat-sheet)
- [Python Loop Helpers](#️-python-loop-helpers-the-complete-cheat-sheet)
---
## **Summary Cheat Sheet**
| Control Structure | Best For | Syntax |
|-------------------|----------|--------|
| **Simple IF** | Single condition check | `if condition:` |
| **IF-ELSE** | Two outcomes | `if: ... else:` |
| **IF-ELIF-ELSE** | Multiple conditions | `if: ... elif: ... else:` |
| **Nested IF** | Dependent conditions | `if: ... if: ...` |
| **FOR Loop** | Known iterations | `for i in sequence:` |
| **WHILE Loop** | Unknown iterations | `while condition:` |
| **Nested Loop** | Multi-dimensional data | `for: ... for: ...` |
| **BREAK** | Exit loop early | `break` |
| **CONTINUE** | Skip iteration | `continue` |
| **PASS** | Placeholder | `pass` |

**Dictionaries: Keys, Values, and Items**
| Method | What it returns | Example Usage |
| --- | --- | --- |
| `.keys()` | Just the keys | `for k in dict.keys():` |
| `.values()` | Just the values | `for v in dict.values():` |
| **`.items()`** | **Both (Key & Value)** | `for k, v in dict.items():` |

> **Pro Tip:** Always use `.items()` when you need both the key and value; it's much faster and cleaner than looking up the value manually inside the loop.

**Python loop helpers enumerate, zip, sorted...**
| If you want to... | Use this... |
| --- | --- |
| Access the **index** and the **item** | `enumerate(list)` |
| Loop through **multiple lists** together | `zip(list1, list2)` |
| Loop in **reverse** | `reversed(list)` |
| Loop in **alphabetical/numerical** order | `sorted(list)` |
| Loop a **fixed number** of times | `range(n)` |

---
# **DETAILED CONTENT**

## **1. Introduction to Control Flow**

### 1.1 What is Control Flow?
- **Control flow** determines the order in which code is executed
- Allows programs to make decisions and repeat actions
- Makes code dynamic and responsive

### 1.2 Types of Control Structures
1. **Sequential**: Code executes line by line (default)
2. **Conditional**: Code executes based on conditions (if statements)
3. **Iterative**: Code repeats multiple times (loops)

### 1.3 Conditional Operators in Control Flow
Conditions can use:
- **Comparison operators**: `==`, `!=`, `>`, `<`, `>=`, `<=`
- **Logical operators**: `and`, `or`, `not`
- **Membership operators**: `in`, `not in`
- **Identity operators**: `is`, `is not`

---

## **2. Conditional Statements**

---

## 2.1 Simple IF Statement

### Syntax:
```python
if condition:
    code_block
```

### How it Works:
- **If condition is True**: Execute the if block (all lines inside)
- **If condition is False**: Ignore the if block (skip all lines inside)

### ⚠️ Important Rules:
- Condition must evaluate to `True` or `False`
- **Indentation is mandatory** (usually 4 spaces or 1 tab)
- Colon (`:`) is required after condition

### Examples:

**Example 1: Basic IF**
```python
if 2 < 3:
    print("srk")
    print("python")
```
**Output:**
```
srk
python
```
**Explanation**: Condition `2 < 3` is True, so both lines execute

---

**Example 2: False Condition**
```python
if 5 > 10:
    print("This won't print")

print("This always prints")
```
**Output:**
```
This always prints
```
**Explanation**: Condition `5 > 10` is False, so if block is skipped

---

**Example 3: With Variable**
```python
x = 2
if x == 2:
    print("x is 2")
```
**Output:**
```
x is 2
```

---

**Example 4: Using Logical Operators**
```python
age = 25
if age > 18 and age < 30:
    print("You are a young adult")
```
**Output:**
```
You are a young adult
```

---

**Example 5: Using Membership Operator**
```python
fruits = ["apple", "banana", "mango"]
if "apple" in fruits:
    print("Apple is available")
```
**Output:**
```
Apple is available
```

---

## 2.2 IF-ELSE Statement

### Syntax:
```python
if condition:
    code_block1
else:
    code_block2
```

### Flow of Execution:
- **If condition is True**: Execute if block only
- **If condition is False**: Execute else block only
- **Only ONE block executes**, never both

### Examples:

**Example 1: Basic IF-ELSE**
```python
if 2 < 3:
    print("python")
else:
    print("ai")
```
**Output:**
```
python
```

---

**Example 2: Even or Odd**
```python
number = 7
if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")
```
**Output:**
```
Odd number
```

---

**Example 3: Age Check**
```python
age = 16
if age >= 18:
    print("You can vote")
else:
    print("You cannot vote yet")
```
**Output:**
```
You cannot vote yet
```

---

**Example 4: Login System**
```python
password = "python123"
user_input = "python123"

if user_input == password:
    print("Login successful")
else:
    print("Invalid password")
```
**Output:**
```
Login successful
```

---

## 2.3 IF-ELIF Statement

### Syntax:
```python
if condition1:
    code_block1
elif condition2:
    code_block2
elif condition3:
    code_block3
```

### How it Works:
- Checks conditions **in order from top to bottom**
- Executes the **first True condition** and **stops**
- If all conditions are False, **nothing executes**

### Examples:

**Example 1: Grade System**
```python
marks = 85

if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
```
**Output:**
```
Grade B
```

---

**Example 2: Multiple Conditions**
```python
x = 0

if x > 0:
    print("Positive")
elif x < 0:
    print("Negative")
```
**Output:**
```
(No output because both conditions are False)
```

---

## 2.4 IF-ELIF-ELSE Statement

### Syntax:
```python
if condition1:
    code_block1
elif condition2:
    code_block2
elif condition3:
    code_block3
else:
    code_block_default
```

### How it Works:
- Checks conditions from top to bottom
- Executes **first True condition**
- If **all conditions are False**, executes **else block**
- **Guarantees at least one block will execute**

### Examples:

**Example 1: Complete Grade System**
```python
marks = 65

if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
elif marks >= 60:
    print("Grade D")
else:
    print("Grade F")
```
**Output:**
```
Grade D
```

---

**Example 2: Number Classification**
```python
x = 0

if x > 0:
    print("Positive number")
elif x < 0:
    print("Negative number")
else:
    print("Zero")
```
**Output:**
```
Zero
```

---

**Example 3: Day of Week**
```python
day = 3

if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
else:
    print("Weekend")
```
**Output:**
```
Wednesday
```

---

**Example 4: Traffic Light**
```python
light = "yellow"

if light == "red":
    print("Stop")
elif light == "yellow":
    print("Slow down")
elif light == "green":
    print("Go")
else:
    print("Invalid light color")
```
**Output:**
```
Slow down
```

---

## 2.5 Nested IF Statement

### Syntax:
```python
if outer_condition:
    # Outer if block
    if inner_condition:
        # Inner if block
        code
    else:
        code
else:
    code
```

### Key Points:
- **IF inside another IF**
- Inner condition is checked **only if outer condition is True**
- Can have **multiple levels of nesting**
- Use proper **indentation** (very important!)

### Examples:

**Example 1: Age and License Check**
```python
age = 20
has_license = True

if age >= 18:
    print("Age requirement met")
    if has_license:
        print("You can drive")
    else:
        print("Get a license first")
else:
    print("Too young to drive")
```
**Output:**
```
Age requirement met
You can drive
```

---

**Example 2: Number Analysis**
```python
number = 24

if number > 0:
    print("Positive number")
    if number % 2 == 0:
        print("Even number")
    else:
        print("Odd number")
else:
    print("Not a positive number")
```
**Output:**
```
Positive number
Even number
```

---

**Example 3: Login System with Role**
```python
username = "admin"
password = "pass123"
user_role = "admin"

if username == "admin":
    if password == "pass123":
        if user_role == "admin":
            print("Admin access granted")
        else:
            print("User access granted")
    else:
        print("Wrong password")
else:
    print("User not found")
```
**Output:**
```
Admin access granted
```

---

**Example 4: Grade with Bonus**
```python
marks = 85
attendance = 95

if marks >= 80:
    print("Good marks!")
    if attendance >= 90:
        print("Bonus: +5 marks")
        marks += 5
        print(f"Final marks: {marks}")
    else:
        print("No bonus")
else:
    print("Need to improve")
```
**Output:**
```
Good marks!
Bonus: +5 marks
Final marks: 90
```

---

**Example 5: Three-Level Nesting**
```python
age = 25
income = 50000
credit_score = 750

if age >= 21:
    if income >= 30000:
        if credit_score >= 700:
            print("Loan approved")
        else:
            print("Credit score too low")
    else:
        print("Income too low")
else:
    print("Age requirement not met")
```
**Output:**
```
Loan approved
```

---

## **3. Loops (Iterations)**

---

## 3.1 FOR Loop

### What is a FOR Loop?
- Used to **iterate over a sequence** (list, tuple, string, range, etc.)
- Executes a block of code **for each item** in the sequence
- Number of iterations is **predetermined**

### Syntax:
```python
for variable in sequence:
    code_block
```

### How it Works:
1. Takes first item from sequence
2. Assigns it to variable
3. Executes code block
4. Repeats until sequence ends

---

### 3.1.1 Iterating Over Different Sequences

**Example 1: List**
```python
fruits = ["apple", "banana", "mango"]
for fruit in fruits:
    print(fruit)
```
**Output:**
```
apple
banana
mango
```

---

**Example 2: String**
```python
for char in "Python":
    print(char)
```
**Output:**
```
P
y
t
h
o
n
```

---

**Example 3: Tuple**
```python
numbers = (1, 2, 3, 4, 5)
for num in numbers:
    print(num * 2)
```
**Output:**
```
2
4
6
8
10
```

---

### 3.1.2 Range Function

**Syntax:**
- `range(stop)` → 0 to stop-1
- `range(start, stop)` → start to stop-1
- `range(start, stop, step)` → start to stop-1 with step

**Example 1: range(stop)**
```python
for i in range(5):
    print(i)
```
**Output:**
```
0
1
2
3
4
```

---

**Example 2: range(start, stop)**
```python
for i in range(2, 7):
    print(i)
```
**Output:**
```
2
3
4
5
6
```

---

**Example 3: range(start, stop, step)**
```python
for i in range(0, 10, 2):
    print(i)
```
**Output:**
```
0
2
4
6
8
```

---

**Example 4: Reverse Range**
```python
for i in range(10, 0, -1):
    print(i)
```
**Output:**
```
10
9
8
7
6
5
4
3
2
1
```

---

### 3.1.3 Practical FOR Loop Examples

**Example 1: Sum of Numbers**
```python
total = 0
for i in range(1, 6):
    total += i
print(f"Sum: {total}")
```
**Output:**
```
Sum: 15
```

---

**Example 2: Multiplication Table**
```python
number = 5
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")
```
**Output:**
```
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
...
5 x 10 = 50
```

---

**Example 3: List with Index**
```python
fruits = ["apple", "banana", "mango"]
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
```
**Output:**
```
0: apple
1: banana
2: mango
```

---

**Example 4: Dictionary Iteration**
```python
student = {"name": "John", "age": 20, "grade": "A"}

# Iterate over keys
for key in student:
    print(key)

# Iterate over values
for value in student.values():
    print(value)

# Iterate over key-value pairs
for key, value in student.items():
    print(f"{key}: {value}")
```
**Output:**
```
name
age
grade

John
20
A

name: John
age: 20
grade: A
```

---

## 3.2 WHILE Loop

### What is a WHILE Loop?
- Executes code block **as long as condition is True**
- Number of iterations is **not predetermined**
- Must have a way to make condition False (avoid infinite loops)

### Syntax:
```python
while condition:
    code_block
```

### How it Works:
1. Checks condition
2. If True, executes code block
3. Returns to step 1
4. If False, exits loop

---

### Examples:

**Example 1: Basic WHILE Loop**
```python
count = 1
while count <= 5:
    print(count)
    count += 1
```
**Output:**
```
1
2
3
4
5
```

---

**Example 2: User Input Validation**
```python
password = ""
while password != "python123":
    password = input("Enter password: ")
    if password != "python123":
        print("Wrong password, try again")
print("Access granted!")
```

---

**Example 3: Sum Until Zero**
```python
total = 0
number = int(input("Enter number (0 to stop): "))

while number != 0:
    total += number
    number = int(input("Enter number (0 to stop): "))

print(f"Total: {total}")
```

---

**Example 4: Countdown**
```python
countdown = 10
while countdown > 0:
    print(countdown)
    countdown -= 1
print("Blast off!")
```
**Output:**
```
10
9
8
...
1
Blast off!
```

---

### 3.2.1 Infinite Loops

**⚠️ WARNING**: Infinite loops run forever and can crash your program

**Example of Infinite Loop (DON'T RUN)**
```python
# This will run forever!
while True:
    print("This never stops")
```

**How to Stop Infinite Loops:**
- Use `Ctrl + C` in terminal
- Use `break` statement
- Ensure condition becomes False eventually

---

## 3.3 Nested Loops

### What are Nested Loops?
- **Loop inside another loop**
- **Inner loop completes fully** for each iteration of outer loop

### Syntax:
```python
for outer_variable in outer_sequence:
    for inner_variable in inner_sequence:
        code_block
```

---

### Examples:

**Example 1: Multiplication Table (1-5)**
```python
for i in range(1, 6):
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")
    print("---")
```
**Output:**
```
1 x 1 = 1
1 x 2 = 2
...
1 x 10 = 10
---
2 x 1 = 2
...
```

---

**Example 2: Pattern Printing**
```python
for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()
```
**Output:**
```
* 
* * 
* * * 
* * * * 
* * * * * 
```

---

**Example 3: Matrix**
```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    for element in row:
        print(element, end=" ")
    print()
```
**Output:**
```
1 2 3 
4 5 6 
7 8 9 
```

---

**Example 4: Nested WHILE Loop**
```python
i = 1
while i <= 3:
    j = 1
    while j <= 3:
        print(f"({i}, {j})", end=" ")
        j += 1
    print()
    i += 1
```
**Output:**
```
(1, 1) (1, 2) (1, 3) 
(2, 1) (2, 2) (2, 3) 
(3, 1) (3, 2) (3, 3) 
```

---

**Example 5: Finding Prime Numbers**
```python
for num in range(2, 20):
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")
```
**Output:**
```
2 3 5 7 11 13 17 19 
```

---

## 3.4 Loop Control Statements

---

### 3.4.1 BREAK Statement

**Purpose**: Exits the loop immediately

**Syntax:**
```python
for/while loop:
    if condition:
        break
```

**Example 1: Stop at Specific Value**
```python
for i in range(1, 11):
    if i == 6:
        break
    print(i)
```
**Output:**
```
1
2
3
4
5
```

---

**Example 2: Search in List**
```python
numbers = [10, 20, 30, 40, 50]
search = 30

for num in numbers:
    if num == search:
        print(f"Found {search}")
        break
    print(f"Checking {num}")
```
**Output:**
```
Checking 10
Checking 20
Found 30
```

---

**Example 3: BREAK in WHILE Loop**
```python
count = 0
while True:
    print(count)
    count += 1
    if count == 5:
        break
```
**Output:**
```
0
1
2
3
4
```

---

### 3.4.2 CONTINUE Statement

**Purpose**: Skips current iteration and continues to next

**Syntax:**
```python
for/while loop:
    if condition:
        continue
    code
```

**Example 1: Skip Even Numbers**
```python
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)
```
**Output:**
```
1
3
5
7
9
```

---

**Example 2: Skip Specific Value**
```python
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
```
**Output:**
```
1
2
4
5
```

---

**Example 3: Filter List**
```python
words = ["apple", "banana", "kiwi", "mango"]
for word in words:
    if len(word) < 5:
        continue
    print(word)
```
**Output:**
```
apple
banana
mango
```

---

### 3.4.3 PASS Statement

**Purpose**: Does nothing (placeholder)

**Syntax:**
```python
for/while loop:
    pass
```

**Example 1: Empty Loop**
```python
for i in range(5):
    pass  # Will implement later
```

---

**Example 2: Conditional PASS**
```python
for i in range(1, 11):
    if i % 2 == 0:
        pass  # Even numbers - do nothing
    else:
        print(i)
```
**Output:**
```
1
3
5
7
9
```

---

### 3.4.4 ELSE with Loops

**Purpose**: Executes when loop completes normally (not via break)

**Syntax:**
```python
for/while loop:
    code
else:
    code_after_loop
```

**Example 1: FOR with ELSE**
```python
for i in range(1, 6):
    print(i)
else:
    print("Loop completed")
```
**Output:**
```
1
2
3
4
5
Loop completed
```

---

**Example 2: ELSE Not Executed (BREAK)**
```python
for i in range(1, 6):
    if i == 3:
        break
    print(i)
else:
    print("Loop completed")
```
**Output:**
```
1
2
```
*Note: ELSE doesn't execute because of break*

---

**Example 3: Search with ELSE**
```python
numbers = [10, 20, 30, 40]
search = 50

for num in numbers:
    if num == search:
        print("Found!")
        break
else:
    print("Not found")
```
**Output:**
```
Not found
```

---

**Example 4: Prime Number Check**
```python
num = 17
for i in range(2, num):
    if num % i == 0:
        print("Not prime")
        break
else:
    print("Prime number")
```
**Output:**
```
Prime number
```

---

## **4. Use Cases & When to Use**

---

## 4.1 Conditional Statements Use Cases

### **Simple IF** - Use When:
✅ You only need action for one condition
✅ No alternative action needed

**Real-World Examples:**
- Check if user is logged in before showing profile
- Verify age before granting access
- Check if file exists before opening
- Validate form input

```python
# Example: Send notification only if new messages
if new_messages > 0:
    send_notification()
```

---

### **IF-ELSE** - Use When:
✅ You have **two possible outcomes**
✅ Need action for both True and False cases

**Real-World Examples:**
- Login success/failure
- Even/odd number check
- Pass/fail determination
- On/off toggle

```python
# Example: Eligibility check
if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible")
```

---

### **IF-ELIF-ELSE** - Use When:
✅ You have **multiple conditions** to check
✅ Need different actions for different ranges
✅ Only **one condition** should execute

**Real-World Examples:**
- Grade calculation (A, B, C, D, F)
- Traffic light system (Red, Yellow, Green)
- Pricing tiers (Basic, Pro, Enterprise)
- Weather conditions

```python
# Example: Shipping cost calculator
if weight <= 1:
    cost = 5
elif weight <= 5:
    cost = 10
elif weight <= 10:
    cost = 15
else:
    cost = 20
```

---

### **Nested IF** - Use When:
✅ Condition depends on **another condition**
✅ Need **multi-level validation**
✅ Complex decision trees

**Real-World Examples:**
- Multi-factor authentication
- Loan approval (age → income → credit score)
- Access control (user type → permissions → resource)
- Game logic (level → score → achievement)

```python
# Example: Movie ticket pricing
if age < 18:
    if is_student:
        price = 5
    else:
        price = 7
else:
    if is_senior:
        price = 6
    else:
        price = 10
```

---

## 4.2 Loop Use Cases

### **FOR Loop** - Use When:
✅ You know **how many times** to iterate
✅ Iterating over a **sequence** (list, string, range)
✅ Processing each **element** in collection

**Real-World Examples:**
- Processing all files in a folder
- Displaying all products in shopping cart
- Sending emails to all subscribers
- Calculating total from list of prices
- Generating reports for each department

```python
# Example: Process all orders
orders = get_all_orders()
for order in orders:
    process_order(order)
    send_confirmation(order.customer)
```

---

### **WHILE Loop** - Use When:
✅ You **don't know** how many iterations needed
✅ Loop depends on **dynamic condition**
✅ Need to **wait** for something to happen
✅ User input validation

**Real-World Examples:**
- Password retry (until correct)
- Game loop (until game over)
- Reading file (until end)
- Server listening (until shutdown)
- Menu systems

```python
# Example: ATM withdrawal with attempts
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    pin = input("Enter PIN: ")
    if verify_pin(pin):
        process_withdrawal()
        break
    attempts += 1
else:
    lock_account()
```

---

### **Nested Loops** - Use When:
✅ Working with **multi-dimensional data** (matrices, tables)
✅ Need to compare **every item with every other item**
✅ Generating **combinations/permutations**
✅ Pattern printing

**Real-World Examples:**
- Processing spreadsheet (rows and columns)
- Comparing all users with all posts
- Generating seating arrangements
- Chess board analysis
- Product comparison matrix

```python
# Example: Find duplicate emails
users = get_all_users()
for i, user1 in enumerate(users):
    for j, user2 in enumerate(users):
        if i != j and user1.email == user2.email:
            flag_duplicate(user1, user2)
```

---

## 4.3 Real-World Scenarios

### Scenario 1: E-Commerce Discount System
```python
# Customer cart checkout
cart_total = 150
customer_type = "premium"
is_first_purchase = False

if customer_type == "premium":
    discount = 0.20
    if cart_total > 100:
        discount += 0.05  # Additional discount
elif customer_type == "regular":
    if is_first_purchase:
        discount = 0.15
    else:
        discount = 0.10
else:
    discount = 0.05

final_price = cart_total * (1 - discount)
print(f"Final price: ${final_price}")
```

---

### Scenario 2: Student Attendance System
```python
# Calculate attendance percentage
students = ["Alice", "Bob", "Charlie", "David"]
attendance = {
    "Alice": [1, 1, 0, 1, 1],  # 1=present, 0=absent
    "Bob": [1, 1, 1, 1, 1],
    "Charlie": [1, 0, 1, 0, 1],
    "David": [0, 0, 1, 1, 0]
}

for student in students:
    total_days = len(attendance[student])
    present_days = sum(attendance[student])
    percentage = (present_days / total_days) * 100
    
    if percentage >= 75:
        print(f"{student}: {percentage}% - Eligible for exam")
    else:
        print(f"{student}: {percentage}% - Not eligible")
```

---

### Scenario 3: Password Strength Checker
```python
password = input("Create password: ")

has_upper = False
has_lower = False
has_digit = False
has_special = False

for char in password:
    if char.isupper():
        has_upper = True
    elif char.islower():
        has_lower = True
    elif char.isdigit():
        has_digit = True
    elif char in "!@#$%^&*":
        has_special = True

if len(password) >= 8:
    if has_upper and has_lower and has_digit and has_special:
        print("Strong password")
    elif has_upper and has_lower and has_digit:
        print("Medium password")
else:
        print("Weak password")
else:
    print("Password too short")
```

---

### Scenario 4: Restaurant Order System
```python
menu = {
    "burger": 5.99,
    "pizza": 8.99,
    "salad": 4.99,
    "drink": 1.99
}

order_items = []
total = 0

while True:
    print("\n--- MENU ---")
    for item, price in menu.items():
        print(f"{item}: ${price}")
    
    choice = input("\nEnter item (or 'done' to finish): ").lower()
    
    if choice == "done":
        break
    
    if choice in menu:
        order_items.append(choice)
        total += menu[choice]
        print(f"Added {choice}")
    else:
        print("Item not found")

print("\n--- ORDER SUMMARY ---")
for item in order_items:
    print(f"{item}: ${menu[item]}")
print(f"Total: ${total:.2f}")
```

---

### Scenario 5: Data Cleaning System
```python
# Clean and validate user data
users_data = [
    {"name": "john", "age": 25, "email": "john@email.com"},
    {"name": "ALICE", "age": -5, "email": "invalid"},
    {"name": "bob", "age": 150, "email": "bob@email.com"},
    {"name": "", "age": 30, "email": "test@email.com"}
]

cleaned_users = []

for user in users_data:
    # Validate and clean
    is_valid = True
    
    # Check name
    if not user["name"] or len(user["name"]) < 2:
        print(f"Invalid name: {user['name']}")
        is_valid = False
    else:
        user["name"] = user["name"].capitalize()
    
    # Check age
    if user["age"] < 0 or user["age"] > 120:
        print(f"Invalid age: {user['age']}")
        is_valid = False
    
    # Check email
    if "@" not in user["email"] or "." not in user["email"]:
        print(f"Invalid email: {user['email']}")
        is_valid = False
    
    if is_valid:
        cleaned_users.append(user)

print(f"\nCleaned {len(cleaned_users)} out of {len(users_data)} users")
```

---

## 4.4 Best Practices

### ✅ DO's:

1. **Use Meaningful Variable Names**
```python
# Good
for student in students:
    print(student.name)

# Bad
for s in st:
    print(s.n)
```

2. **Keep It Simple**
```python
# Good
if age >= 18:
    print("Adult")

# Avoid unnecessary complexity
if age >= 18 and age < 150:
    if True:
        if age != None:
            print("Adult")
```

3. **Use ELIF Instead of Multiple IFs**
```python
# Good - Only one condition executes
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"

# Bad - All conditions check (slower)
if score >= 90:
    grade = "A"
if score >= 80:
    grade = "B"
if score >= 70:
    grade = "C"
```

4. **Avoid Deep Nesting**
```python
# Good - Early return/continue
for item in items:
    if not item.is_valid:
        continue
    process(item)

# Bad - Deep nesting
for item in items:
    if item.is_valid:
        if item.has_permission:
            if item.is_active:
                process(item)
```

5. **Use BREAK/CONTINUE Wisely**
```python
# Good - Exit early when found
for user in users:
    if user.id == search_id:
        found_user = user
        break

# Bad - Check all even after finding
found_user = None
for user in users:
    if user.id == search_id:
        found_user = user
```

---

### ❌ DON'Ts:

1. **Don't Use `==True` or `==False`**
```python
# Good
if is_logged_in:
    show_profile()

# Bad
if is_logged_in == True:
    show_profile()
```

2. **Don't Modify List While Iterating**
```python
# Bad - Can cause issues
for item in my_list:
    if condition:
        my_list.remove(item)

# Good - Use list comprehension
my_list = [item for item in my_list if not condition]
```

3. **Don't Forget to Update Loop Variable in WHILE**
```python
# Bad - Infinite loop
count = 0
while count < 10:
    print(count)
    # Forgot: count += 1

# Good
count = 0
while count < 10:
    print(count)
    count += 1
```

4. **Don't Use ELSE After BREAK Unless Necessary**
```python
# Usually not needed
for item in items:
    if item == target:
        print("Found")
        break
else:
    print("Not found")

# Simpler
found = False
for item in items:
    if item == target:
        found = True
        break
if not found:
    print("Not found")
```

---

## **Summary Cheat Sheet**

| Control Structure | Best For | Syntax |
|-------------------|----------|--------|
| **Simple IF** | Single condition check | `if condition:` |
| **IF-ELSE** | Two outcomes | `if: ... else:` |
| **IF-ELIF-ELSE** | Multiple conditions | `if: ... elif: ... else:` |
| **Nested IF** | Dependent conditions | `if: ... if: ...` |
| **FOR Loop** | Known iterations | `for i in sequence:` |
| **WHILE Loop** | Unknown iterations | `while condition:` |
| **Nested Loop** | Multi-dimensional data | `for: ... for: ...` |
| **BREAK** | Exit loop early | `break` |
| **CONTINUE** | Skip iteration | `continue` |
| **PASS** | Placeholder | `pass` |


---


## 🛠️ Python Loop Helpers: The Complete Cheat Sheet

### 1. `range()` — The Counter

Used when you need to repeat an action a specific number of times or need access to numeric indices.

* **Syntax:** `range(start, stop, step)`
* **Example:**
```python
# Loops from 0 to 4
for i in range(5):
    print(i)

```



### 2. `enumerate()` — The Indexer

The best way to loop through a collection when you need **both** the index (position) and the value.

* **Why use it:** Avoids the clunky `range(len(list))` pattern.
* **Example:**
```python
fruits = ["Apple", "Banana", "Cherry"]
for index, fruit in enumerate(fruits, start=1):
    print(f"#{index}: {fruit}")
# Output: #1: Apple, #2: Banana...

```



### 3. `zip()` — The Combiner

Used to loop through **two or more lists at the same time** in parallel. It stops as soon as the shortest list is exhausted.

* **Example:**
```python
names = ["Alice", "Bob"]
scores = [85, 92]
for name, score in zip(names, scores):
    print(f"{name} scored {score}")

```



### 4. `reversed()` — The Backtracker

Loops through a sequence in reverse order without modifying the original collection.

* **Example:**
```python
for item in reversed([1, 2, 3]):
    print(item) # 3, 2, 1

```



### 5. `sorted()` — The Organizer

Loops through a collection in a specific order (alphabetical or numerical) without changing the original list.

* **Example:**
```python
nums = [5, 1, 8]
for n in sorted(nums):
    print(n) # 1, 5, 8

```



---

## 💡 Collection-Specific Looping Patterns

### Dictionaries: Keys, Values, and Items


| Method | What it returns | Example Usage |
| --- | --- | --- |
| `.keys()` | Just the keys | `for k in dict.keys():` |
| `.values()` | Just the values | `for v in dict.values():` |
| **`.items()`** | **Both (Key & Value)** | `for k, v in dict.items():` |

> **Pro Tip:** Always use `.items()` when you need both the key and value; it's much faster and cleaner than looking up the value manually inside the loop.

---

## 🚀 Quick Reference Comparison

| If you want to... | Use this... |
| --- | --- |
| Access the **index** and the **item** | `enumerate(list)` |
| Loop through **multiple lists** together | `zip(list1, list2)` |
| Loop in **reverse** | `reversed(list)` |
| Loop in **alphabetical/numerical** order | `sorted(list)` |
| Loop a **fixed number** of times | `range(n)` |

---
