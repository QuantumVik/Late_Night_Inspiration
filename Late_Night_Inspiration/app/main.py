from fastapi import FastAPI
from Late_Night_Inspiration.app.api.v1.endpoints import ideas
from Late_Night_Inspiration.app.db.init__db import init_db
from Late_Night_Inspiration.app.task.schedular import scheduler_on
from extra.potato import lifespan
from contextlib import asynccontextmanager
import uvicorn


@asynccontextmanager
# Start the schedular when the app starts
async def schedule(app:FastAPI):
    init_db() # Ensure the database is initialized
    scheduler_on()

app = FastAPI(lifespan=lifespan)

app.include_router(ideas.router, prefix='/ideas', tags=['Ideas'])

# @app.get('/')
# def helo():
#     return {'very good'}

if __name__=='__main__':
    uvicorn.run("main:app",port = 8081)
# app.include_router(users.router,prefix='/users',tags=['Users'])

# @app.on_event("startup")
# def on_start():
#     init_db()

