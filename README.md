Чтобы сделать ваш `README.md` более читабельным и избежать "слипания" текста, нужно правильно отформатировать его с использованием Markdown. Вот исправленная версия:

---

# 🎵 pyBotiCkMuSbot

**pyBotiCkMuSbot** — это Telegram-бот для поиска музыки на Bandcamp и видео на Rutube. Просто отправьте боту название песни, исполнителя или видео, и он найдёт для вас трек или видео и отправит ссылку. Быстро, просто и удобно! Бот также поддерживает историю запросов и удобное меню для навигации.

---

## 🚀 Особенности

- **Поиск музыки**: Бот ищет треки на Bandcamp по запросу пользователя.
- **Поиск видео**: Бот ищет видео на Rutube по запросу пользователя.
- **История запросов**: Сохраняет последние 10 запросов для каждого пользователя.
- **Простота использования**: Удобное меню с кнопками для навигации.
- **Быстрый ответ**: Бот моментально возвращает ссылку на первый найденный результат.
- **Дополнительные функции**:
  - **Искать ещё**: Позволяет просмотреть следующие результаты поиска.
  - **Искать другой запрос**: Сбрасывает текущие результаты и предлагает ввести новый запрос.
  - **Не хочу искать**: Завершает текущий поиск и возвращает в главное меню.
- **Кулдаун в чате**: Ограничение на частоту запросов в рамках одного чата.

---

## 🎯 Как использовать

1. Найдите бота в Telegram по его имени: **pyBotiCkMuSbot**.
2. Отправьте команду `/start`, чтобы начать.
3. Используйте кнопки для навигации:
   - **▶️ Начать**: Выбрать тип поиска.
   - **🎥 Искать видео на Rutube**: Поиск видео.
   - **🎵 Искать музыку на Bandcamp**: Поиск музыки.
   - **📜 История запросов**: Просмотр последних 10 запросов.
   - **🏠 Главное меню**: Вернуться в главное меню.
4. Введите название песни, исполнителя или видео, например: `The Rolling Stones Paint It, Black`.
5. Бот найдёт результат и отправит вам ссылку.
6. Используйте кнопки:
   - **Искать ещё**: Показывает следующий результат.
   - **Искать другой запрос**: Сбрасывает текущие результаты и предлагает ввести новый запрос.
   - **Не хочу искать**: Завершает поиск и возвращает в главное меню.

---

## 📂 Структура проекта

```
pyBotiCkMuSbot/
├── bot.py             # Основной код бота
├── README.md          # Документация
```

---

## 📝 Зависимости

Для работы бота необходимы следующие библиотеки:

- **aiogram** — для работы с Telegram API.
- **aiohttp** — для отправки HTTP-запросов.
- **beautifulsoup4** — для парсинга HTML.

---

## 🛠️ Установка и запуск

### 1. Установите Python
Убедитесь, что у вас установлен Python 3.8 или выше. Если нет, скачайте и установите его с [официального сайта](https://www.python.org/downloads/).

### 2. Установите зависимости
Установите необходимые библиотеки с помощью команды:

```bash
pip install aiogram beautifulsoup4 aiohttp
```

### 3. Создайте бота в Telegram
1. Откройте Telegram и найдите бота **BotFather**.
2. Создайте нового бота с помощью команды `/newbot`.
3. Следуйте инструкциям, чтобы задать имя и username бота.
4. После создания бота вы получите токен. Сохраните его.

### 4. Настройте токен
1. Откройте файл `bot.py`.
2. Найдите строку с токеном:
   ```python
   BOT_TOKEN = 'ВАШ_ТОКЕН_БОТА'
   ```
3. Замените значение токена на ваш.

### 5. Запустите бота
Запустите бота с помощью команды:

```bash
python bot.py
```

### 6. Проверка работы
1. Перейдите в Telegram и найдите вашего бота по username.
2. Отправьте команду `/start` и начните поиск музыки или видео.

---

## 📄 Лицензия

Этот проект распространяется под лицензией [MIT](LICENSE). Вы можете свободно использовать, изменять и распространять код.

---

**pyBotiCkMuSbot** — ваш помощник в поиске музыки и видео! 🎶🎥

---
