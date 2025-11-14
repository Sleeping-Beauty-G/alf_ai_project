

from fastapi import FastAPI
from app.routes import query, ping
from app.database import engine, Base
import asyncio

app = FastAPI(title="ALF AI Project")

# Роутеры
app.include_router(query.router)
app.include_router(ping.router)

# Корневой маршрут
@app.get("/")
async def root():
    return {"message": "Welcome to ALF AI Project!"}

# Создание таблиц при старте приложения
@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
