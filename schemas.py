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
        from_attributes = True
        json_schema_extra = {
            'example': {
                'username': 'John',
                'email': 'JohnSmith@gmail.com',
                'password': 'smith2004',
                'is_active': True,
                'is_staff': False
            }
        }

class Settings(BaseModel):
    authjwt_secret_key: str = '7b8769aee43cc5c7fbbf6759699aaf598f5bf42e7319207ad432a78c84cfcd55'

class LogInModel(BaseModel):
    username: str
    password: str





