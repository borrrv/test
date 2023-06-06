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

Формат:
```
{
    "iq_score": 11
}
```
```
api/result_test_iq/<str:login>/
```
- (POST) Сохранить результаты теста EQ

обязательно поле: eq_letters

Формат:
```
{
    "eq_letters": "в, а, б, д, г"
}
```
```
api/result_test_eq/<str:login>/
```
- (GET) Результаты тестов по логину

обязательное поле: login

Формат:
```
{
    "login": "UytYoEFudJ"
}
```
```
api/results/
```

### Технологии
- Python 3.10
- Django 3.2
- DRF 3.12
