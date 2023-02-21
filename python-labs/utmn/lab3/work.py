# Кинотеатр. Для взаимодействия с клиентами кинотеатр использует систему,
# которая хранит информацию о фильмах: название, список актеров, стоимость билета, список сеансов и др.
#
# Фильм – название (str), краткое описание (str), список актеров (list of strs), стоимость билета (float),
# список сеансов (list of strs), оценка фильма (float)

# from tkinter import *
import re
import statistics
import string
from operator import itemgetter

films = [{'name': 'Восхождение короля',
          'desc': 'Эта история рассказывает о том, как короли сражались между собой: кто-то из-за денег, '
                  'кто-то из-за власти. У каждого из них есть свои цели, и каждый готов '
                  'достичь их любыми методами несмотря ни на что.\n\nСкоро наш главный герой, Николай, '
                  'столкнётся со своими возможными противниками, но будет добиваться всего дипломатией, а не силой.\n'
                  'Посмотрим, кто выиграет в данной ситуации.',
          'actors': ['Актёр А', 'Актёр Б', 'Актёр В'],
          'cost': 350,
          'time': ['01.01.2012 9:30', '01.01.2012 12:00', '01.01.2012 13:45', '01.01.2012 16:10', '01.01.2012 19:35'],
          'rating': 3.8},
         {'name': 'Реинкарнация безработного',
          'desc': 'Всё началось с того, что некий парень спасает школьников и, как следствие, падает под автобус. '
                  'После этого он перерождается в мире, затянутом войнами. Причём в этом новом мире некоторые люди '
                  'обладают дарами.\n\nПосмотрим, справится ли наш новоиспечённый герой со всеми трудностями.',
          'actors': ['Актёр А', 'Актёр Б', 'Актёр В'],
          'cost': 450,
          'time': ['01.01.2012 9:30', '01.01.2012 12:00', '01.01.2012 13:45', '01.01.2012 16:10', '01.01.2012 19:35'],
          'rating': 4.2},
         {'name': 'Разлом',
          'desc': '«Это – Разлом, самое худшее место для жизни. Там обитают организмы, которые очень сильно отличаются'
                  'от большинства жителей Земли. Я – путешественница этого места, которая хочет разгадать его тайны.»'
                  '\n\n«Надеюсь, что останусь, хотя бы, в живых.»',
          'actors': ['Актёр А', 'Актёр Б', 'Актёр В'],
          'cost': 400,
          'time': ['01.01.2012 9:30', '01.01.2012 12:00', '01.01.2012 13:45', '01.01.2012 16:10', '01.01.2012 19:35'],
          'rating': 4.15},
         {'name': 'Страх рядом',
          'desc': 'Диалог друзей у костра. Каждый по очереди начинает рассказывать ту или иную жуткую ситуацию, '
                  'в которой побывал. Однако они чувствуют что-то странное...\n\nМожет быть, групповая галлюцинация, '
                  'может быть, все сошли с ума. Кто знает...',
          'actors': ['Актёр А', 'Актёр Б', 'Актёр В'],
          'cost': 380,
          'time': ['01.01.2012 9:30', '01.01.2012 12:00', '01.01.2012 13:45', '01.01.2012 16:10', '01.01.2012 19:35'],
          'rating': 4.72},
         {'name': 'Дятел Вуди: захватывающие приключения',
          'desc': 'Вот и снова мы встречаем любимого с детства дятла Вуди! Вместе с ним мы обойдём весь земной шар, '
                  'в поисках того, что ищут неприятели Вуди.\n\nПосмотрим, кто обыграет всех.',
          'actors': ['Актёр А', 'Актёр Б', 'Актёр В'],
          'cost': 270,
          'time': ['01.01.2012 9:30', '01.01.2012 12:00', '01.01.2012 13:45', '01.01.2012 16:10', '01.01.2012 19:35'],
          'rating': 4.44}]


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
        films.append({'name': adding_film[0],
                      'desc': adding_film[1],
                      'actors': list(adding_film[2].split('||')),
                      'cost': int(adding_film[3]),
                      'time': list(adding_film[4].split('||')),
                      'rating': float(adding_film[5])})
        print('\nФильм добавлен\n')
    else:
        print('\nВы ввели неверное количество элементов описания или некоторые элементы описания введены неверно\n')
        return False
    return True


