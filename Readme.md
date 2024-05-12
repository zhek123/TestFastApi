Создайте .env файл и добавте в него переменные окружения:
```
DATABASE_URL=postgresql://user:password@localhost:5432/dbname
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