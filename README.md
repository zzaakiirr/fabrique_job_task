# Задача
Cпроектировать и разработать API для системы опросов пользователей.

## Функционал для администратора системы:

- авторизация в системе (регистрация не нужна)
- добавление/изменение/удаление опросов. Атрибуты опроса: название, дата старта, дата окончания, описание. После создания поле "дата старта" у опроса менять нельзя
- добавление/изменение/удаление вопросов в опросе. Атрибуты вопросов: текст вопроса, тип вопроса (ответ текстом, ответ с выбором одного варианта, ответ с выбором нескольких вариантов)

## Функционал для пользователей системы:

- получение списка активных опросов
- прохождение опроса: опросы можно проходить анонимно, в качестве идентификатора пользователя в API передаётся числовой ID, по которому сохраняются ответы пользователя на вопросы; один пользователь может участвовать в любом количестве опросов
- получение пройденных пользователем опросов с детализацией по ответам (что выбрано) по ID уникальному пользователя

# Как развернуть локально
- Создаем virtual environment
```
virtualenv -p /usr/bin/python3 venv

```
- Активируем virtual environment
```
source venv/bin/activate
```
- Устанавливаем необходимые пакеты:
```
install -r requirements.txt
```
- Запускаем сервер
```
python manage.py runserver
```

## Дополнительно
- Создаем superuser'а
```
python manage createsuperuser
```

# Документация по API

## Дополнительно
- _/admin/_ - Панель администратора

## Опрос - `/poll`
### GET запросы
- Поддерживается стандратный CRUD
- `/poll/` - Список опросов
- `/poll/?user_identificator=<user_identificator>/` - Все опросы, пройденные пользователем, identifier которого равен <user_identificator>
- `/poll/<poll_pk>/` - Конкретный опрос, <poll_pk> - id опроса
- `/poll/<poll_pk>/answers/?user_identificator=<user_identificator>/` - Ответы на опрос с id <poll_pk> пользователя с идентификатором <user_identificator>
- `/poll/verbose/?user_identifier=<user_identifier>/` - Опросы c ответами, которые прошел пользователь с идентификатором <user_identifier> 
### POST запросы
- `/poll/` - необходимо указать: `start_date`, `end_date`, `desc` (опционально)

## Вопрос - `/question`
- Поддерживается стандарный CRUD
- `/question/?poll=<poll_pk>/` - Список всех вопросов, относящихся к Опросу с id равной <poll_pk>

## Ответ - `/answer`
- Поддерживается стандарный CRUD
- `/answer/?question=<question_pk>/` - Ответы на вопрос, чей id равен <question_pk> 
- `/answer/?user_identifier=<user_identifier>/` - Ответы пользователя с идентификатором, равным <user_identifier>

