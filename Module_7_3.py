import string

class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            try:
                with open(file_name, 'r', encoding='utf-8') as file:
                    content = file.read().lower()  # Читаем содержимое файла и переводим в нижний регистр
                    # Убираем пунктуацию
                    content = content.translate(str.maketrans('', '', string.punctuation.replace('-', '')))
                    words = content.split()  # Разбиваем текст на слова
                    all_words[file_name] = words  # Записываем в словарь
            except FileNotFoundError:
                print(f"Файл {file_name} не найден.")
            except Exception as e:
                print(f"Ошибка при обработке файла {file_name}: {e}")
        return all_words

    def find(self, word):
        result = {}
        all_words = self.get_all_words()
        for name, words in all_words.items():
            word_lower = word.lower()
            if word_lower in words:
                result[name] = words.index(word_lower) + 1  # Возвращаем позицию первого вхождения (по счёту)
        return result

    def count(self, word):
        result = {}
        all_words = self.get_all_words()
        for name, words in all_words.items():
            word_lower = word.lower()
            count = words.count(word_lower)  # Считаем количество вхождений слова
            if count > 0:
                result[name] = count
        return result

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('Child'))
print(finder2.count('ChiLd'))