def apothecary():
    # noinspection PyBroadException
    try:
        count = int(input('К-во витаминок: '))
        if count < 1:
            raise Exception

        price = round(float(input('Стоимость: ')), 2)
        if price < 0.01:
            raise Exception

        social_card = str(input('Есть ли у вас соц. карта? '))
        if social_card not in {'да', 'нет', 'yes', 'no'}:
            raise Exception

        for_printing = '\n# Чек:\n\n'
        summary = count * price

        if count in range(5, 9):
            for_printing += '# Вам положена скидка в 10%!\n\n'
            summary = round(summary * 0.9, 2)
        elif count > 9:
            for_printing += '# Вам положена скидка — каждая 10-я витаминка бесплатно!\n\n'
            summary = (count - count // 10) * price

        if social_card in {'да', 'yes'}:
            for_printing += '# Социальная карта: имеется\n\n'
            summary = int(summary * 0.9)
        else:
            for_printing += '# Социальная карта: не имеется\n\n'

        for_printing += '# Сумма покупки: ' + str(count * price) + ' руб.\n\n'
        for_printing += '# Скидка: ' + str(round(count * price - summary, 2)) + ' руб.\n\n'
        for_printing += '# Итого: ' + str(summary) + ' руб.\n\n'
        
        return for_printing
    except Exception:
        error = 'Введите верные данные'
        return error


print(apothecary())
