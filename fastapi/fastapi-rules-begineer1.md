# FastAPI Rules for Beginners
## 📊 **Quick Reference Table**

| Operation | Decorator | Returns | Changes Data? |
|-----------|-----------|---------|---------------|
| Get All   | `@app.get("/items")` | List | No |
| Get One   | `@app.get("/items/{id}")` | Single item | No |
| Create    | `@app.post("/items")` | Created item | Yes |
| Delete    | `@app.delete("/items/{id}")` | Success message | Yes |

## 🔄 **HTTP Method Rules**

### **GET Requests** (Read Data)
```
@ + app + . + get + ("/path")
     ↓
@app.get("/items")
def function_name():
    return data  # Never modify data!
```

### **POST Requests** (Create Data)
```
1. Define model with BaseModel
2. Add @app.post("/path")
3. Get data from request body
4. Save to database
5. Return created data
```

### **DELETE Requests** (Remove Data)
```
1. @app.delete("/path/{id}")
2. Find item by ID
3. Remove from database
4. Return success message
```

## CORE SETUP RULES
1. Initialize FastAPI App First: Always start by creating the FastAPI instance `app = FastAPI()`
2. This creates your web application framework.
3. Import Required Modules: Always include at the top:
   - `from fastapi import FastAPI`
   - `from pydantic import BaseModel`
   - `from typing import Optional`

BASE MODEL
**BaseModel Fields**: 
   - Required = `name: str`
   - Optional = `name: Optional[str] = None`
   - Optional = `desc:str | None = None`

## PYDANTIC BASEMODEL RULES
1. Use BaseModel to define request/response data structures
0. Required to create `POST` Request. In this case for Inmemory Database. 
1. Create Models with BaseModel: Every model must inherit: `class Item(BaseModel):`
2. Define Required Fields: Simple type annotation: `name: str` (must be provided)
3. Define Optional Fields: Use: `description: Optional[str] = None` (can be omitted)
4. Server-Generated Fields: Make optional: `id: Optional[int] = None` (server fills this)

## GET REQUEST RULES
1. Use GET Decorator: Place above function: `@app.get("/path")`
2. Define Meaningful Paths:
   - Collections: `/items` (plural)
   - Single resource: `/items/{item_id}`
3. Path Parameters Pattern: Path: `"/items/{item_id}"` → Function: `def func(item_id: int)`
4. Always Use Type Hints: Add to parameters: `item_id: int` (enables auto-validation)
5. Invalid types (like `/items/abc`) return 422 error automatically
6. GET = Read Only: Never modify database in GET endpoints

## POST REQUEST RULES
0. `FastAPI` automatically parses `JSON` request body into your model
1. Use POST Decorator: `@app.post("/path")` (for creating resources)
2. Request Body Parameter: Function must have: `def create_item(item: Item):`
3. Generate Server Fields: Calculate IDs before saving: `item.id = new_id`
4. Save to Storage: After validation: `database.append(item)`
5. Return Created Resource: Include success message and new data

## DELETE REQUEST RULES
1. Use DELETE Decorator: `@app.delete("/path/{id}")` (for removing resources)
2. Find Before Deleting: Check if item exists in database first
3. Remove from Storage: Use: `database.remove(item)` or `del database[index]`
4. Confirm Deletion: Return success message and deleted item data

## DATABASE RULES
1. Initialize Storage: Create list: `database = []` (use descriptive names)
2. Generate Sequential IDs: Strategy: `max(item.id for item in db) + 1 if db else 1`
3. Understand Persistence: In-memory lists reset on server restart

## ERROR HANDLING RULES
1. Trust Auto-Validation: FastAPI validates types automatically via type hints
2. Check Resource Existence: Always verify item exists before operations
3. Use Proper HTTP Codes:
   - 200: Success
   - 201: Created (POST)
   - 404: Not Found
   - 422: Validation Error (auto)

## BEST PRACTICE RULES
1. Descriptive Function Names: Use: `get_all_items()`, `create_item()`, not vague names
2. Add Documentation: Include docstrings: `"""Get item by ID"""`
3. Consistent Naming:
   - Routes: plural nouns (`/items`)
   - Functions: verb_noun (`get_items`)
   - Models: singular nouns (`Item`)
