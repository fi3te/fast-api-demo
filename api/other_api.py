from typing import Optional
from uuid import uuid4

from fastapi import APIRouter
from fastapi import Header, Cookie
from starlette.responses import FileResponse, Response

router = APIRouter(prefix='/other')


@router.get("/header")
def user_agent_header(user_agent: Optional[str] = Header(None, convert_underscores=True)):
    return {"User-Agent": user_agent}


@router.get("/file")
async def download_file():
    return FileResponse('../data/model.py')


@router.get("/cookie/write")
def write_cookie(response: Response):
    response.set_cookie(key="session_id", value=str(uuid4()))
    return {"cookie": "updated"}


@router.get("/cookie/read")
def read_cookie(response: Response, session_id: Optional[str] = Cookie(None)):
    response.delete_cookie(key="session_id")
    return {"cookie": session_id}