def deleteFilm():  # Удалить фильм
    print('Какой из фильмов вы хотите удалить:')
    for i in range(len(films)):
        print(str(i + 1) + '. ' + films[i]['name'])
    deleting_film = int(input()) - 1
    if deleting_film in range(len(films)):
        del films[deleting_film]
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
        found = False
        for film in films:
            if found_film in film['name']:
                found = True
                print('\nНазвание:\n' + film['name'] +
                      '\n\nОписание:\n' + film['desc'] +
                      '\n\nСписок актёров:\n' + ', '.join(film['actors']) +
                      '\n\nСтоимость:\n' + str(film['cost']) +
                      '\n\nСписок сеансов:\n' + ', '.join(film['time']) +
                      '\n\nОценка:\n' + str(film['rating']) + '\n')
        if not found:
            print('\nДанного фильма нет\n')
            return False
    elif found_film == '2':
        found_film = input('Введите ФИО актёра фильма:\n')
        found = False
        for film in films:
            if found_film in film['actors']:
                found = True
                print('\nНазвание:\n' + film['name'] +
                      '\n\nОписание:\n' + film['desc'] +
                      '\n\nСписок актёров:\n' + ', '.join(film['actors']) +
                      '\n\nСтоимость:\n' + str(film['cost']) +
                      '\n\nСписок сеансов:\n' + ', '.join(film['time']) +
                      '\n\nОценка:\n' + str(film['rating']) + '\n')
        if not found:
            print('\nДанного фильма нет\n')
            return False
    elif found_film == '3':
        found_film = input('Введите стоимость билета на фильм:\n')
        found = False
        for film in films:
            if found_film in str(film['cost']):
                found = True
                print('\nНазвание:\n' + film['name'] +
                      '\n\nОписание:\n' + film['desc'] +
                      '\n\nСписок актёров:\n' + ', '.join(film['actors']) +
                      '\n\nСтоимость:\n' + str(film['cost']) +
                      '\n\nСписок сеансов:\n' + ', '.join(film['time']) +
                      '\n\nОценка:\n' + str(film['rating']) + '\n')
        if not found:
            print('\nДанного фильма нет\n')
            return False
    elif found_film == '4':
        found_film = input('Введите дату и время фильма:\n')
        found = False
        for film in films:
            if found_film in film['time']:
                found = True
                print('\nНазвание:\n' + film['name'] +
                      '\n\nОписание:\n' + film['desc'] +
                      '\n\nСписок актёров:\n' + ', '.join(film['actors']) +
                      '\n\nСтоимость:\n' + str(film['cost']) +
                      '\n\nСписок сеансов:\n' + ', '.join(film['time']) +
                      '\n\nОценка:\n' + str(film['rating']) + '\n')
        if not found:
            print('\nДанного фильма нет\n')
            return False
    elif found_film == '5':
        found_film = input('Введите оценку фильма:\n')
        found = False
        for film in films:
            if found_film in str(film['rating']):
                found = True
                print('\nНазвание:\n' + film['name'] +
                      '\n\nОписание:\n' + film['desc'] +
                      '\n\nСписок актёров:\n' + ', '.join(film['actors']) +
                      '\n\nСтоимость:\n' + str(film['cost']) +
                      '\n\nСписок сеансов:\n' + ', '.join(film['time']) +
                      '\n\nОценка:\n' + str(film['rating']) + '\n')
        if not found:
            print('\nДанного фильма нет\n')
            return False
    else:
        print('Нет такого элемента характеристики фильма\n')
        return False
    print('')
    return True


def listOfFilms():  # Список фильмов
    print('Список фильмов:')
    for i in range(len(films)):
        print('\nНазвание:\n' + films[i]['name'] + '\n\nОписание:\n' + films[i]['desc'] + '\n\nСписок актёров:\n' +
              ', '.join(films[i]['actors']) + '\n\nСтоимость:\n' + str(films[i]['cost']) + '\n\nСписок сеансов:\n' +
              ', '.join(films[i]['time']) + '\n\nОценка:\n' + str(films[i]['rating']) + '\n')
    return True


def filterFilms():  # Фильтр фильмов
    filtering = input('По какому критерию вы хотите отфильтровать фильмы:\n'
                      '1.1. Название фильмов по возростанию\n1.2. Название фильмов по убыванию\n'
                      '2.1. Стоимость фильмов по возростанию\n2.2. Стоимость фильмов по убыванию\n'
                      '3.1. Оценка фильмов по возростанию\n3.2. Оценка фильмов по убыванию\n')
    if filtering == '1.1':
        filtered_films = sorted(films, key=itemgetter('name'))
    elif filtering == '1.2':
        filtered_films = sorted(films, key=itemgetter('name'), reverse=True)
    elif filtering == '2.1':
        filtered_films = sorted(films, key=itemgetter('cost'))
    elif filtering == '2.2':
        filtered_films = sorted(films, key=itemgetter('cost'), reverse=True)
    elif filtering == '3.1':
        filtered_films = sorted(films, key=itemgetter('rating'))
    elif filtering == '3.2':
        filtered_films = sorted(films, key=itemgetter('rating'), reverse=True)
    else:
        print('Нет такого элемента характеристики или варианта фильтрации фильма\n')
        return False
    for i in range(len(filtered_films)):
        print('\nНазвание:\n' + filtered_films[i]['name'] +
              '\n\nОписание:\n' + filtered_films[i]['desc'] +
              '\n\nСписок актёров:\n' + ', '.join(filtered_films[i]['actors']) +
              '\n\nСтоимость:\n' + str(filtered_films[i]['cost']) +
              '\n\nСписок сеансов:\n' + ', '.join(filtered_films[i]['time']) +
              '\n\nОценка:\n' + str(filtered_films[i]['rating']) + '\n')
    return True


def middleStat():  # Средний показатель
    middle_films_stat = input('Выберите, по какому элементу характеристики фильмов определить среднее значение:\n'
                              '1. Стоимость фильмов\n2. Оценки фильмов\n')
    if middle_films_stat == '1':
        print('\nСредний показатель по стоимости фильмов равен ' + str(int(statistics.mean([film['cost']
                                                                                           for film in films]))))
    elif middle_films_stat == '2':
        print('\nСредний показатель по оценкам фильмов равен ' + str(round(statistics.mean([film['rating']
                                                                                           for film in films]), 2)))
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
    in_val = input('Наберите следующее, чтобы сделать/посмотреть:\n1. Добавить фильм\n2. Удалить фильм\n'
                   '3. Найти фильм/ы\n4. Список фильмов\n5. Фильтр по информации о фильмах\n'
                   '6. Средний показатель фильмов\nend/конец. Закрыть приложение\n')
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