4. Test All Endpoints: Test GET, POST, DELETE operations after creation

# Improved FastAPI Example with Easy-to-Remember Rules

##  `main.py` with Better Practices:

```python
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import Optional

# Rule 1: Always start by creating the FastAPI app instance
app = FastAPI()

# Rule 2: Define your data models using BaseModel
class Item(BaseModel):
    # Rule 3: Required fields - just type annotation
    name: str
    price: float
    
    # Rule 4: Optional fields - use Optional or Union with None default
    description: Optional[str] = None  # Better than str | None = None
    
    # Rule 5: Server-generated fields should be optional
    id: Optional[int] = None  # We'll generate this on the server

# Rule 6: Use descriptive variable names for databases
items_database = []  # In-memory database (clear on server restart)

# ================= GET REQUESTS =================

# Rule 7: Use descriptive route paths (plural for collections)
@app.get("/")
def read_root():
    return {"message": "Welcome to Items API"}

# Rule 8: GET endpoints should return data, not modify it
@app.get("/items")
def get_all_items():
    """Get all items from the database"""
    return {
        "count": len(items_database),
        "items": items_database
    }

# Rule 9: Use path parameters for specific resources
@app.get("/items/{item_id}")
def get_item_by_id(item_id: int):
    """Get a specific item by its ID"""
    # Rule 10: Type hints in function parameters enable automatic validation
    for item in items_database:
        if item.id == item_id:
            return item
    
    # Rule 11: Return proper HTTP errors for missing resources
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Item with ID {item_id} not found"
    )

# ================= POST REQUESTS =================

@app.post("/items")
def create_item(item: Item):
    """Create a new item in the database"""
    # Rule 12: Generate server-side fields before saving
    if items_database:
        new_id = items_database[-1].id + 1
    else:
        new_id = 1  # Start from 1 instead of 0 (more realistic)
    
    # Rule 13: Create a copy with the generated ID
    new_item = item.copy(update={"id": new_id})
    
    # Rule 14: Add to database
    items_database.append(new_item)
    
    # Rule 15: Return 201 Created status for successful creation
    return {
        "message": "Item created successfully",
        "data": new_item
    }, status.HTTP_201_CREATED

# ================= DELETE REQUEST =================

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    """Delete an item from the database"""
    # Rule 16: Check if item exists before deleting
    for index, item in enumerate(items_database):
        if item.id == item_id:
            deleted_item = items_database.pop(index)
            return {
                "message": "Item deleted successfully",
                "deleted_item": deleted_item
            }
    
    # Rule 17: Return error if trying to delete non-existent resource
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Item with ID {item_id} not found"
    )
```

# Complete FastAPI BaseModel Pipeline with Benefits

**BaseModel Benefits List**
**A. DATA VALIDATION**
1. **Request Validation** - Validates incoming HTTP requests automatically, returns 422 for invalid data
2. **Type Validation** - Ensures correct data types (int, str, float, bool) with automatic type checking
3. **Custom Validation Logic** - Add business rules with `Field()` constraints and `@validator` decorators
4. **Required/Optional Field Handling** - Automatically detects mandatory fields vs optional fields with defaults

**B. SERIALIZATION/DESERIALIZATION**
1. **Incoming Request Deserialization** - Automatically converts JSON → Python objects with type conversion
2. **Outgoing Response Serialization** - Automatically converts Python objects → JSON for API responses
3. **Nested Object Handling** - Serializes/deserializes complex nested object hierarchies automatically
4. **Complex Type Support** - Handles datetime, UUID, Decimal, and custom types with proper formatting


**Without BaseModel:** You write 100 lines to:
- Parse JSON
- Validate types
- Convert strings to proper types
- Check business rules
- Serialize to JSON
- Handle errors


## **COMPLETE REQUEST-RESPONSE PIPELINE**

