import re


def t9():
    nls = {'2': ["а", 'б', 'в', 'г'],
           '3': ['д', 'е', 'ё', 'ж', 'з'],
           '4': ['и', 'й', 'к', 'л'],
           '5': ['м', 'н', 'о', 'п'],
           '6': ['р', 'с', 'т', 'у'],
           '7': ['ф', 'х', 'ц', 'ч'],
           '8': ['ш', 'щ', 'ъ', 'ы'],
           '9': ['ь', 'э', 'ю', 'я']}
    in_str = input('Набор слов: ')
    in_int = input('Комбинация чисел: ')
    matched_words = str()

    if re.match(r'^[а-яё\s]+$', in_str, re.I):
        in_str = in_str.split()
    else:
        raise Exception('Введённый текст частично или полностью\nне является кириллицей, разделённой пробелами')

    for word in in_str:
        if len(word) >= len(in_int)\
                and all(word[i].lower() in nls[j] for i, j in enumerate(in_int)):
            matched_words += word + ' '
    return matched_words


print(t9())
