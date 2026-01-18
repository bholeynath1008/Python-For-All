# 📚 FastAPI + SQLAlchemy Database Connection Guide
### This contains `guide`, `basic rules` and `templates` for sql connection.
## 📋 Table of Contents

### 🚀 Getting Started
1. [Quick Start Guide](#quick-start-guide)
2. [Detailed Step-by-Step Guide](#detailed-step-by-step-guide)
3. [File Structure Reference](#file-structure-reference)

### 📖 Core Concepts
4. [The 6-Step Connection Flow](#the-6-step-connection-flow)
5. [Visual Architecture](#visual-architecture)
6. [Key Concepts Explained](#key-concepts-explained)

### 💡 Best Practices
7. [Best Practices Checklist](#best-practices-checklist)
8. [Common Patterns](#common-patterns)
9. [Performance Optimization](#performance-optimization)

### 🔧 Troubleshooting
10. [Debugging Guide](#debugging-guide)
11. [Common Errors & Solutions](#common-errors-solutions)
12. [Testing Practices](#testing-practices)

### 📚 Reference
13. [Ultimate Analogy Cheatsheet](#ultimate-analogy-cheatsheet)
14. [Copy-Paste Template](#copy-paste-template)
15. [Critical Reminders](#critical-reminders)

---

## Quick Start Guide

### The Golden Rule
**One Engine → One SessionLocal Factory → Many Temporary Sessions (one per request)**

### Minimum Required Steps and Templates (Follow this Template if confusion:)
```python
# 1. Create Engine (Once)
from sqlalchemy import create_engine
engine = create_engine("postgresql://user:pass@localhost/db")

# 2. Create Base (Once)
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

# 3. Define Models (Once per table)
from sqlalchemy import Column, Integer, String
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)

# 4. Create SessionLocal Factory (Once)
from sqlalchemy.orm import sessionmaker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 5. Create Tables (Once, at startup)
Base.metadata.create_all(bind=engine)

# 6. Dependency Function (Use in routes)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 7. In Routes (Every endpoint)
from fastapi import Depends
from sqlalchemy.orm import Session

@app.get("/users")
def get_users(db: Session = Depends(get_db)):
    return db.query(User).all()
```

---

## Detailed Step-by-Step Guide

### STEP 1: Create Engine (The Connection Pool Manager)

**File: `database/engine.py`**

```python
from sqlalchemy import create_engine
import os

# Database URL format: dialect://username:password@host:port/database
# PostgreSQL: postgresql://user:pass@localhost:5432/mydb
# MySQL: mysql://user:pass@localhost:3306/mydb
# SQLite: sqlite:///./database.db or sqlite:///:memory:

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:password@localhost:5432/fastapi_db")

# Create the engine - ONE per application
engine = create_engine(
    DATABASE_URL,
    
    # Connection Pool Settings
    pool_size=20,              # Maximum 20 connections in pool
    max_overflow=0,            # No extra connections beyond pool_size
    pool_timeout=30,           # Wait 30 seconds for available connection
    pool_recycle=1800,         # Recycle connections after 30 minutes
    
    # Safety & Performance
    pool_pre_ping=True,        # Test connection before using (prevents stale connections)
    
    # Debugging (Development only!)
    echo=True,                 # Log all SQL queries to console
    echo_pool="debug",         # Log connection pool events
    hide_parameters=False,     # Show query parameters in logs
)
```

**What the Engine Does:**
- Manages a pool of database connections (reuses connections for efficiency)
- Translates Python code to database-specific SQL
- Handles connection lifecycle (open, close, recycle)
- **Critical:** Create only ONE engine per application

**Key Parameters Explained:**

| Parameter | Purpose | Recommendation |
|-----------|---------|----------------|
| `pool_size` | Max connections kept open | 20 for most apps |
| `pool_pre_ping` | Test connection before use | Always `True` |
| `pool_recycle` | Refresh old connections | 1800 (30 min) |
| `echo` | Log SQL queries | `True` in dev, `False` in prod |

---

### STEP 2: Create Base Model (The Parent Class)

**File: `models/base.py`**

```python
from sqlalchemy.ext.declarative import declarative_base

# Create the base class - ALL models inherit from this
Base = declarative_base()

# This Base tracks:
# - All table definitions
# - Relationships between tables
# - Metadata for creating/dropping tables
```

**Why Base?**
- Provides a registry of all your models/tables
- Enables `Base.metadata.create_all()` to create all tables at once
- Manages relationships between models
- Every model class MUST inherit from this Base

---

### STEP 3: Define Models (The Table Definitions)

**File: `models/product.py`**

```python
from sqlalchemy import Column, Integer, String, Float, Index
from .base import Base

class Product(Base):
    __tablename__ = "products"  # REQUIRED: actual table name in database
    
    # Primary Key - Required for every table
    id = Column(Integer, primary_key=True, index=True)
    # primary_key=True: Unique identifier, usually auto-incrementing
    # index=True: Creates database index for fast lookups
    
    # String columns
    name = Column(String(100), nullable=False, index=True)
    # String(100): Maximum 100 characters
    # nullable=False: Required field (NOT NULL in SQL)
    # index=True: Fast searches by name
    
    description = Column(String(500))  # Optional field
    
    # Numeric columns
    price = Column(Float, nullable=False)
    quantity = Column(Integer, default=0)
    # default=0: Value if not provided
    
    # Advanced: Composite indexes
    __table_args__ = (
        Index('idx_name_price', 'name', 'price'),  # Index on multiple columns
    )
```

**When to Use `index=True`:**

✅ **Always index:**
- Primary keys (`id`)
- Foreign keys
- Frequently searched columns (`email`, `username`)
- Columns in WHERE clauses
- Columns used in JOIN operations

❌ **Don't index:**
- Rarely searched columns
- Columns with few unique values (e.g., `is_active`)
- Large text fields (unless using full-text search)

**Performance Impact:**
- Indexes speed up reads (SELECT) by 10-100x
- Indexes slow down writes (INSERT/UPDATE) by ~10-20%
- Use strategically based on your query patterns

---

### STEP 4: Create SessionLocal Factory

**File: `database/session.py`**

```python
from sqlalchemy.orm import sessionmaker, Session
from .engine import engine

# SessionLocal is a FACTORY, not a session
# Calling SessionLocal() creates a NEW session
SessionLocal = sessionmaker(
    autocommit=False,    # We control when to commit
    autoflush=False,     # We control when to flush
    bind=engine,         # Connect to our engine
    expire_on_commit=True,  # Clear cache after commit
    class_=Session,      # Type of session to create
)
```

**Critical Settings Explained:**

#### `autocommit=False` (RECOMMENDED)
```python
# With autocommit=False (SAFE - Recommended)
def transfer_money(db: Session):
    account1.balance -= 100  # Tracked, not saved yet
    account2.balance += 100  # Tracked, not saved yet
    
    try:
        db.commit()  # Both saved together (atomic)
    except:
        db.rollback()  # Neither saved (all-or-nothing)

# With autocommit=True (DANGEROUS - Not recommended)
def transfer_money(db: Session):
    account1.balance -= 100  # IMMEDIATELY SAVED!
    # If crash here, money deducted but not added!
    account2.balance += 100  # Never reaches this line
```

#### `autoflush=False` (RECOMMENDED)
```python
# With autoflush=False (FASTER - Recommended)
db.query(User).filter(User.id == 1).first()
# Executes immediately without checking for pending changes

# With autoflush=True (SLOWER)
db.query(User).filter(User.id == 1).first()
# First flushes ALL pending changes, then executes query
# Unnecessary overhead for most queries
```

**What is Flush vs Commit?**
- **Flush**: Send Python changes to database (but don't save permanently)
- **Commit**: Save changes permanently to database
- Usually you just need commit; flush is handled automatically when needed

---

### STEP 5: Create Tables in Database

**File: `main.py`**

```python
from fastapi import FastAPI
from models.base import Base
from database.engine import engine
from models import product, user  # Import all models!

app = FastAPI()

# Create tables at startup (development)
@app.on_event("startup")
def create_tables():
    Base.metadata.create_all(bind=engine)
    # Creates ALL tables defined in models
    # Safe to run multiple times (won't recreate existing tables)
    # Does NOT delete or modify existing data

# Alternative: Run once manually
if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
```

**When to Run:**
- ✅ First time setting up database
- ✅ After adding new models/tables
- ✅ After changing table structure (in development)
- ❌ Every request (too slow!)
- ⚠️ Production: Use migrations (Alembic) instead

---

### STEP 6: Dependency Injection (The Session Manager)

**File: `dependencies/database.py`**

```python
from database.session import SessionLocal
from sqlalchemy.orm import Session
from typing import Generator

def get_database_session() -> Generator[Session, None, None]:
    """
    Dependency that creates a new database session for each request.
    
    Flow:
    1. Create new session (SessionLocal())
    2. Yield session to route function
    3. Route function uses session
    4. Finally block closes session (even if error occurs)
    """
    db_session = SessionLocal()  # Create NEW session
    
    try:
        yield db_session  # Give session to route function
        # FastAPI pauses here while route executes
        
    except Exception as e:
        # On error: rollback any uncommitted changes
        db_session.rollback()
        raise e
        
    finally:
        # ALWAYS close session to release connection
        db_session.close()
        # Critical: Returns connection to pool for reuse
```

**How It Works Per Request:**

```
User Request
    ↓
FastAPI calls get_database_session()
    ↓
Creates NEW session: SessionLocal()
    ↓
Yields session to route function
    ↓
Route executes: db.query(...)
    ↓
Route returns response
    ↓
FINALLY block executes: db_session.close()
    ↓
Connection returned to pool
    ↓
Response sent to user
```

---

## The 6-Step Connection Flow

### Complete Flow Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                    APPLICATION STARTUP                       │
│                                                              │
│  1. Create Engine         → Connects to DATABASE_URL        │
│  2. Create Base           → Parent class for models         │
│  3. Define Models         → Inherit from Base               │
│  4. Create SessionLocal   → Bound to Engine                 │
│  5. Create Tables         → Base.metadata.create_all()      │
│                                                              │
└─────────────────────────────────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│                     FOR EACH REQUEST                         │
│                                                              │
│  6. Dependency Injection:                                    │
│     a. SessionLocal() creates new session                    │
│     b. Yield session to route function                       │
│     c. Route uses session: db.query(...)                     │
│     d. Finally: session.close()                              │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

## Visual Architecture

### Complete Binding Diagram

```
┌────────────────────────────────────────────────────────────────┐
│                         APPLICATION                             │
│                                                                 │
│  ┌─────────────────┐           ┌─────────────────┐            │
│  │  DATABASE_URL   │           │   Base (Meta)   │            │
│  │"postgresql://..." │           │declarative_base()│            │
│  └────────┬────────┘           └────────┬────────┘            │
│           │                             │                     │
│           ▼ BIND                        │ INHERIT             │
│  ┌─────────────────┐           ┌────────▼────────┐            │
│  │     ENGINE      │◄──────────│    MODELS       │            │
│  │ create_engine() │           │ Product, User   │            │
│  └────────┬────────┘           └─────────────────┘            │
│           │                                                    │
│           │ BIND via sessionmaker(bind=engine)                │
│           ▼                                                    │
│  ┌─────────────────┐                                          │
│  │  SessionLocal   │──Factory──►┌──────────────────────────┐ │
│  │  sessionmaker() │            │ FOR EACH REQUEST:        │ │
│  └─────────────────┘            │ 1. SessionLocal() → db   │ │
│                                 │ 2. Use in route          │ │
│                                 │ 3. db.close()            │ │
│                                 └──────────────────────────┘ │
└────────────────────────────────────────────────────────────────┘
```

---

## Key Concepts Explained

### What is `db` in Route Functions?

```python
@app.get("/products")
def get_products(db: Session = Depends(get_database_session)):
    # ❌ db is NOT "the database"
    # ✅ db IS "a temporary session with the database"
    
    # db = Communication channel
    # db = Created fresh for THIS request
    # db = Automatically closed after response
    # db = Tracks changes until you commit()
    
    return db.query(Product).all()
```

### Session Lifecycle

```python
# Session Creation
db = SessionLocal()  # New session created

# Session Usage
product = db.query(Product).filter(Product.id == 1).first()  # Read
product.price = 99.99  # Modify (tracked, not saved)
db.add(new_product)  # Add (tracked, not saved)

# Session Commit
db.commit()  # Save all changes permanently

# Session Rollback (on error)
try:
    db.query(...)
    db.commit()
except:
    db.rollback()  # Undo all tracked changes

# Session Close
db.close()  # ALWAYS close to release connection
```

### Why Temporary Sessions Per Request?

**Bad (Shared Session):**
```python
# ❌ GLOBAL SESSION (NEVER DO THIS!)
global_db = SessionLocal()  # Created once

@app.get("/products")
def get_products():
    # Multiple concurrent requests share same session
    # Changes from one request affect another
    # Data corruption!
    return global_db.query(Product).all()
```

**Good (Temporary Session):**
```python
# ✅ NEW SESSION PER REQUEST
@app.get("/products")
def get_products(db: Session = Depends(get_database_session)):
    # Request 1 gets Session A (isolated)
    # Request 2 gets Session B (isolated)
    # No interference between requests
    return db.query(Product).all()
```

---

## File Structure Reference

### Recommended Project Structure

```
fastapi-project/
│
├── 📄 main.py                          # FastAPI app & startup
│
├── 📁 database/
│   ├── 📄 __init__.py
│   ├── 📄 engine.py                    # Engine configuration
│   └── 📄 session.py                   # SessionLocal factory
│
├── 📁 models/
│   ├── 📄 __init__.py
│   ├── 📄 base.py                      # Base = declarative_base()
│   ├── 📄 product.py                   # Product model
│   └── 📄 user.py                      # User model
│
├── 📁 schemas/
│   ├── 📄 __init__.py
│   ├── 📄 product.py                   # Pydantic schemas
│   └── 📄 user.py                      # Pydantic schemas
│
├── 📁 dependencies/
│   ├── 📄 __init__.py
│   └── 📄 database.py                  # get_database_session()
│
├── 📁 api/
│   └── 📁 routes/
│       ├── 📄 __init__.py
│       ├── 📄 products.py              # Product endpoints
│       └── 📄 users.py                 # User endpoints
│
├── 📄 .env                              # Environment variables
├── 📄 .env.example                      # Environment template
└── 📄 requirements.txt                  # Dependencies
```

### File Contents Quick Reference

**database/engine.py:**
```python
from sqlalchemy import create_engine
import os

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL, pool_pre_ping=True)
```

**models/base.py:**
```python
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
```

**database/session.py:**
```python
from sqlalchemy.orm import sessionmaker
from .engine import engine

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
```

**dependencies/database.py:**
```python
from database.session import SessionLocal

def get_database_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

**main.py:**
```python
from fastapi import FastAPI
from models.base import Base
from database.engine import engine

app = FastAPI()

@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)
```

---

## Best Practices Checklist

### ✅ Mandatory Practices

#### 1. One Engine Per Application
```python
# ✅ CORRECT: Create once at module level
# database/engine.py
engine = create_engine(DATABASE_URL)

# ❌ WRONG: Creating multiple engines
def get_engine():
    return create_engine(DATABASE_URL)  # New engine each time!
```

#### 2. Always Close Sessions
```python
# ✅ CORRECT: Using dependency with finally
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()  # Always closes

# ❌ WRONG: Forgetting to close
def get_db():
    return SessionLocal()  # Never closed! Memory leak!
```

#### 3. Handle Rollbacks
```python
# ✅ CORRECT: Rollback on error
try:
    db.add(new_item)
    db.commit()
except Exception:
    db.rollback()  # Undo changes
    raise

# ❌ WRONG: No rollback
try:
    db.add(new_item)
    db.commit()
except Exception:
    raise  # Session left in bad state!
```

#### 4. Use autocommit=False
```python
# ✅ CORRECT: Explicit commits
SessionLocal = sessionmaker(autocommit=False, bind=engine)

# Route:
db.add(item)
db.commit()  # We control when to save

# ❌ WRONG: autocommit=True (dangerous)
SessionLocal = sessionmaker(autocommit=True, bind=engine)
# Changes saved immediately, can't rollback!
```

#### 5. Enable Connection Testing
```python
# ✅ CORRECT: Test connections before use
engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True  # Prevents stale connections
)

# ❌ WRONG: No testing
engine = create_engine(DATABASE_URL)
# May use stale/broken connections
```

---

## Common Patterns

### Pattern 1: CRUD Operations

```python
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from dependencies.database import get_database_session
from models.product import Product
from schemas.product import ProductCreate, ProductUpdate

router = APIRouter()

# CREATE
@router.post("/products")
def create_product(
    product: ProductCreate,
    db: Session = Depends(get_database_session)
):
    db_product = Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)  # Get ID and defaults
    return db_product

# READ (Single)
@router.get("/products/{product_id}")
def get_product(
    product_id: int,
    db: Session = Depends(get_database_session)
):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

# READ (List)
@router.get("/products")
def list_products(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_database_session)
):
    products = db.query(Product).offset(skip).limit(limit).all()
    return products

# UPDATE
@router.put("/products/{product_id}")
def update_product(
    product_id: int,
    product_update: ProductUpdate,
    db: Session = Depends(get_database_session)
):
    db_product = db.query(Product).filter(Product.id == product_id).first()
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    for key, value in product_update.dict(exclude_unset=True).items():
        setattr(db_product, key, value)
    
    db.commit()
    db.refresh(db_product)
    return db_product

# DELETE
@router.delete("/products/{product_id}")
def delete_product(
    product_id: int,
    db: Session = Depends(get_database_session)
):
    db_product = db.query(Product).filter(Product.id == product_id).first()
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    db.delete(db_product)
    db.commit()
    return {"message": "Product deleted"}
```

### Pattern 2: Complex Queries

```python
# Filtering
products = db.query(Product).filter(
    Product.price > 100,
    Product.quantity > 0
).all()

# Ordering
products = db.query(Product).order_by(Product.price.desc()).all()

# Limiting
products = db.query(Product).limit(10).all()

# Pagination
page = 1
page_size = 20
products = db.query(Product).offset((page - 1) * page_size).limit(page_size).all()

# Count
total = db.query(Product).count()

# Select specific columns
results = db.query(Product.name, Product.price).all()

# Joins (with relationships defined)
from sqlalchemy.orm import joinedload
products = db.query(Product).options(joinedload(Product.category)).all()
```

### Pattern 3: Bulk Operations

```python
# Bulk insert
products = [
    Product(name="Item 1", price=10),
    Product(name="Item 2", price=20),
    Product(name="Item 3", price=30),
]
db.bulk_save_objects(products)
db.commit()

# Bulk update
db.query(Product).filter(Product.price < 10).update(
    {"price": 15},
    synchronize_session=False
)
db.commit()

# Bulk delete
db.query(Product).filter(Product.quantity == 0).delete()
db.commit()
```

---

## Performance Optimization

### 1. Index Strategic Columns

```python
class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)  # Frequently searched
    username = Column(String, index=True)  # Frequently searched
    full_name = Column(String)  # Not indexed (rarely searched alone)
    
    # Composite index for common query patterns
    __table_args__ = (
        Index('idx_user_email_username', 'email', 'username'),
    )
```

### 2. Use Connection Pooling Wisely

```python
# For small apps (< 100 concurrent users)
engine = create_engine(
    DATABASE_URL,
    pool_size=5,
    max_overflow=10
)

# For medium apps (100-1000 concurrent users)
engine = create_engine(
    DATABASE_URL,
    pool_size=20,
    max_overflow=20
)

# For large apps (1000+ concurrent users)
engine = create_engine(
    DATABASE_URL,
    pool_size=50,
    max_overflow=50,
    pool_recycle=3600  # 1 hour
)
```

### 3. Optimize Queries

```python
# ❌ N+1 Query Problem
products = db.query(Product).all()
for product in products:
    print(product.category.name)  # Separate query for each product!

# ✅ Eager Loading (Single Query)
from sqlalchemy.orm import joinedload
products = db.query(Product).options(
    joinedload(Product.category)
).all()

# ✅ Select Only Needed Columns
# Instead of loading entire objects
results = db.query(Product.id, Product.name).all()

# ✅ Use Pagination
def get_products_paginated(db: Session, page: int = 1, size: int = 50):
    return db.query(Product).offset((page - 1) * size).limit(size).all()
```

### 4. Monitor Query Performance

```python
# Enable query logging in development
engine = create_engine(
    DATABASE_URL,
    echo=True,  # See all queries
    echo_pool="debug"  # See pool events
)

# Use EXPLAIN for slow queries
from sqlalchemy import text
result = db.execute(text("EXPLAIN ANALYZE SELECT * FROM products WHERE price > 100"))
print(result.fetchall())
```

---

## Debugging Guide

### Enable SQL Logging

```python
# Method 1: At engine creation
engine = create_engine(
    DATABASE_URL,
    echo=True,  # Logs all SQL statements
    echo_pool="debug"  # Logs connection pool events
)

# Method 2: Via logging module
import logging
logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)
```

### Debug Session State

```python
def debug_session_info(db: Session):
    """Print session state for debugging"""
    print(f"Session ID: {id(db)}")
    print(f"Is active: {db.is_active}")
    print(f"Is dirty (modified): {len(db.dirty)} objects")
    print(f"Is new (added): {len(db.new)} objects")
    print(f"Is deleted: {len(db.deleted)} objects")
    
    # Show modified objects
    for obj in db.dirty:
        print(f"Modified: {obj}")
    
    # Show new objects
    for obj in db.new:
        print(f"New: {obj}")
```

### Monitor Connection Pool

```python
from sqlalchemy import event

@event.listens_for(engine, "connect")
def receive_connect(dbapi_conn, connection_record):
    print(f"New connection: {id(dbapi_conn)}")

@event.listens_for(engine, "close")
def receive_close(dbapi_conn, connection_record):
    print(f"Closed connection: {id(dbapi_conn)}")

@event.listens_for(engine, "checkout")
def receive_checkout(dbapi_conn, connection_record, connection_proxy):
    print(f"Connection checked out from pool: {id(dbapi_conn)}")

@event.listens_for(engine, "checkin")
def receive_checkin(dbapi_conn, connection_record):
    print(f"Connection checked in to pool: {id(dbapi_conn)}")
```

### Check Database Connections

```python
# For PostgreSQL
@app.get("/debug/connections")
def get_active_connections(db: Session = Depends(get_database_session)):
    from sqlalchemy import text
    result = db.execute(text("""
        SELECT count(*) 
        FROM pg_stat_activity 
        WHERE datname = current_database()
    """))
    return {"active_connections": result.scalar()}
```

---

## Common Errors & Solutions

### Error 1: "This Session's transaction has been rolled back"

**Cause:** Trying to use session after an error without rollback

```python
# ❌ WRONG
try:
    db.query(Product).all()
    # Error occurs
except:
    db.query(User).all()  # Session still in bad state!

# ✅ CORRECT
try:
    db.query(Product).all()
except:
    db.rollback()  # Reset session
    db.query(User).all()  # Now it works
```

### Error 2: "QueuePool limit exceeded"

**Cause:** Too many connections, not closing sessions

```python
# ❌ WRONG
@app.get("/products")
def get_products():
    db = SessionLocal()
    products = db.query(Product).all()
    # Forgot to close!
    return products

# ✅ CORRECT
@app.get("/products")
def get_products(db: Session = Depends(get_database_session)):
    return db.query(Product).all()
    # Automatically closed by dependency
```

### Error 3: "Can't reconnect until invalid transaction is rolled back"

**Cause:** Connection died during transaction

```python
# ✅ SOLUTION: Enable pool_pre_ping
engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True  # Test connection before use
)
```

### Error 4: "Instance is not bound to a Session"

**Cause:** Trying to access relationship after session closed

```python
# ❌ WRONG
@app.get("/products/{id}")
def get_product(id: int, db: Session = Depends(get_database_session)):
    product = db.query(Product).filter(Product.id == id).first()
    return product
# Session closed here, then FastAPI tries to serialize product.category
# Error! Relationship not loaded

# ✅ CORRECT - Method 1: Eager load
from sqlalchemy.orm import joinedload

@app.get("/products/{id}")
def get_product(id: int, db: Session = Depends(get_database_session)):
    product = db.query(Product).options(
        joinedload(Product.category)
    ).filter(Product.id == id).first()
    return product

# ✅ CORRECT - Method 2: Use Pydantic schemas
from pydantic import BaseModel

class ProductResponse(BaseModel):
    id: int
    name: str
    price: float
    
    class Config:
        from_attributes = True

@app.get("/products/{id}", response_model=ProductResponse)
def get_product(id: int, db: Session = Depends(get_database_session)):
    product = db.query(Product).filter(Product.id == id).first()
    return product  # Pydantic converts while session is active
```

### Error 5: "DetachedInstanceError"

**Cause:** Accessing object after session closed

```python
# ❌ WRONG
def get_product_name(product_id: int):
    db = SessionLocal()
    product = db.query(Product).get(product_id)
    db.close()
    return product.name  # Error! Object detached from session

# ✅ CORRECT - Access while session open
def get_product_name(product_id: int):
    db = SessionLocal()
    try:
        product = db.query(Product).get(product_id)
        name = product.name  # Access before close
        return name
    finally:
        db.close()
```

---

## Testing Practices

### Test Database Setup

**Option 1: In-Memory SQLite (Fast, Isolated)**

```python
# conftest.py
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi.testclient import TestClient

from database.session import SessionLocal
from models.base import Base
from main import app
from dependencies.database import get_database_session

# Test database URL (in-memory)
TEST_DATABASE_URL = "sqlite:///:memory:"

# Create test engine
test_engine = create_engine(
    TEST_DATABASE_URL,
    connect_args={"check_same_thread": False}  # For SQLite only
)

# Create test session factory
TestSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=test_engine)

@pytest.fixture(scope="function")
def test_db():
    """Create fresh database for each test"""
    # Create all tables
    Base.metadata.create_all(bind=test_engine)
    
    # Create session
    db = TestSessionLocal()
    
    try:
        yield db
    finally:
        db.close()
        # Drop all tables after test
        Base.metadata.drop_all(bind=test_engine)

@pytest.fixture(scope="function")
def client(test_db):
    """FastAPI test client with test database"""
    def override_get_db():
        try:
            yield test_db
        finally:
            pass  # Don't close, fixture handles it
    
    app.dependency_overrides[get_database_session] = override_get_db
    
    with TestClient(app) as test_client:
        yield test_client
    
    app.dependency_overrides.clear()
```

**Option 2: Separate Test Database (More Realistic)**

```python
# conftest.py
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Separate test database
TEST_DATABASE_URL = "postgresql://postgres:password@localhost:5432/test_db"

test_engine = create_engine(TEST_DATABASE_URL)
TestSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=test_engine)

@pytest.fixture(scope="session", autouse=True)
def setup_test_database():
    """Create tables once for all tests"""
    Base.metadata.create_all(bind=test_engine)
    yield
    Base.metadata.drop_all(bind=test_engine)

@pytest.fixture(scope="function")
def test_db():
    """Rollback after each test"""
    connection = test_engine.connect()
    transaction = connection.begin()
    db = TestSessionLocal(bind=connection)
    
    yield db
    
    db.close()
    transaction.rollback()
    connection.close()
```

### Writing Tests

**Test CRUD Operations:**

```python
# test_products.py
import pytest
from models.product import Product
from schemas.product import ProductCreate

def test_create_product(client, test_db):
    """Test creating a product"""
    response = client.post(
        "/products",
        json={"name": "Test Product", "price": 29.99, "quantity": 10}
    )
    
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Test Product"
    assert data["price"] == 29.99
    
    # Verify in database
    db_product = test_db.query(Product).filter(Product.name == "Test Product").first()
    assert db_product is not None
    assert db_product.quantity == 10

def test_get_product(client, test_db):
    """Test retrieving a product"""
    # Create test data
    product = Product(name="Test Product", price=19.99, quantity=5)
    test_db.add(product)
    test_db.commit()
    test_db.refresh(product)
    
    # Test endpoint
    response = client.get(f"/products/{product.id}")
    assert response.status_code == 200
    
    data = response.json()
    assert data["id"] == product.id
    assert data["name"] == "Test Product"

def test_update_product(client, test_db):
    """Test updating a product"""
    # Create test data
    product = Product(name="Old Name", price=10.00, quantity=1)
    test_db.add(product)
    test_db.commit()
    test_db.refresh(product)
    
    # Update
    response = client.put(
        f"/products/{product.id}",
        json={"name": "New Name", "price": 15.00}
    )
    assert response.status_code == 200
    
    # Verify
    test_db.refresh(product)
    assert product.name == "New Name"
    assert product.price == 15.00

def test_delete_product(client, test_db):
    """Test deleting a product"""
    # Create test data
    product = Product(name="To Delete", price=5.00, quantity=1)
    test_db.add(product)
    test_db.commit()
    product_id = product.id
    
    # Delete
    response = client.delete(f"/products/{product_id}")
    assert response.status_code == 200
    
    # Verify deleted
    deleted_product = test_db.query(Product).filter(Product.id == product_id).first()
    assert deleted_product is None
```

**Test Error Handling:**

```python
def test_get_nonexistent_product(client):
    """Test 404 for nonexistent product"""
    response = client.get("/products/99999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Product not found"

def test_create_invalid_product(client):
    """Test validation errors"""
    response = client.post(
        "/products",
        json={"name": "Test"}  # Missing required price field
    )
    assert response.status_code == 422  # Validation error
```

**Test Database Constraints:**

```python
def test_unique_constraint(test_db):
    """Test database unique constraint"""
    # Create first product
    product1 = Product(name="Unique", price=10.00)
    test_db.add(product1)
    test_db.commit()
    
    # Try to create duplicate (if unique constraint exists)
    from sqlalchemy.exc import IntegrityError
    
    product2 = Product(name="Unique", price=20.00)
    test_db.add(product2)
    
    with pytest.raises(IntegrityError):
        test_db.commit()
    
    test_db.rollback()  # Clean up
```

**Test Transactions:**

```python
def test_rollback_on_error(test_db):
    """Test that errors trigger rollback"""
    initial_count = test_db.query(Product).count()
    
    try:
        product = Product(name="Test", price=10.00)
        test_db.add(product)
        test_db.flush()  # Send to database but don't commit
        
        # Simulate error
        raise ValueError("Simulated error")
        
    except ValueError:
        test_db.rollback()
    
    # Verify nothing was saved
    final_count = test_db.query(Product).count()
    assert final_count == initial_count
```

### Testing Best Practices

**1. Isolate Tests**
```python
# Use function scope for database fixtures
@pytest.fixture(scope="function")  # New DB for each test
def test_db():
    # Setup
    yield db
    # Teardown
```

**2. Use Factories for Test Data**
```python
# factories.py
from faker import Faker
from models.product import Product

fake = Faker()

class ProductFactory:
    @staticmethod
    def create(**kwargs):
        defaults = {
            "name": fake.word(),
            "price": fake.pyfloat(min_value=1, max_value=1000, right_digits=2),
            "quantity": fake.random_int(min=0, max=100)
        }
        defaults.update(kwargs)
        return Product(**defaults)

# In tests:
def test_with_factory(test_db):
    product = ProductFactory.create(name="Specific Name")
    test_db.add(product)
    test_db.commit()
```

**3. Test Database Migrations**
```python
# If using Alembic
def test_migration_up_down():
    """Test migrations work both ways"""
    from alembic import command
    from alembic.config import Config
    
    config = Config("alembic.ini")
    
    # Upgrade
    command.upgrade(config, "head")
    
    # Downgrade
    command.downgrade(config, "base")
    
    # Upgrade again
    command.upgrade(config, "head")
```

---

## Ultimate Analogy Cheatsheet

### Core Components as Real-World Systems

| Component | Analogy | What It Does | Key Rule |
|-----------|---------|--------------|----------|
| **DATABASE_URL** | Home Address | GPS coordinates to find database | Format: `dialect://user:pass@host:port/dbname` |
| **Engine** | City's Water Plant | Manages all water (connections) distribution | **ONE per application** |
| **Base** | Building Code Standard | Rules all buildings must follow | All models inherit from this |
| **SessionLocal** | Car Rental Company | Rents out cars (sessions) | Factory that creates sessions |
| **Session** | Rental Car | Your temporary vehicle | Use it, return it (close) |
| **get_database_session()** | Rental Service Agent | Gets car, gives to you, takes it back | Dependency function |
| **db** (in routes) | The Car Keys | Access to drive (query) the car | One per request |

### Detailed Analogies

#### 1. **Connection Pool = Restaurant Kitchen**

```
Restaurant Analogy:
┌─────────────────────────────────────────┐
│           RESTAURANT KITCHEN            │
│                                         │
│  Chefs = Database Connections          │
│  ├─ pool_size=20 → 20 chefs hired      │
│  ├─ max_overflow=10 → Can hire 10 temp │
│  └─ pool_timeout=30 → Wait 30s for chef│
│                                         │
│  Customers = Requests                   │
│  ├─ Request comes in                    │
│  ├─ Get available chef (connection)     │
│  ├─ Chef cooks (executes query)         │
│  └─ Chef returns to pool (reusable)     │
└─────────────────────────────────────────┘
```

#### 2. **Session Lifecycle = Library Book Checkout**

```
Library Analogy:
┌──────────────────────────────────────────────┐
│  1. SessionLocal() = Check out book          │
│     "I need a book to read"                  │
│                                              │
│  2. db.query() = Read the book               │
│     "I'm reading chapters"                   │
│                                              │
│  3. db.add() = Make notes (tracked)          │
│     "I'm marking pages, not permanent"       │
│                                              │
│  4. db.commit() = Buy the book               │
│     "Changes become permanent"               │
│                                              │
│  5. db.rollback() = Return book unchanged    │
│     "Discard all my notes"                   │
│                                              │
│  6. db.close() = Return book to library      │
│     "MUST return for others to use"          │
└──────────────────────────────────────────────┘
```

#### 3. **autocommit=False = Manual vs Automatic Transmission**

```
Manual Transmission (autocommit=False) ✅
┌────────────────────────────────────────┐
│  You control when to shift gears       │
│  ├─ Step on clutch (start transaction) │
│  ├─ Change gear (make changes)         │
│  ├─ Release clutch (commit)            │
│  └─ Can cancel mid-shift (rollback)    │
│                                        │
│  Benefits: Full control, can undo     │
└────────────────────────────────────────┘

Automatic Transmission (autocommit=True) ❌
┌────────────────────────────────────────┐
│  Car decides when to shift              │
│  ├─ Each change = immediate shift       │
│  ├─ Can't cancel mid-operation          │
│  └─ If crash mid-shift = partial damage │
│                                        │
│  Problem: Can't undo, risky            │
└────────────────────────────────────────┘
```

#### 4. **Index = Book's Table of Contents**

```
Without Index (index=False):
┌────────────────────────────────────────┐
│  Finding "Chapter 7" in 500-page book  │
│  ├─ Start from page 1                  │
│  ├─ Read every page title              │
│  ├─ Finally found at page 347          │
│  └─ Time: 30 minutes ❌                │
└────────────────────────────────────────┘

With Index (index=True):
┌────────────────────────────────────────┐
│  Finding "Chapter 7" in 500-page book  │
│  ├─ Look at Table of Contents          │
│  ├─ "Chapter 7 → Page 347"             │
│  ├─ Jump directly to page 347          │
│  └─ Time: 10 seconds ✅                │
└────────────────────────────────────────┘
```

#### 5. **Dependency Injection = Hotel Concierge**

```
Hotel Concierge (get_database_session):
┌──────────────────────────────────────────────┐
│  Guest arrives (Request comes in)            │
│         ↓                                    │
│  Concierge gets room key (Create session)    │
│         ↓                                    │
│  Gives key to guest (yield session)          │
│         ↓                                    │
│  Guest uses room (Route function queries)    │
│         ↓                                    │
│  Guest leaves (Function returns)             │
│         ↓                                    │
│  Concierge takes key back (finally: close)   │
│         ↓                                    │
│  Room ready for next guest (Connection free) │
└──────────────────────────────────────────────┘
```

#### 6. **One Session Per Request = One Shopping Cart**

```
✅ CORRECT: Each customer has own cart
┌─────────────────────────────────────┐
│  Customer A's Cart (Session A)      │
│  ├─ Milk                            │
│  ├─ Bread                           │
│  └─ Eggs                            │
│                                     │
│  Customer B's Cart (Session B)      │
│  ├─ Apples                          │
│  └─ Juice                           │
│                                     │
│  No mixing! ✅                      │
└─────────────────────────────────────┘

❌ WRONG: Shared cart for all customers
┌─────────────────────────────────────┐
│  Global Shared Cart (One Session)   │
│  ├─ Milk (Customer A)               │
│  ├─ Apples (Customer B)             │
│  ├─ Bread (Customer A)              │
│  └─ Juice (Customer B)              │
│                                     │
│  Chaos! Wrong items! ❌             │
└─────────────────────────────────────┘
```

---

## Copy-Paste Template

### Complete Working Project Template

Copy this entire structure for instant setup:

#### 1. Project Structure
```bash
mkdir -p fastapi_project/{database,models,schemas,api/routes,dependencies}
cd fastapi_project
```

#### 2. File: `database/engine.py`
```python
from sqlalchemy import create_engine
import os

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://postgres:password@localhost:5432/fastapi_db"
)

engine = create_engine(
    DATABASE_URL,
    pool_size=20,
    max_overflow=0,
    pool_timeout=30,
    pool_recycle=1800,
    pool_pre_ping=True,
    echo=True,  # Set to False in production
)
```

#### 3. File: `database/session.py`
```python
from sqlalchemy.orm import sessionmaker
from .engine import engine

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)
```

#### 4. File: `models/base.py`
```python
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
```

#### 5. File: `models/product.py`
```python
from sqlalchemy import Column, Integer, String, Float
from .base import Base

class Product(Base):
    __tablename__ = "products"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False, index=True)
    description = Column(String(500))
    price = Column(Float, nullable=False)
    quantity = Column(Integer, default=0)
    
    def __repr__(self):
        return f"<Product(id={self.id}, name='{self.name}', price={self.price})>"
```

#### 6. File: `schemas/product.py`
```python
from pydantic import BaseModel, Field
from typing import Optional

class ProductBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    price: float = Field(..., gt=0)
    quantity: int = Field(default=0, ge=0)

class ProductCreate(ProductBase):
    pass

class ProductUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    price: Optional[float] = Field(None, gt=0)
    quantity: Optional[int] = Field(None, ge=0)

class ProductResponse(ProductBase):
    id: int
    
    class Config:
        from_attributes = True
```

#### 7. File: `dependencies/database.py`
```python
from sqlalchemy.orm import Session
from database.session import SessionLocal
from typing import Generator

def get_database_session() -> Generator[Session, None, None]:
    """
    Database session dependency for FastAPI routes.
    Creates a new session for each request and closes it after.
    """
    db = SessionLocal()
    try:
        yield db
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()
```

#### 8. File: `api/routes/products.py`
```python
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from dependencies.database import get_database_session
from models.product import Product
from schemas.product import ProductCreate, ProductUpdate, ProductResponse

router = APIRouter(prefix="/products", tags=["products"])

@router.post("/", response_model=ProductResponse, status_code=status.HTTP_201_CREATED)
def create_product(
    product: ProductCreate,
    db: Session = Depends(get_database_session)
):
    """Create a new product"""
    db_product = Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

@router.get("/", response_model=List[ProductResponse])
def list_products(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_database_session)
):
    """List all products with pagination"""
    products = db.query(Product).offset(skip).limit(limit).all()
    return products

@router.get("/{product_id}", response_model=ProductResponse)
def get_product(
    product_id: int,
    db: Session = Depends(get_database_session)
):
    """Get a specific product by ID"""
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Product with id {product_id} not found"
        )
    return product

@router.put("/{product_id}", response_model=ProductResponse)
def update_product(
    product_id: int,
    product_update: ProductUpdate,
    db: Session = Depends(get_database_session)
):
    """Update a product"""
    db_product = db.query(Product).filter(Product.id == product_id).first()
    if not db_product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Product with id {product_id} not found"
        )
    
    update_data = product_update.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_product, key, value)
    
    db.commit()
    db.refresh(db_product)
    return db_product

@router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(
    product_id: int,
    db: Session = Depends(get_database_session)
):
    """Delete a product"""
    db_product = db.query(Product).filter(Product.id == product_id).first()
    if not db_product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Product with id {product_id} not found"
        )
    
    db.delete(db_product)
    db.commit()
    return None
```

#### 9. File: `main.py`
```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database.engine import engine
from models.base import Base
from models import product  # Import all models
from api.routes import products

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="FastAPI SQLAlchemy Demo",
    description="Complete database connection example",
    version="1.0.0"
)

# CORS middleware (optional)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(products.router)

@app.get("/")
def root():
    return {
        "message": "FastAPI + SQLAlchemy Demo",
        "docs": "/docs",
        "redoc": "/redoc"
    }

@app.get("/health")
def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

#### 10. File: `requirements.txt`
```txt
fastapi==0.109.0
uvicorn[standard]==0.27.0
sqlalchemy==2.0.25
psycopg2-binary==2.9.9  # For PostgreSQL
python-dotenv==1.0.0
pydantic==2.5.3
```

#### 11. File: `.env`
```bash
DATABASE_URL=postgresql://postgres:password@localhost:5432/fastapi_db
```

#### 12. File: `.env.example`
```bash
DATABASE_URL=postgresql://username:password@localhost:5432/database_name
```

#### 13. File: `database/__init__.py`
```python
from .engine import engine
from .session import SessionLocal

__all__ = ["engine", "SessionLocal"]
```

#### 14. File: `models/__init__.py`
```python
from .base import Base
from .product import Product

__all__ = ["Base", "Product"]
```

#### 15. File: `api/__init__.py` and `api/routes/__init__.py`
```python
# Empty files to make directories Python packages
```

### Running the Application

```bash
# Install dependencies
pip install -r requirements.txt

# Run the application
python main.py

# Or with uvicorn
uvicorn main:app --reload

# Access API documentation
# http://localhost:8000/docs
```

---

## Critical Reminders

### 🚨 NEVER FORGET - Top 10 Rules

#### 1. **One Engine Per Application**
```python
# ✅ CORRECT: Module level (created once)
engine = create_engine(DATABASE_URL)

# ❌ WRONG: Function level (creates multiple)
def get_engine():
    return create_engine(DATABASE_URL)
```

#### 2. **Always Close Sessions**
```python
# ✅ CORRECT: Using dependency with finally
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()  # ALWAYS executes

# ❌ WRONG: Manual session without close
db = SessionLocal()
db.query(...)  # Forgot to close!
```

#### 3. **Use autocommit=False**
```python
# ✅ CORRECT: Explicit control
SessionLocal = sessionmaker(autocommit=False, bind=engine)
db.add(item)
db.commit()  # We choose when to save

# ❌ WRONG: Automatic commits
SessionLocal = sessionmaker(autocommit=True, bind=engine)
# Can't rollback, partial saves on errors
```

#### 4. **Handle Rollbacks**
```python
# ✅ CORRECT: Always rollback on error
try:
    db.add(item)
    db.commit()
except Exception:
    db.rollback()  # Undo changes
    raise

# ❌ WRONG: No rollback
try:
    db.add(item)
    db.commit()
except Exception:
    raise  # Session in bad state!
```

#### 5. **Enable pool_pre_ping**
```python
# ✅ CORRECT: Test connections before use
engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True  # Prevents stale connections
)

# ❌ WRONG: No connection testing
engine = create_engine(DATABASE_URL)
# May use broken connections
```

#### 6. **Index Strategically**
```python
# ✅ CORRECT: Index frequently queried columns
id = Column(Integer, primary_key=True, index=True)
email = Column(String, unique=True, index=True)

# ❌ WRONG: Index everything or nothing
# Too many indexes slow down writes
# No indexes slow down reads
```

#### 7. **One Session Per Request**
```python
# ✅ CORRECT: New session for each request
@app.get("/items")
def get_items(db: Session = Depends(get_db)):
    return db.query(Item).all()

# ❌ WRONG: Shared global session
global_db = SessionLocal()  # Multiple requests share!
```

#### 8. **Use Environment Variables**
```python
# ✅ CORRECT: Load from environment
import os
DATABASE_URL = os.getenv("DATABASE_URL")

# ❌ WRONG: Hardcoded credentials
DATABASE_URL = "postgresql://admin:password123@localhost/db"
# Never commit passwords to version control!
```

#### 9. **Commit Explicitly**
```python
# ✅ CORRECT: Explicit commit after changes
db.add(new_item)
db.commit()  # Save now

# ❌ WRONG: Expecting auto-save
db.add(new_item)
# Nothing saved! (with autocommit=False)
```

#### 10. **Use Pydantic Schemas**
```python
# ✅ CORRECT: Separate models and schemas
# models/user.py - Database model
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)

# schemas/user.py - API schema
class UserResponse(BaseModel):
    id: int
    class Config:
        from_attributes = True

# ❌ WRONG: Returning database models directly
@app.get("/users")
def get_users(db: Session = Depends(get_db)):
    return db.query(User).all()  # Exposes internal structure!
```

---

### ⚡ Quick Reference Card

```python
# ════════════════════════════════════════════════════════
#                    QUICK SETUP GUIDE
# ════════════════════════════════════════════════════════

# 1️⃣ ENGINE (Once at startup)
from sqlalchemy import create_engine
engine = create_engine("postgresql://user:pass@host/db")

# 2️⃣ BASE (Once at startup)
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

# 3️⃣ MODEL (Define tables)
from sqlalchemy
