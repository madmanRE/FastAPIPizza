from pydantic import BaseModel
from typing import Optional


class SignUpModel(BaseModel):
    id: Optional[int]
    username: str
    email: str
    password: str
    is_staff: Optional[bool]
    is_active: Optional[bool]

    class Config:
        orm_mode = True
        schema_extra = {
            'example': {
                "username": "johndoe",
                "email": "johndoe@gmail.com",
                "password": "password",
                "is_staff": False,
                "is_active": True
            }
        }


class Settings(BaseModel):
    authjwt_secret_key: str = '846ab1c9d63a0f36fcb6ce8da7fb3029a2d278a5892a65d100fe08e6a87b4d22'


class LoginModel(BaseModel):
    username: str
    password: str


class OrderModel(BaseModel):
    id: Optional[int]
    quantity: int
    order_status: Optional[str] = "RENDING"
    pizza_size: Optional[str] = "SMALL"
    user_id: Optional[int]

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "quantity": 2,
                "pizza_size": "LARGE",

            }
        }