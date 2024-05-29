# API Yatube

Yatube — это платформа для блогов. Сервис предлагает возможность зарегистрироваться, создать, отредактировать или удалить собственный пост, прокомментировать пост другого автора и подписаться на него.

## Основные зависимости:
* Python = 3.9
* Django = 3.2

Проект реализован с использованием JWT-токенов.

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

``` 
git@github.com:igorKolomitseff/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

``` 
python3 -m venv venv
```

```
source venv/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

``` 
python3 manage.py runserver
```

Документация к проекту **API Yatube** в формате **Redoc** доступна по адресу:
```
http://127.0.0.1:8000/redoc/
```

### Доступные эндпоинты
```
api/v1/jwt/create/
api/v1/jwt/refresh/
api/v1/jwt/verify/
api/v1/posts/
api/v1/posts/{id}/
api/v1/posts/{post_id}/comments/
api/v1/posts/{post_id}/comments/{id}/
api/v1/groups/
api/v1/groups/{id}/
api/v1/follow/
```

### Примеры запросов к API

POST-запрос на получение JWT-токена
```
api/v1/jwt/create/
```
Request:
```json
{
  "username": "Igor_K",
  "password": "qwerty12345"
}
```
Response:
```json
{
  "refresh": "string",
  "access": "string"
}
```

GET-запрос на получение публикации
```
api/v1/posts/{id}/
```
Response:
```json
{
  "id": 1,
  "author": "Igor_K",
  "text": "some text",
  "pub_date": "2019-08-24T14:15:22Z",
  "image": "string",
  "group": 3
}
```

POST-запрос на создание публикации
```
api/v1/posts/{id}/
```
Request:
```json
{
  "text": "some new text",
  "image": "<binary string>",
  "group": 1
}
```
Response:
```json
{
  "id": 2,
  "author": "Igor_K",
  "text": "some new text",
  "pub_date": "2019-08-24T14:15:22Z",
  "image": "string",
  "group": 1
}
```

GET-запрос на получение комментариев
```
api/v1/posts/{post_id}/comments/
```
Response:
```json
[
  {
    "id": 1,
    "author": "Simple_man",
    "text": "text",
    "created": "2019-08-24T14:15:22Z",
    "post": 1
  }
]
```

POST-запрос на добавление комментария
```
api/v1/posts/{post_id}/comments/
```
Request:
```json
{
  "text": "new text"
}
```
Response:
```json
{
  "id": 2,
  "author": "Igor_K",
  "text": "new text",
  "created": "2019-08-24T14:15:22Z",
  "post": 1
}
```

GET-запрос на получение списка доступных сообществ.
```
api/v1/groups/
```
Response:
```json
[
  {
    "id": 0,
    "title": "string",
    "slug": "^-$",
    "description": "string"
  }
]
```

GET-запрос на получение подписок пользователя, сделавшего запрос
```
api/v1/follow/  
```
Response:
```json
[
  {
    "user": "Igor_K",
    "following": "some user"
  }
]
```

POST-запрос на подписку пользователя, сделавшего запрос
```
api/v1/follow/ 
```
Request:
```json
{
  "following": "new user"
}
```
Response:
```json
{
  "user": "Igor_K",
  "following": "new user"
}
```