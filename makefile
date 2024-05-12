# запуск форматера
black:
	black --line-length=120 src

# запуск линтера
lint:
	flake8 --max-line-length=120 src

# запуск тестов
test:
	pytest

# запуск проекта
run:
	uvicorn main:app --reload

# сделать миграции 
migrations:
	alembic revision --autogenerate

# применить миграции
migrate:
	alembic upgrade head
	
# установка зависимостей
install:
	pip install -r requirements.txt