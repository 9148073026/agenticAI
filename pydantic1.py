from pydantic import BaseModel, Field, EmailStr, field_validator , ValidationError


class Address(BaseModel):
    House_number: str
    street: str
    city: str
    state: str
    zip_code: str


class User(BaseModel):
    user_id: int
    username: str
    email: EmailStr
    is_active: bool
    age: int = Field(ge=0, le=120)
    phone: str | None = None
    address: Address | None = None

    @field_validator("user_id")
    @classmethod
    def validate_user_data(cls, user_id: int) -> User:

        if len(str(user_id)) < 5:
            raise ValueError("user_id must be at least 5 digits long")
        return user_id



class UserGroup(BaseModel):
    group_name: str
    users: list[User]




user1 = User(
    user_id=12754,
    username="john_doe",
    email="abc@abc.com",
    is_active=True,
    age=30
)

address2 = Address(
    House_number="123678",
    street="Main St",
    city="New York",
    state="NY",
    zip_code="10001",
)

user2 = User(
    user_id=288888,
    username="jane_doe",
    email="def@def.com",
    is_active=False,
    age=99,
    address=address2,
)

print(user1)
print(user2)  # Age 99 is valid: it is between 0 and 120


# Dictionary → validated model
data = {
    "user_id": 3988775,
    "username": "alice_smith",
    "email": "alice@alice.com",
    "is_active": True,
    "age": 25,
}

user3 = User.model_validate(data)

print(user3)
print(user3.model_dump())
print(user3.model_dump_json())
print(user3.phone)    # None
print(user3.address)  # None

print(user2.model_dump())
print(user2.model_dump_json())


# Dictionary containing another dictionary
data_with_address = {
    "user_id": 464542,
    "username": "alice_smith",
    "email": "alice@alice.com",
    "is_active": True,
    "age": 25,
    "address": {
        "House_number": "123",
        "street": "Main St",
        "city": "New York",
        "state": "NY",
        "zip_code": "10001",
    },
}

user4 = User.model_validate(data_with_address)

print("Printing user4 address:")
print(user4.address)


# Validate a list of users
user_group1 = UserGroup(
    group_name="Group1",
    users=[user1, user2, user3, user4],
)

print(user_group1.model_dump())

try:
    User4 = User(
        user_id=4,
        username="alice_smith",
        email="alice@alice.com",
        is_active=True,
        age=25
    )
except ValidationError as e:
    print("Validation error occurred:")
    print(e)



