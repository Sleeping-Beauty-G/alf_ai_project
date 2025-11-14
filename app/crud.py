from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from . import models, schemas

async def create_query(db: AsyncSession, query: schemas.QueryCreate, result: bool):
    db_query = models.QueryHistory(
        cadastral_number=query.cadastral_number,
        latitude=query.latitude,
        longitude=query.longitude,
        result=result
    )
    db.add(db_query)
    await db.commit()
    await db.refresh(db_query)
    return db_query

async def get_history(db: AsyncSession):
    result = await db.execute(select(models.QueryHistory))
    return result.scalars().all()

async def get_history_by_cadastral(db: AsyncSession, cadastral_number: str):
    result = await db.execute(select(models.QueryHistory).where(models.QueryHistory.cadastral_number == cadastral_number))
    return result.scalars().all()
