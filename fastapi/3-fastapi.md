# 🚀 **COMPLETE FastAPI Project Guide with Folder Structure**

## 📁 **PROJECT STRUCTURE & FILE FLOW**
```
fastapi-project/
├── 📂 app/                          # Main application package
│   ├── 📄 __init__.py              # Makes 'app' a Python package
│   ├── 📄 app_main.py              # FastAPI app configuration
│   │
│   ├── 📂 models/                  # Database models (SQLAlchemy, etc.)
│   │   ├── 📄 __init__.py         # Exports models
│   │   ├── 📄 todo.py             # Todo database model
│   │   └── 📄 user.py             # User database model
│   │
│   ├── 📂 routing/                 # API endpoints
│   │   ├── 📄 __init__.py         # Exports routers
│   │   ├── 📄 todo.py             # Todo endpoints
│   │   └── 📄 user.py             # User endpoints
│   │
│   ├── 📂 schemas/                 # Pydantic validation schemas
│   │   ├── 📄 __init__.py         # Exports schemas
│   │   ├── 📄 todo.py             # Todo request/response schemas
│   │   └── 📄 user.py             # User request/response schemas
│   │
│   └── 📂 core/                    # Optional: Core utilities
│       ├── 📄 config.py           # Configuration settings
│       └── 📄 dependencies.py     # Dependency injections
│
├── 📄 main.py                      # Server launcher (entry point)
├── 📄 requirements.txt             # Python dependencies
└── 📄 .env                         # Environment variables
```

## 🔄 **COMPLETE REQUEST FLOW**
```
CLIENT Request → http://localhost:8000/todos
        ↓
📄 main.py (Uvicorn server starts)
        ↓
📄 app/app_main.py (FastAPI app instance)
        ↓
📁 app/routing/todo.py (Specific endpoint handler)
        ↓
📁 app/schemas/todo.py (Request validation)
        ↓
📁 app/models/todo.py (Database operations)
        ↓
📁 app/schemas/todo.py (Response validation)
        ↓
CLIENT receives validated JSON response
```

## 📦 **DETAILED FILE EXPLANATIONS**

### **1. 📄 main.py - SERVER LAUNCHER**
```python
#!/usr/bin/env python3
"""
MAIN.PY - SERVER ENTRY POINT
Purpose: Starts the Uvicorn web server
This is the FIRST file that runs when you start your application
Think of it as the "ignition key" for your app
"""

from app.app_main import app  # Import the FastAPI app instance
import uvicorn

if __name__ == "__main__":
    """
    This block only runs when you execute: python main.py
    It DOESN'T run when you import this file elsewhere
    """
    
    # Configure and start the Uvicorn server
    uvicorn.run(
        app,                    # Your FastAPI application instance
        host="localhost",       # Server will run on local machine
        port=8000,              # Access at http://localhost:8000
        
        # Development settings (remove in production):
        reload=True,            # Auto-restart on code changes
        reload_dirs=["app"],    # Watch only 'app' folder for changes
        
        log_level="info",       # Logging: debug, info, warning, error
        access_log=True         # Log HTTP requests
    )
    
    # Alternative production command (for terminal):
    # uvicorn app.app_main:app --host 0.0.0.0 --port 8000 --workers 4
```

**Key Points:**
- Only purpose is to start the server
- Never put application logic here
- Different configurations for dev vs production

