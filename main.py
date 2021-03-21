from fastapi import FastAPI

from api import other_api
from api import user_api

app = FastAPI()
app.include_router(other_api.router)
app.include_router(user_api.router)
