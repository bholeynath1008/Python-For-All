# FastAPI Beginner Notes: 
ref: Code with Tushar

## What is FastAPI?

FastAPI is a **modern, fast (high-performance)** Python web framework used to build **REST APIs**.

### Key Features:

* 🚀 Very fast (built on **Starlette** & **Pydantic**)
* 📄 Automatic **Swagger & ReDoc documentation**
* ✅ Built-in **data validation**
* 🧠 Type-safe using Python type hints
* 🔌 Easy dependency injection


## 1. Quick Setup with `uv` (Faster Alternative to `pip` and `venv`)
`uv` is a **modern Python package manager** (faster than pip + venv).
`uv` is a tool from GitHub for speedy virtual environments and package management. It's great for beginners to avoid setup headaches.

### Steps:
1. **Install `uv`**:
   ```bash
   pip install uv
   ```

2. **Create a Virtual Environment**:
   ```bash
   uv venv
   ```
   - This creates a `.venv` folder in your current directory.
   - Name can be any like `.venv`, `.privatevirtualenv` 

3. **Activate the Virtual Environment**:
   - On Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```
   - Your terminal prompt should now show `(.venv)`.

4. **Install FastAPI (with Standard Extras)**:
   ```bash
   uv pip install "fastapi[standard]"
   ```
   - The `[standard]` includes everything you need: HTTP tools, Uvicorn server, FastAPI core, Mandatory async packages etc.
   - It auto-creates/updates a lockfile for reproducible installs.
   📌 This avoids missing dependency issues.

5. **Save Dependencies** (for sharing your project):
   ```bash
   uv pip freeze > requirements.txt
   ```
   - This exports all installed packages and versions to `requirements.txt`. Others can install with `uv pip install -r requirements.txt`.
   
   📌 `requirements.txt` stores:

   * All installed packages
   * Exact versions
     Used for deployment & sharing projects.

**Tip**: Always work in an activated virtual environment to avoid global pollution.

## 2. Creating Your First FastAPI Server

Start simple: Create an entry file called `main.py`.

### Basic Code (`main.py`):
```python
from fastapi import FastAPI

app = FastAPI()  # Creates your API app instance

@app.get('/')  # Decorator for GET requests to root URL
def root():
    return {"message": "Hello, World!!!"}
```

### Run FastAPI Server:
```bash
uv run fastapi dev main.py
```
- `uv run` executes in your venv without activating it manually.
* 🌐 API Server:
  `http://127.0.0.1:8000`
* 📘 Swagger Docs:
  `http://127.0.0.1:8000/docs`
* 📕 ReDoc Docs:
  `http://127.0.0.1:8000/redoc`

📌 Swagger UI is **auto-generated** by FastAPI.
- Visit `http://127.0.0.1:8000` in your browser for "Hello, World!!!".
- Auto-generated Swagger docs at `http://127.0.0.1:8000/docs` (interactive API playground—super beginner-friendly!).

**Why FastAPI?** It handles routing, validation, and docs out-of-the-box.

## 3. Routing Basics

Routing defines API endpoints (URLs) and HTTP methods (GET, POST, etc.).
### 3.1 Static Route

```python
@app.get("/")
def root():
    return {"message": "Hello FastAPI"}
```
### 3.2 Dynamic Routing (Path Parameters)
Capture parts of the URL as variables/ params (e.g., `/items/5` where `5` is dynamic).

```python
from fastapi import FastAPI

app = FastAPI()

@app.get('/{id}')  # {id} is a path parameter
def root(id: int):  # Type hint: expects an integer
    return {"message": f"Hello, World!!! {id}"}
```
- Test: Visit `http://127.0.0.1:8000/42` → `{"message": "Hello, World!!! 42"}`.
- **Beginner Note**: Type hints (like `int`) auto-validate input—e.g., `/abc` will error if `int` is expected.

📌 `id` is:

* Path parameter
* Automatically validated as `int`

### Query Parameters (e.g., `?name=Alice&age=30`)
These are optional key-value pairs after `?` in the URL.

#### Simple Way (Using `Request`):
```python
from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
def root(request: Request):
    params = request.query_params  # Dict of all query params
    return {"message": "Hello, FastAPI", "params": dict(params)}
```
📌 `request.query_params` returns a dictionary-like object.
- Test: `http://127.0.0.1:8000/?name=Bholeynath&age=25`
- Response: `{"message": "Hello, FastAPI", "params": {"name": "Bholeynath", "age": "25"}}`.

#### [Recommended] Advanced Way (Using Pydantic Models for Validation)
Pydantic is built into FastAPI for data validation. Create a model for structured params.

**Why Use Pydantic?**
* Automatic validation
* Cleaner code
* Type safety
* Better documentation


