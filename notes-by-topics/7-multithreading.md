
# 🧵 Multithreading in Python – Complete Beginner Notes
Content: 
1. Basic concept multi threading
2. Multithreading in Python: Downloading Images Advance
3. Interview questions
---

## 1️⃣ What is Multithreading?

**Multithreading** is a programming technique where **multiple threads run concurrently** within the **same process**.

* A **thread** is the smallest unit of execution.
* All threads **share the same memory space**.
* Useful when your program **waits a lot** (I/O operations).

### Simple definition:

> Multithreading allows a program to perform multiple tasks **at the same time** instead of waiting for one task to finish before starting another.

---
**Key Takeaways:**

`Sequential`: Tasks run one after another - total time = sum of all task times
`Threading`: Tasks run concurrently - total time ≈ longest task time
`ThreadPoolExecutor`: Like threading but with better management
Use `time.perf_counter()` for accurate timing

**When to use which:**
`Sequential`: Simple scripts, few tasks, or tasks that depend on each other
`Threading`: When you need fine control over each thread
`ThreadPoolExecutor`: Most cases! Especially for I/O tasks like downloading files

## 2️⃣ When to Use Threading?
**USE THREADING FOR:**
- Downloading multiple files/images
- Making multiple API calls
- Web scraping
- Database queries
- Any task that involves WAITING (I/O)

**DON'T USE THREADING FOR:**
- Mathematical computations
- Image processing
- Data analysis
- CPU-intensive calculations (use multiprocessing instead)

---
# THE GIL PROBLEM
Python has a Global Interpreter Lock (`GIL`) that allows only ONE thread
to execute Python bytecode at a time.

The `GIL` is a mutex (mutual exclusion lock) that protects access to Python objects, preventing multiple native threads from executing Python bytecode simultaneously. It's a single lock on the interpreter that allows only one thread to hold control of the Python interpreter at any given time.

**IMPORTANT CONSEQUENCES:**
1. For CPU-bound tasks: Threading doesn't help much (use multiprocessing)
2. For I/O-bound tasks: Threading works well (threads release GIL during I/O)

**Historical Reasons:**
1. `SIMPLICITY`: Python was created in 1991 when multi-core CPUs were rare
2. `MEMORY MANAGEMENT`: Python uses reference counting for garbage collection
   Example: obj1 = SomeObject()  # ref count = 1
            obj2 = obj1         # ref count = 2
   Without GIL, two threads could modify ref count simultaneously → corruption
3. `C EXTENSIONS:` Many Python C extensions assumed single-threaded execution


## 3️⃣ Important Concept: CPU-bound vs I/O-bound

### 🔹 I/O-bound tasks (BEST for threading)

* File operations
* Network calls
* API requests
* `time.sleep()`

✅ **Threading helps a lot**

### 🔹 CPU-bound tasks

* Heavy calculations
* Image processing
* Encryption

❌ **Threading does NOT improve performance** in Python
(due to **GIL – Global Interpreter Lock**)

> ⚠️ For CPU-bound tasks → use **multiprocessing**, not threading.

---

## 4️⃣ Time Measurement in Python

### `time.perf_counter()`

* High-resolution timer
* Best for benchmarking
* Includes sleep time

```python
start = time.perf_counter()
# code
end = time.perf_counter()
print(end - start)
```

✅ Always prefer `perf_counter()` over `time.time()` for measuring execution time.

---

## 5️⃣ Example 1: Sequential (Normal) Execution

### 📌 Theory

* Tasks run **one after another**
* Total time = **sum of all task durations**
* No concurrency

### Code (Your Example)

```python
import time

def task(seconds, task_name):
    print(f"{task_name}: Starting (will take {seconds} seconds)")
    time.sleep(seconds)
    print(f"{task_name}: Finished")
    return f"Result from {task_name}"

def sequential_execution():
    start_time = time.perf_counter()

    result1 = task(3, "Task 1")
    result2 = task(2, "Task 2")
    result3 = task(1, "Task 3")

    end_time = time.perf_counter()

    print(f"\nTotal time taken: {end_time - start_time:.2f} seconds")

sequential_execution()
```

