from repository import TaskRepository
from fastapi import APIRouter, Depends
from typing import  Annotated
from schemas import STask, STaskAdd, STaskID

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)

@router.post("")
async def add_task(task: Annotated[STaskAdd, Depends()]):
    task_id = await TaskRepository.add_task(task)
    return {"status": True, "task_id": task_id}

@router.get("")
async def get_tasks():
    tasks = await TaskRepository.find_all()
    return tasks