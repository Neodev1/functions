"""
МОДУЛЬ 2
Программа из 2-го дз
Сначала пользователь вводит год рождения Пушкина, когда отвечает верно вводит день рождения
Можно использовать свой вариант программы из предыдущего дз, мой вариант реализован ниже
Задание: переписать код используя как минимум 1 функцию
"""
def birthday_question(question, data):
    answer=input(question)
    while answer != data:
        print('Не верно')
        answer=input(question)

birthday_question('Ввведите год рождения Киану Ривз:', '1964')
birthday_question('В какой день сентября родился Киану Ривз?', '2')
print('Верно')

# year = input('Ввведите год рождения Киану Ривз:')
# while year != '1964':
#     print("Не верно")
#     year = input('Ввведите год рождения Киану Ривз:')
#
# day = input('В какой день сентября родился Киану Ривз?')
# while day != '2':
#     print("Не верно")
#     day = input('В какой день сентября родился Киану Ривз?')
# print('Верно')

days={
    '01':'первое',
    '02':'второе',
    '03':'третье',
    '04':'четвертое',
    '05':'пятое',
    '06':'шестое',
    '07':'седьмое',
    '08':'восьмое',
    '09':'девятое',
    '10':'десятое',
    '11':'одиннадцатое',
    '12':'двеннадцатое',
    '13':'триннадцатое',
    '14':'четырнадцатое',
    '15':'пятнадцатое',
    '16':'шестнадцатое',
    '17':'семнадцатое',
    '18':'восемнадцатое',
    '19':'девятнадцатое',
    '20':'двадцатое',
    '21':'двадцать первое',
    '22':'двадцать второе',
    '23':'двадцать третье',
    '24':'двадцать четвертое',
    '25':'двадцать пятое',
    '26':'двадцать шестое',
    '27':'двадцать седьмое',
    '28':'двадцать восьмое',
    '29':'двадцать девятое',
    '30':'тридцатое',
    '31':'тридцать первое'
}
months={
    '01':'января',
    '02':'февраля',
    '03':'марта',
    '04':'апреля',
    '05':'мая',
    '06':'июня',
    '07':'июля',
    '08':'августа',
    '09':'сентября',
    '10':'октября',
    '11':'ноября',
    '12':'декабря'
}
print('Викторина  начинается!')
import random
bornyears=['bornyear1', 'bornyear2', 'bornyear3', 'bornyear4', 'bornyear5', 'bornyear6', 'bornyear7']
result=random.sample(bornyears, 5)

total = 0

for bornyear in result:
    if bornyear == 'bornyear1':
        question = (input('Введите дату рождения А.С.Пушкина в формате dd.mm.yy: '))
        data = '06.06.1799'
    elif bornyear == 'bornyear2' :
        question = (input('Введите дату рождения Д.И.Менделеева в формате dd.mm.yy: '))
        data = '08.02.1834'
    elif bornyear == 'bornyear2' :
        question = (input('Введите дату рождения Д.И.Менделеева в формате dd.mm.yy: '))
        data = '08.02.1834'
    elif bornyear == 'bornyear3' :
        question = (input('Введите дату рождения Леонардо Да Винчи в формате dd.mm.yy: '))
        data = '15.04.1452'
    elif bornyear == 'bornyear4' :
        question = (input('Введите дату рождения Адриано Челентано в формате dd.mm.yy: '))
        data = '06.01.1938'
    elif bornyear == 'bornyear5' :
        question = (input('Введите дату рождения Джим Кэрри в формате dd.mm.yy: '))
        data = '17.01.1962'
    elif bornyear == 'bornyear6' :
        question = (input('Введите дату рождения Джекки Чан в формате dd.mm.yy: '))
        data = '07.04.1954'
    elif bornyear == 'bornyear7' :
        question = (input('Введите дату рождения Киану Ривз в формате dd.mm.yy: '))
        data = '02.09.1964'


def birthday_question(question, data):
    answer=question
    if answer == data:
        total+=1
    else:
        data=data
        day, month, year = data.split('.')
        right_answer = (days[day], months[month], year, 'года')
        return right_answer

for bornyear in result:
    birthday_question(bornyear, data)



print('Количество правильных ответов: ', total)
print('Количество ошибок: ', 5 - total)
print('Процент правильных ответов: ', (total * 100) / 5)
print('Процент неправильных ответов: ', (5 - total) * 100 / 5)
print('Хотите начать игру сначала?')
otvet = input()
while otvet == 'да':
    print('Викторина  начинается!')
    import random
    bornyears = ['bornyear1', 'bornyear2', 'bornyear3', 'bornyear4', 'bornyear5', 'bornyear6', 'bornyear7']
    result = random.sample(bornyears, 5)
    total = 0

    for bornyear in result:
        if bornyear == 'bornyear1':
            question = (input('Введите дату рождения А.С.Пушкина в формате dd.mm.yy: '))
            data = '06.06.1799'
        elif bornyear == 'bornyear2':
            question = (input('Введите дату рождения Д.И.Менделеева в формате dd.mm.yy: '))
            data = '08.02.1834'
        elif bornyear == 'bornyear2':
            question = (input('Введите дату рождения Д.И.Менделеева в формате dd.mm.yy: '))
            data = '08.02.1834'
        elif bornyear == 'bornyear3':
            question = (input('Введите дату рождения Леонардо Да Винчи в формате dd.mm.yy: '))
            data = '15.04.1452'
        elif bornyear == 'bornyear4':
            question = (input('Введите дату рождения Адриано Челентано в формате dd.mm.yy: '))
            data = '06.01.1938'
        elif bornyear == 'bornyear5':
            question = (input('Введите дату рождения Джим Кэрри в формате dd.mm.yy: '))
            data = '17.01.1962'
        elif bornyear == 'bornyear6':
            question = (input('Введите дату рождения Джекки Чан в формате dd.mm.yy: '))
            data = '07.04.1954'
        elif bornyear == 'bornyear7':
            question = (input('Введите дату рождения Киану Ривз в формате dd.mm.yy: '))
            data = '02.09.1964'


    def birthday_question(question, data):
        answer = input(question)
        if answer == data:
            total += 1
        else:
            data=data
            day, month, year = data.split('.')
            right_answer = (days[day], months[month], year, 'года')
            return right_answer

    for bornyear in result:
        birthday_question(bornyear, data)

    print('Количество правильных ответов: ', total)
    print('Количество ошибок: ', 5 - total)
    print('Процент правильных ответов: ', (total * 100) / 5)
    print('Процент неправильных ответов: ', (5 - total) * 100 / 5)
    print('Хотите начать игру сначала?')
    otvet = input()


