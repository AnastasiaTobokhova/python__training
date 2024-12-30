# Задача "Меньше текста, больше кликов":
#
# Необходимо дополнить код предыдущей задачи, чтобы вопросы о параметрах тела для расчёта калорий выдавались по нажатию кнопки.
# Измените massage_handler для функции set_age. Теперь этот хэндлер будет реагировать на текст 'Рассчитать',
# а не на 'Calories'.
# Создайте клавиатуру ReplyKeyboardMarkup и 2 кнопки KeyboardButton на ней со следующим текстом:
# 'Рассчитать' и 'Информация'.
# Сделайте так, чтобы клавиатура подстраивалась под размеры интерфейса устройства при помощи параметра resize_keyboard.
# Используйте ранее созданную клавиатуру в ответе функции start, используя параметр reply_markup.
# В итоге при команде /start у вас должна присылаться клавиатура с двумя кнопками.
# При нажатии на кнопку с надписью 'Рассчитать' срабатывает функция set_age с которой начинается работа машины
# состояний для age, growth и weight.

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import asyncio

api = "7292545655:AAEhNcqwcU5idv44vfbQzBJwyfeV7V1vrAQ"
bot = Bot(token = api)
dp = Dispatcher(bot, storage = MemoryStorage())
kb = ReplyKeyboardMarkup()
button = KeyboardButton(text= 'Информация')
button2 = KeyboardButton(text= 'Рассчитать')
kb.add(button)
kb.add(button2)
# kb.row kb.insert

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет', reply_markup = kb)

@dp.message_handler(text='Информация')
async def inform(message):
    await message.answer('Информация о боте: ')

@dp.message_handler(text='Рассчитать')
async def set_age(message):
    await message.answer('Введите свой возраст: ')
    await UserState.age.set()

@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост: ')
    await UserState.growth.set()

@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес: ')
    await UserState.weight.set()

@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    # извлекаем возраст рост вес
    age = int(data['age'])
    growth = int(data['growth'])
    weight = int(data['weight'])
    # Расчет по формуле Миффлина - Сан Жеора (для женщин)
    calories = 10 * weight + 6.25 * growth - 5 * age - 161
    await message.answer(f"Ваша норма калорий: {calories:.0f} ккал в день.")
    await state.finish()


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)