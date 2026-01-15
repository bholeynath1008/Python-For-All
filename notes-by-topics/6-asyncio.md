Includes Interview questions too:
# 🧵 Asyncio in Python 

---
ref: https://www.youtube.com/watch?v=lgoB3_-ejnI&list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg&index=96
## 1️⃣ What is Asyncio?

`asyncio` is a **standard Python library** that allows writing **concurrent, non-blocking code** using the `async` / `await` syntax.

## 🔰 Sequential vs Concurrent Execution (Very Important)
**I. Sequential Execution**
**Meaning:**
Tasks run **one after another**.
Each task must **finish completely** before the next one starts.
**Example:** 
To download 100 images from internet, one downloads completes then another 2nd one starts, then 3rd one starts (one by one) which is very slow. If each image takes ~2 seconds → ~200 seconds (more than 3 minutes) 
**How it is achieved:**
* Normal synchronous code
* Using `await` one by one in async code
```python
await task1()
await task2()
#⏳ Total time = **sum of all tasks**
```
**II. Concurrent Execution**
**Meaning:**
Multiple tasks **start together** and run **overlapping in time**.
While one task waits, another task executes.
**Example:** To download 100 images from internet, Many images at the same time (much faster). No need to wait for first images to be downloaded, all start downloading at same time.
**How it is achieved:**

* `asyncio.gather()`
* `asyncio.create_task()`

```python
await asyncio.gather(task1(), task2())
# ⏱ Total time = **maximum task time**
```

### Why Asyncio Exists

In traditional (synchronous) programs:

* Code executes **line by line**
* When a task waits (network, file, DB), the **entire program waits**

Asyncio solves this by:

* Allowing **multiple tasks to run concurrently**
* Using a **single thread**
* Switching tasks **only when they are waiting**
👉 Uses **single thread + event loop**
👉 Best for **I/O-bound tasks**, not CPU-bound tasks.

---

## 2️⃣ Core Concepts (Must Know ⭐)

| Concept                      | Description                                                                                                                               |
| ---------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| **Event Loop**               | The central controller that schedules and runs all async tasks. It runs in a single thread and switches tasks when they reach an `await`. |
| **Coroutine**                | A function defined using `async def`. Calling it returns a coroutine object that must be awaited to execute.                              |
| **Await**                    | Pauses the current coroutine and yields control back to the event loop until the awaited task completes.                                  |
| **Task**                     | A wrapped coroutine scheduled to run concurrently using `asyncio.create_task()`.                                                          |
| **Awaitable**                | Any object that can be used with `await` (coroutines, tasks, futures).                                                                    |
| **Cooperative Multitasking** | Tasks voluntarily yield control using `await`, unlike threads where the OS handles switching.                                             |

---

## 3. Key Syntax & Functions

| Feature                | Usage & Purpose                                                                 |
|------------------------|---------------------------------------------------------------------------------|
| `async def`            | Defines a coroutine function.                                                   |
| `await`                | Pauses the current coroutine and yields control to the event loop until the awaited operation completes. |
| `asyncio.run()`        | Main entry point: runs a coroutine and manages the event loop.                  |
| `asyncio.create_task()`| Schedules a coroutine to run concurrently. Returns a Task object.               |
| `asyncio.gather()`     | Runs multiple awaitables concurrently and waits for all to complete. Returns a list of results. |
| `async with`           | For asynchronous context managers (e.g., automatic cleanup of connections).    |
| `await asyncio.sleep()`| Non-blocking delay (use instead of `time.sleep()`).                            |

### `create_task` vs `gather`

| Feature               | `asyncio.create_task()`                                   | `asyncio.gather()`                                          |
|-----------------------|-----------------------------------------------------------|-------------------------------------------------------------|
| Purpose               | Schedule one coroutine to run in the background           | Run multiple coroutines concurrently and wait for all       |
| Returns               | A `Task` object (can be awaited later)                    | List of results when all complete                           |
| When to use           | When you want to start a task and continue doing other work| When you need to launch many tasks and wait for completion  |
| Requires `await`?     | Optional (you can `await` the task later)                 | Yes (you `await` the `gather` call itself)                  |

