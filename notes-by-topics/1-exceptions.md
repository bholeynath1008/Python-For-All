**Python Exceptions**
## Level I: Basic Exception Handling
### What is an Exception?
An **exception** is an event that **disrupts the normal flow** of a program (usually because of an error).


### Important Keywords Summary

| Keyword     | When it runs                              | Typical use case                              |
|-------------|-------------------------------------------|-----------------------------------------------|
| `try`       | Code that might fail                      | This block is use on code which may have exception                         |
| `except`    | When specific exception occurs            | Handle/handle known errors (exceptions)                    |
| `else`      | When **no** exception occurred            | Normal success path                           |
| `finally`   | **Always** (even after return/break)      | Executes wheather or not expection occured ie. on success and error, it allows you to clean-up(close files, connections, etc.)      |
| `raise`     | Manually trigger/throw exception          | create our own exceptions, custom exceptions                        |

### Most Common Built-in Exceptions

```text
ZeroDivisionError     →  1 / 0
ValueError            →  int("pizza"), int("3.14")
TypeError             →  1 + "1", "2" * 3.5
IndexError            →  mylist[999] (index out of range)
KeyError              →  mydict["missing_key"]
FileNotFoundError     →  open("nonexistent.txt")
AttributeError        →  "hello".nonexistent_method()
NameError             →  print(x) when x not defined
```

### Basic Exception Handling Structure

```python
try:
    # Code that might raise an exception
    number = int(input("Enter a number: "))
    result = 1 / number

except ZeroDivisionError:
    print("You can't divide by zero!")

except ValueError:
    print("Please enter a valid number!")

except Exception as e:          # ← Catch-all (use carefully!)
    print(f"Something went wrong: {e}")

else:
    print("Everything worked! Result =", result)   # runs only if NO exception

finally:
    print("This always runs (cleanup)")            # cleanup, close files/connections
```

### Raising Exceptions Manually

```python
raise ValueError("Age cannot be negative!")
raise TypeError("Expected int, got str")
```

### Custom Exceptions (Best Practice for your own libraries/projects)

```python
class InsufficientFundsError(Exception):
    """Raised when trying to withdraw more than available balance"""
    pass

# or with extra information
class InvalidTransactionError(Exception):
    def __init__(self, message, amount):
        self.amount = amount
        super().__init__(message)
```

Usage:

```python
def withdraw(amount, balance):
    if amount <= 0:
        raise ValueError("Amount must be positive!")
    if amount > balance:
        raise InsufficientFundsError(f"Cannot withdraw ${amount}. Balance: ${balance}")
    return balance - amount
```

### Exception Chaining (very useful for debugging)

```python
try:
    x = 1 / 0
except ZeroDivisionError as original_error:
    raise RuntimeError("Math operation failed!") from original_error
    # ↑ keeps the original error in __cause__ attribute
```

### Quick Best Practices Summary

✅ Do: Catch **specific** exceptions  
❌ Don't: Use bare `except:` or only `except Exception:` (hides real bugs)

✅ Use `finally` for cleanup  
✅ Use `else` for success logic  
✅ Create **custom exceptions** for your domain  
✅ Chain exceptions when wrapping (`raise ... from ...`)  
✅ Always give meaningful error messages

## Level II: Exception Handling in Asynchronous Python Code
**Exception Handling in Asynchronous Python Code**  

Here are the most common and recommended patterns for handling exceptions in async Python code:

| Pattern                          | When to use                              | Cleanest / Most Recommended? | Approx. Usage (2025) |
|----------------------------------|------------------------------------------|-------------------------------|-----------------------|
| `try`/`except` inside `async def`| Normal, local error handling             | ★★★★★                        | Very common          |
| `await` + `try`/`except`         | Most frequent real-world case            | ★★★★★                        | Dominant             |
| `asyncio.gather(..., return_exceptions=True)` | Running many tasks, want all to complete | ★★★★                         | Very popular         |
| `try`/`except` around `asyncio.gather()` | Want to fail fast on first exception     | ★★★                          | Common               |
| `asyncio.TaskGroup` (3.11+)      | Modern, clean, fails fast by default     | ★★★★★                        | Strongly recommended (2025+) |
| `asyncio.wait()` + manual checks | Very fine-grained control needed         | ★★                           | Rare                 |

