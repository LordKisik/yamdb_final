![yamdb_final status](https://github.com/LordKisik/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg?branch=master&event=push)

<h1 align="center">yamdb_final</h1>

## Описание проекта
Проект YaMDb собирает отзывы пользователей на произведения. Сами произведения в YaMDb не хранятся, здесь нельзя посмотреть фильм или послушать музыку.<br/>
Произведения делятся на категории, такие как «Книги», «Фильмы», «Музыка». Например, в категории «Книги» могут быть произведения «Винни-Пух и все-все-все» и «Марсианские хроники», а в категории «Музыка» — песня «Давеча» группы «Жуки» и вторая сюита Баха. Список категорий может быть расширен (например, можно добавить категорию «Изобразительное искусство» или «Ювелирка»).<br/>
Благодарные или возмущённые пользователи оставляют к произведениям текстовые отзывы и ставят произведению оценку в диапазоне от одного до десяти (целое число); из пользовательских оценок формируется усреднённая оценка произведения — рейтинг (целое число). На одно произведение пользователь может оставить только один отзыв.<br/>

## Используемые технологии:<br/>
- Django - 2.2.16
- Django Rest Framework - 3.12.4
- Python 3.7
- Docker
- Gunicorn
- Nginx
## Как запустить проект:
1. Клонировать репозиторий и перейти в него в командной строке:
```
git clone git@github.com:LuckyPoRus/infra_sp2.git
```
2. Переход в директорию с проектом:
```
cd api_yamdb
```
3. Cоздать и активировать виртуальное окружение:
```
python -m venv venv
```
4. Активировать виртуальное окружение:
```
source venv/scripts/activate
```
5. Оновление PIP:
```
python -m pip install --upgrade pip
```
6. Установка зависимостей используемых в проекте:
```
pip install -r requirements.txt
```
7. Переходим в папку с файлом docker-compose.yaml:
```
cd infra
```
8. Поднимаем контейнеры (infra_db_1, infra_web_1, infra_nginx_1):
```
docker-compose up -d --build
```
9. Выполняем миграции:
```
docker-compose exec web python manage.py makemigrations
```
```
docker-compose exec web python manage.py migrate
```
10. Создаем суперпользователя:
```
docker-compose exec web python manage.py createsuperuser
```
11. Собираем статику:
```
docker-compose exec web python manage.py collectstatic --no-input
```
12. Создаем дамп базы данных:
```
docker-compose exec web python manage.py dumpdata > dumpPostrgeSQL.json
```
13. Останавливаем контейнеры:
```
docker-compose down -v
```

## Регистрация нового пользователя
- POST
```
http://127.0.0.1:8000/api/v1/auth/signup/
{
  "email": "user@example.com",
  "username": "string"
}
```
## Примеры запросов:
**Получение JWT-токена:**
- POST
```
http://127.0.0.1:8000/api/v1/auth/create/
```
**Получить список всех публикаций:**
- GET
```
http://127.0.0.1:8000/api/v1/posts/
{
  "username": "string",
  "confirmation_code": "string"
}
```
**Добавление нового произведения(администратор):**
- POST
```
http://127.0.0.1:8000/api/v1/titles/
{
  "name": "string",
  "year": 0,
  "description": "string",
  "genre": [
    "string"
  ],
  "category": "string"
}
```
**Получение списка всех отзывов:**
- GET
```
http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/
```
**Получение всех комментариев к отзыву:**
- GET
```
http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/{review_id}/comments/
```
**Подробная документация к проекту доступная по адресу:**
```
http://127.0.0.1:8000/redoc/
```
**Автор проекта:**<br/>

**Виталий** - https://github.com/LordKisik<br/>
