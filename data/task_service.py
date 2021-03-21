import random
from typing import List

from data.model import Task, TaskType


def random_type() -> TaskType:
    return TaskType.onetime if random.randint(0, 1) == 0 else TaskType.recurring


def generate() -> List[Task]:
    return [Task(type=random_type(), description=f'This is a task description ({i})') for i in range(20)]