### Do all async operations need `await`?**  
- You **must** `await` a coroutine to actually run it and get its result.
- `create_task()` schedules without immediate awaiting.
- `gather()` requires awaiting the entire group.

### When to Use Asyncio
- **I/O-bound** tasks: Web scraping, APIs, web servers (FastAPI, Starlette), downloading files, etc.
- Situations needing **many concurrent connections** with minimal overhead.
- **Not ideal** for CPU-bound tasks (use multiprocessing or threading instead).

## Common Pitfalls
1. **Blocking the event loop**  
   - Synchronous calls like `time.sleep()`, `requests.get()`, or heavy computation block **everything**.  
   - Fix: Use `await asyncio.sleep()` and async-compatible libraries.

2. **Using synchronous HTTP libraries**  
   - `requests.get()` blocks the loop → defeats the purpose of asyncio.  
   - Use `aiohttp` instead.

3. **Lost tasks**  
   - If you `create_task()` but don't keep a reference and don't await it, the task may be garbage-collected before finishing.


## 3️⃣ Asyncio Syntax (Basic Structure)

```python
import asyncio

async def my_async_function():
    return "Hello Async"

async def main():
    result = await my_async_function()
    print(result)

asyncio.run(main())
```

### Key Rules

* `async def` → defines coroutine
* `await` → used only inside async functions
* `asyncio.run()` → starts the event loop

---

## 4️⃣ Blocking vs Non-Blocking (Very Important ⚠️)

### ❌ Blocking Code (Wrong in Asyncio)

```python
import time

async def task():
    time.sleep(2)  # blocks event loop
    print("Done")
```

⛔ Blocks the event loop
⛔ Stops all other async tasks

---

### ✅ Non-Blocking Code (Correct)

```python
import asyncio

async def task():
    await asyncio.sleep(2)  # non-blocking
    print("Done")
```

✔ Allows other tasks to run
✔ True concurrency for I/O

---

### 5️⃣ Case 1: Sequential Execution (Synchronous Behavior)

### Scenario

Three tasks run **one after another**.
Total time = **sum of all delays**

```python
import asyncio

async def task1():
    await asyncio.sleep(1)
    print("Task 1 completed")

async def task2():
    await asyncio.sleep(2)
    print("Task 2 completed")

async def task3():
    await asyncio.sleep(1)
    print("Task 3 completed")

async def main():
    await task1()
    await task2()
    await task3()

asyncio.run(main())
```

### Output Order

```
Task 1 completed
Task 2 completed
Task 3 completed
```

⏱ Total time ≈ **4 seconds**

---

### 6️⃣ Case 2: Concurrent Execution (Asyncio Power)

### Same tasks, but run concurrently

```python
import asyncio

async def main():
    await asyncio.gather(
        task1(),
        task2(),
        task3()
    )

asyncio.run(main())
```

### Output Order (May Vary)

```
Task 1 completed
Task 3 completed
Task 2 completed
```

⏱ Total time ≈ **2 seconds (max delay)**

✔ Tasks overlap
✔ No waiting for each other

---

## 7️⃣ `asyncio.gather()` vs `asyncio.create_task()`

### Differences Table

| Feature                 | `asyncio.gather()` | `asyncio.create_task()` |
| ----------------------- | ------------------ | ----------------------- |
| Runs tasks concurrently | ✅                  | ✅                       |
| Waits for all tasks     | ✅                  | ❌                       |
| Returns results         | ✅ (list)           | ❌                       |
| Background execution    | ❌                  | ✅                       |
| Task control            | ❌                  | ✅                       |
| Use case                | Need all results   | Fire-and-forget tasks   |

---

### Return Values

#### `gather()`

```python
results = await asyncio.gather(f1(), f2())
print(results)  # [result1, result2]
```

#### `create_task()`

```python
task = asyncio.create_task(f1())
await task
print(task.result())
```

---

## 8️⃣ Common Mistake: `requests` with Asyncio ⚠️

### ❌ Wrong (Blocking)

```python
import requests

async def download():
    response = requests.get("https://example.com")  # blocks
```

🚨 `requests` is synchronous
🚨 Blocks the event loop

---