### **2. 📄 app/app_main.py - APPLICATION CONFIGURATOR**
```python
"""
APP_MAIN.PY - FASTAPI APPLICATION CONFIGURATION
Purpose: Creates and configures the FastAPI application instance
This is where your entire web application is defined
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

# Import routers (after creating __init__.py in routing folder)
from app.routing import todo_router, user_router

# ========== CREATE FASTAPI APP INSTANCE ==========
app = FastAPI(
    title="Todo API",
    description="A complete Todo management API with users",
    version="1.0.0",
    docs_url="/docs",           # Swagger UI: http://localhost:8000/docs
    redoc_url="/redoc",         # ReDoc: http://localhost:8000/redoc
    openapi_url="/openapi.json" # OpenAPI schema
)

# ========== ADD CORS MIDDLEWARE ==========
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Frontend URLs
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

# ========== REGISTER ALL ROUTERS ==========
# Each router adds its endpoints to the main app
app.include_router(todo_router)  # Adds all /todos endpoints
app.include_router(user_router)  # Adds all /users endpoints

# ========== ROOT ENDPOINT ==========
@app.get("/")
async def root():
    """Health check and API information"""
    return {
        "message": "Welcome to Todo API",
        "version": "1.0.0",
        "docs": "/docs",
        "endpoints": {
            "todos": "/todos",
            "users": "/users"
        }
    }

# ========== CUSTOM ERROR HANDLING ==========
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    """
    Transforms Pydantic validation errors into user-friendly format
    """
    errors = {}
    for error in exc.errors():
        # Extract field name and error message
        field = error['loc'][-1] if error['loc'] else 'unknown'
        errors[field] = error['msg']
    
    return JSONResponse(
        status_code=422,
        content={
            "success": False,
            "message": "Validation failed",
            "errors": errors
        }
    )

# ========== 404 HANDLER ==========
@app.exception_handler(404)
async def not_found_handler(request, exc):
    return JSONResponse(
        status_code=404,
        content={
            "success": False,
            "message": f"Endpoint {request.url.path} not found"
        }
    )

# ========== HEALTH CHECK ==========
@app.get("/health")
async def health_check():
    """Endpoint for monitoring and health checks"""
    return {
        "status": "healthy",
        "timestamp": "2024-01-15T10:30:00Z",
        "service": "todo-api"
    }
```

### **3. 📁 app/schemas/todo.py - DATA VALIDATION**
```python
"""
SCHEMAS/TODO.PY - DATA VALIDATION RULES
Purpose: Define how data should look when sent/received
Pydantic validates ALL incoming/outgoing data automatically
"""

from pydantic import BaseModel, Field, validator
from typing import Optional, List
from datetime import datetime
import re

# ========== REQUEST SCHEMAS (Client → Server) ==========

class TodoCreate(BaseModel):
    """
    Schema for CREATING a new todo
    Used in: POST /todos
    """
    
    # REQUIRED field with length validation
    content: str = Field(
        ...,  # Ellipsis = REQUIRED (cannot be omitted)
        min_length=5,
        max_length=255,
        description="Todo content, 5-255 characters",
        example="Learn FastAPI validation"
    )
    
    # OPTIONAL field with default value
    completed: bool = Field(
        default=False,  # Auto-sets to False if not provided
        description="Completion status"
    )
    
    # OPTIONAL field with range validation
    priority: Optional[int] = Field(
        default=1,
        ge=1,      # Greater than or equal to 1
        le=5,      # Less than or equal to 5
        description="Priority 1-5 (1=low, 5=high)"
    )
    
    # List field with max items
    tags: List[str] = Field(
        default_factory=list,  # Defaults to empty list
        max_items=5,
        description="Up to 5 tags"
    )
    
    # ========== CUSTOM VALIDATORS ==========
    
    @validator('content')
    def validate_content(cls, value):
        """Custom content validation"""
        # Trim whitespace
        value = value.strip()
        
        # Check minimum length after trimming
        if len(value) < 5:
            raise ValueError('Content must be at least 5 characters after trimming')
        
        # Check for offensive words (example)
        offensive_words = ['badword1', 'badword2']
        for word in offensive_words:
            if word in value.lower():
                raise ValueError(f'Content contains inappropriate word: {word}')
        
        return value
    
    @validator('tags', each_item=True)
    def validate_tags(cls, tag):
        """Validate each tag individually"""
        if not tag.strip():
            raise ValueError('Tag cannot be empty')
        if len(tag) > 20:
            raise ValueError('Tag too long (max 20 chars)')
        return tag.strip()

class TodoUpdate(BaseModel):
    """
    Schema for UPDATING a todo (PATCH)
    All fields optional for partial updates
    """
    content: Optional[str] = Field(
        None,
        min_length=5,
        max_length=255,
        description="Updated content"
    )
    completed: Optional[bool] = None
    priority: Optional[int] = Field(None, ge=1, le=5)

# ========== RESPONSE SCHEMAS (Server → Client) ==========

class TodoResponse(BaseModel):
    """
    Schema for TODO RESPONSES
    Defines what clients see when they request todos
    """
    id: int
    content: str
    completed: bool
    priority: int
    tags: List[str]
    created_at: datetime
    updated_at: Optional[datetime]
    
    # ========== PYDANTIC CONFIG ==========
    class Config:
        """
        Special Pydantic configuration
        """
        # Enables conversion from SQLAlchemy models
        from_attributes = True  # Pydantic v2 (was 'orm_mode' in v1)
        
        # Example for response documentation
        json_schema_extra = {
            "example": {
                "id": 1,
                "content": "Complete project documentation",
                "completed": False,
                "priority": 3,
                "tags": ["work", "documentation"],
                "created_at": "2024-01-15T10:30:00Z",
                "updated_at": None
            }
        }

# ========== FILTER SCHEMAS ==========

class TodoFilter(BaseModel):
    """
    Schema for filtering todos (query parameters)
    """
    completed: Optional[bool] = None
    priority: Optional[int] = Field(None, ge=1, le=5)
    tags: Optional[List[str]] = None
    skip: int = Field(0, ge=0, description="Pagination offset")
    limit: int = Field(100, ge=1, le=100, description="Max items per page")
```

