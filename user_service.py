from typing import List
from uuid import uuid4

import names

from model import User

users = [
    User(id=str(uuid4()), first_name=names.get_first_name(), last_name=names.get_last_name())
    for i in range(100)
]


def get_users() -> List[User]:
    return users


def create_user(user: User) -> User:
    user.id = uuid4()
    return user


def update_user(id: str, user: User) -> User:
    user.id = id
    return user