### ⏱️ Result

```
3 + 2 + 1 = 6 seconds
```

---

## 6️⃣ Example 2: Basic Threading

### 📌 Theory

* Threads start **almost at the same time**
* Main thread continues execution
* `join()` waits for thread completion

### Key Methods

| Method     | Purpose             |
| ---------- | ------------------- |
| `Thread()` | Create thread       |
| `start()`  | Start execution     |
| `join()`   | Wait for completion |

### Code (Your Example)

```python
import threading
import time

def task(seconds, task_name):
    print(f"{task_name}: Starting")
    time.sleep(seconds)
    print(f"{task_name}: Finished")

def threading_execution():
    start_time = time.perf_counter()

    t1 = threading.Thread(target=task, args=(3, "Thread 1"))
    t2 = threading.Thread(target=task, args=(2, "Thread 2"))
    t3 = threading.Thread(target=task, args=(1, "Thread 3"))

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    end_time = time.perf_counter()
    print(f"Total time taken: {end_time - start_time:.2f} seconds")

threading_execution()
```

### ⏱️ Result

```
~3 seconds (longest task)
```

---

## 7️⃣ Example 3: ThreadPoolExecutor (BEST PRACTICE)

### 📌 Theory

`ThreadPoolExecutor`:

* Manages thread creation automatically
* Reuses threads
* Cleaner and safer than manual threading

### Key Terms

| Term       | Meaning                 |
| ---------- | ----------------------- |
| Executor   | Manages threads         |
| `submit()` | Assign task             |
| `future`   | Represents async result |
| `result()` | Wait & fetch result     |

### Code (Your Example)

```python
from concurrent.futures import ThreadPoolExecutor
import time

def task(seconds, name):
    print(f"{name}: Starting")
    time.sleep(seconds)
    print(f"{name}: Finished")
    return name

def threadexecutor_execution():
    start_time = time.perf_counter()

    with ThreadPoolExecutor(max_workers=3) as executor:
        f1 = executor.submit(task, 3, "Task 1")
        f2 = executor.submit(task, 2, "Task 2")
        f3 = executor.submit(task, 1, "Task 3")

        f1.result()
        f2.result()
        f3.result()

    end_time = time.perf_counter()
    print(f"Total time: {end_time - start_time:.2f} seconds")

threadexecutor_execution()
```

---

## 8️⃣ Example 4: All-in-One Comparison

### 📌 Theory Summary

| Method     | Execution  | Time         |
| ---------- | ---------- | ------------ |
| Sequential | One by one | Sum of all   |
| Threading  | Concurrent | Longest task |
| ThreadPool | Concurrent | Longest task |

Your comparison example is **perfect** for interviews and demos 👍
(Keep it exactly as you wrote.)

---

## 9️⃣ Example 5: Real-World Analogy (Sandwich Example)

### 📌 Concept Mapping

| Real World | Programming    |
| ---------- | -------------- |
| Person     | Thread         |
| Kitchen    | ThreadPool     |
| Sandwich   | Task           |
| Time       | Execution time |

This analogy is **excellent for beginners** and interview explanations.

---

## 🔑 Key Takeaways (VERY IMPORTANT)

1. **Sequential**

   * Simple
   * Slow for waiting tasks

2. **Threading**

   * Faster for I/O tasks
   * Manual control

3. **ThreadPoolExecutor**

   * Clean
   * Recommended
   * Scales better

4. **Python Threading ≠ True Parallelism**

   * Due to **GIL**
   * Best for **I/O-bound tasks**

---

## 🧠 When to Use What?

| Scenario                    | Use                |
| --------------------------- | ------------------ |
| Simple scripts              | Sequential         |
| Few threads, control needed | threading          |
| API calls, downloads, DB    | ThreadPoolExecutor |
| Heavy CPU work              | multiprocessing    |

---

## 📝 Interview One-Liners

* **Multithreading** improves performance for **I/O-bound tasks**.
* **GIL** prevents true parallel CPU execution.
* **ThreadPoolExecutor** is preferred over manual threading.
* `join()` ensures main thread waits.
* `perf_counter()` is best for benchmarking.

---

If you want next:

* 🔄 **Threading vs Multiprocessing**
* 🔐 **Race condition & Locks**
* ⚠️ **Common threading mistakes**
* 📦 **Async vs Threading vs Multiprocessing**


# Multithreading for Beginners: Simple Examples with Time Measurement

## **Example 1: Sequential (Normal) Execution**

```python
import time

def task(seconds, task_name):
    """Simulates a task that takes some time"""
    print(f"{task_name}: Starting (will take {seconds} seconds)")
    time.sleep(seconds)
    print(f"{task_name}: Finished")
    return f"Result from {task_name}"

# Sequential execution (one after another)
def sequential_execution():
    print("="*50)
    print("SEQUENTIAL EXECUTION")
    print("="*50)
    
    start_time = time.perf_counter()
    
    # Tasks run one after another
    result1 = task(3, "Task 1")
    result2 = task(2, "Task 2")
    result3 = task(1, "Task 3")
    
    end_time = time.perf_counter()
    
    print(f"\nResults: {result1}, {result2}, {result3}")
    print(f"Total time taken: {end_time - start_time:.2f} seconds")
    print("Note: 3+2+1 = 6 seconds (tasks run sequentially)")

# Run sequential execution
sequential_execution()
```

**Output:**
```
==================================================
SEQUENTIAL EXECUTION
==================================================
Task 1: Starting (will take 3 seconds)
Task 1: Finished
Task 2: Starting (will take 2 seconds)
Task 2: Finished
Task 3: Starting (will take 1 seconds)
Task 3: Finished

Results: Result from Task 1, Result from Task 2, Result from Task 3
Total time taken: 6.01 seconds
Note: 3+2+1 = 6 seconds (tasks run sequentially)
```

---

## **Example 2: Basic Threading**

```python
import threading
import time

def task(seconds, task_name):
    """Simulates a task that takes some time"""
    print(f"{task_name}: Starting (will take {seconds} seconds)")
    time.sleep(seconds)
    print(f"{task_name}: Finished")
    return f"Result from {task_name}"

def threading_execution():
    print("\n" + "="*50)
    print("THREADING EXECUTION")
    print("="*50)
    
    start_time = time.perf_counter()
    
    # Create threads
    t1 = threading.Thread(target=task, args=(3, "Thread 1"))
    t2 = threading.Thread(target=task, args=(2, "Thread 2"))
    t3 = threading.Thread(target=task, args=(1, "Thread 3"))
    
    # Start all threads (they run concurrently)
    t1.start()
    t2.start()
    t3.start()
    
    print("\nAll threads started! Main thread continues...")
    
    # Wait for all threads to complete
    t1.join()
    t2.join()
    t3.join()
    
    end_time = time.perf_counter()
    
    print(f"\nTotal time taken: {end_time - start_time:.2f} seconds")
    print("Note: Only ~3 seconds (longest task time) not 6 seconds!")

# Run threading execution
threading_execution()
```

**Output:**
```
==================================================
THREADING EXECUTION
==================================================
Thread 1: Starting (will take 3 seconds)
Thread 2: Starting (will take 2 seconds)
Thread 3: Starting (will take 1 seconds)

All threads started! Main thread continues...
Thread 3: Finished
Thread 2: Finished
Thread 1: Finished

Total time taken: 3.01 seconds
Note: Only ~3 seconds (longest task time) not 6 seconds!
```

---

## **Example 3: ThreadPoolExecutor (Recommended)**

