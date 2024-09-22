first = 'Мама мыла раму'
second = 'Рамена мало было'

# Определение lambda-функции
compare_letters = lambda x, y: x == y

# Применение функции через map
result = list(map(compare_letters, first, second))

# Вывод результата
print(result)

def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'a') as file:
            for item in data_set:
                file.write(str(item) + '\n')
    return write_everything

# Пример использования
write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])
from random import choice

class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return choice(self.words)

# Пример использования
first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())