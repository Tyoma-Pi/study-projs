# ввели любую строку, кинули в нижний регистр !!! ЕСТЬ !!!
# проверили, записано ли ФИО в три слова и подходит ли каждое слово отдельно под словарь !!! НЕТ !!!
# транслитеровали и вывели с первой заглавной буквы в каждом слове !!! НЕТ !!!

def translit():
    # noinspection PyBroadException
    try:
        in_str = str(input('Введите ФИО: ')).lower()
        tr_alph = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'e', 'ж': 'zh', 'з': 'z',
                   'и': 'i', 'й': 'i', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r',
                   'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'sch',
                   'ъ': 'ie', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'iu', 'я': 'ia', ' ': ' '}
        if len(in_str.split()) == 3\
                and all(letter in tr_alph for letter in in_str):
            for key in tr_alph.keys():
                in_str = in_str.replace(key, tr_alph[key])
            in_str = in_str.title()
        else:
            raise Exception
        return in_str
    except Exception:
        out_error = 'Введите ФИО правильно'
        return out_error
# иванов иван иванович


print(translit())
