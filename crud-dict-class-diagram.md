```python
# ┌──────────────────────────────────────────────────────────────┐
# │                      CLASS DIAGRAM (simple text version)      │
# └──────────────────────────────────────────────────────────────┘
#
#                         +-------------------+
#                         │     Product       │
#                         +-------------------+
#                         │ - id: int         │
#                         │ - name: str       │
#                         │ - price: float    │
#                         │ - stock: int      │
#                         │ - category: str   │
#                         +-------------------+
#                         │ + to_dict()       │
#                         │ + from_dict()     │  ← classmethod
#                         │ + __str__()       │
#                         +-------------------+
#                                   ▲
#                                   │  (contains many)
#                                   ▼
#                    +---------------------------------+
#                    │        ProductManager           │
#                    +---------------------------------+
#                    │ - products: list[Product]       │
#                    │ - _next_id: int                 │
#                    +---------------------------------+
#                    │ + create_product(...)           │  ← CREATE
#                    │ + create_from_dict(...)         │  ← CREATE (alternative)
#                    │ + get_all()                     │  ← READ
#                    │ + get_by_id(id)                 │  ← READ
#                    │ + find_by_name(query)           │  ← READ (search)
#                    │ + get_by_category(category)     │  ← READ (filter)
#                    │ + update_full(id, ...)          │  ← UPDATE (PUT-like)
#                    │ + update_partial(id, **kwargs)  │  ← UPDATE (PATCH-like)
#                    │ + delete(id)                    │  ← DELETE
#                    │ + display_all()                 │  ← presentation
#                    +---------------------------------+
#
# Relationship: ProductManager 1 ───► * Product   (composition)

class Product:
    """
    Represents a single product entity in the inventory system.
    
    This is the data model class - it holds product information
    and provides basic conversion methods (to/from dictionary).
    """
    
    def __init__(self, id: int, name: str, price: float, stock: int, category: str = "Uncategorized"):
        """
        Initialize a new Product instance.
        
        Args:
            id: Unique identifier of the product
            name: Product name
            price: Price per unit
            stock: Current quantity in stock
            category: Product category (optional)
        """
        self.id = id
        self.name = name
        self.price = price
        self.stock = stock
        self.category = category

    def __str__(self) -> str:
        """Human-readable string representation of the product (used in prints)"""
        return (f"ID: {self.id:3d} | {self.name:18} | "
                f"${self.price:8.2f} | Stock: {self.stock:4d} | "
                f"Cat: {self.category}")

    def to_dict(self) -> dict:
        """Convert product object to dictionary (useful for JSON serialization)"""
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "stock": self.stock,
            "category": self.category
        }

    @classmethod
    def from_dict(cls, data: dict) -> 'Product':
        """
        Factory method: create Product instance from dictionary.
        Very useful when loading data from JSON/API/files.
        """
        return cls(
            id=data.get("id", 0),
            name=data.get("name", ""),
            price=data.get("price", 0.0),
            stock=data.get("stock", 0),
            category=data.get("category", "Uncategorized")
        )


class ProductManager:
    """
    Manages the collection of products - main business logic class.
    
    Implements full CRUD operations + searching + display functionality.
    Acts as Repository/Service layer in small applications.
    """
    
    def __init__(self):
        """Initialize empty product collection with automatic ID generator"""
        self.products: list[Product] = []
        self._next_id: int = 1

    def _find_product_index(self, product_id: int) -> int:
        """
        Internal helper: finds index of product by ID.
        Returns -1 if product was not found.
        """
        for i, product in enumerate(self.products):
            if product.id == product_id:
                return i
        return -1

    # ── CREATE ─────────────────────────────────────────────────────

    def create_product(self, name: str, price: float, stock: int, category: str = "Uncategorized") -> Product | None:
        """
        Create and add a new product to the collection (most common create method).
        
        Returns created Product object or None if validation failed.
        """
        if not name.strip() or price < 0 or stock < 0:
            print("❌ Invalid product data (empty name or negative values)")
            return None

        product = Product(
            id=self._next_id,
            name=name.strip(),
            price=price,
            stock=stock,
            category=category.strip()
        )

        self.products.append(product)
        self._next_id += 1

        print(f"✓ Product created: {product.name} (ID: {product.id})")
        return product

    def create_from_dict(self, data: dict) -> Product | None:
        """
        Alternative create method - useful when receiving data from JSON,
        API, file, database etc.
        """
        required_fields = {"name", "price", "stock"}
        if not all(field in data for field in required_fields):
            print("❌ Missing required fields (name, price, stock)")
            return None

        product = Product.from_dict(data)
        
        # Protect auto-increment ID sequence
        if product.id < self._next_id:
            product.id = self._next_id

        self.products.append(product)
        self._next_id = max(self._next_id, product.id + 1)

        print(f"✓ Product created from dictionary: {product.name} (ID: {product.id})")
        return product

    # ── READ ───────────────────────────────────────────────────────

    def get_all(self) -> list[Product]:
        """Return copy of all products (defensive copy)"""
        return self.products.copy()

    def get_by_id(self, product_id: int) -> Product | None:
        """Find product by its unique ID"""
        for product in self.products:
            if product.id == product_id:
                return product
        print(f"⚠ Product with ID {product_id} not found")
        return None

    def find_by_name(self, query: str, case_sensitive: bool = False) -> list[Product]:
        """Search products by name (partial match)"""
        query = query if case_sensitive else query.lower()
        return [
            p for p in self.products
            if query in (p.name if case_sensitive else p.name.lower())
        ]

    def get_by_category(self, category: str) -> list[Product]:
        """Get all products belonging to given category"""
        cat_lower = category.lower()
        return [p for p in self.products if p.category.lower() == cat_lower]

    # ── UPDATE ─────────────────────────────────────────────────────

    def update_full(self, product_id: int, name=None, price=None, stock=None, category=None) -> Product | None:
        """Full update of product (PUT style)"""
        product = self.get_by_id(product_id)
        if not product:
            return None

        if name is not None:     product.name = name
        if price is not None:    product.price = price
        if stock is not None:    product.stock = stock
        if category is not None: product.category = category

        print(f"↻ Full update completed → ID {product_id}")
        return product

    def update_partial(self, product_id: int, **kwargs) -> Product | None:
        """
        Partial update of product (PATCH style).
        Only provided fields will be changed.
        """
        product = self.get_by_id(product_id)
        if not product:
            return None

        for key, value in kwargs.items():
            if key == "id":
                print("⚠ Cannot change product ID")
                continue
            if hasattr(product, key):
                setattr(product, key, value)
            else:
                print(f"⚠ Unknown field skipped: {key}")

        print(f"✎ Partial update completed → ID {product_id}")
        return product

    # ── DELETE ─────────────────────────────────────────────────────

    def delete(self, product_id: int) -> bool:
        """Remove product from collection by ID"""
        idx = self._find_product_index(product_id)
        if idx == -1:
            print(f"⚠ Cannot delete - product ID {product_id} not found")
            return False

        deleted = self.products.pop(idx)
        print(f"🗑 Deleted: {deleted.name} (ID: {product_id})")
        return True

    # ── PRESENTATION ───────────────────────────────────────────────

    def display_all(self) -> None:
        """Pretty print all products in the inventory"""
        if not self.products:
            print("📦 Inventory is empty")
            return

        print("\n" + "═" * 78)
        print(" " * 25 + "CURRENT INVENTORY")
        print("═" * 78)
        for product in self.products:
            print(str(product))
        print("═" * 78)
        print(f"  Total products: {len(self.products)}")
        print()
    # ──────────────────────────────────────────────
#                USAGE EXAMPLE
# ──────────────────────────────────────────────

if __name__ == "__main__":
    store = ProductManager()

    # Initial data
    initial_products = [
        {"name": "Laptop",      "price": 1299.99, "stock": 15, "category": "Electronics"},
        {"name": "Mouse",       "price": 24.99,   "stock": 80, "category": "Accessories"},
        {"name": "Keyboard",    "price": 59.99,   "stock": 45, "category": "Accessories"}
    ]

    print("Loading initial products...\n")
    for data in initial_products:
        store.create_from_dict(data)

    store.display_all()

    # Create
    print("\nAdding new products:")
    store.create_product("Monitor", 249.99, 22, "Electronics")
    store.create_product("USB-C Cable", 12.99, 150)

    store.display_all()

    # Read
    print("\nFinding products with 'mouse':")
    mice = store.find_by_name("mouse")
    for item in mice:
        print("   →", item)

    # Update
    print("\nUpdating Mouse (ID probably 2):")
    store.update_partial(2, price=29.99, stock=95, name="Wireless Mouse")

    store.display_all()

    # Delete
    print("\nDeleting Keyboard...")
    store.delete(3)  # assuming Keyboard got ID 3

    store.display_all()
```

### Summary - Design Decisions

- Two classes → clear separation of concerns  
- `Product` = data + basic behavior  
- `ProductManager` = collection management + business logic (CRUD)  
- Automatic ID generation  
- Defensive copying where appropriate  
- Both dictionary-based and explicit parameter create methods  
- Full (PUT) + partial (PATCH) update styles  
- Good naming + type hints + detailed documentation
