# Панель администратора интернет-магазина

## Запуск в production mode

Для запуска приложения потребуется docker engine

```
git clone https://github.com/vkhvorostov/django-testshop.git
cd django-testshop
docker compose up -d
docker compose run testshop python manage.py migrate
docker compose run testshop python manage.py createsuperuser
docker compose run testshop python manage.py collectstatic
```

Приложение будет доступно на порту 8000, куда следует перенаправлять запросы от веб-сервера. Также нужно настроить, чтобы файлы из папок static и media веб-сервер отдавал напрямую. Пример конфига для nginx:

```
server {
    listen 80;
    listen [::]:80;
    #server_name example.org;
    access_log  /var/log/nginx/example.log;

    location ~ ^/(static|media)/ {
        root /var/www/django-testshop;
        try_files $uri $uri/ =404;
    }

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}
```

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