```python
from concurrent.futures import ThreadPoolExecutor
import time

def task(seconds, task_name):
    """Simulates a task that takes some time"""
    print(f"{task_name}: Starting (will take {seconds} seconds)")
    time.sleep(seconds)
    print(f"{task_name}: Finished")
    return f"Result from {task_name}"

def threadexecutor_execution():
    print("\n" + "="*50)
    print("THREADPOOLEXECUTOR EXECUTION")
    print("="*50)
    
    start_time = time.perf_counter()
    
    # Using ThreadPoolExecutor (automatically manages threads)
    with ThreadPoolExecutor(max_workers=3) as executor:
        print("Creating ThreadPoolExecutor with 3 workers...")
        
        # Submit tasks to the executor
        future1 = executor.submit(task, 3, "Executor Task 1")
        future2 = executor.submit(task, 2, "Executor Task 2")
        future3 = executor.submit(task, 1, "Executor Task 3")
        
        # Get results (waits for completion automatically)
        result1 = future1.result()
        result2 = future2.result()
        result3 = future3.result()
    
    end_time = time.perf_counter()
    
    print(f"\nResults: {result1}, {result2}, {result3}")
    print(f"Total time taken: {end_time - start_time:.2f} seconds")

# Run ThreadPoolExecutor execution
threadexecutor_execution()
```

**Output:**
```
==================================================
THREADPOOLEXECUTOR EXECUTION
==================================================
Creating ThreadPoolExecutor with 3 workers...
Executor Task 1: Starting (will take 3 seconds)
Executor Task 2: Starting (will take 2 seconds)
Executor Task 3: Starting (will take 1 seconds)
Executor Task 3: Finished
Executor Task 2: Finished
Executor Task 1: Finished

Results: Result from Executor Task 1, Result from Executor Task 2, Result from Executor Task 3
Total time taken: 3.01 seconds
```

---

## **Example 4: Comparison All Together**

```python
import time
import threading
from concurrent.futures import ThreadPoolExecutor

def simulated_task(task_id, duration):
    """Simulates a time-consuming task"""
    print(f"  Task {task_id}: Working for {duration} seconds...")
    time.sleep(duration)
    return f"Task {task_id} completed in {duration}s"

def measure_time(method_name, function_to_run):
    """Helper to measure execution time"""
    print(f"\n{'='*60}")
    print(f"METHOD: {method_name}")
    print(f"{'='*60}")
    
    start = time.perf_counter()
    results = function_to_run()
    end = time.perf_counter()
    
    print(f"\nResults: {results}")
    print(f"Time taken: {end - start:.2f} seconds")
    return end - start

# ===== METHOD 1: SEQUENTIAL =====
def run_sequential():
    results = []
    results.append(simulated_task(1, 2))
    results.append(simulated_task(2, 1))
    results.append(simulated_task(3, 3))
    return results

# ===== METHOD 2: BASIC THREADING =====
def run_threading():
    results = []
    
    def worker(task_id, duration):
        result = simulated_task(task_id, duration)
        results.append(result)
    
    threads = []
    threads.append(threading.Thread(target=worker, args=(1, 2)))
    threads.append(threading.Thread(target=worker, args=(2, 1)))
    threads.append(threading.Thread(target=worker, args=(3, 3)))
    
    for t in threads:
        t.start()
    
    for t in threads:
        t.join()
    
    return results

# ===== METHOD 3: THREADPOOLEXECUTOR =====
def run_threadpool():
    results = []
    
    with ThreadPoolExecutor(max_workers=3) as executor:
        # Submit all tasks
        future1 = executor.submit(simulated_task, 1, 2)
        future2 = executor.submit(simulated_task, 2, 1)
        future3 = executor.submit(simulated_task, 3, 3)
        
        # Collect results
        results.append(future1.result())
        results.append(future2.result())
        results.append(future3.result())
    
    return results

# ===== MAIN COMPARISON =====
if __name__ == "__main__":
    print("MULTITHREADING COMPARISON DEMO")
    print("Three tasks: Task1=2s, Task2=1s, Task3=3s")
    
    times = {}
    
    # Run all methods
    times['Sequential'] = measure_time("Sequential (Normal)", run_sequential)
    times['Threading'] = measure_time("Basic Threading", run_threading)
    times['ThreadPool'] = measure_time("ThreadPoolExecutor", run_threadpool)
    
    # Summary
    print(f"\n{'='*60}")
    print("SUMMARY COMPARISON")
    print(f"{'='*60}")
    
    for method, t in times.items():
        print(f"{method:20} : {t:.2f} seconds")
    
    print(f"\nThreading is {times['Sequential']/times['Threading']:.1f}x faster than Sequential!")
```

