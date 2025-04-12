# Pydantic: Fast and Easy Data Validation in Python 🚀

## 📌 What is Pydantic?

**Pydantic** is a powerful data validation and settings management library in Python. It's built on top of **Python type hints** and uses them to validate and serialize data.

## 💡 Why Use Pydantic?

- ✅ Type safety and validation out-of-the-box
- 🔄 Data serialization/deserialization (JSON-friendly)
- 📦 Great for APIs (especially with FastAPI)
- 📐 Automatic error handling and messages
- 🔍 Easier debugging with clear traceback

---

## 📚 Key Concepts (Theory First)

### 1. `BaseModel`
The core of Pydantic. Every model should inherit from `BaseModel`.

```python
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
```

### 2. Data Validation

Pydantic validates input data automatically.

```python
user = User(id="123", name="John")  # id will be converted to int
```

### 3. Type Coercion

Pydantic is smart. It converts types when possible:
- `"123"` → `123` (str to int)
- `"true"` → `True` (str to bool)
- `"2023-01-01"` → `datetime.date`

### 4. Constraints

You can set limits using types like `conint`, `constr`, `confloat`, etc.

```python
from pydantic import conint

class Product(BaseModel):
    quantity: conint(gt=0, lt=100)
```

### 5. Aliases (Renaming fields)

```python
class User(BaseModel):
    full_name: str = Field(..., alias='fullName')
```

### 6. Nested Models

Models can be nested for structured data.

```python
class Address(BaseModel):
    city: str
    zipcode: str

class Person(BaseModel):
    name: str
    address: Address
```

### 7. Default Values & Optional Fields

```python
from typing import Optional

class User(BaseModel):
    name: str
    age: Optional[int] = None
```

### 8. Validators

Add custom logic for validation.

```python
from pydantic import validator

class User(BaseModel):
    name: str

    @validator('name')
    def name_must_be_capitalized(cls, v):
        if not v.istitle():
            raise ValueError('Name must be capitalized')
        return v
```

#### 🔒 10. Immutability
```python
class ImmutableUser(BaseModel):
    id: int
    name: str

    class Config:
        allow_mutation = False
```

#### ⚙️ 11. Model Config Example
```python
class ORMUser(BaseModel):
    id: int
    username: str

    class Config:
        orm_mode = True
        extra = "forbid"  # Forbid unknown fields
        allow_population_by_field_name = True
```

---

## 🧪 Run the Examples

Make sure you install Pydantic:

```bash
pip install pydantic
```

# Check the code in pydantic_basemodel.py