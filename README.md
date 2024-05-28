# API Yatube

Yatube — это платформа для блогов. Сервис предлагает возможность зарегистрироваться, создать, отредактировать или удалить собственный пост, прокомментировать пост другого автора и подписаться на него.

## Основные зависимости:
* Python = 3.9
* Django = 3.2

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
