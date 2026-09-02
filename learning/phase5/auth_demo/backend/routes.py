from fastapi import APIRouter, Depends

from fastapi.security import OAuth2PasswordRequestForm
from auth_service import login
from dependencies import get_current_user


router = APIRouter()


@router.post("/login")
def login_user(form_data: OAuth2PasswordRequestForm = Depends()):

    token = login(form_data.username, form_data.password)

    return {"access_token": token, "token_type": "bearer"}


@router.get("/profile")
def profile(user=Depends(get_current_user)):

    return {"id": user.id, "username": user.username, "role": user.role}
