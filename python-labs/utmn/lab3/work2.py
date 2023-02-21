# Кинотеатр. Для взаимодействия с клиентами кинотеатр использует систему,
# которая хранит информацию о фильмах: название, список актеров, стоимость билета, список сеансов и др.
#
# Фильм – название (str), краткое описание (str), список актеров (list of strs), стоимость билета (float),
# список сеансов (list of strs), оценка фильма (float)

# from tkinter import *
import re
import string
from functools import reduce

films = {'name': ['Восхождение короля', 'Реинкарнация безработного', 'Разлом', 'Страх рядом',
                  'Дятел Вуди: захватывающие приключения'],
         'desc': ['Эта история рассказывает о том, как короли сражались между собой: кто-то из-за денег, '
                  'кто-то из-за власти. У каждого из них есть свои цели, и каждый готов '
                  'достичь их любыми методами несмотря ни на что.\n\nСкоро наш главный герой, Николай, '
                  'столкнётся со своими возможными противниками, но будет добиваться всего дипломатией, а не силой.\n'
                  'Посмотрим, кто выиграет в данной ситуации.',
                  'Всё началось с того, что некий парень спасает школьников и, как следствие, падает под автобус. '
                  'После этого он перерождается в мире, затянутом войнами. Причём в этом новом мире некоторые люди '
                  'обладают дарами.\n\nПосмотрим, справится ли наш новоиспечённый герой со всеми трудностями.',
                  '«Это – Разлом, самое худшее место для жизни. Там обитают организмы, которые очень сильно отличаются'
                  'от большинства жителей Земли. Я – путешественница этого места, которая хочет разгадать его тайны.»'
                  '\n\n«Надеюсь, что останусь, хотя бы, в живых.»',
                  'Диалог друзей у костра. Каждый по очереди начинает рассказывать ту или иную жуткую ситуацию, '
                  'в которой побывал. Однако они чувствуют что-то странное...\n\nМожет быть, групповая галлюцинация, '
                  'может быть, все сошли с ума. Кто знает...',
                  'Вот и снова мы встречаем любимого с детства дятла Вуди! Вместе с ним мы обойдём весь земной шар, '
                  'в поисках того, что ищут неприятели Вуди.\n\nПосмотрим, кто обыграет всех.'],
         'actors': [['Актёр А', 'Актёр Б', 'Актёр В'],
                    ['Актёр А', 'Актёр Б', 'Актёр В'],
                    ['Актёр А', 'Актёр Б', 'Актёр В'],
                    ['Актёр А', 'Актёр Б', 'Актёр В'],
                    ['Актёр А', 'Актёр Б', 'Актёр В']],
         'cost': [350, 450, 400, 380, 270],
         'time': [['01.01.2012 9:30', '01.01.2012 12:00', '01.01.2012 13:45', '01.01.2012 16:10', '01.01.2012 19:35'],
                  ['01.01.2012 9:30', '01.01.2012 12:00', '01.01.2012 13:45', '01.01.2012 16:10', '01.01.2012 19:35'],
                  ['01.01.2012 9:30', '01.01.2012 12:00', '01.01.2012 13:45', '01.01.2012 16:10', '01.01.2012 19:35'],
                  ['01.01.2012 9:30', '01.01.2012 12:00', '01.01.2012 13:45', '01.01.2012 16:10', '01.01.2012 19:35'],
                  ['01.01.2012 9:30', '01.01.2012 12:00', '01.01.2012 13:45', '01.01.2012 16:10', '01.01.2012 19:35']],
         'rating': [3.8, 4.2, 4.15, 4.72, 4.44]}


def addFilm():  # Добавить фильм
    # Тители__Тители – эра Альфача__Ари||Бэри||Вэри__375__01.01.2020 09:00||01.02.2020 09:00||02.02.2020 09:00__3.25
    adding_film = input('Опишите фильм, который хотите добавить (элементы описания разделять через знак "__", '
                        'списки в элементах – через "||"; можно скопировать символы из кавычек):'
                        '\nНазвание\nОписание\nСписок актёров\nСтоимость\nДата и время сеансов\nОценка\n').split('__')
    if len(adding_film) == 6\
            and re.match(r'^[а-яё\s'+''.join(string.punctuation)+'–—]+$', adding_film[0], re.I)\
            and re.match(r'^[а-яё\s'+''.join(string.punctuation)+'–—]+$', adding_film[1], re.I)\
            and re.match(r'^[А-ЯЁ][а-яё]{2,}(\s[А-ЯЁ][а-яё]{2,}){,2}(\|\|[А-ЯЁ][а-яё]{2,}(\s[А-ЯЁ][а-яё]{2,}){,2})*$',
                         adding_film[2])\
            and re.match(r'^\d+$', adding_film[3])\
            and re.match(r'^((0[1-9]|[12]\d|3[01])\.(0[13578]|1[02])|(0[1-9]|[12]\d|30)\.(0[469]|11)|(0[1-9]|[12]\d)\.'
                         r'(02))\.\d+\s(([01]\d)|(2[0-3])):[0-5]\d(\|\|((0[1-9]|[12]\d|3[01])\.'
                         r'(0[13578]|1[02])|(0[1-9]|[12]\d|30)\.(0[469]|11)|(0[1-9]|[12]\d)\.'
                         r'(02))\.\d+\s(([01]\d)|(2[0-3])):[0-5]\d)*$', adding_film[4])\
            and re.match(r'^([0-4](\.\d{1,2})?|5)$', adding_film[5]):
        films['name'].append(adding_film[0])
        films['desc'].append(adding_film[1])
        films['actors'].append(list(adding_film[2].split('||')))
        films['cost'].append(int(adding_film[3]))
        films['time'].append(list(adding_film[4].split('||')))
        films['rating'].append(float(adding_film[5]))
        print('\nФильм добавлен\n')
    else:
        print('\nВы ввели неверное количество элементов описания или некоторые элементы описания введены неверно\n')
        return False
    return True


