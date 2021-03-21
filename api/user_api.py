from typing import List, Optional

from fastapi import APIRouter

from data import user_service
from data.model import User

router = APIRouter(prefix='/user')


@router.get('')
def get_users(id: Optional[str] = None, first_name: Optional[str] = None,
              last_name: Optional[str] = None) -> List[User]:
    return [user for user in user_service.get_users()
            if (id is None or user.id == id)
            and (first_name is None or user.first_name == first_name)
            and (last_name is None or user.last_name == last_name)]


@router.get('/{id}')
def get_user(id: str) -> User:
    user = get_users(id)
    return user[0] if len(user) == 1 else None


@router.post('')
def create_user(user: User) -> User:
    return user_service.create_user(user)


@router.put('/{id}')
def update_user(id: str, user: User) -> User:
    return user_service.update_user(id, user)
