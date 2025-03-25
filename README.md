# Yatube - платформа для блогов (часть 2)

Проект является финальным этапом разработки API Yatube. 
Предназначен для изучения библиотеки Django REST Framework (DRF).

## Функции проекта

* Выкладывание публикаций, работа с публикациями (редактирование, удаление).
* Комментирование публикаций, работа с комментариями (редактирование, удаление).
* Подписка на пользователей, получение подписок пользователя, сделавшего запрос.
* Доступны сообщества, только для просмотра.
* Редактировать и удалять публикации и комментарии может только автор.
* Приложение работает на основе REST API, аутентификация осуществляется при 
помощи JWT-токена. Для неаутентифицированных пользователей доступ к API только 
на чтение.

## Стек технологий
* [Python](https://www.python.org/)
* [Django](https://www.djangoproject.com/)
* [DRF](https://www.django-rest-framework.org/)
* [Djoser](https://djoser.readthedocs.io/en/latest/getting_started.html)
* [SQLite](https://www.sqlite.org/)

## Как развернуть проект
1. Клонируйте репозиторий и перейдите в директорию api_final_yatube:
```bash
git clone git@github.com:igorKolomitseff/api_final_yatube.git
cd api_final_yatube
```

2. Создайте виртуальное окружение и активируйте его:
```bash
python3 -m venv venv
source venv/bin/activate  # Для Linux и macOS
source venv/Scripts/activate  # Для Windows
```

3. Обновите pip и установите зависимости проекта:
```bash
python3 -m pip install --upgrade pip
pip install -r requirements.txt
```

4. Перейдите в директорию yatube_api и примените миграции:
```bash
cd yatube_api/
python3 manage.py migrate
```

5. Создайте суперпользователя, укажите запрашиваемые данные:
```bash
python3 manage.py createsuperuser
```

6. Запустите проект:
```bash
python3 manage.py runserver
```

## Документация API

Техническая документация к API доступна при запущенном проекте по ссылке:

* [ReDoc](http://127.0.0.1:8000/redoc/)

Документация без развёртывания проекта:

[Техническая документация к API](https://github.com/igorKolomitseff/api_final_yatube/blob/master/yatube_api/static/redoc.yaml)

### Автор

[Игорь Коломыцев](https://github.com/igorKolomitseff)