### **4. 📁 app/routing/todo.py - ENDPOINT HANDLERS**
```python
"""
ROUTING/TODO.PY - API ENDPOINT DEFINITIONS
Purpose: Define URL endpoints and their business logic
This is where HTTP requests are processed
"""

from fastapi import APIRouter, HTTPException, Depends, Query, status
from typing import List, Optional

# Import schemas for validation
from app.schemas.todo import (
    TodoCreate, 
    TodoUpdate, 
    TodoResponse,
    TodoFilter
)

# ========== CREATE ROUTER INSTANCE ==========
router = APIRouter(
    prefix="/todos",      # All endpoints start with /todos
    tags=["todos"],       # Groups in Swagger/ReDoc
    responses={
        400: {"description": "Bad Request"},
        404: {"description": "Not Found"},
        422: {"description": "Validation Error"}
    }
)

# Temporary in-memory storage (replace with database)
todos_db = []
current_id = 1

# ========== GET ALL TODOS ==========
@router.get("/", response_model=List[TodoResponse])
async def get_todos(
    filter_params: TodoFilter = Depends(),  # Query params validation
    search: Optional[str] = Query(None, min_length=2, description="Search in content")
):
    """
    GET /todos - Retrieve all todo items
    
    Query Parameters:
    - completed: Filter by completion status
    - priority: Filter by priority level
    - tags: Filter by tags
    - skip: Pagination offset
    - limit: Max items per page
    - search: Search in content
    
    Returns: List of todos
    """
    filtered_todos = todos_db.copy()
    
    # Apply filters
    if filter_params.completed is not None:
        filtered_todos = [t for t in filtered_todos if t['completed'] == filter_params.completed]
    
    if filter_params.priority is not None:
        filtered_todos = [t for t in filtered_todos if t['priority'] == filter_params.priority]
    
    if filter_params.tags:
        filtered_todos = [t for t in filtered_todos 
                         if any(tag in t['tags'] for tag in filter_params.tags)]
    
    # Apply search
    if search:
        search_lower = search.lower()
        filtered_todos = [t for t in filtered_todos 
                         if search_lower in t['content'].lower()]
    
    # Apply pagination
    start = filter_params.skip
    end = start + filter_params.limit
    paginated_todos = filtered_todos[start:end]
    
    return paginated_todos

# ========== GET SINGLE TODO ==========
@router.get("/{todo_id}", response_model=TodoResponse)
async def get_todo(todo_id: int):
    """
    GET /todos/{id} - Get a specific todo by ID
    
    Path Parameters:
    - todo_id: The ID of the todo to retrieve
    
    Returns: Single todo item
    """
    for todo in todos_db:
        if todo['id'] == todo_id:
            return todo
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Todo with ID {todo_id} not found"
    )

# ========== CREATE TODO ==========
@router.post("/", 
            response_model=TodoResponse, 
            status_code=status.HTTP_201_CREATED)
async def create_todo(todo_data: TodoCreate):
    """
    POST /todos - Create a new todo
    
    Request Body (TodoCreate schema):
    - content: string (5-255 chars) - REQUIRED
    - completed: boolean (default: false)
    - priority: integer 1-5 (default: 1)
    - tags: array of strings (max 5)
    
    Returns: Created todo with ID
    """
    global current_id
    from datetime import datetime
    
    new_todo = {
        'id': current_id,
        'content': todo_data.content,
        'completed': todo_data.completed,
        'priority': todo_data.priority,
        'tags': todo_data.tags,
        'created_at': datetime.now(),
        'updated_at': None
    }
    
    todos_db.append(new_todo)
    current_id += 1
    
    return new_todo

# ========== UPDATE TODO ==========
@router.patch("/{todo_id}", response_model=TodoResponse)
async def update_todo(todo_id: int, todo_update: TodoUpdate):
    """
    PATCH /todos/{id} - Partially update a todo
    
    Path Parameters:
    - todo_id: ID of todo to update
    
    Request Body (TodoUpdate schema):
    - Any combination of fields (all optional)
    
    Returns: Updated todo
    """
    from datetime import datetime
    
    for index, todo in enumerate(todos_db):
        if todo['id'] == todo_id:
            # Get update data (only provided fields)
            update_data = todo_update.dict(exclude_unset=True)
            
            # Apply updates
            for field, value in update_data.items():
                todos_db[index][field] = value
            
            # Update timestamp
            todos_db[index]['updated_at'] = datetime.now()
            
            return todos_db[index]
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Todo with ID {todo_id} not found"
    )

# ========== DELETE TODO ==========
@router.delete("/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(todo_id: int):
    """
    DELETE /todos/{id} - Delete a todo
    
    Path Parameters:
    - todo_id: ID of todo to delete
    
    Returns: No content (204)
    """
    global todos_db
    
    initial_count = len(todos_db)
    todos_db = [todo for todo in todos_db if todo['id'] != todo_id]
    
    if len(todos_db) == initial_count:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Todo with ID {todo_id} not found"
        )
    
    # 204 No Content - successful deletion, no response body

# ========== BULK OPERATIONS ==========
@router.post("/bulk", response_model=List[TodoResponse])
async def bulk_create_todos(todos: List[TodoCreate]):
    """
    POST /todos/bulk - Create multiple todos at once
    """
    created_todos = []
    for todo_data in todos:
        # Reuse create logic (in real app, refactor into service)
        from datetime import datetime
        new_todo = {
            'id': current_id,
            'content': todo_data.content,
            'completed': todo_data.completed,
            'priority': todo_data.priority,
            'tags': todo_data.tags,
            'created_at': datetime.now(),
            'updated_at': None
        }
        todos_db.append(new_todo)
        created_todos.append(new_todo)
        current_id += 1
    
    return created_todos
```

