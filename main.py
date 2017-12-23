#!/bin/python
from random import randrange

my_defense = 'О-о, моя оборона!\n'
data = [
    ['Солнечный', 'Траурный', 'Плюшевый', 'Бешеный', 'Памятный', 'Трепетный', 'Базовый', 'Скошенный', 'Преданный', 'Ласковый', 'Пойманный', 'Радужный', 'Огненный', 'Радостный', 'Тензорный', 'Шёлковый', 'Пепельный', 'Ламповый', 'Жареный', 'Загнанный'],
    ['зайчик', 'Верник', 'глобус', 'ветер', 'щавель', 'пёсик', 'копчик', 'ландыш', 'стольник', 'мальчик', 'дольщик', 'Игорь', 'невод', 'егерь', 'пончик', 'лобстер', 'жемчуг', 'кольщик', 'йогурт', 'овод'],
    ['стеклянного', 'ванильного', 'резонного', 'широкого', 'дешёвого', 'горбатого', 'собачьего', 'исконного', 'волшебного', 'картонного', 'лохматого', 'арбузного', 'огромного', 'запойного', 'великого', 'бараньего', 'вандального', 'едрёного', 'парадного', 'укромного'],
    ['глаза', 'плова', 'Пельша', 'мира', 'деда', 'жира', 'мема', 'ада', 'бура', 'жала', 'нёба', 'гунна', 'хлама', 'шума', 'воза', 'сала', 'фена', 'зала', 'рака']
]


def main():
    print(gen_default())
    print(multi_gen(16))


def gen_line():
    out: str = str()
    for i in range(len(data)):
        out += data[i][randrange(len(data[i]))] + ' '
    return out + chr(10)


def multi_gen(n: int):
    out: str = str()
    for i in range(n):
        out += gen_line()
    return out


def gen_default():
    out: str = str()
    out += my_defense
    out += gen_line()
    out += my_defense
    out += gen_line()
    out += gen_line()
    out += chr(10)

    out += my_defense
    out += gen_line()
    out += my_defense
    out += gen_line()
    out += gen_line()
    out += chr(10)

    out += my_defense
    out += gen_line()
    out += my_defense
    out += gen_line()
    return out


if __name__ == '__main__':
    main()