## 9️⃣ Correct Way: Using `aiohttp` (Async HTTP)

### Case: Download a Website Asynchronously

```python
import aiohttp
import asyncio

async def download_page(filename):
    url = "https://example.com"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.read()
            with open(filename, "wb") as f:
                f.write(data)

async def main():
    await asyncio.gather(
        download_page("page1.html"),
        download_page("page2.html")
    )

asyncio.run(main())
```

✔ Non-blocking HTTP
✔ True concurrency
✔ Efficient I/O usage

---
## 8️⃣ Instagram Example – ❌ Wrong Way (Blocking)

### Using `requests` (DO NOT DO THIS)

```python
import requests
import asyncio

async def download_instagram():
    response = requests.get("https://www.instagram.com")
    with open("instagram.html", "wb") as f:
        f.write(response.content)

asyncio.run(download_instagram())
```

🚨 `requests` is synchronous
🚨 Blocks event loop
🚨 Asyncio benefit is lost

---

## 9️⃣ Instagram Example – ✅ Correct Way (aiohttp)

```python
import aiohttp
import asyncio

async def download_instagram(filename):
    url = "https://www.instagram.com"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.read()
            with open(filename, "wb") as f:
                f.write(data)

async def main():
    await asyncio.gather(
        download_instagram("insta1.html"),
        download_instagram("insta2.html")
    )

asyncio.run(main())
```

✔ True async HTTP
✔ Non-blocking
✔ High-performance I/O

---


## 🔟 Requests vs Aiohttp (Comparison)

| Feature             | requests | aiohttp |
| ------------------- | -------- | ------- |
| Blocking            | ✅        | ❌       |
| Async support       | ❌        | ✅       |
| Event loop friendly | ❌        | ✅       |
| Use in asyncio      | ❌        | ✅       |

---

## 1️⃣1️⃣ When to Use Asyncio

### ✅ Best For

* API calls
* Web servers (FastAPI)
* Web scraping
* Database I/O
* File & network operations

### ❌ Not For

* CPU-heavy tasks
* Image processing
* ML training

(Use **multiprocessing** instead)

---

# Most Common Asyncio Interview Questions for Python Backend Developers

Asyncio is a frequent topic in Python backend interviews, especially for roles involving web frameworks like **FastAPI**, **Django** (async views), **Flask** with async extensions, or high-concurrency services (APIs, microservices, web scraping). Interviewers focus on understanding concurrency for I/O-bound tasks (e.g., database queries, external API calls, websockets).

Below is a curated list of the **most commonly asked questions**, aggregated from popular sources (DEV Community, Medium advanced guides, and backend interview compilations). I've grouped them by difficulty and included brief key points/answers for preparation. These overlap heavily across sources, indicating high frequency.

## Basic/Conceptual Questions
1. **What is asyncio and when should you use it?**  
   Asyncio enables concurrent I/O-bound code in a single thread using `async/await`. Use for network requests, database queries, file I/O, or handling many connections (e.g., web servers). Avoid for CPU-bound tasks—use multiprocessing instead.

2. **Explain the event loop.**  
   The event loop is the core scheduler: it runs in one thread, picks ready tasks, executes until `await`, switches to other tasks during waits (I/O, timers), and resumes when ready. It's like a conductor managing non-blocking operations.

3. **What is the difference between coroutines, Tasks, and Futures?**  
   - **Coroutine**: Object from `async def`—awaitable but not scheduled.  
   - **Task**: Wrapper that schedules a coroutine on the loop (`asyncio.create_task`).  
   - **Future**: Low-level placeholder for a result (rarely used directly).

4. **Why can't you use `await` at the top level (outside async functions)?**  
   `await` requires an active event loop and coroutine context. Top-level code must use `asyncio.run(main())` to create/manage the loop.

5. **Explain `asyncio.sleep()` vs `time.sleep()`. Why is one blocking?**  
   `time.sleep()` blocks the entire thread/event loop. `asyncio.sleep()` is non-blocking—it yields control, allowing other tasks to run.

