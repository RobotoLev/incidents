# Система "Инцидент"

Использовал фреймворк Django.

Запуск: установить Python 3.8, создать virtualenv, установить Django, django-access и django-allauth, запустить python manage.py runserver.

Сервер будет доступен на 127.0.0.1:8000

Входить на главной странице. Доступы:
- admin/admin - суперадмин, всемогущий разработчик
- test/test7890 - администратор
- test2/test7890 - Пользователь РСО
- test3/test7890 - Диспетчер 
- test4/test7890 - Наблюдатель

Права уменьшаются с удалением от суперадмина. У наблюдателя доступ только к статистике по адресу /stat.

Чтобы определить пользователю роль, он должен принадлежать к соответствующей группе и иметь соответствующую пометку в "Профиле".
