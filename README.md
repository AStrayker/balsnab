# Telegram Channel Bot

Этот бот для Telegram пересылает сообщения пользователей в указанный канал.

## Установка и запуск

1. Клонируйте репозиторий:

    ```sh
    git clone https://github.com/ВАШ_ЛОГИН/telegram-channel-bot.git
    ```

2. Перейдите в директорию проекта:

    ```sh
    cd telegram-channel-bot
    ```

3. Установите необходимые зависимости:

    ```sh
    pip install -r requirements.txt
    ```

4. Создайте файл `.env` и добавьте туда ваши токены:

    ```env
    API_TOKEN=ваш_токен_бота
    CHANNEL_ID=@название_вашего_канала
    ```

5. Запустите бота:

    ```sh
    python telegram_bot.py
    ```

## Лицензия

Этот проект лицензируется на условиях MIT License.
