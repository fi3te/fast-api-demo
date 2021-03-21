from enum import Enum
from typing import Optional

from pydantic import BaseModel


class User(BaseModel):
    id: Optional[str]
    first_name: str
    last_name: str


class TaskType(str, Enum):
    onetime = 'onetime'
    recurring = 'recurring'


class Task(BaseModel):
    type: TaskType
    description: str
