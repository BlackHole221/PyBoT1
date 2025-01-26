from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
import aiohttp
from bs4 import BeautifulSoup
import logging
import asyncio

# Настройка логирования
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

# Токен бота
BOT_TOKEN = 'ВАШ_ТОКЕН_БОТА'

# Инициализация бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Словарь для хранения данных пользователей
user_data = {}

# Функция для сохранения запросов пользователя
def save_user_query(chat_id: int, query: str):
    if chat_id not in user_data:
        user_data[chat_id] = {"history": [], "results": [], "index": 0, "type": None}
    user_data[chat_id]["history"].append(query)
    # Ограничиваем историю последними 10 запросами
    if len(user_data[chat_id]["history"]) > 10:
        user_data[chat_id]["history"] = user_data[chat_id]["history"][-10:]

# Создание клавиатуры для старта (только кнопка "Начать")
def create_start_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="▶️ Начать")]
        ],
        resize_keyboard=True
    )

# Создание основной клавиатуры
def create_main_menu():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="🎥 Видео на Rutube"), KeyboardButton(text="🎵 Музыка на Bandcamp")],
            [KeyboardButton(text="📜 История"), KeyboardButton(text="❌ Очистить историю")],
            [KeyboardButton(text="🏠 Главное меню")]
        ],
        resize_keyboard=True
    )

# Создание клавиатуры только с кнопкой "Главное меню"
def create_menu_only_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="🏠 Главное меню")]
        ],
        resize_keyboard=True
    )

# Создание клавиатуры для поиска
def create_search_buttons():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Искать ещё", callback_data="more"),
                InlineKeyboardButton(text="Новый поиск", callback_data="new")
            ],
            [InlineKeyboardButton(text="Закончить", callback_data="stop")]
        ]
    )

# Поиск видео на Rutube
async def find_videos(query: str):
    url = f"https://rutube.ru/api/search/video/?query={query}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}

    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            if response.status == 200:
                data = await response.json()
                return [(item.get("title", "Без названия"), f"https://rutube.ru/video/{item.get('id')}/") for item in data.get("results", [])]
            logger.error(f"Ошибка запроса: {response.status}")
    return []

# Поиск музыки на Bandcamp
async def find_music(query: str):
    url = f"https://bandcamp.com/search?q={query}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}

    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            if response.status == 200:
                soup = BeautifulSoup(await response.text(), 'html.parser')
                return [(item.find('div', {'class': 'heading'}).text.strip(), item.find('a')['href']) for item in soup.find_all('li', {'class': 'searchresult'})]
            logger.error(f"Ошибка запроса: {response.status}")
    return []

# Обработчик команды /start
@dp.message(Command("start"))
async def start_bot(message: types.Message):
    name = message.from_user.first_name
    username = message.from_user.username
    greeting = f"Привет, {name}!" + (f" (@{username})" if username else "")
    await message.answer(greeting)
    await message.answer("Я бот для поиска видео и музыки. Нажми «▶️ Начать», чтобы выбрать тип поиска.)", reply_markup=create_start_keyboard())

# Обработчик кнопки "Начать"
@dp.message(lambda message: message.text == "▶️ Начать")
async def start_search(message: types.Message):
    await message.answer("Выбери, что ты хочешь искать:", reply_markup=create_main_menu())

# Обработчик кнопки "Главное меню"
@dp.message(lambda message: message.text == "🏠 Главное меню")
async def return_to_menu(message: types.Message):
    await message.answer("Вы вернулись в главное меню.", reply_markup=create_main_menu())



# Обработчик выбора типа поиска
@dp.message(lambda message: message.text in ["🎥 Видео на Rutube", "🎵 Музыка на Bandcamp"])
async def choose_search_type(message: types.Message):
    chat_id = message.chat.id
    if chat_id not in user_data:
        user_data[chat_id] = {"history": [], "results": [], "index": 0, "type": None}
    user_data[chat_id]["type"] = "video" if message.text == "🎥 Видео на Rutube" else "music"
    await message.answer(
        f"Отлично! Теперь я буду искать {'видео на Rutube' if user_data[chat_id]['type'] == 'video' else 'музыку на Bandcamp'}. Введи запрос:",
        reply_markup=create_menu_only_keyboard()  # Только кнопка "Главное меню"
    )

