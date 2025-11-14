from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from .. import schemas, crud, database
import random, asyncio

router = APIRouter()

@router.post("/query", response_model=schemas.QueryResponse)
async def create_query(query: schemas.QueryCreate, db: AsyncSession = Depends(database.get_db)):
    # Эмуляция задержки внешнего сервера (до 60 секунд)
    await asyncio.sleep(random.randint(1, 5))  # для теста ставим 1-5 сек
    result = random.choice([True, False])
    return await crud.create_query(db, query, result)

@router.get("/history", response_model=list[schemas.QueryResponse])
async def history(db: AsyncSession = Depends(database.get_db)):
    return await crud.get_history(db)

@router.get("/result")
async def fake_server():
    # Эмуляция внешнего сервера
    return {"result": random.choice([True, False])}
