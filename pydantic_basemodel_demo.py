from pydantic import (
    BaseModel, Field, validator,
    conint, constr, confloat, EmailStr,
    root_validator
)
from typing import Optional, List, Dict
from datetime import datetime

# ✅ Simple BaseModel
class User(BaseModel):
    id: int
    name: str
    email: EmailStr
    is_active: bool = True
    signup_ts: Optional[datetime] = None

# ✅ Nested Model
class Address(BaseModel):
    city: str
    zip_code: str

class Profile(BaseModel):
    user: User
    address: Address

# ✅ Aliases
class UserAlias(BaseModel):
    full_name: str = Field(..., alias="fullName")

# ✅ Constraints
class Product(BaseModel):
    name: constr(min_length=3)
    price: confloat(gt=0)
    quantity: conint(gt=0, le=100)

# ✅ List and Dict Types
class Store(BaseModel):
    products: List[Product]
    metadata: Dict[str, str]

# ✅ Custom Validator
class CapitalNameUser(BaseModel):
    name: str

    @validator("name")
    def check_capital(cls, v):
        if not v.istitle():
            raise ValueError("Name must be title-cased")
        return v

# ✅ Root Validator (multiple fields at once)
class DateRange(BaseModel):
    start: datetime
    end: datetime

    @root_validator
    def check_dates(cls, values):
        start, end = values.get('start'), values.get('end')
        if start and end and start >= end:
            raise ValueError("start must be before end")
        return values

                               
# 🔒 Immutability

class ImmutableUser(BaseModel):
    id: int
    name: str

    class Config:
        allow_mutation = False


# ⚙️ Model Config Example
class ORMUser(BaseModel):
    id: int
    username: str

    class Config:
        orm_mode = True
        extra = "forbid"  # Forbid unknown fields
        allow_population_by_field_name = True


# ✅ Model Usage
if __name__ == "__main__":
    user = User(id=1, name="John", email="john@example.com")
    print(user.dict())

    address = Address(city="New York", zip_code="10001")
    profile = Profile(user=user, address=address)
    print(profile.json(indent=2))

    product = Product(name="Laptop", price=1200.99, quantity=2)
    print(product)

    store = Store(products=[product], metadata={"location": "NYC"})
    print(store)

    # Validation error
    try:
        invalid_user = CapitalNameUser(name="john")
    except Exception as e:
        print("Validation Error:", e)
