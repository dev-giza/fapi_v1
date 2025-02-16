from db import new_session, TaskOrm
from schemas import STask, STaskAdd
from sqlalchemy import select

class TaskRepository:
    @classmethod
    async def add_task(cls, data: STaskAdd):
        async with new_session() as session:
            task_dict = data.model_dump() # transfer to dict

            task = TaskOrm(**task_dict) # ** unzip

            session.add(task)
            await session.flush() # to return id before commitment
            await session.commit()

            return task.id

    @classmethod
    async def find_all(cls):
        async with new_session() as session:

            query = select(TaskOrm)

            result = await session.execute(query) # return iterator
            task_models = result.scalars().all()

            return task_models
    