**Output:**
```
MULTITHREADING COMPARISON DEMO
Three tasks: Task1=2s, Task2=1s, Task3=3s

============================================================
METHOD: Sequential (Normal)
============================================================
  Task 1: Working for 2 seconds...
  Task 2: Working for 1 seconds...
  Task 3: Working for 3 seconds...

Results: ['Task 1 completed in 2s', 'Task 2 completed in 1s', 'Task 3 completed in 3s']
Time taken: 6.01 seconds

============================================================
METHOD: Basic Threading
============================================================
  Task 1: Working for 2 seconds...
  Task 2: Working for 1 seconds...
  Task 3: Working for 3 seconds...

Results: ['Task 1 completed in 2s', 'Task 2 completed in 1s', 'Task 3 completed in 3s']
Time taken: 3.01 seconds

============================================================
METHOD: ThreadPoolExecutor
============================================================
  Task 1: Working for 2 seconds...
  Task 2: Working for 1 seconds...
  Task 3: Working for 3 seconds...

Results: ['Task 1 completed in 2s', 'Task 2 completed in 1s', 'Task 3 completed in 3s']
Time taken: 3.01 seconds

============================================================
SUMMARY COMPARISON
============================================================
Sequential           : 6.01 seconds
Threading            : 3.01 seconds
ThreadPool           : 3.01 seconds

Threading is 2.0x faster than Sequential!
```

---

## **Example 5: Simple Real-World Analogy**

```python
import time
import threading
from concurrent.futures import ThreadPoolExecutor

# Analogy: Making 3 different sandwiches
def make_sandwich(sandwich_type, time_needed):
    """Simulates making a sandwich"""
    print(f"🍞 Starting {sandwich_type} sandwich (takes {time_needed}s)")
    time.sleep(time_needed)
    print(f"✅ Finished {sandwich_type} sandwich")
    return f"{sandwich_type} sandwich"

print("ANALOGY: MAKING SANDWICHES")
print("-" * 40)

# Method 1: One person making all sandwiches (Sequential)
print("\nMethod 1: ONE PERSON (Sequential)")
start = time.perf_counter()

sandwich1 = make_sandwich("Cheese", 3)
sandwich2 = make_sandwich("Ham", 2)
sandwich3 = make_sandwich("Veggie", 1)

end = time.perf_counter()
print(f"Time: {end-start:.1f}s (3+2+1 = 6 seconds)")

# Method 2: Three people working together (Threading)
print("\nMethod 2: THREE PEOPLE (Threading)")
start = time.perf_counter()

def make_sandwich_thread(stype, stime):
    return make_sandwich(stype, stime)

threads = []
for s_type, s_time in [("Cheese", 3), ("Ham", 2), ("Veggie", 1)]:
    t = threading.Thread(target=make_sandwich_thread, args=(s_type, s_time))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

end = time.perf_counter()
print(f"Time: {end-start:.1f}s (only as long as the longest sandwich!)")

# Method 3: Kitchen with 3 stations (ThreadPoolExecutor)
print("\nMethod 3: KITCHEN WITH STATIONS (ThreadPoolExecutor)")
start = time.perf_counter()

with ThreadPoolExecutor(max_workers=3) as kitchen:
    orders = [
        ("Cheese", 3),
        ("Ham", 2),
        ("Veggie", 1)
    ]
    
    # Submit all orders at once
    futures = []
    for order in orders:
        future = kitchen.submit(make_sandwich, order[0], order[1])
        futures.append(future)
    
    # Collect finished sandwiches
    sandwiches = []
    for future in futures:
        sandwiches.append(future.result())

end = time.perf_counter()
print(f"Time: {end-start:.1f}s")
print(f"\nAll sandwiches ready: {sandwiches}")
```

**Key Takeaways:**

1. **Sequential**: Tasks run one after another - total time = sum of all task times
2. **Threading**: Tasks run concurrently - total time ≈ longest task time
3. **ThreadPoolExecutor**: Like threading but with better management
4. **Use `time.perf_counter()`** for accurate timing

