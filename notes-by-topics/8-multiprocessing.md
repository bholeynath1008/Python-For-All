
# 🚀 Multiprocessing in Python – Complete Notes
ref: [reference youtube](https://www.youtube.com/watch?v=zGe-9LfnAaA)
Content: 
1. Basic Information

---

## 0️⃣ Tutorial Overview

* **Multiprocessing** is a Python module used to run multiple processes **in parallel**.
* Each process has its **own memory space**.
* It is best suited for **CPU-bound tasks** and also works well for heavy I/O tasks.
* It allows Python programs to utilize **multiple CPU cores**, bypassing the **Global Interpreter Lock (GIL)**.

---

## 1️⃣ What is Multiprocessing?

**Multiprocessing** allows you to execute multiple independent processes at the same time.

### Why Multiprocessing?

* Uses **multiple CPU cores**
* Faster execution for CPU-intensive tasks
* True parallelism (unlike threading in Python)

### Difference from Multithreading

| Feature  | Multithreading | Multiprocessing |
| -------- | -------------- | --------------- |
| Memory   | Shared         | Separate        |
| GIL      | Affected       | Not affected    |
| Best for | I/O bound      | CPU bound       |
| Overhead | Low            | Higher          |

---

## 2️⃣ Importing Multiprocessing

```python
import multiprocessing
```

This module provides:

* `Process`
* `Queue`
* `Pool`
* `current_process()`
* `cpu_count()`

---

## 3️⃣ Basic Syntax of Multiprocessing

### Steps to create a process

1. Define a function
2. Create a `Process` object
3. Call `start()`
4. Call `join()`

---

### Example: Creating a Simple Process

```python
import multiprocessing

def my_func():
    print("Hello from process", multiprocessing.current_process().name)

if __name__ == "__main__":
    p = multiprocessing.Process(target=my_func)
    p.start()
    p.join()
```

### Important:

* `start()` → starts the process
* `join()` → waits for the process to finish
* `current_process()` → gives process details

---

## 4️⃣ Case I – Normal Sequential Execution (No Multiprocessing)

```python
import multiprocessing, requests

url = "https://picsum.photos/200/3000"

def downloadFile(url, name):
    response = requests.get(url)
    open(f"{name}.jpg", "wb").write(response.content)

for i in range(5):
    downloadFile(url, i)
```

### 🔍 What happens here?

* Files are downloaded **one after another**
* Each download **waits** for the previous one to finish
* Uses **only one CPU core**
* Execution is **slow**

### 📌 Execution Flow

```
Download 0 → Done
Download 1 → Done
Download 2 → Done
...
```

This is **synchronous / blocking execution**.

---

## 5️⃣ Case II – Using Multiprocessing (Your Example Explained)

```python
import multiprocessing, requests

url = "https://picsum.photos/200/3000"

def downloadFile(url, name):
    response = requests.get(url)
    open(f"{name}.jpg", "wb").write(response.content)
    print(f"finish downloading {name}")

pros = []

for i in range(5):
    downloadFile(url, i)   # ❌ sequential call
    p = multiprocessing.Process(target=downloadFile, args=[url, i])
    p.start()
    pros.append(p)

for p in pros:
    p.join()
```

---

### ⚠️ What is happening here?

You are doing **BOTH sequential and multiprocessing execution**.

### Breakdown:

#### ❌ This line:

```python
downloadFile(url, i)
```

* Executes **normally**
* Blocks execution
* Downloads file **sequentially**

#### ✅ This part:

```python
p = multiprocessing.Process(target=downloadFile, args=[url, i])
p.start()
```

* Creates a **new process**
* Runs in parallel

### ❗ Result:

Each file is downloaded **TWICE**

1. Once sequentially
2. Once via multiprocessing

---

## 6️⃣ Correct Multiprocessing Version (Fixed)

```python
import multiprocessing, requests

url = "https://picsum.photos/200/3000"

def downloadFile(url, name):
    response = requests.get(url)
    open(f"{name}.jpg", "wb").write(response.content)
    print(f"finish downloading {name}")

if __name__ == "__main__":
    pros = []

    for i in range(5):
        p = multiprocessing.Process(target=downloadFile, args=(url, i))
        p.start()
        pros.append(p)

    for p in pros:
        p.join()
```

---

## 7️⃣ Why `join()` is Important?

```python
p.join()
```

* Makes the **main program wait**
* Ensures all processes finish before exiting
* Prevents incomplete execution

Without `join()`:

* Program may exit early
* Files may not download fully

---

## 8️⃣ Why `if __name__ == "__main__":` is Required?

* Prevents **infinite child process creation**
* Mandatory on **Windows**
* Makes the script:

  * Reusable
  * Standalone
  * Safe for multiprocessing

---

## 9️⃣ CPU Count

```python
import multiprocessing
print(multiprocessing.cpu_count())
```

Returns number of CPU cores available.

---

## 🔟 When to Use Multiprocessing?

✅ Use when:

* CPU-bound tasks
* Image processing
* Data analysis
* File processing
* Heavy computations

❌ Avoid when:

* Simple scripts
* Lightweight tasks
* Shared memory is required

---

## 🔚 Summary

* Multiprocessing runs tasks **in parallel**
* Uses multiple CPU cores
* Avoid calling functions **outside** the process
* Always use `start()` + `join()`
* Use `if __name__ == "__main__"`

---
