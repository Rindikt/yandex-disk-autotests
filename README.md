# Автотесты для API Яндекс.Диска

Проект содержит набор автоматизированных тестов для проверки базовых операций с ресурсами Яндекс.Диска (создание, получение информации, копирование и удаление).

## Технологии
* **Python 3.10+**
* **Pytest** (тестовый фреймворк)
* **Requests** (HTTP-клиент)
* **Python-dotenv** (работа с переменными окружения)

## Архитектура
Проект построен с соблюдением принципа **SRP (Single Responsibility Principle)**:
* `api/disk_client.py` — низкоуровневая логика запросов к API.
* `tests/conftest.py` — конфигурация тестов и управление состоянием через фикстуры.
* `tests/test_disk.py` — атомарные тест-кейсы.

## Запуск проекта локально

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/Rindikt/yandex-disk-autotests.git
   ```
2. Создайте и активируйте виртуальное окружение:
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # Для Linux/macOS
    .venv\Scripts\activate     # Для Windows
    ```

3. Установите зависимости:
    ```bash
   pip install -r requirements.txt
   ```

4. Настройте авторизацию:
* Создайте файл .env в корне проекта.
* Скопируйте содержимое из .env.example и вставьте свой OAuth-токен в переменную YANDEX_TOKEN.

5. Запустите тесты:
    ```bash
   pytest -v
   ```
