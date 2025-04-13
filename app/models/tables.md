# Часы


## `watch` часы

| Поле | Тип | Описание |
|------|-----|----------|
| id | INT PK | ID часов 
| folder | STR UNIQUE | Название папки
| integrated_bracelet | BOOL | Есть ли браслет  
| date_creat | DATE | дата создание            
| gender_id | INT | FK на `gender(id)` 
| case_material_id | INT | FK на `case_material(id)` 
| mechanism_id | INT | FK на `mechanism(id)`              
| factory_id | INT | FK на `factory(id)`              
| brand_id | INT | FK на `brand(id)`              
| user_id | INT | FK на `user(id)`              

---

## `factory` часовой завод

| Поле | Тип | Описание |
|------|-----|----------|
| id | INT PK | ID завода 
| name | STR UNIQUE | Название завода
| city | STR | Город завода

---

## `alias` ключевые слова часов

| Поле | Тип | Описание |
|------|-----|----------|
| id | INT PK | ID  
| watch_id | STR | FK на `watch(id)
| key | STR | Ключ

---

## `brand` брэнд часов

| Поле | Тип | Описание |
|------|-----|----------|
| id | INT PK | ID  
| name | STR UNIQUE | название брэнда

---

## `case_material` материал корпуса часов

| Поле | Тип | Описание |
|------|-----|----------|
| id | INT PK | ID  
| name | STR UNIQUE | материал

---

## `gender` тип часов

| Поле | Тип | Описание |
|------|-----|----------|
| id | INT PK | ID  
| name | STR UNIQUE | пол


# Механизмы 


## `mechanism` механизмы

| Поле | Тип | Описание |
|------|-----|----------|
| id | INT PK | ID механизма 
| stone | STR | кол. камней
| mechanism_type_id | INT | FK на `mechanism_type(id)           
| user_id | INT | FK на `user(id)` 
| date_creat | DATE | дата создание

---

## `function` функции механизма

| Поле | Тип | Описание |
|------|-----|----------|
| id | INT PK | ID 
| name | STR UNIQUE | Функции механизма

---

## `mechanism_function` соединение механизмов и функций

| Поле | Тип | Описание |
|------|-----|----------|
| id | INT PK | ID 
| mechanism_id | INT | FK на `mechanism(id)` 
| function_id | INT | FK на `function(id)` 

---

## `mechanism_type` тип механизма

| Поле | Тип | Описание |
|------|-----|----------|
| id | INT PK | ID 
| name | STR UNIQUE | Тип механизма 

---


# Пользователь 


## `user` часы

| Поле | Тип | Описание |
|------|-----|----------|
| id | INT PK | ID 
| login | STR | логин
| password | STR | пароль         
| email | STR UNIQUE | почта
| date_creat | DATE | дата создание
| role_id | STR | FK на `role(id)` 

---

## `role` виды ролей

| Поле | Тип | Описание |
|------|-----|----------|
| id | INT PK | ID 
| name | STR UNIQUE | Роль

---

## `collection` коллекции пользователей

| Поле | Тип | Описание |
|------|-----|----------|
| id | INT PK | ID 
| user_id | STR | FK на `user(id)` 
| watch_id | STR | FK на `watch(id)           
