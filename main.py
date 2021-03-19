from typing import List, Optional
from uuid import uuid4

from fastapi import FastAPI, Header, Cookie
from starlette.responses import FileResponse, Response

import user_service
from model import User

app = FastAPI()


@app.get('/user')
def get_users(id: Optional[str] = None, first_name: Optional[str] = None,
              last_name: Optional[str] = None) -> List[User]:
    return [user for user in user_service.get_users()
            if (id is None or user.id == id)
            and (first_name is None or user.first_name == first_name)
            and (last_name is None or user.last_name == last_name)]


@app.get('/user/{id}')
def get_user(id: str) -> User:
    user = get_users(id)
    return user[0] if len(user) == 1 else None


@app.post('/user')
def create_user(user: User) -> User:
    return user_service.create_user(user)


@app.put('/user/{id}')
def update_user(id: str, user: User) -> User:
    return user_service.update_user(id, user)


@app.get("/other/header")
def user_agent_header(user_agent: Optional[str] = Header(None, convert_underscores=True)):
    return {"User-Agent": user_agent}


@app.get("/other/file")
async def download_file():
    return FileResponse('model.py')


@app.get("/other/cookie/write")
def write_cookie(response: Response):
    response.set_cookie(key="session_id", value=str(uuid4()))
    return {"cookie": "updated"}


@app.get("/other/cookie/read")
def read_cookie(response: Response, session_id: Optional[str] = Cookie(None)):
    response.delete_cookie(key="session_id")
    return {"cookie": session_id}