# Обработчик текстовых сообщений
@dp.message()
async def process_query(message: types.Message):
    chat_id = message.chat.id
    query = message.text.strip()

    if query == "📜 История":
        if chat_id in user_data and user_data[chat_id]["history"]:
            history = "\n".join(f"{i}. {item}" for i, item in enumerate(user_data[chat_id]["history"], 1))
            await message.answer(f"История запросов:\n{history}")
        else:
            await message.answer("История запросов пуста.")
        return

    if query == "❌ Очистить историю":
        if chat_id in user_data:
            user_data[chat_id]["history"] = []
            await message.answer("История запросов очищена.", reply_markup=create_main_menu())
        else:
            await message.answer("История запросов уже пуста.", reply_markup=create_main_menu())
        return

    if query == "🏠 Главное меню":
        await return_to_menu(message)
        return

    if chat_id not in user_data or not user_data[chat_id]["type"]:
        await message.answer("Сначала выбери тип поиска.", reply_markup=create_main_menu())
        return

    save_user_query(chat_id, query)
    if user_data[chat_id]["type"] == "video":
        results = await find_videos(query)
    else:
        results = await find_music(query)

    if not results:
        await message.answer("Ничего не найдено. Попробуй другой запрос.", reply_markup=create_main_menu())
        return

    user_data[chat_id]["results"] = results
    user_data[chat_id]["index"] = 0
    await show_result(chat_id, message)

# Отправка результата пользователю
async def show_result(chat_id: int, message: types.Message = None):
    if chat_id not in user_data or not user_data[chat_id]["results"]:
        return

    result = user_data[chat_id]["results"][user_data[chat_id]["index"]]
    text = f"🎵 Найдено: <b>{result[0]}</b>\n🔗 Ссылка: {result[1]}"

    if message:
        await message.answer(text, parse_mode=ParseMode.HTML, reply_markup=create_search_buttons())
    else:
        await bot.send_message(chat_id, text, parse_mode=ParseMode.HTML, reply_markup=create_search_buttons())



# Обработчик кнопки "Искать ещё"
@dp.callback_query(lambda callback: callback.data == "more")
async def next_result(callback: types.CallbackQuery):
    chat_id = callback.message.chat.id

    if chat_id not in user_data or not user_data[chat_id]["results"]:
        await callback.answer("Результаты устарели. Начни новый поиск.")
        return

    user_data[chat_id]["index"] += 1
    if user_data[chat_id]["index"] >= len(user_data[chat_id]["results"]):
        await callback.answer("Больше результатов нет.")
        return

    await callback.answer("Загружаю следующий результат...")
    await show_result(chat_id)

# Обработчик кнопки "Новый поиск"
@dp.callback_query(lambda callback: callback.data == "new")
async def new_search(callback: types.CallbackQuery):
    chat_id = callback.message.chat.id
    user_data[chat_id]["results"] = []
    user_data[chat_id]["index"] = 0
    await callback.answer("Начни новый поиск.")
    await callback.message.answer("Введи новый запрос:", reply_markup=create_main_menu())



# Обработчик кнопки "Закончить"
@dp.callback_query(lambda callback: callback.data == "stop")
async def stop_search(callback: types.CallbackQuery):
    chat_id = callback.message.chat.id
    user_data[chat_id]["results"] = []
    user_data[chat_id]["index"] = 0
    await callback.answer("Поиск завершён.")
    await callback.message.answer("Поиск остановлен. Выбери что - то: ", reply_markup=create_main_menu())





# Запуск бота
async def run_bot():
    try:
        logger.info("Бот запущен!")
        await dp.start_polling(bot)
    except Exception as e:
        logger.error(f"Ошибка: {e}")

if __name__ == '__main__':
    asyncio.run(run_bot())
