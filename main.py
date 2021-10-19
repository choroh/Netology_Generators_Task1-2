"""
Netology. Iteratoes, Generators
1.  Написать класс итератора, который по каждой стране из файла countries.json ищет страницу из википедии.
    Записывает в файл пару: страна – ссылка. Ссылку формировать самостоятельно.

2. Написать генератор, который принимает путь к файлу. При каждой итерации возвращает md5 хеш каждой строки файла.
18.10.21
"""
import json
import hashlib

url = "https://en.wikipedia.org/"
file_in = 'files/countries.json'
file_out = 'files/countries.txt'

print('Задание 1')
class MyIterator:
    """
    Класс выполняющий работу итератора
    """
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.cursor = None

    def __iter__(self):
        self.cursor = self.start - 1
        return self

    def __next__(self):
        self.cursor += 1
        if self.cursor == self.end:
            raise StopIteration
        return line[self.cursor]['name']['official']


with open(file_in, encoding="UTF-8")as f:
    line = json.load(f)

countrys = MyIterator(0, len(line))
country = [i.replace(' ', '_') for i in countrys]
#  Получаем список стран из файла, заменяем пробелы на "_"

country_out = []
#  список с результатом

for i in country:
    http = url + "wiki/" + i.replace("'", ("")).replace('(', '').replace(')', '')
    #  Получаем ссылку на статью в Википедии, удаляем "'" и скобки
    out = f'{i} - {http}'
    country_out.append(out)

with open(file_out, 'w', encoding='UTF-8') as f1:
    for i in country_out:
        f1.write(i+'\n')
    print("Список стран со ссылками на Википедию записан в файл countries.txt \n")


#  2. Написать генератор, который принимает путь к файлу.
print('Задание 2')
print('Список хешированных строк из файла со странами\n')


def generator_h(file):
    """
    Функция получает имя файла со списком, построчно хеширует и выадет
    :param file:
    :return:
    """
    with open(file, encoding='UTF-8') as f2:
        line = (i.strip() for i in f2.readlines())
        for i in line:
            i_hash = hashlib.md5(i.encode())
            print(i_hash.hexdigest())


generator_h(file_out)