```
┌─────────────────────────────────────────────────────────────────────┐
│                       CLIENT SIDE                                   │
│  1. Client sends HTTP POST request with JSON body                   │
│     Content-Type: application/json                                  │
│     Body: {"name":"Laptop","price":"1299.99","quantity":"2"}        │
└─────────────────────────────────────────────────────────────────────┘
                                  ↓
┌─────────────────────────────────────────────────────────────────────┐
│                    FASTAPI FRAMEWORK                                │
│  2. FastAPI receives HTTP request                                   │
│  3. Extracts JSON payload from request body                         │
│  4. Routes to appropriate endpoint based on URL                     │
└─────────────────────────────────────────────────────────────────────┘
                                  ↓
┌─────────────────────────────────────────────────────────────────────┐
│               🎯 BASEMODEL DESERIALIZATION PHASE                   │
│  5. Parse JSON string → Python dictionary                           │
│     {"name":"Laptop","price":"1299.99","quantity":"2"}             │
│     ↓                                                              │
│     {"name": "Laptop", "price": "1299.99", "quantity": "2"}        │
└─────────────────────────────────────────────────────────────────────┘
                                  ↓
┌─────────────────────────────────────────────────────────────────────┐
│               🎯 BASEMODEL VALIDATION PHASE                        │
│  6. Type Validation & Conversion:                                   │
│     • "Laptop" → str (valid)                                       │
│     • "1299.99" → float (converts string to float)                 │
│     • "2" → int (converts string to integer)                       │
│  7. Field Validation:                                              │
│     • Checks all required fields present                           │
│     • Applies default values for optional fields                   │
│     • Runs custom validators if defined                            │
└─────────────────────────────────────────────────────────────────────┘
                                  ↓
┌─────────────────────────────────────────────────────────────────────┐
│                    PYTHON OBJECT CREATION                          │
│  8. Creates validated Python object:                               │
│     Item(name="Laptop", price=1299.99, quantity=2)                 │
│     • Type-safe: IDE knows item.name is str                        │
│     • Validated: All business rules satisfied                      │
│     • Ready for use: Clean Python object                           │
└─────────────────────────────────────────────────────────────────────┘
                                  ↓
┌─────────────────────────────────────────────────────────────────────┐
│                   YOUR BUSINESS LOGIC                              │
│  9. Perform calculations & operations:                             │
│     total = item.price * item.quantity  # 1299.99 * 2              │
│     discount = apply_discount(total)                               │
│     save_to_database(item)                                         │
│  10. Prepare response data                                         │
└─────────────────────────────────────────────────────────────────────┘
                                  ↓
┌─────────────────────────────────────────────────────────────────────┐
│               🎯 BASEMODEL SERIALIZATION PHASE                     │
│  11. Python object → Python dictionary:                            │
│      item.dict() returns:                                          │
│      {"name": "Laptop", "price": 1299.99, "quantity": 2}           │
│  12. Nested objects also serialized automatically                  │
│  13. Complex types handled (datetime, UUID, etc.)                  │
└─────────────────────────────────────────────────────────────────────┘
                                  ↓
┌─────────────────────────────────────────────────────────────────────┐
│                    FASTAPI FRAMEWORK                               │
│  14. Python dictionary → JSON string                               │
│  15. Set HTTP headers (Content-Type: application/json)             │
│  16. Send HTTP response with status code                           │
└─────────────────────────────────────────────────────────────────────┘
                                  ↓
┌─────────────────────────────────────────────────────────────────────┐
│                       CLIENT SIDE                                  │
│  17. Client receives JSON response:                                │
│     {"name":"Laptop","price":1299.99,"quantity":2,"total":2599.98} │
│  18. Client processes the response                                 │
└─────────────────────────────────────────────────────────────────────┘
```

---

## **BENEFITS OF USING BASEMODEL AT EACH STAGE**

### **1. DESERIALIZATION BENEFITS**

**Benefit: Automatic Type Conversion**
```python
# Without BaseModel:
data = {"price": "1299.99"}  # String from JSON
try:
    price = float(data["price"])  # Manual conversion
except ValueError:
    raise Exception("Invalid price")

# With BaseModel:
class Item(BaseModel):
    price: float  # ✅ Auto-converts "1299.99" → 129.99
```

