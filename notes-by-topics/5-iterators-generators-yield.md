# Python Iterators and Generators – Comprehensive Notes

## 1. Iterators

### What is an Iterator?
- An **iterator** is an object that allows you to traverse a container (like a list, tuple, etc.) one element at a time. Remembers its **current position** and returns **one value at a time**, not all at once.
  
- It implements the **iterator** by using two methods:
  - 1. `__iter__()` → must return the iterator object itself.
  - 2. `__next__()` → returns the next value in the sequence. When there are no more items, it raises `StopIteration`.

### Built-in Iterators (Example with List)
```python
nums = [7, 6, 4, 6, 7, 11]

it = iter(nums)                # Convert iterable to iterator
print(it)                      # <list_iterator object at 0x...>

print(next(it))                # 7   (or it.__next__())
print(next(it))                # 6   (state is preserved, Remember previous iterator)
print(next(it))                # 4
print(next(it))                # 6
print(next(it))                # 7
print(next(it))                # 11
print(next(it))                # Raises StopIteration
```

* `iter(nums)` converts the list into an **iterator**
* `__next__()` gives the **next value**
* Iterator **preserves state** (it remembers where it stopped)
* When values are exhausted → `StopIteration` is raised

### How `for` Loop Works Internally ?
```python
for i in nums:
    print(i)
```
- The `for` loop does this automatically:
  1. Calls `iter(nums)` to get an iterator.
  2. Repeatedly calls `next()` on the iterator.
  3. Stops when `StopIteration` is raised.
- You don’t have to call `__next__()` manually — the loop handles it.

### Creating Your Own Iterator (Class-Based)
To create your own iterator, you **must implement**:

1. `__iter__()`
2. `__next__()`

### Example: Custom Iterator (TopTen)
```python
class TopTen:
    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self                    # Return the iterator object

    def __next__(self):
        if self.num <= 10:
            val = self.num
            self.num += 1
            return val
        else:
            raise StopIteration        # Signal end of iteration
```
**Using It (above class TopTen usage with for loop)**
```python
values = TopTen()

for i in values:                   # for loop works automatically
    print(i)                       # Prints 1 to 10
```
**Output:**

```
1
2
3
...
10
```
- Dunder methods used: `__iter__` and `__next__`.

## 2. Generators

### What is a Generator?
- A **generator** is a special kind of iterator that is written as a function using the `yield` keyword. Which is used to create an iterators.
* Uses the keyword `yield`
* Automatically implements `__iter__()` and `__next__()`
* Returns values **one at a time**
* Saves memory (lazy execution)
### Simple Generator
```python
def topten():
    yield 1
    yield 2
    yield 3
    yield 4

values = topten()                   # Returns a generator object
print(values)                      # <generator object topten at 0x...>

for i in values:                   # Prints 1, 2, 3, 4
    print(i)
```

### Why Does the `for` Loop Get All Values?
- The generator object implements `__iter__` and `__next__` automatically.
- When you write `for i in values:`, Python:
  1. Calls `iter(values)` (returns the generator itself).
  2. Calls `next()` repeatedly.
  3. Each `yield` pauses the function, returns a value, and remembers the exact state (variables, position).
  4. When the function ends or no more `yield`, it raises `StopIteration`.

### More Realistic Generator Example
```python
def topten_squares():
    n = 1
    while n <= 10:
        sq = n * n
        yield sq               # Produce one value, pause here
        n += 1

values = topten_squares()

for i in values:
    print(i)                   # 1, 4, 9, 16, ..., 100
```

### What Does `yield` Do?
- `yield` is like `return`, but:
  - It returns a value **and pauses** the function.
  - The function resumes from the same point on the next `next()` call.
  - It does **not** terminate the function (unlike `return`).
- The generator remembers local variables and execution point between yields.

### Manual Iteration on Generator (Using `__next__`)
```python
values = topten_squares()
print(next(values))   # 1
print(next(values))   # 4
print(next(values))   # 9
# ... continues until StopIteration
```

## 3. Key Differences: Iterators vs Generators

| Feature                  | Class-Based Iterator                     | Generator (yield)                          |
|--------------------------|------------------------------------------|--------------------------------------------|
| Definition               | Class with `__iter__` and `__next__`     | Function with `yield`                      |
| Memory Usage             | Stores all data if needed                | Lazy – produces one item at a time          |
| State Management         | Manual (instance variables)              | Automatic (remembers local variables)      |
| Ease of Writing          | More code, explicit `StopIteration`      | Simpler, cleaner syntax                    |
| Reusability              | Can be reused if reset logic added       | One-time use (exhausted after iteration)   |
| Common Use               | Custom complex traversal logic           | Large/infinite sequences, data streams     |

## 4. Real-World Use Cases

### Iterators (Class-Based)
- Custom data structures (e.g., tree traversal, linked list).
- When you need full control over iteration behavior (reverse, filtering, etc.).

### Generators (yield)
- Processing large files line-by-line (without loading everything into memory).
- Infinite sequences (e.g., Fibonacci numbers).
- Data pipelines / streaming (e.g., reading from API, database cursors).
- Memory efficiency: generating millions of values without storing them all.

**Example: Reading Large File Lazily**
```python
def read_lines(file_path):
    with open(file_path) as f:
        for line in f:          # f is iterable, internally uses iterator
            yield line.strip()

for line in read_lines('huge_file.txt'):
    process(line)               # Only one line in memory at a time
```
