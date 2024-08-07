def custom_write(file_name, strings):
    strings_positions = {}

    with open(file_name, 'w', encoding='utf-8') as file:
        for index, string in enumerate(strings):
            if isinstance(string, str):  # Проверяем, что элемент является строкой
                byte_position = file.tell()  # Получаем текущую позицию байта
                file.write(string + '\n')  # Записываем строку с новой строки
                strings_positions[(index + 1, byte_position)] = string  # Сохраняем номер строки и позицию в словарь
            else:
                raise ValueError(f'Элемент {string} не является строкой.')

    return strings_positions


# Пример использования:
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)