### **5. 📁 app/models/todo.py - DATABASE MODEL**
```python
"""
MODELS/TODO.PY - DATABASE STRUCTURE
Purpose: Define how data is stored in the database
SQLAlchemy models map to database tables
"""

from sqlalchemy import Column, Integer, String, Boolean, DateTime, Text
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import ARRAY  # For PostgreSQL array type

# Assuming you have a Base class in app/models/__init__.py
from app.models import Base

class Todo(Base):
    """
    SQLAlchemy model for todos table
    Each instance = one row in database
    """
    
    # Table name in database
    __tablename__ = "todos"
    
    # ========== COLUMN DEFINITIONS ==========
    
    # Primary key
    id = Column(Integer, primary_key=True, index=True)
    
    # Content with constraints
    content = Column(String(255), nullable=False)
    
    # Status
    completed = Column(Boolean, default=False, nullable=False)
    
    # Priority with constraint
    priority = Column(Integer, default=1, nullable=False)
    
    # For PostgreSQL: tags = Column(ARRAY(String(50)), default=[])
    # For SQLite/MySQL (stored as JSON string):
    tags = Column(Text, default="[]")  # Store as JSON string
    
    # Timestamps (auto-managed)
    created_at = Column(DateTime(timezone=True), 
                       server_default=func.now())  # Auto-set on insert
    updated_at = Column(DateTime(timezone=True), 
                       onupdate=func.now())  # Auto-update on change
    
    # ========== METHODS ==========
    
    def __repr__(self):
        """String representation for debugging"""
        return f"<Todo(id={self.id}, content='{self.content[:20]}...')>"
    
    def to_dict(self):
        """Convert to dictionary (useful for JSON responses)"""
        return {
            "id": self.id,
            "content": self.content,
            "completed": self.completed,
            "priority": self.priority,
            "tags": self.tags if isinstance(self.tags, list) else json.loads(self.tags),
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }
```

## 🎯 **THE MAGIC OF `__init__.py` - DETAILED EXPLANATION**

### **What is `__init__.py`?**
A Python **package marker** file that transforms a regular folder into an **importable Python package**.

### **Without `__init__.py`:**
```python
# Trying to import from a plain folder
from app.routing.todo import router  # ❌ ERROR: ModuleNotFoundError
# Python says: "I don't recognize 'app' as a package!"
```

### **With `__init__.py`:**
```python
# Empty __init__.py makes it importable
from app.routing.todo import router  # ✅ SUCCESS!
# Python says: "Found the 'app' package, now looking inside..."
```

