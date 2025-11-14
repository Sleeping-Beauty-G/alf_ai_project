# ALF AI Project

### Версия: 0.1.0
### Стек: FastAPI, PostgreSQL, SQLAlchemy, Alembic, Docker, AsyncPG

## 📖 О проекте

ALF AI Project — это асинхронное REST API-приложение на Python, предназначенное для работы с запросами, хранения их истории и демонстрации базовой структуры CRUD-сервисов.

## Особенности проекта:
- Асинхронная работа с базой данных через SQLAlchemy + asyncpg

- Миграции Alembic для управления схемой базы данных

- FastAPI с автогенерацией документации OpenAPI

- Docker и Docker Compose для изоляции и удобного запуска

## 📂 Структура проекта
```
alf_ai_project/
├── app/
│   ├── __init__.py
│   ├── main.py                 # FastAPI сервер
│   ├── models.py               # SQLAlchemy модели
│   ├── database.py             # Настройка async DB
│   ├── crud.py                 # CRUD операции
│   ├── schemas.py              # Pydantic схемы
│   ├── deps.py                 # Зависимости FastAPI
│   └── routes/
│       ├── __init__.py
│       ├── query.py            # /query, /history, /result
│       └── ping.py             # /ping
├── alembic/                     # Alembic миграции
│   ├── env.py
│   ├── script.py.mako
│   └── versions/
│       └── 0001_create_query_history_table.py
├── tests/                       # Pytest тесты
│   ├── __init__.py
│   └── test_main.py
├── wait_for_db.py               # Скрипт ожидания запуска БД
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```
## ⚙️ Установка и локальный запуск

- Требования

- Python 3.11+

- Docker 20+

- Docker Compose 2+

- (Опционально) pipenv или poetry для локальной разработки без Docker

## Запуск через Docker
1. Перейдите в корень проекта:
```bash
cd alf_ai_project
```
2. Поднимите контейнеры:
```bash
docker-compose up --build
```
3. Контейнеры:
- db: PostgreSQL 15, порт 5432

- web: FastAPI + Uvicorn, порт 8000
4. Swagger UI доступен по адресу: http://localhost:8000/docs
5. Приветственный маршрут: http://localhost:8000/
 ## Локальный запуск без Docker
1. Создайте виртуальное окружение:
```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```
2. Установите зависимости:
```bash
pip install -r requirements.txt
```
3. Запустите PostgreSQL локально и настройте переменные окружения:
```bash
export DATABASE_URL=postgresql+asyncpg://postgres:postgres@localhost:5432/alf_ai
```
4. Примените миграции Alembic:
```bash
alembic upgrade head
```
5. Запустите FastAPI сервер:
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```
## 🌐 API Endpoints
| Метод | Путь     | Описание                             |
| ----- | -------- | ------------------------------------ |
| GET   | /        | Приветственное сообщение             |
| POST  | /query   | Создать новый запрос                 |
| GET   | /history | Получить историю запросов            |
| GET   | /result  | Заглушка сервера (тестовый endpoint) |
| GET   | /ping    | Проверка доступности сервера         |
Swagger UI автоматически генерирует документацию по адресу /docs. OpenAPI JSON доступен по /openapi.json.
## 🗄️ Работа с базой данных

- Используется PostgreSQL 15

- Миграции через Alembic

- Все таблицы создаются при старте приложения и при вызове скрипта wait_for_db.py

Пример создания таблицы:
```python
from app.database import engine, Base
import asyncio

async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

asyncio.run(create_tables())
```
## 🧪 Тестирование

 Тесты лежат в папке tests/.

 Запуск тестов через pytest:
```bash
pytest tests/
```
## 🐳 Docker & Docker Compose

- Dockerfile создаёт образ с FastAPI и зависимостями

- docker-compose.yml поднимает два сервиса: web и db

- Скрипт wait_for_db.py гарантирует, что база данных готова перед применением миграций

## 🔧 Особенности проекта

- Асинхронная работа с базой данных (asyncpg, SQLAlchemy)

- Автоматическое применение миграций Alembic при старте контейнера

- Поддержка Swagger UI для быстрого тестирования API

- Лёгкая масштабируемость через Docker

## 👩‍💻  АВТОР
**Гюнай Фаталиева**





