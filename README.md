# api_final_yatube

### Описание проекта:
Финальная часть учебного проекта социальной сети с постами, комментариями, возможностью подписаться на авторов 

### Технологии:
Python 3.9, Django 3.2.16, djangorestframework 3.12.4, JWT, pytest 6.2.4

### Как запустить проект:
Клонируй репозиторий и перейди в него в командной строке:

`git clone https://github.com/Tumanova-Alina/api_final_yatube.git`

 `cd api_final_yatube`

Cоздай виртуальное окружение:

Если у тебя Linux/macOs:

`python3 -m venv venv`

Если у тебя Windows:

`python -m venv venv`


Активируй окружение:

Если у тебя Linux/macOS:

`source venv/bin/activate`

Если у тебя windows:

`source venv/Scripts/activate`


Установи и обнови пакетный менеджер:

`python3 -m pip install --upgrade pip`


Установи зависимости из файла requirements.txt:

`pip install -r requirements.txt`


Выполни миграции:

`python3 manage.py migrate`


Запусти проект:

`python3 manage.py runserver`


### Примеры запросов:


POST-запрос с токеном, добавление новой публикации в базу.

`POST http://localhost:port/api/v1/posts/`

```
{
  "text": "Панграмма — это фраза, содержащая в себе все буквы алфавита. Обычно её используют для презентации шрифтов, чтобы можно было в одной фразе рассмотреть все глифы.",
  "group": 4
}
```

Ответ:

```
{
    "id": 7,
    "author": "string",
    "text": "Панграмма — это фраза, содержащая в себе все буквы алфавита. Обычно её используют для презентации шрифтов, чтобы можно было в одной фразе рассмотреть все глифы.",
    "pub_date": "2019-08-24T14:15:22Z",
    "image": null,
    "group": 4
}
```


GET-запрос, получение информации о комментариях к посту с id=5.

`GET http://localhost:port/api/v1/posts/5/comments/`

Ответ:

```
{
    "id": 5,
    "author": "string",
    "text": "string",
    "created": "2019-08-24T14:15:22Z",
    "post": 5
}
```


GET-запрос, получение информации о подписках пользователя. Возвращает все подписки пользователя, сделавшего запрос.

`GET http://localhost:port/api/v1/follow/`

Ответ:

```
[
    {
        "user": "string",
        "following": "string"
    }
]
```


### Автор:
Туманова Алина
