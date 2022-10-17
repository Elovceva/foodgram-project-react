## 🍳 Проект Foodgram

**Foodgram** - приложение в котором пользователи могут публиковать рецепты, добавлять чужие рецепты в избранное и подписываться на публикации других авторов. Сервис «Foodgram» позволяет пользователям создавать список продуктов, которые нужно купить для приготовления выбранных блюд.

## ⚙ Используемые технологии:

▪ **Python**<br>
▪ **Django**<br>
▪ **Django Rest Framework**<br>
▪ **Docker**<br>
▪ **Gunicorn**<br>
▪ **NGINX**<br>
▪ **PostgreSQL**<br>
▪ **Yandex Cloud**<br>
▪ **CI/CD**<br>

## 📃 Как развернуть проект на локальной машине:

Клонировать репозиторий:
```
git@github.com:Elovceva/foodgram-project-react.git
```
### Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

#### команда для Linux

. venv/bin/activate
```
source venv/bin/activate
```

#### команда для windows

```
source venv/Scripts/activate
```
#### Обновить пакетный менежер pip

```
python3 -m pip install --upgrade pip
```

### Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

### Выполнить миграции:

```
python3 manage.py migrate
```

### Запустить

```
python3 manage.py runserver
```

## Использование

После запуска сервера вам будет доступна [документация](http://localhost/api/docs/redoc.html)

### Регистрация для пользователей

```
POST /api/users 
```

в body
{
  "email": "vpupkin@yandex.ru",
  "username": "vasya.pupkin",
  "first_name": "Вася",
  "last_name": "Пупкин",
  "password": "Qwerty123"
}

POST /api/auth/token/login/ - получение токена 
```
в body
{
"password": "string",
"email": "string"
}

### Примеры работы с API для пользователей

Для неавторизованных пользователей работа с API доступна в режиме чтения.

```
GET /api/recipes/ - получение списка всех рецептов
GET /api/recipes/{id}/ - получение информации о рецепте по id
GET /api/v1/users/ - получение списка всех пользователей


### Примеры работы с API для авторизованных пользователей

Добавление рецепта:

```
POST /api/recipes/
```

в body
{
  "ingredients": [
    {
      "id": 1123,
      "amount": 10
    }
  ],
  "tags": [
    1,
    2
  ],
  "image": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABAgMAAABieywaAAAACVBMVEUAAAD///9fX1/S0ecCAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAACklEQVQImWNoAAAAggCByxOyYQAAAABJRU5ErkJggg==",
  "name": "string",
  "text": "string",
  "cooking_time": 1
}

Частичное обновление рецепта:

```
PATCH /api/recipes/{id}/
```

в body
{
  "ingredients": [
    {
      "id": 1123,
      "amount": 10
    }
  ],
  "tags": [
    1,
    2
  ],
  "image": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABAgMAAABieywaAAAACVBMVEUAAAD///9fX1/S0ecCAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAACklEQVQImWNoAAAAggCByxOyYQAAAABJRU5ErkJggg==",
  "name": "string",
  "text": "string",
  "cooking_time": 1
}

Удаление рецепта:

```
DELETE /api/recipes/{id}/
```


```
### Остальные примеры работы с сервисом возможно изучить [здесь](http://localhost/api/docs/redoc.html)


## 👾 Автор проекта:

### Елена Еловцева
```
GitHub: github.com/Elovceva
```