def deleteFilm():  # Удалить фильм
    print('Какой из фильмов вы хотите удалить:')
    for i in range(len(films['name'])):
        print(str(i + 1) + '. ' + films['name'][i])
    deleting_film = int(input()) - 1
    if deleting_film in range(len(films['name'])):
        del films['name'][deleting_film]
        del films['desc'][deleting_film]
        del films['actors'][deleting_film]
        del films['cost'][deleting_film]
        del films['time'][deleting_film]
        del films['rating'][deleting_film]
        print('\nФильм удалён\n')
    else:
        print('\nДанного фильма нет в списке\n')
        return False
    return True


def findFilm():  # Найти фильм
    found_film = input('По какому элементу из характеристик вы хотите найти фильм:'
                       '\n1. Название\n2. Список актёров\n3. Стоимость\n4. Дата и время сеансов\n5. Оценка\n')
    print('')
    if found_film == '1':
        found_film = input('Введите название фильма:\n')
        if found_film in films['name']:
            name_pos = films['name'].index(found_film)
            print('\nНазвание:\n' + films['name'][name_pos] +
                  '\n\nОписание:\n' + films['desc'][name_pos] +
                  '\n\nСписок актёров:\n' + ', '.join(films['actors'][name_pos]) +
                  '\n\nСтоимость:\n' + str(films['cost'][name_pos]) +
                  '\n\nСписок сеансов:\n' + ', '.join(films['time'][name_pos]) +
                  '\n\nОценка:\n' + str(films['rating'][name_pos]) + '\n')
        else:
            print('\nДанного фильма нет\n')
            return False
    elif found_film == '2':
        found_film = input('Введите ФИО актёра, участвующего в фильме:\n')
        found = False
        film = ''
        for i in range(len(films['actors'])):
            for j in range(len(films['actors'][i])):
                if found_film in films['actors'][i][j]:
                    film += '\nНазвание:\n' + films['name'][i] +\
                                 '\n\nОписание:\n' + films['desc'][i] +\
                                 '\n\nСписок актёров:\n' + ', '.join(films['actors'][i]) +\
                                 '\n\nСтоимость:\n' + str(films['cost'][i]) +\
                                 '\n\nСписок сеансов:\n' + ', '.join(films['time'][i]) +\
                                 '\n\nОценка:\n' + str(films['rating'][i]) + '\n'
                    found = True
        if found:
            print('\n' + film)
        else:
            print('\nДанного фильма нет\n')
            return False
    elif found_film == '3':
        found_film = input('Введите стоимость фильма:\n')
        if found_film in films['cost']:
            cost_pos = films['cost'].index(int(found_film))
            print('\nНазвание:\n' + films['name'][cost_pos] +
                  '\n\nОписание:\n' + films['desc'][cost_pos] +
                  '\n\nСписок актёров:\n' + ', '.join(films['actors'][cost_pos]) +
                  '\n\nСтоимость:\n' + str(films['cost'][cost_pos]) +
                  '\n\nСписок сеансов:\n' + ', '.join(films['time'][cost_pos]) +
                  '\n\nОценка:\n' + str(films['rating'][cost_pos]) + '\n')
        else:
            print('\nДанного фильма нет\n')
            return False
    elif found_film == '4':
        found_film = input('Введите время сеанса фильма:\n')
        found = False
        film = ''
        for i in range(len(films['time'])):
            for j in range(len(films['time'][i])):
                if found_film in films['time'][i][j]:
                    film += '\nНазвание:\n' + films['name'][i] +\
                                 '\n\nОписание:\n' + films['desc'][i] +\
                                 '\n\nСписок актёров:\n' + ', '.join(films['actors'][i]) +\
                                 '\n\nСтоимость:\n' + str(films['cost'][i]) +\
                                 '\n\nСписок сеансов:\n' + ', '.join(films['time'][i]) +\
                                 '\n\nОценка:\n' + str(films['rating'][i]) + '\n'
                    found = True
        if found:
            print('\n' + film)
        else:
            print('\nДанного фильма нет\n')
            return False
    elif found_film == '5':
        found_film = input('Введите оценку фильма:\n')
        if found_film in films['rating']:
            tate_pos = films['rating'].index(float(found_film))
            print('\nНазвание:\n' + films['name'][tate_pos] +
                  '\n\nОписание:\n' + films['desc'][tate_pos] +
                  '\n\nСписок актёров:\n' + ', '.join(films['actors'][tate_pos]) +
                  '\n\nСтоимость:\n' + str(films['cost'][tate_pos]) +
                  '\n\nСписок сеансов:\n' + ', '.join(films['time'][tate_pos]) +
                  '\n\nОценка:\n' + str(films['rating'][tate_pos]) + '\n')
        else:
            print('\nДанного фильма нет\n')
            return False
    else:
        print('Нет такого элемента характеристики фильма\n')
        return False
    print('')
    return True