### Case 1: Mandatory Query Parameters
file: `types.py`
```python
from pydantic import BaseModel

class QueryParams(BaseModel):
    name: str
    age: int
```

📌 If missing → **422 Validation Error (Field Required)**
---
### Case 2: Optional Query Parameters (for reusable models):
**STEP 1:** Create `types.py`

Optional Query Parameters used when:
* Params may or may not exist
* Only one param might be passed

 ```python
   from pydantic import BaseModel
   from typing import Optional  # For optional fields

   class QueryParams(BaseModel):
       name: Optional[str] = None  # Optional string
       age: Optional[int] = None   # Optional integer
   ```
   - **Why Optional?** Params might be missing—without it, you'll get "field required" errors.
   - Test without optional: Sending `?name=Alice` without `age` would fail.

📌 Prevents query error
📌 Allows flexibility

**STEP 2:** Create `main.py` 

 **Use in `main.py`** (with Dependency Injection):
   ```python
   from fastapi import FastAPI, Depends, Request
   from typing import Annotated  # For advanced typing
   from type import QueryParams  # Import your model

   app = FastAPI()

   @app.get("/")
   def root(query: Annotated[QueryParams, Depends()]):  # Injects validated params
       return {
           "message": "Hello, FastAPI",
           "name": query.name,
           "age": query.age
       }
   ```
 **Using `Annotated` + `Depends`:**

   - **What is `Depends()`?** It's FastAPI's way to inject dependencies (like validated params) into functions. Keeps code clean and reusable.
    ### Why `Depends()`?
    * Reusable logic
    * Clean separation of concerns
    * Automatic request parsing

   - **What is `Annotated`?** Adds metadata (here, the dependency) to the type hint for better auto-docs and validation.
   - Test: Same URL as above → Clean response with validated types.
  
    ## Why `Annotated`?
    * Adds metadata to type hints
    * Improves clarity
    * Recommended in modern FastAPI versions

    📌 Combines:

    * Type (`QueryParams`)
    * Dependency (`Depends()`)

**Pro Tip**: Start with simple `Request` for quick tests, switch to Pydantic for production (auto-validation + docs).

## API Creating Rules (Best Practice)

### Step 1:Create Type/ Models

Create `type.py`

```python
class QueryParams(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
```

### Step 2: API Logic

Use in `main.py`

📌 Keeps code modular & reusable
📌 Avoids large `main.py`


### POST Requests (Sending Data)
For creating resources (e.g., adding a todo).

```python
from fastapi import FastAPI
from typing import dict  # Or use Pydantic for better validation

app = FastAPI()

@app.post("/todo")
def create_todo(item: dict):  # Expects JSON body
    return {"message": "Todo created", "item": item}
```
- Test in Swagger docs: Click POST `/todo`, enter JSON like `{"task": "Buy milk"}`.
- **Beginner Note**: Use Pydantic `BaseModel` instead of `dict` for typed validation (e.g., `class Todo(BaseModel): task: str`).

## 4. Recommended Folder Structure

FastAPI apps grow—organize like this for scalability:

```
my_app/
├── app/
│   ├── __init__.py     # Makes 'app' a Python package (importable)
│   ├── config/         # Settings, env vars (e.g., database URLs)
│   ├── models/         # Pydantic models (e.g., type.py for data schemas)
│   ├── routing/        # Route files (e.g., users.py, todos.py)
│   ├── helpers.py      # Utility functions
│   └── app.py          # Main app: Import and include all routes here
├── requirements.txt    # Dependencies
└── .venv/              # Virtual env (git ignore this)
```

- **Why?** Keeps `main.py` lean—import routes into `app.py` for a single entry point.
- Run: `uv run fastapi dev app/app.py` (from project root).

### `__init__.py`

* Treats folder as a package
* Allows imports between files

---

### app.py (Main File)

* Imports all route files
* Registers routers
* Starts FastAPI app

📌 Keeps project scalable and clean.
---

### ✅What is BaseModel in FastAPI / Pydantic?

`BaseModel` comes from Pydantic and is used to **define the structure, type, and validation rules of data.**

In simple words:

`BaseModel` = **a blueprint (schema) for data**

### Why BaseModel is Used
- FastAPI Reads request body, Validates it and Converts it into Python object.
BaseModel helps to:
    - ✅ Validate incoming data
    - 🔍 Automatically check data types
    - ❌ Reject invalid or missing fields
    - 📄 Generate API documentation
    - 🔁 Convert JSON → Python objects
    FastAPI heavily depends on **BaseModel**.

    Incomming Request: 
    ```json
    {
    "name": "Saroj",
    "age": 25
    }
    ✔ Valid → Request accepted
    ```
    Incomming Request: 
    ```json
    {
    "name": "Saroj",
    "age": "twenty"
    }
    ❌ Error → age must be an integer
    ```
