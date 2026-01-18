# Methods, Keywords, and Their Work

## Methods/Functions Used:
1. **`max()`** - Returns the maximum value from an iterable
2. **`if...else`** - Conditional statement for flow control
3. **`isinstance()`** - Checks if an object is of a specific type
4. **`.copy()`** - Creates a shallow copy of a dictionary
5. **`.append()`** - Adds an element to the end of a list
6. **`next()`** - Returns the next item from an iterator
7. **`for...in`** - Loop through items in an iterable
8. **List Comprehension** - `[expression for item in iterable if condition]`
9. **Generator Expression** - `(expression for item in iterable if condition)`
10. **dict.get(key, default) Method**

## Keywords Used:
1. **`def`** - Defines a function
2. **`if`/`elif`/`else`** - Conditional statements
3. **`for`** - Loop iteration
4. **`return`** - Function return value
5. **`None`** - Represents absence of value
6. **`in`** - Membership testing in loops and conditions

---
## 📚 **Essential Methods, Keywords & Syntax**

### **1. `dict.get(key, default)` Method**
**Syntax:** `dictionary.get(key, default_value)`
**Purpose:** Safely retrieve value from dictionary without raising KeyError
```python
# Example:
product = {"name": "Laptop", "price": 999.99}
name = product.get("name", "Unknown")  # Returns "Laptop"
stock = product.get("stock", 0)        # Returns 0 (default), not KeyError
category = product.get("category")     # Returns None if key doesn't exist
```

### **2. `isinstance(object, type)` Function**
**Syntax:** `isinstance(variable, data_type)`
**Purpose:** Check if variable is of specific type
```python
# Example:
products = [{"id": 1}, {"id": 2}]
print(isinstance(products, list))      # True
print(isinstance(products, tuple))     # False
print(isinstance(products[0], dict))   # True
```

### **3. List Comprehension Syntax**
**Syntax:** `[expression for item in iterable if condition]`
**Purpose:** Create new list by transforming/filtering items
```python
# Examples:
# Basic: Get all names
names = [p["name"] for p in products]

# With condition: Get expensive products (>100)
expensive = [p for p in products if p["price"] > 100]

# With transformation: Get names in uppercase
upper_names = [p["name"].upper() for p in products]
```

### **4. Generator Expression Syntax**
**Syntax:** `(expression for item in iterable if condition)`
**Purpose:** Create memory-efficient iterator (not stored in memory all at once)
```python
# Examples:
# Generator for expensive products
expensive_gen = (p for p in products if p["price"] > 100)

# Use with next() to get first match
first_expensive = next(expensive_gen, None)

# Convert to list if needed
expensive_list = list(expensive_gen)
```

### **5. `enumerate()` Function with Index**
**Syntax:** `for index, value in enumerate(iterable, start=0)`
**Purpose:** Get both index and value while iterating
```python
# Example:
products = ["Laptop", "Mouse", "Keyboard"]
for i, product in enumerate(products):
    print(f"Index {i}: {product}")
# Output: Index 0: Laptop, Index 1: Mouse, Index 2: Keyboard

# With custom start index:
for i, product in enumerate(products, start=1):
    print(f"#{i}: {product}")
```
---
## Multiple Ways Comparison:

### 1. **Finding a single item:**
- **Best**: `next((p for p in products if condition), None)` - Stops at first match
- **Alternative**: `[p for p in products if condition][0]` - Creates full list first
- **Alternative**: Filter with lambda: `next(filter(lambda p: condition, products), None)`

### 2. **Filtering multiple items:**
- **Best**: List comprehension `[p for p in products if condition]`
- **Alternative**: `filter(lambda p: condition, products)`
- **Alternative**: Traditional for loop with append

### 3. **Updating items:**
- **PUT**: Replace entire object - good for complete updates
- **PATCH**: Update only specified fields - good for partial updates

### 4. **Deleting items:**
- **Best**: List comprehension to filter out: `products[:] = [p for p in products if p["id"] != id]`
- **Alternative**: `enumerate()` with `pop(index)` - modifies while iterating
- **Alternative**: Create new list and reassign
---

# Complete CRUD Operations for Products Dictionary