### 1. Most Common – try/except around await

```python
async def fetch_user(user_id: int) -> User:
    try:
        response = await client.get(f"/users/{user_id}")
        response.raise_for_status()
        return User(**await response.json())
    except aiohttp.ClientResponseError as e:
        if e.status == 404:
            raise UserNotFoundError(user_id) from e
        raise
    except aiohttp.ClientConnectionError:
        logger.error("Connection failed", exc_info=True)
        raise ServiceUnavailableError() from None
    except Exception as e:
        logger.exception("Unexpected error while fetching user %d", user_id)
        raise
```

### 2. Multiple tasks – asyncio.gather (two popular styles)

```python
# Style A: Let everything finish, collect all exceptions (very common)
async def process_all():
    results = await asyncio.gather(
        process_order(1),
        process_order(2),
        process_order(3),
        return_exceptions=True
    )
    
    for i, result in enumerate(results, 1):
        if isinstance(result, Exception):
            print(f"Order {i} failed: {result!r}")
        else:
            print(f"Order {i} succeeded")
```

```python
# Style B: Fail fast (first exception stops everything)
async def process_critical():
    try:
        await asyncio.gather(
            important_task_1(),
            important_task_2(),
            important_task_3(),
        )
    except Exception as e:
        logger.error("Critical flow failed", exc_info=True)
        await rollback_all()
        raise
```

### 3. Modern & Recommended way (Python 3.11+): TaskGroup

```python
# Cleanest & safest way in 2024–2025
async def fan_out():
    async with asyncio.TaskGroup() as tg:
        tg.create_task(download_image("cat.jpg"))
        tg.create_task(download_image("dog.jpg"))
        tg.create_task(send_email("welcome"))

    print("All tasks completed successfully!")  # ← only reached if ALL succeeded
```

Key advantages of `TaskGroup`:

- First exception is immediately raised (fail-fast)
- All tasks are still properly cancelled on exception
- Much better stack traces than `gather`
- Context manager → very clean resource management
- No need for `return_exceptions=True` gymnastics

### Quick Reference Table – What should you choose?

```text
Situation                                    │ Recommended pattern                  │ Python version
─────────────────────────────────────────────┼──────────────────────────────────────┼────────────────
Normal single await                          │ try/except around await              │ all
Many independent background tasks            │ gather(…, return_exceptions=True)    │ all
Critical tasks – fail on first error         │ gather() + try/except                │ all
Modern code & want cleanest solution         │ async with TaskGroup()               │ 3.11+
Very fine grained control / timeouts         │ asyncio.wait() + manual handling     │ all
Structured concurrency, many nested levels   │ TaskGroup (nested is fine!)          │ 3.11+
```

### Mini Cheat-sheet (2025 recommendation)

```python
# Quick decision tree

if python >= 3.11:
    → Prefer asyncio.TaskGroup()
else:
    if tasks are independent and you want all results/errors:
        → gather(..., return_exceptions=True)
    if tasks are critical / should fail fast:
        → gather() in try/except
    if single await:
        → just normal try/except around await
```
## Interview: 
**Most Asked Python Exception Handling Interview Questions**  
*(Backend Developer Focus – 2025/2026 Trends)*

Exception handling is a **core topic** in Python backend interviews (Flask, Django, FastAPI, async services). Interviewers test understanding of robust error management, graceful degradation, custom errors for APIs, and async concurrency.

Compiled from popular sources (GeeksforGeeks, InterviewBit, Medium, Analytics Vidhya, DataCamp) – these are the **most frequently appearing questions**.