**When to use which:**
- **Sequential**: Simple scripts, few tasks, or tasks that depend on each other
- **Threading**: When you need fine control over each thread
- **ThreadPoolExecutor**: Most cases! Especially for I/O tasks like downloading files

# Multithreading in Python: Downloading Images (Beginner to Advanced)

Downloading images from URLs is an **I/O-bound** task (waiting for network responses), which makes it perfect for concurrency with threads. Threads allow multiple downloads to happen in parallel, reducing total time compared to sequential downloads.

Python's **Global Interpreter Lock (GIL)** prevents true CPU parallelism in threads, but for I/O-bound tasks like network requests, threads release the GIL during waiting, so real concurrency is achieved.

We will progress from:
1. Sequential (one by one)
2. Basic `threading` module
3. `concurrent.futures.ThreadPoolExecutor` (recommended real-world approach)
4. Advanced topics and best practices

We’ll use the `requests` library for downloading. Install it with `pip install requests` if needed.

```python
import requests
import os
from pathlib import Path

def download_image(url: str, folder: str = "downloads", filename: str = None):
    """Download a single image and save it to disk."""
    if filename is None:
        filename = url.split("/")[-1].split("?")[0]  # Extract name from URL
    path = Path(folder) / filename
    path.parent.mkdir(parents=True, exist_ok=True)
    
    response = requests.get(url, stream=True)
    response.raise_for_status()  # Raise exception for bad status
    
    with open(path, "wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)
    
    print(f"Downloaded: {filename}")
    return path
```

Sample list of image URLs for testing (replace with your own):

```python
image_urls = [
    "https://example.com/image1.jpg",
    "https://example.com/image2.png",
    "https://example.com/image3.webp",
    # ... add up to hundreds
]
```

## 1. Beginner: Sequential Download (One by One)

```python
import time

start = time.perf_counter()

for url in image_urls:
    download_image(url)

duration = time.perf_counter() - start
print(f"Total time: {duration:.2f} seconds")
```

- Total time ≈ sum of individual download times.
- Simple, but slow when there are many URLs or slow servers.

## 2. Intermediate: Manual Multithreading with `threading` Module

```python
import threading
import time

start = time.perf_counter()

threads = []
for url in image_urls:
    t = threading.Thread(target=download_image, args=(url,))
    threads.append(t)
    t.start()

# Wait for all threads to finish
for t in threads:
    t.join()

duration = time.perf_counter() - start
print(f"Total time: {duration:.2f} seconds")
```

**Pros**:
- All downloads start almost simultaneously.
- Total time ≈ time of the slowest download.

**Cons**:
- Creating hundreds of threads is expensive (memory + overhead).
- No built-in limit on number of concurrent threads.
- Hard to handle errors or get results cleanly.

Use this only for small numbers (< 20–30) of threads.

## 3. Recommended: `concurrent.futures.ThreadPoolExecutor`

This is the modern, clean way. It manages a pool of threads automatically.

### Basic Usage with `map` (preserves order)

```python
from concurrent.futures import ThreadPoolExecutor, as_completed
import time

start = time.perf_counter()

with ThreadPoolExecutor(max_workers=10) as executor:  # 10 parallel downloads
    executor.map(download_image, image_urls)

duration = time.perf_counter() - start
print(f"Total time: {duration:.2f} seconds")
```

### Usage with `submit` + `as_completed` (get results as they finish)

```python
start = time.perf_counter()

results = []
with ThreadPoolExecutor(max_workers=10) as executor:
    future_to_url = {executor.submit(download_image, url): url for url in image_urls}
    
    for future in as_completed(future_to_url):
        try:
            path = future.result()  # Get result or raise exception
            results.append(path)
        except Exception as e:
            url = future_to_url[future]
            print(f"Failed to download {url}: {e}")

duration = time.perf_counter() - start
print(f"Total time: {duration:.2f} seconds")
```

**Why `ThreadPoolExecutor` is better**:
- Reuses threads (pool) → low overhead even for 500+ URLs.
- `max_workers` controls concurrency (good default: 10–20 for downloads; too many can overwhelm server or your connection).
- Easy error handling.
- `map` is simplest when order doesn’t matter for processing.
- `as_completed` lets you process results as soon as they finish.

