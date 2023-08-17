from fastapi import APIRouter, status
from fastapi.exceptions import HTTPException

from schemas import SignUpModel
from database import session, engine
from models import User

auth_router = APIRouter(
    prefix='/auth'
)

@auth_router.get('/')
async def signup():
    return {'message': 'This is auth rote signup page'}

@auth_router.post('/signup')
async def signup(user: SignUpModel):
    db_email = session.query(User).filter(User.email == user.email).first()
    if db_email is not None:
        return HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='User with this email already exists'
        )

    db_username = session.query(User).filter(User.username == user.username).first()
    if db_username is not None:
        return HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='User with this username already exists'
        )

    new_user = User(
        username=user.username,
        email=user.email,
        password=user.password,
        is_staff=user.is_staff,
        is_active=user.is_active
    )

