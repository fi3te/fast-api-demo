from fastapi import FastAPI

from api import other, task
from api import user

app = FastAPI()
app.include_router(other.router)
app.include_router(user.router)
app.include_router(task.router)