## Intermediate Questions
6. **How do you run multiple coroutines concurrently? Compare `asyncio.gather()` and `asyncio.create_task()`.**  
   - `create_task(coro)`: Schedules immediately, returns a Task (fire-and-forget or await later).  
   - `gather(*coros)`: Runs multiple concurrently, waits for all, returns results list. Cancels others on failure (unless `return_exceptions=True`).  
   Use `gather` for simple parallel execution; `create_task` for more control.

7. **How do you run blocking/synchronous code in an async function without blocking the loop?**  
   Offload to a thread/process:  
   ```python
   await asyncio.to_thread(blocking_func)  # Python 3.9+
   # or
   loop = asyncio.get_running_loop()
   await loop.run_in_executor(None, blocking_func)
   ```

8. **Differences between asyncio, threading, and multiprocessing? When to choose each?**  
   | Model          | Threads | Asyncio | Multiprocessing |
   |----------------|---------|---------|-----------------|
   | Threading      | Preemptive, OS-managed | Cooperative, single-thread | True parallelism |
   | GIL Impact     | Releases on I/O | Avoids contention via yields | Bypasses GIL |
   | Best For       | Blocking libs, simple I/O | High-concurrency I/O (e.g., 1000+ connections) | CPU-bound |
   | Overhead       | Medium (memory) | Low | High (processes) |
   For backend I/O (APIs, DB): Prefer asyncio for scale; threading if mixing sync libs.

9. **How does asyncio handle the GIL for I/O-bound tasks?**  
   It doesn't remove the GIL but avoids contention: during `await` for I/O, the GIL releases, and the loop switches tasks. Scales better than threads for many connections.

10. **What is cooperative multitasking in asyncio?**  
    Tasks voluntarily yield at `await`. No OS preemption—makes reasoning easier but requires avoiding blocking calls.

## Advanced Questions
11. **How is exception handling done in asyncio tasks?**  
    Exceptions store in the Task. They raise when awaited. Unawaited tasks log warnings. Use `gather(return_exceptions=True)` to collect them. With TaskGroups (3.11+), multiple exceptions group as `ExceptionGroup`.

12. **Explain cancellation in asyncio. How to handle cleanup?**  
    `task.cancel()` raises `CancelledError` in the coroutine. Handle in `try/except CancelledError` and use `finally` for cleanup (e.g., close connections).

13. **What is structured concurrency? How does `asyncio.TaskGroup` help? (Python 3.11+)**  
    Ensures child tasks cancel/wait properly when parent exits (prevents leaks).  
    ```python
    async with asyncio.TaskGroup() as tg:
        tg.create_task(task1())
        tg.create_task(task2())
    # Auto-waits and propagates exceptions
    ```

14. **What is a semaphore in asyncio? When to use it in backend code?**  
    Limits concurrent access to resources (e.g., rate-limit API calls, DB connections).  
    ```python
    sem = asyncio.Semaphore(10)  # Max 10 concurrent
    async def fetch():
        async with sem:
            # Limited section
    ```
    Common in backend to prevent overwhelming external services.

15. **What are async iterators/generators? When useful in backend?**  
    Use `__aiter__`/`__anext__` and `async for`. Great for streaming data (e.g., async database cursors, websocket streams).

16. **When should you avoid asyncio in a backend application?**  
    - CPU-heavy processing.  
    - Mostly sync libraries (e.g., `requests` instead of `aiohttp`).  
    - Small apps where complexity outweighs benefits.  
    - Need true parallelism.

## Bonus: Common Practical/Coding Questions
- Implement concurrent URL fetching with `aiohttp` and `gather`.
- Build a simple async retry decorator with backoff.
- Handle timeouts: Use `asyncio.wait_for()` or `asyncio.timeout()` (3.11+).
- Compare sync vs async performance for downloading multiple files.

**Preparation Tips for Backend Roles**:
- Know async web frameworks: FastAPI (native async), Django 3.1+ async views.
- Practice with `aiohttp` for clients, `asyncio.Queue` for producer-consumer patterns.
- Be ready to discuss real-world use: "How would you make this endpoint faster with async?"

These cover ~90% of asyncio questions in mid/senior backend interviews. Focus on explaining trade-offs and pitfalls (e.g., blocking the loop). Good luck, Saroj!


