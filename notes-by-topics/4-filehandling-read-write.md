
# 📂 File Handling in Python 
## Level: I
---

## 1. What is File Handling?

**File Handling** in Python allows you to:

* Read data from files
* Write data to files
* Store data permanently
* Work with large datasets (logs, CSVs, reports, etc.)

Python provides **built-in functions and libraries** to work with files easily.

---

## 2. Why File Handling is Important?

* Data persistence (data stays even after program ends)
* Efficient handling of large data
* Reading configuration files
* Working with real-world formats (CSV, Excel, PDF)

---

## 3. Steps in File Handling

1. Open a file
2. Read / Write / Append
3. Close the file

---

## 4. Opening a File

To perform any operation on a file, it must be opened using `open()`.

### Syntax

```python
file_object = open('filename', 'mode')
```

### Parameters

* **filename** → File name or full path (string, inside quotes)
* **mode** → Operation mode (read, write, append, etc.)

> If the file is in a subfolder or another directory, provide the **full path**.

---

## 5. File Modes

| Mode | Meaning                                                |
| ---- | ------------------------------------------------------ |
| `r`  | Read only (file must exist)                            |
| `w`  | Write (overwrites content, creates file if not exists) |
| `a`  | Append (adds data at end, creates file if not exists)  |
| `r+` | Read and write (file must exist)                       |
| `rb` | Read binary (images, pdf, audio)                       |
| `wb` | Write binary                                           |

---

### Difference Between `w` and `a`

* **`w`** → Deletes old content and rewrites
* **`a`** → Adds content after existing data

---

### When to Use `rb` / `wb`?

Used for **non-text files**, such as:

* Images
* PDFs
* Audio / Video

---

## 6. Reading from a File (FIRST)

### Read Mode

* `r` → Read only

---

### 6.1 `read()` – Read Entire File

* Reads complete file at once
* Returns a single string
* Best for small files

```python
file = open('example.txt', 'r')
content = file.read()
print(content)
file.close()
```

---

### 6.2 `readline()` – Read One Line

* Reads **first line only**
* Each call reads the next line

```python
file = open('example.txt', 'r')
line1 = file.readline()
line2 = file.readline()
print(line1)
print(line2)
file.close()
```

---

### 6.3 `readlines()` – Read All Lines

* Reads all lines
* Returns a list
* Each line is a separate element

```python
file = open('example.txt', 'r')
lines = file.readlines()
print(lines)
file.close()
```

#### Output Format

```python
['First line\n', 'Second line\n', 'Third line']
```

---

## 7. Writing to a File

### Write Mode

* `w` → Write (overwrites content)

### Write Example (Overwrite)

```python
file = open('example.txt', 'w')
file.write("Hello, world!")
file.close()
```

---

### Writing in New Line using `\n`

```python
file = open('test.txt', 'w')
file.write("First line\n")
file.write("Second line")
file.close()
```

---

## 8. Creating a New File

If file does not exist, `w` or `a` mode creates it automatically.

```python
file = open('example1.txt', 'w')
file.write("namesat")
file.close()
```

---

## 9. Appending to a File

### Append Mode

* `a` → Adds content at end

```python
file = open('example.txt', 'a')
file.write("\nThis is an appended line.")
file.close()
```

---

## 10. Read and Write Mode (`r+`)

* Allows reading and writing
* File must exist
* Cursor starts at beginning

```python
file = open('example.txt', 'r+')
print(file.read())
file.write("\nAdded using r+")
file.close()
```

---

## 11. Using `with` Statement (Best Practice) [Context Manager: with]
Instead of manually closing files, use `with`. It automatically closes the file.
syntax:
```python
with open('<filename>', '<mode>') as file:
    # file operations
```

```python
with open('example1.txt', 'r') as file:
    content = file.read()
    print(content)
```

✔ No need to call `close()`
✔ Cleaner and safer

---

## 12. Closing a File

```python
file.close()
```

### Why Close Files?

* Prevents memory leaks
* Ensures data is saved

---

## 13. Working with Different File Formats

### CSV Files

Using `csv` module:

```python
import csv
file = open('file.csv', 'r')
reader = csv.reader(file)
for row in reader:
    print(row)
```

Using `pandas`:

```python
import pandas as pd
df = pd.read_csv('file.csv')
print(df)
```

---

### Excel Files

```python
import pandas as pd
df = pd.read_excel('file.xlsx')
```

---

### PDF Files

```python
import PyPDF2
file = open('file.pdf', 'rb')
pdf_reader = PyPDF2.PdfReader(file)
```

It looks like you're encountering an error because you're trying to use a function or a module named `import` (which is a reserved keyword) or perhaps just getting a "file not found" error.

In Python, you don't actually need to "import" anything to open a file—`open()` is a built-in function. However, if you are trying to handle files safely, there are a few best practices to follow.

## Level: II
### 1. The Standard Way (Using `with`)

The best way to open a file is using the `with` statement. This ensures the file is automatically closed after the block finishes, even if an error occurs.

```python
# No import needed for basic file reading
try:
    with open('test.txt', 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("Error: 'test.txt' was not found in this directory.")

```

### 2. If you need the `os` or `pathlib` module

If you are trying to check if a file exists before opening it, or if you need to work with specific file paths, you should import `os` or `pathlib`.

```python
import os

if os.path.exists('test.txt'):
    file = open('test.txt', 'r')
    # Do something
    file.close() # Remember to close it manually if not using 'with'
else:
    print("File does not exist.")

```

