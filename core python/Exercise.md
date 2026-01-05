
# Python Basics to Advanced – Rules + Examples (Well Organized Notes)
---

## 🔰 PART 1: IMPORTANT PYTHON RULES (READ FIRST)

### 1. `print()` Function Rules

* `print()` can print **multiple values** separated by commas.
* By default, values are separated by **space**.
* `sep` parameter changes the separator.
* `\n` moves output to a **new line**.

---

### 2. `input()` Function Rules

* `input()` **ALWAYS returns a string**, even if user enters a number.
* To use numbers, you **must typecast**:

  * `int(input())`
  * `float(input())`

---

### 3. f-String Rules (`f"..."`)

* Used for **dynamic variable insertion**.
* Variables are written inside `{}`.
* Faster and cleaner than `+` concatenation.

Example:

```python
age = 25
print(f"My age is {age}")
```

---

### 4. Type Conversion (Type Casting)

* `int("10")` → converts string to integer
* `float("2.5")` → converts string to float
* `str(100)` → converts number to string

---

### 5. Mathematical Rules

* `**` → power (square, cube)
* `%` → remainder
* `*` → multiplication
* String × number → repetition
* Float × string ❌ (error)

---

### 6. Multiple Assignment Rules

* Assign multiple values in one line:

```python
x, y, z = 5, 10, 15
```

---

### 7. Python Swapping Rule (No Temp Variable)

```python
a, b = b, a
```

---

## 🔰 PART 2: BEGINNER LEVEL EXAMPLES

---

### Printing Multiple Variables on New Lines

```python
x, y, z = 5, 10, 15
print(x, y, z, sep='\n')
```

OR

```python
print(x, "\n", y, "\n", z)
```

---

### Printing Names

```python
fname, lname = "Saroj", "kali"
print(fname, lname)
```

---

### Custom Separator Using `sep`

```python
a = 10
b = 20
c = 30
print(a, b, c, sep='|')
```

---

### Same Output Using f-String

```python
print(f"{a}|{b}|{c}")
```

---

### Same Output Using `join()`

```python
values = [str(a), str(b), str(c)]
print("|".join(values))
```

📌 **Rule:** `join()` works only with **strings**

---

## 🔰 PART 3: INTERMEDIATE CONCEPTS

---

### Swapping Two Numbers

```python
a, b = 10, 20
a, b = b, a
print(f'num is {a} and {b}')
```

---

### Multiplying Float with String (Type Conversion)

```python
a = 4.3
b = '2'
# print(a * b) ❌ Error
print(a * int(b))  # 8.6
```

---

### Boolean Check and Type

```python
x = True
if x is True:
    print(type(x))
```

---

### Taking Age Input and Calculating Years Left

```python
age = int(input("Enter your age "))
print(f"your age is {age} and remaining {100-age} to reach 100")
```

---

## 🔰 PART 4: USER INPUT PRACTICE

---

### Add Two Float Numbers from User

```python
a = float(input("Enter float no 1 "))
b = float(input("Enter float no 2 "))
print(a + b)
```

---

### Convert String Input to Integer and Add

```python
num = input("Enter a number:")
sum = 10 + int(num)
print(f"Sum is {sum}")
```

---

### Ask First and Last Name

```python
fname = input("Enter your first name ")
lname = input("Enter your last name ")
print(f"Your full name is {fname} {lname}")
```

---

## 🔰 PART 5: MATHEMATICAL OPERATIONS

---

### Square Using `**`

```python
radius = float(input("Enter radius "))
area = 3.14 * radius**2
print(f"Area of circle is {area} cm2")
```

---

### Find Remainder

```python
num1 = 17
num2 = 4
print(f"Remainder when {num1} is divided by {num2} is {num1 % num2}")
```

---

### Multiply Float and Convert to Integer

```python
floatnum = 22.34
print(f"Multiply {floatnum} by 100 is {int(floatnum * 100)}")
```

---

## 🔰 PART 6: BASIC SET OPERATIONS (ADVANCED BASIC)

```python
A = {1, 2, 3}
B = {3, 4, 5}

print(A.union(B))        # Union
print(A.intersection(B)) # Intersection
print(A - B)             # Difference
```

---
