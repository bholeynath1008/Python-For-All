# 📘 FastAPI + SQLAlchemy Notes (Beginner Friendly)

---

## 1️⃣ Installation & Environment Setup

### 📌 Create virtual environment (recommended)

```bash
python -m venv venv
venv\Scripts\activate
```

### 📌 Install required packages

```bash
pip install fastapi uvicorn sqlalchemy psycopg2-binary
```

📌 **What each package does**

* **fastapi** → Web framework
* **uvicorn** → ASGI server to run FastAPI
* **sqlalchemy** → ORM (Object Relational Mapper)
* **psycopg2-binary** → PostgreSQL driver

---

## 2️⃣ Project Structure (Best Practice)

```
fastapi-telusko/
│
├── app/
│   ├── __init__.py
│   ├── database.py          # DB connection & session
│   ├── models.py            # SQLAlchemy models
│   ├── schemas.py           # Pydantic schemas
│   ├── crud.py              # Database operations
│   └── main.py              # FastAPI app
│
└── venv/
```

---

## 3️⃣ Database Configuration (`database.py`)

📍 **Purpose:**

* Create DB engine
* Create DB session
* Reuse session using dependency injection

```python
# app/database.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "postgresql://postgres:sanu@localhost:5432/fastapi_db"

# Engine → Manages DB connection
engine = create_engine(DATABASE_URL)

# Session → Used to talk to DB
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Base class for models
Base = declarative_base()
```

### 🔑 Key Concepts

* **engine** → Opens connection to database
* **sessionmaker** → Factory for DB sessions
* **autocommit=False** → Manual control of commits
* **autoflush=False** → Changes are flushed only on commit
* **Base** → Parent class for all DB models

---

## 4️⃣ Database Model (`models.py`)

📍 **Purpose:**
Maps Python class → Database table

```python
# app/models.py

from sqlalchemy import Column, Integer, String, Float
from .database import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String)
    price = Column(Float, nullable=False)
    quantity = Column(Integer, nullable=False)
```

### 🔑 Keyword Explanation

* `__tablename__` → Table name in DB
* `Column` → Represents a column
* `primary_key=True` → Unique identifier
* `index=True` → Faster search
* `nullable=False` → Cannot be empty

---

## 5️⃣ Pydantic Schemas (`schemas.py`)

📍 **Purpose:**

* Validate request data
* Control API response structure

```python
# app/schemas.py

from pydantic import BaseModel

class ProductBase(BaseModel):
    name: str
    description: str | None = None
    price: float
    quantity: int

class ProductCreate(ProductBase):
    pass

class ProductResponse(ProductBase):
    id: int

    class Config:
        orm_mode = True
```

### 🔑 Why Schemas?

* Prevent invalid data
* Separate DB models from API contracts
* `orm_mode=True` allows SQLAlchemy objects → JSON

---

## 6️⃣ CRUD Operations (`crud.py`)

📍 **Purpose:**
Keep DB logic separate from API logic

```python
# app/crud.py

from sqlalchemy.orm import Session
from . import models, schemas

def create_product(db: Session, product: schemas.ProductCreate):
    db_product = models.Product(**product.model_dump())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def get_all_products(db: Session):
    return db.query(models.Product).all()

def get_product_by_id(db: Session, product_id: int):
    return db.query(models.Product).filter(models.Product.id == product_id).first()

def delete_product(db: Session, product_id: int):
    product = get_product_by_id(db, product_id)
    if product:
        db.delete(product)
        db.commit()
    return product
```

### 🔑 Explanation

* `db.add()` → Add record
* `db.commit()` → Save changes
* `db.refresh()` → Fetch updated data
* `filter()` → WHERE clause
* `first()` → Single row

---

## 7️⃣ FastAPI App (`main.py`)

📍 **Purpose:**

* Create API routes
* Inject DB session
* Connect everything

