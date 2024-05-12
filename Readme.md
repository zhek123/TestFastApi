Создай .env файл и добавь в него переменные окружения:
```
DATABASE_URL=postgresql://user:password@localhost:5432/dbname
```
Примени миграции:
```
make migrate
```
Запусти сервер:
```
make run
```

Запуск тестов:
```
make test
```