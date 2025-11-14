# Используем официальный образ Python 3.11
FROM python:3.11-slim

# Рабочая директория в контейнере
WORKDIR /app

# Копируем зависимости
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем приложение и Alembic
COPY ./app ./app
COPY alembic.ini .
COPY alembic ./alembic
COPY wait_for_db.py .

# Устанавливаем PYTHONPATH
ENV PYTHONPATH=/app

# Команда запуска: ждем БД, применяем миграции, запускаем Uvicorn
CMD ["sh", "-c", "python wait_for_db.py && alembic upgrade head && uvicorn app.main:app --host 0.0.0.0 --port 8000"]
