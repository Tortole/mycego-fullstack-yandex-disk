# Яндеск Диск интерфейс

Содержание:

-   [Яндеск Диск интерфейс](#яндеск-диск-интерфейс)
    -   [О проекте](#о-проекте)
    -   [Установка](#установка)
        -   [Установка через Python и pip](#установка-через-python-и-pip)
        -   [Установка через Poetry](#установка-через-poetry)
    -   [Использование](#использование)
    -   [Возможности проекта](#возможности-проекта)

## О проекте

Проект для просмотра и скачивания файлов с Яндекс Диска по публичной ссылке.

Сделан по тестовому заданию на позицию full-stack разработчика компании MYCEGO.<br>
[Полный текст задания - task_text.md](task_text.md)

## Установка

### Установка через Python и pip

1. Клонировать проект с GitHub

```bash
git clone https://github.com/Tortole/mycego-fullstack-yandex-disk.git
```

2. Перейти в папку с проектом

```bash
cd mycego-fullstack-yandex-disk
```

3. Установить виртуальное окружение Python

```bash
python venv .venv
```

4. Активировать виртуальное окружение

    - Windows

    ```bash
    .\.venv\Scripts\activate
    ```

    - GNU/Linux

    ```bash
    source venv/bin/activate
    ```

5. Установить библиотеки

```bash
pip install -r requirements.txt
```

6. Разместить в `yandex_disk/.env` настройки проекта по примеру из `yandex_disk/example.env`

    - пример для запуска проекта на SQLite3 без необходимости дополнительных программ

    ```bash
    # Django secret key
    SECRET_KEY="tazse*@ik!qfbhyf1zh673^g&*ea=oe4zs^r147d)t=#9r="

    # If TRUE activate Django debug mod
    DEBUG=TRUE

    # Database parapets in django-environment library formate, for SQLite3
    DATABASE_URL=sqlite:///db.sqlite3
    ```

7. Запустить миграцию Django

```bash
python manage.py makemigrations
python manage.py migrate
```

8. Запустить локальный Django сервер

```bash
python manage.py runserver
```

### Установка через Poetry

1. Установить poetry в основное пространство, если отсутствует

```bash
pip install poetry
```

2. При необходимости, настроить poetry на размещение виртуального окружения в папке с проектом:

```bash
poetry config virtualenvs.in-project true
```

3. Клонировать проект с GitHub

```bash
git clone https://github.com/Tortole/mycego-fullstack-yandex-disk.git
```

4. Перейти в папку с проектом

```bash
cd mycego-fullstack-yandex-disk
```

5. Установить виртуальное окружение Python

```bash
poetry install
```

&ensp; &ensp; &ensp; &ensp; или, если нужны только библиотеки для запуска:

```bash
poetry install --only main
```

6. Разместить в `yandex_disk/.env` настройки проекта по примеру из `yandex_disk/example.env`

    - пример для запуска проекта на SQLite3 без необходимости дополнительных программ

    ```bash
    # Django secret key
    SECRET_KEY="tazse*@ik!qfbhyf1zh673^g&*ea=oe4zs^r147d)t=#9r="

    # If TRUE activate Django debug mod
    DEBUG=TRUE

    # Database parapets in django-environment library formate, for SQLite3
    DATABASE_URL=sqlite:///db.sqlite3
    ```

7. Запустить миграцию Django

```bash
poetry run full_migrate
```

8. Запустить локальный сервер Django с проектом

```bash
poetry run m runserver
```

## Использование

1. Открыть браузер и вбить в адресную строку адрес локального сервера: [127.0.0.1:8000](http://127.0.0.1:8000/)
2. Зарегистрироваться по ссылке ниже
3. Войти по логину и паролю
4. Ввести в поле публичную ссылку на папку на Яндекс Диске и нажать на кнопку "Получить файлы"
5. Нажимать на кнопочки (по желанию)

## Возможности проекта

1. Просмотр файлов по публичной ссылке
2. Фильтрация файлов по типу
3. Скачивание файлов
4. Скачивание нескольких файлов
5. Скачивание всей папки
6. Переход по подпапкам