```python
# app/main.py

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from .database import Base, engine, SessionLocal
from . import models, schemas, crud

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="FastAPI Product CRUD")

# Dependency → DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home():
    return {"message": "Welcome to Telusko FastAPI"}

# CREATE
@app.post("/products", response_model=schemas.ProductResponse)
def create_product(
    product: schemas.ProductCreate,
    db: Session = Depends(get_db)
):
    return crud.create_product(db, product)

# READ ALL
@app.get("/products", response_model=list[schemas.ProductResponse])
def get_products(db: Session = Depends(get_db)):
    return crud.get_all_products(db)

# READ ONE
@app.get("/products/{product_id}", response_model=schemas.ProductResponse)
def get_product(product_id: int, db: Session = Depends(get_db)):
    product = crud.get_product_by_id(db, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

# DELETE
@app.delete("/products/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    product = crud.delete_product(db, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"message": "Product deleted successfully"}
```

---

## 8️⃣ Run the Application

```bash
uvicorn app.main:app --reload
```

### 🌐 Access

* API → [http://127.0.0.1:8000](http://127.0.0.1:8000)
* Swagger UI → [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 9️⃣ CRUD Summary

| Operation | HTTP Method | Endpoint         |
| --------- | ----------- | ---------------- |
| Create    | POST        | `/products`      |
| Read All  | GET         | `/products`      |
| Read One  | GET         | `/products/{id}` |
| Delete    | DELETE      | `/products/{id}` |

---


# 📘 FastAPI + SQLAlchemy Complete Beginner Notes (Installation → CRUD)
---

## 1️⃣ Project Setup & Environment

### 📁 Project Folder

```
fastapi-telusko/
```

---

### 🔹 Create Virtual Environment

```bash
python -m venv myenv
```

**Why virtual environment?**

* Keeps project dependencies isolated
* Avoids version conflicts
* Required for professional projects

---

### 🔹 Activate Virtual Environment (Windows)

📍 Activation scripts are inside:

```
myenv\Scripts\
```

#### ✅ PowerShell

```powershell
.\myenv\Scripts\Activate.ps1
```

> ⚠️ `./` is mandatory in PowerShell

#### ✅ CMD

```cmd
myenv\Scripts\activate.bat
```

---

### 🔹 Deactivate Virtual Environment

```bash
deactivate
```

### 🔹 Delete Virtual Environment

Delete the folder:

```
myenv/
```

---

### 🔹 pip list (Before vs After)

#### Before activation

```bash
pip list
```

Shows **all globally installed packages**.

#### After activation

```bash
(myenv) pip list
```

```
Package Version
------- -------
pip     25.1.1
```

✔ Clean environment
✔ Best practice

---

### 🔹 Install FastAPI & Uvicorn

```bash
pip install fastapi uvicorn sqlalchemy psycopg2-binary
```

After install:

```bash
pip list
```

You will see fastapi, uvicorn, pydantic, starlette, sqlalchemy, etc.

---

### 🔹 What is Uvicorn?

Uvicorn is an **ASGI web server**.

**What it does:**

* Runs FastAPI application
* Listens for HTTP requests
* Sends response back to frontend
* Very fast & async‑friendly

📌 **Web server responsibility:**

> Web server’s task is to receive requests from frontend and return data.

---

### 🔹 Run FastAPI App

```bash
uvicorn app.main:app --reload
```

| Part     | Meaning                              |
| -------- | ------------------------------------ |
| app.main | file path                            |
| app      | FastAPI instance (`app = FastAPI()`) |
| --reload | Auto restart server                  |

Access:

* API → [http://127.0.0.1:8000](http://127.0.0.1:8000)
* Swagger → [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 2️⃣ Project Structure (Best Practice)

```
fastapi-telusko/
│
├── app/
│   ├── __init__.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   └── main.py
│
└── myenv/
```

✔ Separation of concerns
✔ Scalable

---

## 3️⃣ Database Configuration (`database.py`)

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "postgresql://postgres:sanu@localhost:5432/fastapi_db"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()
```

### 🔑 Keywords

* **engine** → DB connection
* **sessionmaker** → DB session factory
* **autocommit=False** → manual commit
* **autoflush=False** → flush on commit only
* **Base** → parent for all models

---

## 4️⃣ SQLAlchemy Model (`models.py`)

```python
from sqlalchemy import Column, Integer, String, Float
from .database import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String)
    price = Column(Float, nullable=False)
    quantity = Column(Integer, nullable=False)
```

### 🔑 Keywords

* `__tablename__` → DB table name
* `primary_key=True` → unique ID
* `nullable=False` → required field

---

## 5️⃣ Pydantic Schemas (`schemas.py`)

```python
from pydantic import BaseModel

class ProductBase(BaseModel):
    name: str
    description: str | None = None
    price: float
    quantity: int

class ProductCreate(ProductBase):
    pass

class ProductResponse(ProductBase):
    id: int

    class Config:
        orm_mode = True
```

### Why Schemas?

* Data validation
* Clean API contracts
* Protect DB structure

---

## 6️⃣ CRUD Logic (`crud.py`)

```python
from sqlalchemy.orm import Session
from . import models, schemas

def create_product(db: Session, product: schemas.ProductCreate):
    db_product = models.Product(**product.model_dump())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def get_all_products(db: Session):
    return db.query(models.Product).all()

def get_product_by_id(db: Session, product_id: int):
    return db.query(models.Product).filter(models.Product.id == product_id).first()

def delete_product(db: Session, product_id: int):
    product = get_product_by_id(db, product_id)
    if product:
        db.delete(product)
        db.commit()
    return product
```

### 🔑 Important Line Explained

```python
models.Product(**product.model_dump())
```

* `model_dump()` → Pydantic → dict
* `**` → unpack dictionary
* Converts API input → DB model object

---

## 7️⃣ Dependency Injection (`Depends`)

```python
from fastapi import Depends
```

```python
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

```python
@app.get("/products")
def get_products(db: Session = Depends(get_db)):
    return db.query(Product).all()
```

✔ Auto session creation
✔ Auto closing
✔ No memory leaks

---

## 8️⃣ FastAPI Application (`main.py`)

```python
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from .database import Base, engine, SessionLocal
from . import models, schemas, crud

Base.metadata.create_all(bind=engine)

app = FastAPI(title="FastAPI Product CRUD")

@app.get("/")
def home():
    return {"message": "Welcome to Telusko FastAPI"}
```

---

## 9️⃣ CRUD APIs

### CREATE

```python
@app.post("/products")
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    return crud.create_product(db, product)
```

### READ ALL

```python
@app.get("/products")
def get_products(db: Session = Depends(get_db)):
    return crud.get_all_products(db)
```

### READ ONE

```python
@app.get("/products/{id}")
def get_product(id: int, db: Session = Depends(get_db)):
    return crud.get_product_by_id(db, id)
```

### DELETE

```python
@app.delete("/products/{id}")
def delete_product(id: int, db: Session = Depends(get_db)):
    return crud.delete_product(db, id)
```

---

## 🔟 PUT vs PATCH

### PUT (Full Update)

* Updates entire object
* Missing fields overwritten

### PATCH (Partial Update)

* Updates only provided fields

```python
@app.patch("/products/{id}")
def patch_product(id: int, product: schemas.ProductBase, db: Session = Depends(get_db)):
    db_product = crud.get_product_by_id(db, id)
    for key, value in product.model_dump(exclude_unset=True).items():
        setattr(db_product, key, value)
    db.commit()
    db.refresh(db_product)
    return db_product
```

---

## 1️⃣1️⃣ HTTP Method Summary

| Method | Purpose        |
| ------ | -------------- |
| POST   | Create         |
| GET    | Read           |
| PUT    | Full Update    |
| PATCH  | Partial Update |
| DELETE | Delete         |

---

## ✅ Final Best Practices

✔ Virtual environment
✔ Clean architecture
✔ Dependency injection
✔ Separate DB / API / Logic
✔ Beginner‑friendly & production‑ready

---