# Python File Handling Interview Questions (Beginner to Advanced)
   **Sample Answer**:  
   - `'r'` – read (default)  
   - `'w'` – write (truncates file if exists)  
   - `'a'` – append  
   - `'x'` – exclusive creation (fails if file exists)  
   - `'+'` – read + write  
   - `'b'` – binary mode  
   - `'t'` – text mode (default)  
   Example: `open('file.txt', 'rb')` opens in read-binary mode.

2. **How do you open and read a file in Python?**  
   **Concepts**: `open()`, `read()`, `close()`.  
   **Sample Answer**:  
   ```python
   file = open('example.txt', 'r')
   content = file.read()
   file.close()
   ```
   Better to use context manager (see next question).

3. **Why should you use the `with` statement when working with files?**  
   **Concepts**: Context manager, automatic cleanup.  
   **Sample Answer**: The `with` statement ensures the file is properly closed even if an exception occurs.  
   ```python
   with open('example.txt', 'r') as file:
       content = file.read()
   # file is automatically closed here
   ```

4. **What is the difference between `read()`, `readline()`, and `readlines()`?**  
   **Concepts**: Reading methods.  
   **Sample Answer**:  
   - `read()` → entire file as single string  
   - `readline()` → one line as string  
   - `readlines()` → list of all lines

5. **How do you write to a file in Python?**  
   **Concepts**: Write modes.  
   **Sample Answer**:  
   ```python
   with open('output.txt', 'w') as f:
       f.write('Hello\n')
       f.writelines(['Line 2\n', 'Line 3'])
   ```

### Medium Level (Common Practical Questions)

6. **What happens if you open a file in `'w'` mode that already exists?**  
   **Answer**: The file is truncated (emptied). Use `'a'` to append instead.

7. **How do you append data to an existing file without overwriting it?**  
   **Answer**: Use `'a'` mode.

8. **Explain the difference between text mode and binary mode.**  
   **Concepts**: Encoding, newlines.  
   **Sample Answer**: Text mode handles encoding/decoding and translates platform-specific newlines (`\n`). Binary mode reads/writes raw bytes (useful for images, executables).

9. **How do you move the file pointer to a specific position?**  
   **Concepts**: `seek()`, `tell()`.  
   **Sample Answer**:  
   ```python
   with open('file.txt', 'r') as f:
       f.seek(10)      # move to 10th byte
       print(f.tell()) # current position
   ```

10. **How would you read a large file efficiently without loading it all into memory?**  
    **Concepts**: Iteration, buffering.  
    **Sample Answer**: Iterate line by line:  
    ```python
    with open('large.txt', 'r') as f:
        for line in f:
            process(line)
    ```

11. **How do you handle file-related exceptions?**  
    **Concepts**: `FileNotFoundError`, `PermissionError`, `IOError`.  
    **Sample Answer**:  
    ```python
    try:
        with open('missing.txt', 'r') as f:
            print(f.read())
    except FileNotFoundError:
        print("File does not exist")
    except PermissionError:
        print("Permission denied")
    ```

12. **How do you check if a file exists before opening it?**  
    **Concepts**: `os.path` or `pathlib`.  
    **Sample Answer**:  
    ```python
    from pathlib import Path
    if Path('file.txt').exists():
        # open file
    ```

13. **What is the difference between `write()` and `writelines()`?**  
    **Answer**: `write()` takes a single string. `writelines()` takes an iterable of strings (doesn't add newlines automatically).

### Advanced Level (Deeper Understanding)

14. **How do you work with CSV files in Python?**  
    **Concepts**: `csv` module.  
    **Sample Answer**:  
    ```python
    import csv
    with open('data.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            print(row['name'])
    ```

15. **How do you write JSON data to a file?**  
    **Concepts**: `json` module.  
    **Sample Answer**:  
    ```python
    import json
    data = {'name': 'Saroj', 'age': 30}
    with open('data.json', 'w') as f:
        json.dump(data, f, indent=4)
    ```

16. **What is buffering in file operations? How can you control it?**  
    **Concepts**: Buffering modes.  
    **Sample Answer**: Python buffers output for performance. Use `flush()` or open with `buffering=0` (unbuffered) or `buffering=1` (line buffering in text mode).

17. **How do you copy a file in Python?**  
    **Sample Answer**: Using `shutil`:  
    ```python
    import shutil
    shutil.copy('src.txt', 'dst.txt')
    ```

18. **Explain how to create a custom context manager for file handling.**  
    **Concepts**: `__enter__`, `__exit__`.  
    **Sample Answer**: Useful for understanding `with` under the hood.

19. **What is the difference between `Path.read_text()` and `open()` from pathlib?**  
    **Answer**: `pathlib` provides a modern, object-oriented way:  
    ```python
    from pathlib import Path
    content = Path('file.txt').read_text()
    ```

20. **How do you handle large binary files (e.g., images)?**  
    **Answer**: Use binary mode and read in chunks:  
    ```python
    with open('image.jpg', 'rb') as f:
        while chunk := f.read(8192):
            process(chunk)
    ```

### Bonus Tricky Questions

21. **What happens if you forget to close a file?**  
    **Answer**: Resources may leak, especially in long-running programs. Context manager prevents this.

22. **Can you open multiple files in a single `with` statement?**  
    **Answer**: Yes (Python 3+):  
    ```python
    with open('in.txt') as fin, open('out.txt', 'w') as fout:
        fout.write(fin.read())
    ```

23. **How do you get the file size without reading it?**  
    **Answer**: `os.path.getsize('file.txt')` or `Path('file.txt').stat().st_size`

24. **What is the difference between `'r+'` and `'w+'` modes?**  
    **Answer**: `'r+'` – read/write but fails if file doesn't exist. `'w+'` – read/write but truncates/creates file.

25. **How would you safely read a file that might be corrupted or incomplete?**  
    **Answer**: Use try/except around read operations, read in chunks, validate data.


---

