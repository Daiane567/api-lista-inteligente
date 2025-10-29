from pydantic import BaseModel
from typing import Optional

class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    priority: int = 1

class TaskCreate(TaskBase):
    pass

class Task(TaskBase):
    id: int
    completed: bool

    model_config = {
        "from_attributes": True
    }