### 1. Core Concepts (Asked in 90%+ interviews)
1. **What is exception handling in Python? Explain the role of try, except, else, and finally.**  
   - `try`: Block where exceptions might occur.  
   - `except`: Catches and handles specific exceptions.  
   - `else`: Runs only if no exception occurred (ideal for success logic).  
   - `finally`: Always executes (cleanup: close DB connections, release locks).  
   Example:  
   ```python
   try:
       result = 10 / int(user_input)
   except ZeroDivisionError:
       print("Division by zero!")
   except ValueError:
       print("Invalid input!")
   else:
       print("Success:", result)
   finally:
       print("Cleanup done")
   ```

2. **How do you handle multiple exceptions? Why is the order important?**  
   Specific exceptions first, then general. Parent exceptions (like `Exception`) must come last.  
   Wrong order causes the broader one to catch everything earlier.  
   ```python
   try:
       value = int("abc") / 0
   except ValueError:
       print("Bad value")
   except ZeroDivisionError:
       print("Divide by zero")
   except Exception as e:  # Catch-all (use sparingly!)
       print("Unexpected:", e)
   ```

3. **What is the purpose of the finally block? When does it execute?**  
   Executes **always** – even if there's a `return`, `break`, or unhandled exception. Used for resource cleanup (closing files, DB connections, API clients).

4. **Can you raise exceptions manually? How?**  
   Yes, use `raise`. Common in backend validation.  
   ```python
   if balance < amount:
       raise ValueError("Insufficient funds")
   # Or custom
   raise InsufficientFundsError("Balance too low")
   ```

5. **How do you create and use custom exceptions?**  
   Inherit from `Exception` (or a more specific built-in).  
   ```python
   class APIValidationError(Exception):
       pass
   
   raise APIValidationError("Invalid payload")
   ```

### 2. Common Tricky / Advanced Core Questions
6. **What happens if you have return in both try and finally?**  
   The `return` in `finally` **overrides** the one in `try`. (Surprising but true – avoid returns in finally!)

7. **How do you chain exceptions (preserve original traceback)?**  
   Use `raise NewError() from original_error`.  
   ```python
   try:
       1 / 0
   except ZeroDivisionError as e:
       raise RuntimeError("Calc failed") from e
   ```

8. **What are best practices for exception handling?**  
   - Catch **specific** exceptions, not bare `except:` or just `Exception`.  
   - Log exceptions properly (`logger.exception()`).  
   - Don't use exceptions for flow control.  
   - In APIs: Convert to proper HTTP responses (400, 500, etc.).

9. **What is the difference between errors and exceptions?**  
   - **Errors**: Usually syntax or compile-time (unrecoverable).  
   - **Exceptions**: Runtime issues that can be caught/handled (e.g., ZeroDivisionError, KeyError).

### 3. Backend Framework-Specific (Flask/Django/FastAPI)
10. **How do you handle errors globally in Flask?**  
    Use `@app.errorhandler()`. Common for 404, 500, custom API errors.  
    ```python
    @app.errorhandler(404)
    def not_found(error):
        return {"error": "Not found"}, 404
    
    @app.errorhandler(Exception)
    def handle_exception(e):
        return {"error": str(e)}, 500
    ```

11. **How do you handle exceptions in Django views?**  
    - Use middleware or override `handle_exception`.  
    - Common: Custom 404/500 views, or in class-based views: `try/except` + return JsonResponse with status.

### 4. Async Python (Increasingly asked – FastAPI, async services)
12. **How are exceptions handled in asyncio tasks?**  
    - Exceptions propagate when you `await` a task.  
    - Unawaited tasks log exceptions as warnings.  
    - `asyncio.gather(..., return_exceptions=True)` collects exceptions instead of failing fast.  
    - Preferred (Python 3.11+): Use `asyncio.TaskGroup` – auto-cancels on first exception.

13. **How to handle exceptions when running multiple coroutines?**  
    ```python
    # Fail fast
    try:
        await asyncio.gather(task1(), task2(), task3())
    except Exception as e:
        await cleanup()
        raise
    
    # Or collect all
    results = await asyncio.gather(t1, t2, t3, return_exceptions=True)
    for r in results:
        if isinstance(r, Exception):
            handle_error(r)
    ```
