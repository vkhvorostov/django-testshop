# Панель администратора интернет-магазина

## Запуск 

Для запуска приложения потребуется docker engine

```
git clone https://github.com/vkhvorostov/django-testshop.git
cd django-testshop
docker compose up -d
docker compose run testshop python manage.py migrate
docker compose run testshop python manage.py createsuperuser
```

После успешного выполнения вышенаписанных команд можно переходить в браузере по адресу http://127.0.0.1:8000/admin/

## Запуск для разработки

Склонируйте себе репозитарий и откройте его в VSCode с использованием devcontainer. В терминале контейнера выполните команду
```
python manage.py runserver 0.0.0.0:8000
```
Приложение будет доступно в браузере по адресу http://127.0.0.1:8000/admin/

При необходимости нужно выполнить также команды
```
python manage.py migrate
python manage.py createsuperuser
```
