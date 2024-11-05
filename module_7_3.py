import string
import os


class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            try:
                with open(file_name, 'r', encoding='utf-8') as file:
                    content = file.read().lower()
                    # Убираем пунктуацию
                    content = content.translate(str.maketrans('', '', string.punctuation))
                    words = content.split()
                    all_words[file_name] = words
            except FileNotFoundError:
                print(f"Файл {file_name} не найден. Проверьте путь или название файла.")
        return all_words

    def find(self, word):
        word = word.lower()
        result = {}
        for file_name, words in self.get_all_words().items():
            try:
                result[file_name] = words.index(word) + 1
            except ValueError:
                result[file_name] = None
        return result

    def count(self, word):
        word = word.lower()
        result = {}
        for file_name, words in self.get_all_words().items():
            result[file_name] = words.count(word)  # Подсчитываем количество вхождений
        return result


# проверяем наличие файла в директории
file_path = '/mnt/data/Mother Goose - Monday’s Child.txt'

if os.path.exists(file_path):
    finder2 = WordsFinder(file_path)


    print(finder2.get_all_words())


    print(finder2.find('child'))

    print(finder2.count('child'))
else:
    print(f"Файл {file_path} не найден!")