### **📁 app/__init__.py**
```python
"""
APP PACKAGE INITIALIZATION
This file makes the entire 'app' folder a Python package
"""

# Version information
__version__ = "1.0.0"
__author__ = "Your Name"

# Optional: Initialize when package is imported
print(f"🚀 Initializing Todo API v{__version__}")

# Export commonly used items (optional)
# from .app_main import app
# __all__ = ["app"]
```

### **📁 app/routing/__init__.py**
```python
"""
ROUTING PACKAGE - EXPORTS ALL ROUTERS
Purpose: Central place to import all routers
Makes imports cleaner throughout the app
"""

# Import individual routers
from .todo import router as todo_router
from .user import router as user_router

# Export them for easy importing
__all__ = ["todo_router", "user_router"]

# Optional: Create a list of all routers
routers = [todo_router, user_router]
```

### **📁 app/schemas/__init__.py**
```python
"""
SCHEMAS PACKAGE - EXPORTS ALL SCHEMAS
Purpose: One-stop shop for importing schemas
"""

# Todo schemas
from .todo import (
    TodoCreate,
    TodoUpdate,
    TodoResponse,
    TodoFilter
)

# User schemas (if you have them)
from .user import (
    UserCreate,
    UserResponse
)

# Export everything
__all__ = [
    "TodoCreate",
    "TodoUpdate", 
    "TodoResponse",
    "TodoFilter",
    "UserCreate",
    "UserResponse"
]
```

### **📁 app/models/__init__.py**
```python
"""
MODELS PACKAGE - DATABASE MODELS
Purpose: Centralize database model definitions
"""

from sqlalchemy.ext.declarative import declarative_base

# Create Base class for all models
Base = declarative_base()

# Import models (AFTER creating Base)
from .todo import Todo
from .user import User

# Export
__all__ = ["Base", "Todo", "User"]
```

## 🔄 **HOW IMPORTS WORK WITH `__init__.py`**

### **BEFORE (Without clean exports):**
```python
# app_main.py - Messy imports
from app.routing.todo import router as todo_router
from app.routing.user import router as user_router
from app.schemas.todo import TodoCreate, TodoResponse
from app.schemas.user import UserCreate
# ... many more imports
```

### **AFTER (With `__init__.py` exports):**
```python
# app_main.py - Clean imports
from app.routing import todo_router, user_router
from app.schemas import TodoCreate, TodoResponse, UserCreate
# Much cleaner and maintainable!
```

## 🎨 **VALIDATION TECHNIQUES IN SCHEMAS**

### **1. Field-Level Validation**
```python
from pydantic import BaseModel, Field, EmailStr, HttpUrl
from typing import Optional
import re

class UserSchema(BaseModel):
    # String validations
    username: str = Field(..., min_length=3, max_length=50, regex="^[a-zA-Z0-9_]+$")
    
    # Email validation
    email: EmailStr  # Automatically validates email format
    
    # URL validation
    website: Optional[HttpUrl] = None
    
    # Number validations
    age: int = Field(..., gt=0, lt=150)  # Greater than 0, less than 150
    
    # Decimal validation
    price: float = Field(..., ge=0.0)  # Greater than or equal to 0
    
    # List validations
    items: list = Field(default_factory=list, max_items=10)
    
    # Optional with default
    is_active: bool = Field(default=True)
```

### **2. Custom Validators**
```python
from pydantic import validator

class PaymentSchema(BaseModel):
    card_number: str
    expiry_date: str
    
    @validator('card_number')
    def validate_card_number(cls, value):
        # Remove spaces and dashes
        clean_value = value.replace(" ", "").replace("-", "")
        
        # Check if all digits
        if not clean_value.isdigit():
            raise ValueError("Card number must contain only digits")
        
        # Check length
        if len(clean_value) not in [15, 16]:
            raise ValueError("Card number must be 15 or 16 digits")
        
        return clean_value
    
    @validator('expiry_date')
    def validate_expiry_date(cls, value):
        # Format: MM/YY or MM/YYYY
        import datetime
        try:
            if "/" in value:
                month, year = value.split("/")
                month = int(month)
                year = int(year)
                
                # Convert 2-digit year to 4-digit
                if year < 100:
                    year += 2000
                
                # Check if date is in future
                expiry = datetime.date(year, month, 1)
                if expiry < datetime.date.today():
                    raise ValueError("Card has expired")
                
                return value
        except:
            raise ValueError("Invalid expiry date format. Use MM/YY or MM/YYYY")
```

