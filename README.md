# Drinks Catalog

Простой каталог напитков с отзывами на Django.  
Развёртывание через Docker + Docker Compose + PostgreSQL + Nginx.

---

## Структура проекта

drinks_site/
├─ catalog/
├─ drinks_site/
├─ nginx/
│ └─ default.conf
├─ Dockerfile
├─ docker-compose.yml
├─ requirements.txt
└─ .env

yaml
Копировать код

---

## Настройки

Создайте `.env` в корне проекта:

```dotenv
# Django
DJANGO_SECRET_KEY=supersecretkey
DJANGO_DEBUG=0
DJANGO_ALLOWED_HOSTS=example.com,www.example.com

# PostgreSQL
POSTGRES_DB=drinks
POSTGRES_USER=drinks_user
POSTGRES_PASSWORD=drinks_pass
POSTGRES_HOST=db
POSTGRES_PORT=5432
В settings.py:

python
Копировать код
STATIC_URL = "/static/"
MEDIA_URL = "/media/"
STATIC_ROOT = BASE_DIR / "staticfiles"
MEDIA_ROOT = BASE_DIR / "media"
ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS", "").split(",")
Сборка и запуск
Собрать образы и поднять сервисы:

bash
Копировать код
docker-compose up --build -d
Собрать статику:

bash
Копировать код
docker-compose exec web python manage.py collectstatic --noinput
Создать суперпользователя:

bash
Копировать код
docker-compose exec web python manage.py createsuperuser
Теперь сайт доступен на порту 80 (или на твоём домене, если настроен DNS).

Docker Compose
Сервисы:

db — PostgreSQL

web — Django + Gunicorn

nginx — отдаёт статику/медиа, проксирует на Gunicorn

Управление
Логи веб-сервиса:

bash
Копировать код
docker-compose logs -f web
Остановить сервисы:

bash
Копировать код
docker-compose down
Выполнить миграции вручную:

bash
Копировать код
docker-compose exec web python manage.py migrate
Админка
После создания суперпользователя админка доступна по /admin/.