**Benefit: No Manual JSON Parsing**
```python
# Without BaseModel:
import json
raw_body = await request.body()
data = json.loads(raw_body)  # Manual parsing

# With BaseModel:
@app.post("/items")
def create_item(item: Item):  # ✅ Auto-parsed
    # item is already Python object
```

### **2. VALIDATION BENEFITS**

**Benefit: Comprehensive Validation**
```python
class Product(BaseModel):
    name: str
    price: float = Field(gt=0, le=10000)  # Price between 0-10000
    quantity: int = Field(ge=0)  # Non-negative
    
# ✅ Single line validates:
# 1. Types (str, float, int)
# 2. Value ranges (price > 0, quantity >= 0)
# 3. Required fields (name must be present)
```

**Benefit: Clean Error Messages**
```python
# BaseModel provides structured errors:
try:
    Product(name="", price=-10, quantity=-5)
except ValidationError as e:
    print(e.json())
    # Returns:
    # [
    #   {
    #     "loc": ["name"],
    #     "msg": "field required",
    #     "type": "value_error.missing"
    #   },
    #   {
    #     "loc": ["price"],
    #     "msg": "ensure this value is greater than 0",
    #     "type": "value_error.number.not_gt"
    #   }
    # ]
```

### **3. BUSINESS LOGIC BENEFITS**

**Benefit: Type Safety & IDE Support**
```python
class User(BaseModel):
    email: str
    age: int

user = User(email="test@example.com", age=25)

# ✅ IDE autocomplete works:
user.em  # IDE suggests "email"
user.ag  # IDE suggests "age"

# ✅ Type checking works:
def calculate(user: User):
    # IDE knows user.age is int
    # IDE knows user.email is str
    return user.age * 2  # Type-safe operation
```

**Benefit: Clean Business Logic**
```python
# Without BaseModel:
def process_order(data: dict):
    # Validation clutter
    if not isinstance(data.get('quantity'), int):
        raise ValueError("Quantity must be integer")
    if data.get('quantity', 0) <= 0:
        raise ValueError("Quantity must be positive")
    # ... more validation
    # Finally business logic
    total = data['price'] * data['quantity']

# With BaseModel:
def process_order(item: Item):  # ✅ Already validated
    # Clean business logic only
    total = item.price * item.quantity
```

### **4. SERIALIZATION BENEFITS**

**Benefit: Automatic JSON Conversion**
```python
class Order(BaseModel):
    id: int
    items: List[Item]
    created_at: datetime

order = Order(id=1, items=[...], created_at=datetime.now())

# ✅ One-line serialization:
json_response = order.json()
# Returns valid JSON with datetime converted to ISO string
# {"id": 1, "items": [...], "created_at": "2024-01-12T10:30:00Z"}

# Without BaseModel:
response = {
    "id": order.id,
    "items": [item.__dict__ for item in order.items],
    "created_at": order.created_at.isoformat()  # Manual conversion
}
```

**Benefit: Nested Serialization**
```python
class Address(BaseModel):
    street: str
    city: str

class User(BaseModel):
    name: str
    address: Address  # Nested BaseModel

user = User(name="John", address=Address(street="123 Main", city="NYC"))

# ✅ Nested serialization automatic:
user_dict = user.dict()
# {
#   "name": "John",
#   "address": {"street": "123 Main", "city": "NYC"}
# }
```

### **5. DEVELOPMENT BENEFITS**

**Benefit: Automatic API Documentation**
```python
class Item(BaseModel):
    name: str
    price: float
    
@app.post("/items")
def create_item(item: Item):
    return item

# ✅ FastAPI automatically generates:
# - Swagger UI docs at /docs
# - ReDoc at /redoc
# - OpenAPI schema with full model definitions
# - Example requests and responses
```

**Benefit: Code Reusability**
```python
# Define once, use everywhere
class User(BaseModel):
    email: str
    name: str

# Use in multiple endpoints:
@app.get("/users/{user_id}")
def get_user(user_id: int) -> User:  # Response model
    return user

@app.post("/users")
def create_user(user: User):  # Request model
    return user

@app.put("/users/{user_id}")
def update_user(user_id: int, user: User):  # Request model
    return user
```