def listOfFilms():  # Список фильмов
    print('Список фильмов:')
    for i in range(len(films['name'])):
        print('\nНазвание:\n' + films['name'][i] + '\n\nОписание:\n' + films['desc'][i] + '\n\nСписок актёров:\n' +
              ', '.join(films['actors'][i]) + '\n\nСтоимость:\n' + str(films['cost'][i]) + '\n\nСписок сеансов:\n' +
              ', '.join(films['time'][i]) + '\n\nОценка:\n' + str(films['rating'][i]) + '\n')
    return True


def filterFilms():  # Фильтр фильмов
    filtered_films = input('По какому критерию вы хотите отфильтровать фильмы:\n1. Название фильмов\n'
                           '2. Стоимость фильмов\n3. Оценка фильмов')
    print(sorted(films['name']))
    return True


def middleStat():  # Средний показатель
    middle_films_stat = input('Выберите, по какому элементу характеристики фильмов определить среднее значение:\n'
                              '1. Стоимость фильмов\n2. Оценки фильмов\n')
    if middle_films_stat == '1':
        print('\nСредний показатель по стоимости фильмов равен ' + str(int(reduce(lambda x, y: x + y, films['cost']) /
                                                                           len(films['cost']))))
    elif middle_films_stat == '2':
        print('\nСредний показатель по оценкам фильмов равен ' + str(round(reduce(lambda x, y: x + y, films['rating']) /
                                                                           len(films['rating']), 2)))
    else:
        print('Невозможно найти средний показатель')
        return False
    print('')
    return True


def checking_input(val):  # Проверка ввода
    print('')
    if val == '1':  # Добавить фильм
        addFilm()
    elif val == '2':  # Удалить фильм
        deleteFilm()
    elif val == '3':  # Найти фильм
        findFilm()
    elif val == '4':  # Список фильмов
        listOfFilms()
    elif val == '5':  # Фильтр фильмов
        filterFilms()
    elif val == '6':  # Средний показатель
        middleStat()
    elif val in ['end', 'конец']:  # Закрыть программу
        raise SystemExit('Программа закрыта')
    else:  # Если вдруг введённое значение не соответствует ни одной из описанных выше функций,
        # то повторная попытка записи функции
        print('У нас нет такой функции\n')
        return False
    return True


while True:  # Работа приложения (постоянная)
    in_val = input('Наберите следующее, чтобы сделать/посмотреть:\n1. Добавить фильм\n2. Удалить фильм\n3. Найти фильм'
                   '\n4. Список фильмов\n5. Фильтр по информации о фильмах\n6. Средний показатель фильмов'
                   '\nend/конец. Закрыть приложение\n')
    checking_input(in_val)  # Проверка ввода


# def moveNext(i = i):
#     i += 1
#     print(i)
#     return i
#
#
# def movePrev():
#     return True
#
#
# def prr():
#     root2 = Tk()
#     root2.rowconfigure(0, minsize=50, weight=1)
#     root2.columnconfigure(0, minsize=100, weight=1)
#     root2.columnconfigure(1, minsize=100, weight=1)
#     btn2 = Button(root2, text='Close me!', command=root2.destroy) # root2.withdraw
#     btn2.grid(row=0, column=0)
#     root2.mainloop()
#     return True
#
#
# root = Tk()
# root.title('Кинотеатр')
# # Entry(root, width=10,).grid(column=3, row=0)
#
# lbl1 = Label(root, text='Вы просматриваете информацию о фильме:').grid(column=0, row=0, padx=(0, 0), pady=(0, 0))
# lbl2 = Label(root, text=films['name'][i]).grid(column=0, row=1, padx=(0, 0), pady=(0, 0))
# lbl3 = Label(root, text=films['desc'][i], wraplength=300).grid(column=1, row=1, padx=(0, 0), pady=(0, 0))
# lbl4 = Label(root, text=films['actors'][i]).grid(column=2, row=1, padx=(0, 0), pady=(0, 0))
# lbl5 = Label(root, text=films['cost'][i]).grid(column=3, row=1, padx=(0, 0), pady=(0, 0))
# lbl6 = Label(root, text=films['time'][i]).grid(column=4, row=1, padx=(0, 0), pady=(0, 0))
# lbl7 = Label(root, text=films['rating'][i]).grid(column=5, row=1, padx=(0, 0), pady=(0, 0))
#
# Button(root, text='>', command=moveNext).grid(column=5, row=2, pady=(0, 10))
# Button(root, text='<', command=movePrev).grid(column=0, row=2)
#
#
# root.mainloop()