## 4. Advanced Topics & Best Practices

### Choosing `max_workers`
- Default: `min(32, os.cpu_count() + 4)`
- For downloads: 10–50 is usually optimal.
- Too high → server may block you (rate limiting), or you hit connection limits.

### Error Handling & Retries
Add retries using `tenacity` or simple loop:

```python
from tenacity import retry, stop_after_attempt, wait_fixed

@retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
def download_image_robust(url: str, ...):
    # same as before
```

### Progress Bar
Use `tqdm` for nice progress:

```python
from tqdm import tqdm

with ThreadPoolExecutor(max_workers=10) as executor:
    list(tqdm(executor.map(download_image, image_urls), total=len(image_urls)))
```

### Naming Files Safely
URLs may have same filename → add index:

```python
for i, url in enumerate(image_urls):
    filename = f"image_{i:04d}.{url.split('.')[-1]}"
    download_image(url, filename=filename)
```

### When to Use `asyncio` + `aiohttp` Instead
For **very large** numbers (1000+) of downloads, `asyncio` with asynchronous HTTP is faster (single thread, no thread overhead):

```python
import asyncio
import aiohttp
from aiofiles import open as async_open

async def download_async(session, url, filename):
    async with session.get(url) as resp:
        resp.raise_for_status()
        async with async_open(filename, "wb") as f:
            async for chunk in resp.content.iter_chunked(8192):
                await f.write(chunk)

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [download_async(session, url, f"img_{i}.jpg") for i, url in enumerate(image_urls)]
        await asyncio.gather(*tasks)
```

`asyncio` is more efficient at scale but harder to write/debug.

### Multiprocessing (Not Recommended Here)
Use `ProcessPoolExecutor` only for CPU-bound tasks. For downloads (I/O), threads or asyncio are better.

## Summary Table

| Approach                  | Best For                  | Difficulty | Max Concurrent | Recommended |
|---------------------------|---------------------------|------------|----------------|-------------|
| Sequential                | < 10 images               | Easy       | 1              | No          |
| Manual `threading`        | 10–30 images              | Medium     | Unlimited (bad)| Rarely      |
| `ThreadPoolExecutor`      | 10–1000 images            | Easy       | Controlled     | Yes         |
| `asyncio` + `aiohttp`     | 1000+ images              | Hard       | Very high      | For scale   |

Use `ThreadPoolExecutor` for almost all real-world image downloading tasks in Python. It’s clean, safe, and fast enough.


Got it 👍
Here are the **most asked Python multithreading interview questions**, **from beginner to advanced**, with **clear, interview-ready answers**. These are *real-world common* questions recruiters love to ask.

---

# 🧵 Most Asked Multithreading Interview Questions in Python

---

## 1️⃣ What is Multithreading?

**Answer:**
Multithreading is a technique where **multiple threads run concurrently within a single process** to perform tasks in parallel.

In Python, threads are mainly useful for **I/O-bound tasks** (file operations, network calls, API requests).

---

## 2️⃣ Difference Between Process and Thread?

| Process          | Thread           |
| ---------------- | ---------------- |
| Heavyweight      | Lightweight      |
| Own memory space | Shares memory    |
| Slower to create | Faster to create |
| No GIL issue     | Affected by GIL  |

---

## 3️⃣ What is the GIL (Global Interpreter Lock)?

**Answer:**
The **GIL** is a mutex that allows **only one thread to execute Python bytecode at a time**, even on multi-core CPUs.

👉 This means:

* Python threads **do not give true parallelism for CPU-bound tasks**
* Threads are best for **I/O-bound tasks**

---

## 4️⃣ Why Does Python Have a GIL?

**Answer:**

* Simplifies **memory management**
* Makes CPython **thread-safe**
* Improves performance for **single-threaded programs**

---

## 5️⃣ When Should You Use Multithreading in Python?

**Use multithreading when:**

* Task is **I/O-bound**
* Waiting on network / file / database
* Making multiple API calls

**Avoid multithreading for:**

* Heavy CPU calculations

---

## 6️⃣ How Do You Create a Thread in Python?

