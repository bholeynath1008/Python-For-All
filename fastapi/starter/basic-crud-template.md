# FastAPI Project Setup & Run Guide (Best Practices)

This guide shows **how to correctly structure, configure, and run a FastAPI application**, clearly explaining **which file Uvicorn runs and why**.

---

## Dependency Installation (Required)

Install these dependencies inside a virtual environment:

* **fastapi** – Web framework
* **uvicorn** – ASGI server
* **pydantic** – Data validation (installed automatically)

```bash
pip install fastapi uvicorn
```

---

## Recommended Project Structure (Best Practice)

```
fastapi-starter/
│
├── main.py                  # Uvicorn entry point (ONLY server startup)
│
├── app/
│   ├── __init__.py
│   ├── app.py               # FastAPI app instance
│   ├── routes.py            # API routes
│   ├── schemas.py           # Pydantic models
│   ├── crud.py              # Business logic
│
└── myenv/                   # Virtual environment
```

### Why this structure?

* `main.py` → **Only for running the server**
* `app/` → **Actual application logic**
* Clear separation = scalable, testable, interview-ready

---

## Step-by-Step Setup

---

### 1. Create project folder

```bash
mkdir fastapi-starter
cd fastapi-starter
```

---

### 2. Create a virtual environment

```bash
python -m venv myenv
```

---

### 3. Activate the virtual environment (Windows PowerShell)

```powershell
.\myenv\Scripts\Activate.ps1
```

If execution policy error occurs:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

---

### 4. Install dependencies

```bash
pip install fastapi uvicorn
```

---

## Application Code (Correct Order)

---

### 5.1 Create **FastAPI app instance** (`app/app.py`)

> This file **creates the FastAPI object only**

```python
from fastapi import FastAPI
from app.routes import router

def create_app() -> FastAPI:
    app = FastAPI(title="FastAPI starter")
    app.include_router(router)
    return app
```

✅ Best practice: use an **app factory** (`create_app()`)

*Other simplified way without app factory:*
```python
from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="FastAPI Starter")

app.include_router(router)
```
---

### 5.2 Create **schemas** (`app/schemas.py`)

```python
from pydantic import BaseModel

class ProductItem(BaseModel):
    id: int
    name: str
    description: str
    price: float
    quantity: int
```

---

### 5.3 Create **CRUD logic** (`app/crud.py`)

> Business logic should NEVER be inside routes

```python
from app.schemas import ProductItem

db: list[ProductItem] = []

def get_all_products():
    return db

def create_product(item: ProductItem):
    db.append(item)
    return item
```

---

### 5.4 Create **routes** (`app/routes.py`)

```python
from fastapi import APIRouter
from app.schemas import ProductItem
from app import crud

router = APIRouter()

@router.get("/")
def home():
    return {"message": "FastAPI is running!"}

@router.get("/products")
def get_products():
    return crud.get_all_products()

@router.post("/products")
def add_product(item: ProductItem):
    return crud.create_product(item)
```

✅ Routes only handle **request/response**
✅ Logic lives in `crud.py`

---

### 5.5 Create **Uvicorn entry point** (`main.py`)

> This is the **ONLY file run by Uvicorn**

```python
import uvicorn
from app.app import create_app

app = create_app()

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )
```

✅ Clean
✅ Production-ready
✅ Interview-approved

---

## 6. Run the application

From the project root:

```bash
uvicorn main:app --reload
```

### Command explanation:

* **`main`** → `main.py`
* **`app`** → FastAPI instance inside `main.py`
* **`--reload`** → Auto-restart on file changes (development)

---

## 7. Access the API

* Server:
  [http://127.0.0.1:8000](http://127.0.0.1:8000)

* Home route:
  [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

* Swagger UI:
  [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

* ReDoc:
  [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 8. Stop the server

```text
Ctrl + C
```

---

## 9. Deactivate virtual environment

```bash
deactivate
```

---

## Important Best-Practice Notes

* **Never put business logic in routes**
* **Never start Uvicorn inside route files**
* **Only `main.py` should be used to run the app**
* File name in Uvicorn **must match exactly**

Example:

```bash
uvicorn main:app --reload
```

If file name changes to `server.py`:

```bash
uvicorn server:app --reload
```

## Sample data: 
```python
products = [
{"id": 1, "name": "Phone", "description": "5G smartphone", "price": 699.99, "quantity": 6, "stock": "Y"}
{"id": 2, "name": "Laptop", "description": "14-inch laptop", "price": 1299.00, "quantity": 3, "stock": "Y"}
{"id": 3, "name": "Headphones", "description": "Noise cancelling", "price": 199.99, "quantity": 0, "stock": "N"}
{"id": 4, "name": "Tablet", "description": "10-inch tablet", "price": 499.99, "quantity": 8, "stock": "Y"}
{"id": 5, "name": "Smartwatch", "description": "Fitness tracker", "price": 249.99, "quantity": 2, "stock": "Y"}
]
```

---

If you want next, I can:

* Add **SQLAlchemy + database**
* Add **JWT authentication**
* Add **env config (.env)**
* Convert this into **exam/interview notes**
* Create **production deployment structure (Docker + Gunicorn)**
