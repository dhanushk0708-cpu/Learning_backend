class User:
    def __init__(self, id, username, password_hash, role):
        self.id = id
        self.username = username
        self.password_hash = password_hash
        self.role = role


from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass
