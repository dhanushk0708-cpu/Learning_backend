from models import User
from security import password_hash, verify_password, create_access_token


users = [
    User(1, "dhanush", password_hash.hash("dhanush123"), "citizen"),
    User(2, "mohan", password_hash.hash("mohan123"), "officer"),
    User(3, "admin", password_hash.hash("admin123"), "admin"),
]


def get_user_by_username(username):

    for user in users:
        if user.username == username:
            return user

    return None


def get_user_by_id(user_id):

    for user in users:
        if user.id == user_id:
            return user

    return None


def login(username, password):

    user = get_user_by_username(username)

    if user is None:
        raise Exception("Invalid username or password")

    if not verify_password(password, user.password_hash):
        raise Exception("Invalid username or password")

    return create_access_token(user)
