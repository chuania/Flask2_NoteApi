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
6. Для тестирования API используем Swagger: http://127.0.0.1:5000/swagger-ui 
7. Тестирование pytest: в директории tests вводим `pytest`


## Дополнительный команды 

1. Остановка сервера в терминале: Ctrl+C 
2. Выход из pipenv: `exit`
3. Проверка coverage на покрытие тестами: `coverage run -m pytest ./tests/` 
4. Вывод результата провеки coverage: `coverage report`
5. Сохранение проверки coverage в html: `coverage html`


