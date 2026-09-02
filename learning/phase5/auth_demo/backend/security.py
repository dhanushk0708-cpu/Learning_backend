import jwt
from pwdlib import PasswordHash

SECRET_KEY = "12345"
ALGORITHM = "HS256"

password_hash = PasswordHash.recommended()


def verify_password(password, hashed_password):
    return password_hash.verify(password, hashed_password)


def create_access_token(user):
    payload = {"sub": str(user.id), "role": user.role}

    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

    return token


def decode_access_token(token):
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

    return payload
