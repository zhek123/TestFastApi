Создайте .env файл и добавте в него переменные окружения:
```
DATABASE_URL=postgresql://user:password@localhost:5432/dbname
```
Установите зависимости:
```
pip install -r requirements.txt
```
Примените миграции:
```
make migrate
```
Запустите сервер:
```
make run
```

Запуск тестов:
```
make test
```