```python
from threading import Thread

def task():
    print("Running in a thread")

t = Thread(target=task)
t.start()
t.join()
```

---

## 7️⃣ What Does `start()` and `join()` Do?

**start():**

* Starts a new thread
* Calls the target function

**join():**

* Waits for the thread to finish
* Blocks main thread until completion

---

## 8️⃣ What is a Race Condition?

**Answer:**
A race condition occurs when **multiple threads access shared data simultaneously**, leading to **inconsistent results**.

Example:

```python
counter += 1
```

This operation is **not atomic**.

---

## 9️⃣ How Do You Prevent Race Conditions?

By using **Locks**.

```python
from threading import Lock

lock = Lock()

with lock:
    counter += 1
```

---

## 🔟 What is a Lock?

**Answer:**
A lock ensures that **only one thread can access a shared resource at a time**.

---

## 1️⃣1️⃣ Difference Between Lock and RLock?

| Lock                             | RLock                                  |
| -------------------------------- | -------------------------------------- |
| Non-reentrant                    | Reentrant                              |
| Same thread cannot acquire twice | Same thread can acquire multiple times |
| Faster                           | Slightly slower                        |

---

## 1️⃣2️⃣ What is Deadlock?

**Answer:**
A deadlock happens when **two or more threads wait forever for each other to release locks**.

```text
Thread A → Lock 1 → waits for Lock 2  
Thread B → Lock 2 → waits for Lock 1
```

---

## 1️⃣3️⃣ How Do You Avoid Deadlock?

* Acquire locks in **same order**
* Use **timeouts**
* Keep critical sections small

---

## 1️⃣4️⃣ What is a Daemon Thread?

**Answer:**
A daemon thread runs in the background and **stops automatically when the main program exits**.

```python
t = Thread(target=task, daemon=True)
```

---

## 1️⃣5️⃣ Difference Between Daemon and Non-Daemon Threads?

| Daemon Thread           | Non-Daemon Thread |
| ----------------------- | ----------------- |
| Killed with main thread | Main waits for it |
| Background tasks        | Important tasks   |

---

## 1️⃣6️⃣ What is `threading.current_thread()`?

**Answer:**
Returns the **current executing thread object**.

```python
import threading
print(threading.current_thread().name)
```

---

## 1️⃣7️⃣ What is Thread Safety?

**Answer:**
A program is **thread-safe** if it behaves correctly when accessed by multiple threads simultaneously.

---

## 1️⃣8️⃣ What is the `threading.Event`?

**Answer:**
Used for **signaling between threads**.

```python
event.set()    # Signal
event.wait()   # Wait for signal
```

---

## 1️⃣9️⃣ What is `ThreadPoolExecutor`?

**Answer:**
A high-level API for managing thread pools.

```python
from concurrent.futures import ThreadPoolExecutor

with ThreadPoolExecutor(max_workers=3) as executor:
    executor.map(task, items)
```

---

## 2️⃣0️⃣ Threading vs Multiprocessing?

| Threading       | Multiprocessing |
| --------------- | --------------- |
| Shared memory   | Separate memory |
| Affected by GIL | No GIL          |
| Best for I/O    | Best for CPU    |

---

## 2️⃣1️⃣ Can Python Threads Run in Parallel?

**Answer:**
❌ **No for CPU-bound tasks** (due to GIL)
✅ **Yes for I/O-bound tasks**

---

## 2️⃣2️⃣ What Happens If a Thread Raises an Exception?

**Answer:**

* Exception **does not stop main thread**
* Thread terminates silently (unless handled)

---

## 2️⃣3️⃣ How Do You Pass Arguments to Threads?

```python
Thread(target=task, args=(10, "Task1"))
```

---

## 2️⃣4️⃣ What is the `queue.Queue` Used For?

**Answer:**
Thread-safe communication between threads.

```python
from queue import Queue
q = Queue()
q.put(1)
q.get()
```

---

## 2️⃣5️⃣ How Do You Stop a Thread?

**Answer:**
Python does **not support force-stopping threads**.
Use:

* Flags
* Events

```python
stop_event = Event()
```

---
