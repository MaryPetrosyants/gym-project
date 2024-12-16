FROM python:3.10-slim-bullseye

# Устанавливаем системные зависимости
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libssl-dev \
    libffi-dev \
    zlib1g-dev \
    libmariadb-dev \
    pkg-config \
    && apt-get clean

# Устанавливаем Python-зависимости
RUN pip install --upgrade pip
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r /app/requirements.txt

# Настраиваем рабочую директорию
COPY . /app
WORKDIR /app/gymapp

# Запуск приложения
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
