Проект **"NoteApi"** - построение **REST API** с помощью **Flask** для работы с заметками. Авторизованный пользаватель может оставлять свои заметки, изменять и удалять их. Заметки других пользователей доступны, если они публичные. 
Что было добавлено в данную работу:

- Работа со **Swagger** с помощью библиотек ***flasgger*** и ***apispec***
- Тестирование запросов с помощью ***pytest*** и просмотр покрытия с ***coverage***

## Инструкция по запуску проекта после клонирования

1. Устанавливаем pipenv: `pip install pipenv`
2. Создаем и активируем pipenv: `pipenv shell`
Имя окружения = имя директории
3. Устанавливаем пакеты из Pipfile: `pipenv install`
4. Создаем базу данных: `flask db upgrade`
5. Запускаем проект: `pipenv run python app.py`
6. Для тестирования API-интерфейсов импортируйте json из директории PostmanCollection в соответствующие инструменты(Postman, Thunder Client для VS Code и др.)

## Дополнительный команды 

1. Остановка сервера в терминале: Ctrl+C 
2. Выход из pipenv: `exit`

