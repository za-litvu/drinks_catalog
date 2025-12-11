# Drinks Catalog

  

Простой каталог напитков с отзывами на Django.  

Развёртывание через Docker + Docker Compose + PostgreSQL + Nginx.

  

---

## Структура проекта

```

  

drinks_site/

├─ catalog/

├─ drinks_site/

├─ nginx/

│ └─ default.conf

├─ Dockerfile

├─ docker-compose.yml

├─ requirements.txt

└─ .env

```

  
  

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

```

  

Сборка и запуск

Собрать образы и поднять сервисы:
```bash
docker compose up --build -d
```
Собрать статику: 
```bash
docker compose exec web python manage.py collectstatic --noinput
```
Создать суперпользователя:
```bash
docker compose exec web python manage.py createsuperuser
```


Теперь сайт доступен на порту 80 (или на домене, если настроен DNS).
