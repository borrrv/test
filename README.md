# Тесты IQ и EQ
## Запуск проекта
- Клонировать репозиторий к себе на компьютер
```
git clone https://github.com/borrrv/test.git
```
- Установить зависимости (из папки test)
```
poetry shell
poetry install
```
- Запуск проекта
```
python manage.py runserver
```
## Запросы*
*- относительно http://127.0.0.1:8000/
- (POST) Создание тестов
```
api/create_tests/
```
- (POST) Сохранить результаты теста IQ

обязательно поле: iq_score
```
api/result_test_iq
```
- (POST) Сохранить результаты теста EQ

обязательно поле: eq_letters
```
api/result_test_eq
```
- (GET) Результаты тестов по логину

обязательное поле: login
```
api/results/
```
