# Задача "Продуктовая база":
#
# Подготовка:
#
# Для решения этой задачи вам понадобится код из предыдущей задачи. Дополните его, следуя пунктам задачи ниже.
#
# Дополните ранее написанный код для Telegram-бота:
#
# Создайте файл crud_functions.py и напишите там следующие функции:
# initiate_db, которая создаёт таблицу Products, если она ещё не создана при помощи SQL запроса.
# Эта таблица должна содержать следующие поля:
# id - целое число, первичный ключ
# title(название продукта) - текст (не пустой)
# description(описание) - текст
# price(цена) - целое число (не пустой)
# get_all_products, которая возвращает все записи из таблицы Products, полученные при помощи SQL запроса.
#
# Изменения в Telegram-бот:
# В самом начале запускайте ранее написанную функцию get_all_products.
# Измените функцию get_buying_list в модуле с Telegram-ботом,
# используя вместо обычной нумерации продуктов функцию get_all_products.
# Полученные записи используйте в выводимой надписи: "Название: <title> | Описание: <description> | Цена: <price>"
# Перед запуском бота пополните вашу таблицу Products 4 или более записями для последующего вывода в чате Telegram-бота.

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from crud_functions import initiate_db, populate_products, get_all_products

# Создание базы данных и таблицы
initiate_db()

# Заполнение таблицы продуктами
populate_products()

# API токен
api = "7292545655:AAEhNcqwcU5idv44vfbQzBJwyfeV7V1vrAQ"
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

# Машина состояний
class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

# Инлайн-клавиатура для продуктов
product_inline_kb = InlineKeyboardMarkup(row_width=2)
products = [
    InlineKeyboardButton(text="Product1", callback_data="product_buying"),
    InlineKeyboardButton(text="Product2", callback_data="product_buying"),
    InlineKeyboardButton(text="Product3", callback_data="product_buying"),
    InlineKeyboardButton(text="Product4", callback_data="product_buying")
]
product_inline_kb.add(*products)

# Обычная клавиатура с кнопкой "Купить"
main_menu_kb = ReplyKeyboardMarkup(resize_keyboard=True)
main_menu_kb.add(KeyboardButton('Рассчитать'), KeyboardButton('Информация'), KeyboardButton('Купить'))

# Обработчик команды /start
@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.answer('Рады вас видеть!', reply_markup=main_menu_kb)

# Обработчик текстовой команды "Рассчитать"
@dp.message_handler(text='Рассчитать')
async def main_menu(message: types.Message):
    await message.answer('Выберите опцию:', reply_markup=inline_kb)

# Обработчик текстовой команды "Купить"
@dp.message_handler(text='Купить')
async def get_buying_list(message: types.Message):
    for i in range(1, 5):
        with open(f'image{i}.jpg', 'rb') as image:
            await message.answer_photo(image, caption=f'Название: Product{i} | Описание: описание {i} | Цена: {i * 100}')
    await message.answer("Выберите продукт для покупки:", reply_markup=product_inline_kb)

# Обработчик инлайн-кнопок продуктов
@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call: types.CallbackQuery):
    await call.message.answer("Вы успешно приобрели продукт!")
    await call.answer()

# Обработчик инлайн-кнопки "Формулы расчёта"
@dp.callback_query_handler(text='formulas')
async def get_formulas(call: types.CallbackQuery):
    formula = (
        "Формула Миффлина-Сан Жеора:\n"
        "Для женщин: 10 * вес (кг) + 6.25 * рост (см) - 5 * возраст (лет) - 161\n"
        "Для мужчин: 10 * вес (кг) + 6.25 * рост (см) - 5 * возраст (лет) + 5"
    )
    await call.message.answer(formula)
    await call.answer()

# Обработчик инлайн-кнопки "Рассчитать норму калорий"
@dp.callback_query_handler(text='calories')
async def set_age(call: types.CallbackQuery):
    await call.message.answer('Введите свой возраст: ')
    await UserState.age.set()
    await call.answer()

@dp.message_handler(state=UserState.age)
async def set_growth(message: types.Message, state: FSMContext):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост: ')
    await UserState.growth.set()

@dp.message_handler(state=UserState.growth)
async def set_weight(message: types.Message, state: FSMContext):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес: ')
    await UserState.weight.set()

@dp.message_handler(state=UserState.weight)
async def send_calories(message: types.Message, state: FSMContext):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    # Извлекаем возраст, рост, вес
    age = int(data['age'])
    growth = int(data['growth'])
    weight = int(data['weight'])
    # Расчет по формуле Миффлина-Сан Жеора (для женщин)
    calories = 10 * weight + 6.25 * growth - 5 * age - 161
    await message.answer(f"Ваша норма калорий: {calories:.0f} ккал в день.")
    await state.finish()

@dp.message_handler(text='Купить')
async def get_buying_list(message: types.Message):
    products = get_all_products()
    for product in products:
        product_id, title, description, price = product
        await message.answer(f"Название: {title}\nОписание: {description}\nЦена: {price} рублей")
    await message.answer("Выберите продукт для покупки:", reply_markup=product_inline_kb)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)