```python
products = [
    {"id": 1, "name": "Laptop", "price": 1299.99, "stock": 15, "category": "Electronics"},
    {"id": 2, "name": "Mouse", "price": 24.99, "stock": 80, "category": "Accessories"},
    {"id": 3, "name": "Keyboard", "price": 59.99, "stock": 45, "category": "Accessories"}
]


# =============== CREATE ===============
def add_product(product_data):
    """Add a new product to the list"""
    # Way 1: Dynamic ID with error handling
    try:
        max_id = max(p["id"] for p in products) if products else 0
        new_id = max_id + 1
        
        # Validate required fields
        required_fields = ["name", "price", "stock"]
        for field in required_fields:
            if field not in product_data:
                print(f"Error: Missing required field '{field}'")
                return None
        
        # Create new product with all fields from data plus ID
        new_product = {"id": new_id, **product_data}
        products.append(new_product)
        print(f"✅ Product added: {product_data['name']} (ID: {new_id})")
        return new_product
    
    except (ValueError, KeyError, TypeError) as e:
        print(f"❌ Error adding product: {e}")
        return None
    
    # Way 2: Alternative with explicit field mapping
    """
    new_product = {
        "id": new_id,
        "name": product_data.get("name", ""),
        "price": product_data.get("price", 0.0),
        "stock": product_data.get("stock", 0),
        "category": product_data.get("category", "Uncategorized")
    }
    """


# =============== READ ===============
def get_all_products():
    """Get all products"""
    return products.copy()  # Return copy to prevent accidental modification


def get_product_by_id(product_id):
    """Get a single product by ID"""
    # Way 1: Using next() with generator expression (Most efficient)
    product = next((p for p in products if p["id"] == product_id), None)
    
    # Way 2: Using list comprehension
    # product_list = [p for p in products if p["id"] == product_id]
    # product = product_list[0] if product_list else None
    
    # Way 3: Using filter()
    # product = next(filter(lambda p: p["id"] == product_id, products), None)
    
    if product:
        return product.copy()  # Return copy
    else:
        print(f"⚠️  Product with ID {product_id} not found")
        return None


def search_products_by_name(name_query):
    """Search products by name (case-insensitive partial match)"""
    # Way 1: List comprehension
    results = [p for p in products if name_query.lower() in p["name"].lower()]
    
    # Way 2: Using filter with lambda
    # results = list(filter(lambda p: name_query.lower() in p["name"].lower(), products))
    
    # Way 3: For loop
    """
    results = []
    for product in products:
        if name_query.lower() in product["name"].lower():
            results.append(product)
    """
    
    if results:
        print(f"🔍 Found {len(results)} product(s) matching '{name_query}'")
    else:
        print(f"🔍 No products found matching '{name_query}'")
    
    return results


def get_products_by_category(category):
    """Get all products in a specific category"""
    return [p for p in products if p.get("category", "").lower() == category.lower()]


# =============== UPDATE ===============
def update_product(product_id, update_data):
    """Update a product (PUT - replace entire product)"""
    product = get_product_by_id(product_id)
    
    if not product:
        return None
    
    # Find product index
    product_index = None
    for i, p in enumerate(products):
        if p["id"] == product_id:
            product_index = i
            break
    
    if product_index is not None:
        # Keep the original ID, update everything else
        updated_product = {"id": product_id, **update_data}
        products[product_index] = updated_product
        print(f"🔄 Product ID {product_id} fully updated")
        return updated_product
    
    return None


def patch_product(product_id, patch_data):
    """Partially update a product (PATCH - update only provided fields)"""
    product = get_product_by_id(product_id)
    
    if not product:
        return None
    
    # Find product index
    product_index = None
    for i, p in enumerate(products):
        if p["id"] == product_id:
            product_index = i
            break
    
    if product_index is not None:
        # Update only the fields provided in patch_data
        updated_product = products[product_index].copy()
        for key, value in patch_data.items():
            if key != "id":  # Prevent changing the ID
                updated_product[key] = value
        
        products[product_index] = updated_product
        print(f"🔧 Product ID {product_id} partially updated")
        return updated_product
    
    return None


# =============== DELETE ===============
def delete_product(product_id):
    """Delete a product by ID"""
    # Way 1: Using list comprehension to filter out
    original_length = len(products)
    products[:] = [p for p in products if p["id"] != product_id]
    
    # Way 2: Using enumerate and pop
    """
    for i, p in enumerate(products):
        if p["id"] == product_id:
            deleted_product = products.pop(i)
            print(f"🗑️  Product deleted: {deleted_product['name']}")
            return deleted_product
    """
    
    if len(products) < original_length:
        print(f"🗑️  Product ID {product_id} deleted")
        return True
    else:
        print(f"⚠️  Product ID {product_id} not found for deletion")
        return False


# =============== HELPER FUNCTIONS ===============
def display_product(product):
    """Display a single product in readable format"""
    if product:
        print(f"\n{'='*40}")
        print(f"ID: {product['id']}")
        print(f"Name: {product['name']}")
        print(f"Price: ${product['price']:.2f}")
        print(f"Stock: {product['stock']}")
        if 'category' in product:
            print(f"Category: {product['category']}")
        print(f"{'='*40}")
    return product


def display_all_products():
    """Display all products in readable format"""
    if not products:
        print("No products available")
        return
    
    print(f"\n{'='*60}")
    print(f"{'PRODUCTS LIST':^60}")
    print(f"{'='*60}")
    for product in products:
        print(f"ID: {product['id']:3} | {product['name']:15} | "
              f"${product['price']:8.2f} | Stock: {product['stock']:3} | "
              f"Category: {product.get('category', 'N/A'):15}")
    print(f"{'='*60}")
    print(f"Total: {len(products)} products")
    return products


# =============== TESTING THE CRUD OPERATIONS ===============
if __name__ == "__main__":
    print("🧪 Testing CRUD Operations\n")
    
    # 1. CREATE - Add new products
    print("1. CREATE Operations:")
    new_data = {"name": "Tablet", "price": 299.99, "stock": 30, "category": "Electronics"}
    add_product(new_data)
    
    new_data2 = {"name": "Gaming Mouse", "price": 79.99, "stock": 25}
    add_product(new_data2)
    
    # 2. READ - Retrieve products
    print("\n2. READ Operations:")
    
    # Get all products
    display_all_products()
    
    # Get by ID
    print("\nSearching for product ID 2:")
    product = get_product_by_id(2)
    display_product(product)
    
    # Search by name
    print("\nSearching for products with 'mouse':")
    mouse_products = search_products_by_name("mouse")
    for p in mouse_products:
        display_product(p)
    
    # Get by category
    print("\nProducts in 'Accessories' category:")
    accessories = get_products_by_category("Accessories")
    for p in accessories:
        display_product(p)
    
    # 3. UPDATE - Modify products
    print("\n3. UPDATE Operations:")
    
    # PUT - Full update
    print("Full update (PUT) for product ID 2:")
    update_data = {"name": "Wireless Mouse Pro", "price": 34.99, "stock": 60, "category": "Premium"}
    update_product(2, update_data)
    display_product(get_product_by_id(2))
    
    # PATCH - Partial update
    print("\nPartial update (PATCH) for product ID 3:")
    patch_data = {"price": 49.99, "stock": 50}  # Only update price and stock
    patch_product(3, patch_data)
    display_product(get_product_by_id(3))
    
    # 4. DELETE - Remove product
    print("\n4. DELETE Operations:")
    print("Before deletion:")
    display_all_products()
    
    delete_product(1)  # Delete Laptop
    
    print("\nAfter deletion:")
    display_all_products()
    
    # 5. Error handling
    print("\n5. Error Handling:")
    get_product_by_id(999)  # Non-existent ID
    update_product(999, {"name": "Test"})  # Update non-existent
    delete_product(999)  # Delete non-existent
```


