## Задачи:
1. Добавить логирование
2. Удаление связанных строк
3. Подробные маршруты
4. Обновление данных
5. Авторизация через Яндекс и Гугл
6. Привести в порядок маршруты
7. Для продакшена, убрать удаление таблиц и автообновление
8. Запись в папку часов с разных сторон main left right bottom
9. Добавить alembic
10. Реализовать обработку ошибок


### Linux

```bash

docker-compose -f docker-compose.yml up -d

python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt

python3 main.py (запуск файла main.py )
```

### Windows

```bash
docker-compose -f docker-compose.yml up -d

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

python main.py (запуск файла main.py )

```

### Миграции

```bash
alembic revision --autogenerate -m "Initial revision"

```

# Часы

## `watch` часы

| Поле                | Тип             | Описание                  |
| ------------------- | --------------- | ------------------------- |
| id                  | INT PK          | ID часов                  |
| folder              | STR UNIQUE      | название папки            |
| code                | STR None UNIQUE | номер оформления          |
| integrated_bracelet | BOOL            | Есть ли браслет           |
| start_release       | INT             | Начало производства       |
| end_release         | INT             | Конец производства        |
| gender_id           | INT             | FK на `gender(id)`        |
| case_material_id    | INT             | FK на `case_material(id)` |
| mechanism_id        | INT             | FK на `mechanism(id)`     |
| factory_id          | INT             | FK на `factory(id)`       |
| brand_id            | INT             | FK на `brand(id)`         |
| user_id             | INT             | FK на `user(id)`          |
| created_at          | DATE            | дата создание             |
| update_at           | DATE            | дата обновления           |

---

## `factory` часовой завод

| Поле | Тип        | Описание        |
| ---- | ---------- | --------------- |
| id   | INT PK     | ID завода       |
| name | STR UNIQUE | Название завода |

---

## `alias` ключевые слова часов

| Поле     | Тип    | Описание          |
| -------- | ------ | ----------------- |
| id       | INT PK | ID                |
| watch_id | STR    | FK на `watch(id)` |
| key      | STR    | Ключ              |

---

## `brand` брэнд часов

| Поле | Тип        | Описание        |
| ---- | ---------- | --------------- |
| id   | INT PK     | ID              |
| name | STR UNIQUE | название брэнда |

---

## `case_material` материал корпуса часов

| Поле | Тип        | Описание |
| ---- | ---------- | -------- |
| id   | INT PK     | ID       |
| name | STR UNIQUE | материал |

---

## `gender` тип часов

| Поле | Тип        | Описание |
| ---- | ---------- | -------- |
| id   | INT PK     | ID       |
| name | STR UNIQUE | пол      |

# Механизмы

## `mechanism` механизмы

| Поле              | Тип    | Описание                   |
| ----------------- | ------ | -------------------------- |
| id                | INT PK | ID механизма               |
| stones            | STR    | кол. камней                |
| start_release     | INT    | Начало производства        |
| end_release       | INT    | Конец производства         |
| mechanism_type_id | INT    | FK на `mechanism_type(id)` |
| factory_id        | INT    | FK на `factory(id)`        |
| user_id           | INT    | FK на `user(id)`           |
| created_at        | DATE   | дата создание              |
| update_at         | DATE   | дата обновления            |

---

## `function` функции механизма

| Поле | Тип        | Описание          |
| ---- | ---------- | ----------------- |
| id   | INT PK     | ID                |
| name | STR UNIQUE | Функции механизма |

---

## `mechanism_function` соединение механизмов и функций

| Поле         | Тип    | Описание              |
| ------------ | ------ | --------------------- |
| id           | INT PK | ID                    |
| mechanism_id | INT    | FK на `mechanism(id)` |
| function_id  | INT    | FK на `function(id)`  |

---

## `mechanism_type` тип механизма

| Поле | Тип        | Описание      |
| ---- | ---------- | ------------- |
| id   | INT PK     | ID            |
| name | STR UNIQUE | Тип механизма |

---

# Пользователь

## `user` часы

| Поле       | Тип        | Описание         |
| ---------- | ---------- | ---------------- |
| id         | INT PK     | ID               |
| login      | STR UNIQUE | логин            |
| password   | STR        | пароль           |
| email      | STR UNIQUE | почта            |
| role_id    | STR        | FK на `role(id)` |
| avito_url  | STR        | ссылка на авито  |
| meshok_url | STR        | ссылка на мешок  |
| rating     | INT        | рэйтинг          |
| created_at | DATE       | дата создание    |
| update_at  | DATE       | дата обновления  |

---

## `role` виды ролей

| Поле | Тип        | Описание |
| ---- | ---------- | -------- |
| id   | INT PK     | ID       |
| name | STR UNIQUE | Роль     |

---

## `collection` коллекции пользователей

| Поле     | Тип    | Описание          |
| -------- | ------ | ----------------- |
| id       | INT PK | ID                |
| user_id  | INT    | FK на `user(id)`  |
| watch_id | INT    | FK на `watch(id)` |

---

# Черновик с часами

## `draft_watch` часы

| Поле                | Тип        | Описание                  |
| ------------------- | ---------- | ------------------------- |
| id                  | INT PK     | ID часов                  |
| message             | STR        | сообщение от админа       |
| folder              | STR UNIQUE | название папки            |
| code                | STR None   | номер оформления          |
| integrated_bracelet | BOOL       | Есть ли браслет           |
| start_release       | INT        | Начало производства       |
| end_release         | INT        | Конец производства        |
| gender_id           | INT        | FK на `gender(id)`        |
| case_material_id    | INT        | FK на `case_material(id)` |
| mechanism_id        | INT        | FK на `mechanism(id)`     |
| factory_id          | INT        | FK на `factory(id)`       |
| brand_id            | INT        | FK на `brand(id)`         |
| user_id             | INT        | FK на `user(id)`          |
| created_at          | DATE       | дата создание             |
| update_at           | DATE       | дата обновления           |

---

## `draft_alias` ключевые слова часов

| Поле     | Тип    | Описание          |
| -------- | ------ | ----------------- |
| id       | INT PK | ID                |
| watch_id | STR    | FK на `watch(id)` |
| key      | STR    | Ключ              |

---

## `draft_mechanism` механизмы

| Поле              | Тип    | Описание                   |
| ----------------- | ------ | -------------------------- |
| id                | INT PK | ID механизма               |
| message           | STR    | сообщение от админа        |
| stones            | STR    | кол. камней                |
| start_release     | INT    | Начало производства        |
| end_release       | INT    | Конец производства         |
| mechanism_type_id | INT    | FK на `mechanism_type(id)` |
| user_id           | INT    | FK на `user(id)`           |
| created_at        | DATE   | дата создание              |
| update_at         | DATE   | дата обновления            |

---

## `draft_mechanism_function` соединение механизмов и функций

| Поле         | Тип    | Описание              |
| ------------ | ------ | --------------------- |
| id           | INT PK | ID                    |
| mechanism_id | INT    | FK на `mechanism(id)` |
| function_id  | INT    | FK на `function(id)`  |

---
