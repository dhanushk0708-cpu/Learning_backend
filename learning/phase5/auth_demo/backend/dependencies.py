from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

from auth_service import get_user_by_id
from security import decode_access_token


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")


def get_current_user(token: str = Depends(oauth2_scheme)):

    payload = decode_access_token(token)

    user_id = int(payload["sub"])

    user = get_user_by_id(user_id)

    if user is None:
        raise Exception("Invalid authentication credentials")

    return user
