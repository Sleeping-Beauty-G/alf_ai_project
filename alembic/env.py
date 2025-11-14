import asyncio
from logging.config import fileConfig

from sqlalchemy import pool
from sqlalchemy.engine import Connection
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine
from alembic import context

import sys
import os

# Добавляем путь к app, чтобы Alembic видел модуль
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from app.models import Base  # Все модели твоего приложения

# Конфиг Alembic
config = context.config
fileConfig(config.config_file_name)

target_metadata = Base.metadata

# Используем синхронный URL для миграций
def get_sync_url():
    url = config.get_main_option("sqlalchemy.url")
    return url.replace("postgresql+asyncpg", "postgresql")

# Миграции в оффлайн-режиме (sql script)
def run_migrations_offline():
    url = get_sync_url()
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()

# Миграции в онлайн-режиме (применение к базе)
def do_run_migrations(connection: Connection):
    context.configure(connection=connection, target_metadata=target_metadata)
    with context.begin_transaction():
        context.run_migrations()

async def run_migrations_online():
    # Создаем async engine только для Alembic
    connectable = create_async_engine(
        config.get_main_option("sqlalchemy.url"),
        poolclass=pool.NullPool,
    )

    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)
    await connectable.dispose()

# Выбор режима
if context.is_offline_mode():
    run_migrations_offline()
else:
    asyncio.run(run_migrations_online())
