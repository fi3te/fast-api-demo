from typing import List

from fastapi import APIRouter

from data import task_service
from data.model import Task, TaskType

router = APIRouter(prefix='/task', tags=['Task'])


@router.get('')
def get_tasks() -> List[Task]:
    return task_service.generate()


@router.get('/{task_type}')
def get_tasks_of_specific_type(task_type: TaskType) -> List[Task]:
    return [task for task in task_service.generate() if task.type == task_type]
