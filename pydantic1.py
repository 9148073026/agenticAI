from pydantic import BaseModel, Field, EmailStr

class User(BaseModel):
    user_id: int
    username: str 
    email: EmailStr
    is_active: bool 
    age: int = Field(ge=0, le=120)  # Age must be between 0 and 120

User1 = User(user_id=1, username="john_doe", email="abc@abc.com", is_active=True, age=30)
#User2 = User(user_id=2, username="jane_doe", email="def@def.com", is_active=False, age=125)

print(User1)
#print(User2)  # This will raise a validation error due to age being out of range

# Dictionary → validated model

data = {
    "user_id": 3, 
    "username": "alice_smith",
    "email": "alice@alice.com",
    "is_active": True,
    "age": 25
}

User = User.model_validate(data)
print(User)