### **3. Root Validators**
```python
from pydantic import BaseModel, root_validator

class RegistrationSchema(BaseModel):
    password: str
    confirm_password: str
    email: str
    
    @root_validator
    def validate_passwords_match(cls, values):
        """Check if password and confirm_password match"""
        password = values.get('password')
        confirm_password = values.get('confirm_password')
        
        if password and confirm_password and password != confirm_password:
            raise ValueError("Passwords do not match")
        
        return values
    
    @root_validator
    def validate_email_domain(cls, values):
        """Business rule: Disallow certain email domains"""
        email = values.get('email', '')
        blocked_domains = ['tempmail.com', 'trashmail.com']
        
        for domain in blocked_domains:
            if domain in email:
                raise ValueError(f"Email domain {domain} is not allowed")
        
        return values
```

## 🚀 **RUNNING THE APPLICATION**

### **Development Mode:**
```bash
# Method 1: Using main.py
python main.py

# Method 2: Direct uvicorn command
uvicorn app.app_main:app --reload --host localhost --port 8000

# Output:
# INFO:     Uvicorn running on http://localhost:8000 (Press CTRL+C to quit)
# INFO:     Started reloader process [12345] watching 'app'
# INFO:     Started server process [12346]
# INFO:     Waiting for application startup.
# INFO:     Application startup complete.
```

### **Production Mode:**
```bash
# Disable reload, add workers
uvicorn app.app_main:app --host 0.0.0.0 --port 8000 --workers 4

# With gunicorn (for production)
gunicorn -w 4 -k uvicorn.workers.UvicornWorker app.app_main:app
```

## 📚 **API ENDPOINTS SUMMARY**

| Method | URL | Purpose | Request Body |
|--------|-----|---------|--------------|
| GET | `/` | API info | None |
| GET | `/todos` | List todos | Query params |
| GET | `/todos/{id}` | Get single todo | None |
| POST | `/todos` | Create todo | `TodoCreate` |
| PATCH | `/todos/{id}` | Update todo | `TodoUpdate` |
| DELETE | `/todos/{id}` | Delete todo | None |
| POST | `/todos/bulk` | Bulk create | List of `TodoCreate` |
| GET | `/health` | Health check | None |
| GET | `/docs` | Swagger UI | None |
| GET | `/redoc` | ReDoc | None |

## 💡 **BEST PRACTICES SUMMARY**

### **1. Folder Structure:**
- Keep related files together
- Use singular folder names (`routing/`, not `routings/`)
- Each folder needs `__init__.py`
- Separate concerns (models, schemas, routing)

### **2. Naming Conventions:**
- Files: `snake_case.py` (`todo_routes.py`)
- Classes: `PascalCase` (`TodoCreate`, `UserResponse`)
- Variables/functions: `snake_case` (`get_todos`, `user_data`)
- Constants: `UPPER_SNAKE_CASE` (`MAX_ITEMS`, `API_VERSION`)

### **3. Import Rules:**
- Use absolute imports: `from app.schemas.todo import TodoCreate`
- Use `__init__.py` for clean exports
- Avoid circular imports (A imports B, B imports A)

### **4. Validation Rules:**
- Validate early with Pydantic schemas
- Use descriptive error messages
- Add examples for documentation
- Separate request/response schemas

### **5. Error Handling:**
- Centralize in `app_main.py`
- Use appropriate HTTP status codes
- Log errors but don't expose sensitive info
- Return consistent error format

## 🎉 **QUICK START CHEATSHEET**

```bash
# 1. Create project structure
mkdir fastapi-project
cd fastapi-project

# 2. Create folders
mkdir -p app/{models,routing,schemas,core}
touch app/__init__.py app/app_main.py
touch app/models/__init__.py app/models/todo.py
touch app/routing/__init__.py app/routing/todo.py
touch app/schemas/__init__.py app/schemas/todo.py
touch main.py requirements.txt

# 3. Install dependencies
echo "fastapi>=0.104.0" > requirements.txt
echo "uvicorn[standard]>=0.24.0" >> requirements.txt
echo "pydantic>=2.0.0" >> requirements.txt
pip install -r requirements.txt

# 4. Copy code from above into respective files

# 5. Run the application
python main.py

# 6. Visit in browser
# http://localhost:8000/docs  # Swagger UI
# http://localhost:8000/redoc # ReDoc
```

This complete guide provides everything you need to build, understand, and maintain a FastAPI project with proper structure and best practices! 🚀
