## 🎵 pyBotiCkMuSbot

**pyBotiCkMuSbot** — это Telegram-бот для поиска музыки на Bandcamp. Просто отправьте боту название песни или исполнителя, и он найдет для вас трек и отправит ссылку. Быстро, просто и удобно!

---

## 🚀 Особенности

- **Поиск музыки**: Бот ищет треки на Bandcamp по запросу пользователя.
- **Простота использования**: Просто отправьте боту название песни или исполнителя.
- **Быстрый ответ**: Бот моментально возвращает ссылку на первый найденный трек.

---

## 🎯 Как использовать

1. Найдите бота в Telegram по его имени: **pyBotiCkMuSbot**.
2. Отправьте команду `/start`, чтобы начать.
3. Введите название песни или исполнителя, например: **Radiohead**.
4. Бот найдет трек и отправит вам ссылку.

---

## 📂 Структура проекта

```
pyBotiCkMuSbot/
├── bot.py              # Основной код бота
├── requirements.txt    # Список зависимостей
├── README.md           # Документация
└── .env                # Файл для хранения токена (не включен в репозиторий)
```

---

## 📝 Зависимости

Для работы бота необходимы следующие библиотеки:

- **aiogram** — для работы с Telegram API.
- **aiohttp** — для отправки HTTP-запросов.
- **beautifulsoup4** — для парсинга HTML.

Установите зависимости с помощью команды:

```bash
pip install -r requirements.txt
```

---

## 🛠️ Установка и запуск

1. **Клонируйте репозиторий**:
   ```bash
   git clone https://github.com/ваш-username/pyBotiCkMuSbot.git
   cd pyBotiCkMuSbot
   ```

2. **Установите зависимости**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Создайте файл `.env`**:
   Создайте файл `.env` в корневой директории проекта и добавьте туда токен вашего бота:
   ```
   BOT_TOKEN=ваш_токен
   ```

4. **Запустите бота**:
   ```bash
   python bot.py
   ```

---

## 🙏 Благодарности

- **Bandcamp** — за возможность искать музыку.
- **Aiogram** — за удобную библиотеку для работы с Telegram API.

---

## 📄 Лицензия

Этот проект распространяется под лицензией MIT. Подробнее см. в файле [LICENSE](LICENSE).