## Best Practices Implemented:
1. **Return copies** to prevent unintended modifications
2. **Error handling** with try-except blocks
3. **Input validation** for required fields
4. **Case-insensitive search** for better UX
5. **Meaningful return values** (None for not found, product for success)
6. **Clear console output** with emojis and formatting
7. **Flexible field handling** with `.get()` method and default values
8. **Modular functions** with single responsibility
9. **Documentation** with docstrings
10. **Testing section** to demonstrate all operations

## 🎯 **Key Takeaways:**

### **When to use `dict.get()`:**
1. **Accessing optional fields** - Won't crash if key doesn't exist
2. **Providing default values** - `get("field", default_value)`
3. **Avoiding KeyError** - Safer than direct access with `[]`
4. **Checking existence** - Returns `None` if key doesn't exist

### **When to use index operations:**
1. **Direct modification** - `products[index] = new_value`
2. **Efficient deletion** - `products.pop(index)`
3. **Batch operations** - Process multiple items by index
4. **Tracking position** - Know where item is in list

### **Performance Tips:**
1. **Generator expressions** - Use `()` for memory efficiency with large data
2. **`next()` with generator** - Fastest way to find first match
3. **Index-based operations** - Faster than searching each time
4. **List comprehensions** - Cleaner and often faster than loops

### **Error Prevention:**
1. **Always validate input** - Use `isinstance()` and `get()`
2. **Handle missing keys** - Use `.get()` with defaults
3. **Check list bounds** - Verify index exists before accessing
4. **Use copies for safety** - `dict.copy()` prevents unintended mutations
