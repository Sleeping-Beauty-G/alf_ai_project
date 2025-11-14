
import asyncio
import os
import asyncpg

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+asyncpg://postgres:postgres@db:5432/alf_ai")

async def wait_for_db():
    while True:
        try:
            # asyncpg не использует префикс sqlalchemy+asyncpg
            # поэтому убираем "postgresql+asyncpg://"
            url = DATABASE_URL.replace("postgresql+asyncpg://", "postgres://")
            conn = await asyncpg.connect(url)
            await conn.close()
            print("Database is ready!")
            break
        except Exception as e:
            print("Waiting for database...", e)
            await asyncio.sleep(2)

if __name__ == "__main__":
    asyncio.run(wait_for_db())
