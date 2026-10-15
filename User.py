from pydantic import BaseModel, Field, EmailStr, field_validator , ValidationError
from starlette.datastructures import Address

class User(BaseModel):
    user_id: int
    username: str
    password: str
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

class UserRegistration(BaseModel):
    username: str
    password: str = Field(min_length=8)
    confirm_password: str = Field(min_length=8)

    @field_validator("username")
    @classmethod
    def validate_username(cls, username: str) -> str:
        if len(username) < 3:
            raise ValueError("Username must be at least 3 characters long")
        return username

    @field_validator("password")
    @classmethod
    def validate_password(cls, password: str) -> str:
        if len(password) < 8:
            raise ValueError("Password must be at least 8 characters long")
        return password
    