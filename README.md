# 📝 Task Manager — Django приложение для управления задачами

Простое, но функциональное веб-приложение для создания, редактирования, удаления и просмотра задач с поддержкой авторизации, фильтрации и красивым интерфейсом на Bootstrap.

---

## 🚀 Стек технологий

- **Backend:** [Python 3.x](https://www.python.org/), [Django 5.x](https://www.djangoproject.com/)
- **База данных:** [PostgreSQL](https://www.postgresql.org/)
- **Frontend:** [Bootstrap 5](https://getbootstrap.com/), [crispy-bootstrap5](https://github.com/django-crispy-forms/crispy-bootstrap5)
- **Аутентификация:** стандартная система пользователей Django
- **Прочее:**
  - Django Messages Framework
  - Django Class-Based Views (CBV)
  - Миксины для проверки прав доступа
  - Django Signals для логики при изменении данных

---

## ✨ Реализованный функционал

- **Регистрация и авторизация пользователей**
  - Форма регистрации без лишних подсказок, только поля + ошибки валидации
  - Логин/логаут
  - Доступ к задачам только для авторизованных пользователей

- **Управление задачами**
  - Создание, просмотр, редактирование и удаление задач
  - Поля: заголовок, описание, приоритет, дата выполнения, статус
  - Фильтрация задач по пользователю
  - Защита: нельзя просматривать или редактировать чужие задачи (OwnerRequiredMixin)

- **UI и UX**
  - Полностью стилизовано с использованием Bootstrap 5
  - Адаптивный дизайн (mobile-friendly)
  - Пагинация списка задач
  - Красивое отображение сообщений об ошибках и успехах
  - Применение [django-crispy-forms](https://django-crispy-forms.readthedocs.io/) для аккуратных форм

- **Технические фишки**
  - Использование Class-Based Views (ListView, DetailView, CreateView, UpdateView, DeleteView)
  - Собственные миксины (`OwnerRequiredMixin`)
  - Сигналы Django для дополнительной логики
  - Разделение шаблонов (tasks, registration)
  - Настройка работы с PostgreSQL

---

## 📦 Установка и запуск

1. **Клонировать репозиторий**
   ```bash
   git clone https://github.com/username/task-manager.git
   cd task-manager

2. Создать и активировать виртуальное окружение
    python -m venv venv
    source venv/bin/activate   # для Linux/MacOS
    venv\Scripts\activate      # для Windows

3. Установить зависимости
    pip install -r requirements.txt

4. Настроить базу данных PostgreSQL
   - Создайте базу данных и пользователя в PostgreSQL (например, task_db, пользователь postgres, пароль 1231)
   - Проверьте настройки в `config/settings.py`:
     ```python
     DATABASES = {
         "default": {
             "ENGINE": "django.db.backends.postgresql",
             "NAME": "task_db",
             "USER": "postgres",
             "PASSWORD": "1231",
             "HOST": "localhost",
             "PORT": 5432,
         }
     }
     ```
   - При необходимости измените параметры под себя.

5. **Выполнить миграции**
   ```bash
   python manage.py migrate
   ```

6. **Создать суперпользователя (админ-панель)**
   ```bash
   python manage.py createsuperuser
   ```

7. **Запустить сервер**
   ```bash
   python manage.py runserver
   ```

8. Перейти на [http://127.0.0.1:8000/](http://127.0.0.1:8000/) и зарегистрировать нового пользователя или войти как админ.

---

## 📁 Структура проекта

```
task_manager/
├── config/                  # Конфигурация Django-проекта
│   ├── __init__.py
│   ├── asgi.py              # ASGI-стартер
│   ├── settings.py          # Основные настройки проекта
│   ├── urls.py              # Главные URL-ы проекта
│   └── wsgi.py              # WSGI-стартер
│
├── tasks/                   # Приложение задач
│   ├── __init__.py
│   ├── admin.py             # Админка для задач
│   ├── apps.py              # Конфиг приложения
│   ├── forms.py             # Django-формы для задач
│   ├── migrations/          # Миграции БД для задач
│   │   ├── __init__.py
│   │   └── 0001_initial.py
│   ├── mixins.py            # Миксины (например, OwnerRequiredMixin)
│   ├── models.py            # Модель Task
│   ├── signals.py           # Сигналы для задач
│   ├── templates/
│   │   └── tasks/           # Шаблоны для задач
│   │       ├── task_confirm_delete.html
│   │       ├── task_detail.html
│   │       ├── task_form.html
│   │       └── task_list.html
│   ├── tests.py             # Тесты для задач
│   ├── urls.py              # URL-ы приложения задач
│   └── views.py             # View-классы для задач
│
├── users/                   # Приложение пользователей
│   ├── __init__.py
│   ├── admin.py             # Админка для пользователей
│   ├── apps.py              # Конфиг приложения
│   ├── forms.py             # Формы регистрации/логина
│   ├── migrations/          # Миграции БД для пользователей
│   │   ├── __init__.py
│   │   └── 0001_initial.py
│   ├── models.py            # Кастомная модель пользователя
│   ├── tests.py             # Тесты для пользователей
│   ├── urls.py              # URL-ы приложения пользователей
│   └── views.py             # View-классы для пользователей
│
├── templates/               # Глобальные шаблоны
│   ├── base.html            # Базовый шаблон
│   └── registration/        # Шаблоны аутентификации
│       ├── login.html
│       └── signup.html
│
├── manage.py                # Управляющий скрипт Django
├── requirements.txt         # Зависимости проекта
└── README.md                # Документация
```

**Кратко по основным элементам:**
- `config/` — настройки, точки входа, маршрутизация всего проекта.
- `tasks/` — бизнес-логика задач, модели, формы, шаблоны, миграции, сигналы, тесты.
- `users/` — кастомная модель пользователя, формы, миграции, тесты, view для регистрации.
- `templates/` — базовые и auth-шаблоны, наследование от base.html.
- `requirements.txt` — список всех зависимостей (Django, crispy-forms, psycopg2 и др).
- `manage.py` — точка входа для команд Django.

---

## 🗂️ Структура моделей

- **Пользователь** (`users.models.CustomUser`)
  - username, email (уникальный), пароль и стандартные поля Django
- **Задача** (`tasks.models.Task`)
  - title (заголовок)
  - description (описание)
  - completed (статус выполнения)
  - priority (приоритет: низкий, средний, высокий)
  - due_date (дата выполнения)
  - owner (владелец — ForeignKey на пользователя)
  - created_at, updated_at (даты создания/обновления)

---

## 🛠️ Примечания
- Для отправки email используется консольный backend (настройка в `settings.py`).
- Все формы стилизованы с помощью crispy-bootstrap5.
- Для защиты доступа к задачам используется миксин `OwnerRequiredMixin`.
- Сигналы Django используются для отправки уведомлений при создании задач.
- Проект легко расширяется под свои нужды.
