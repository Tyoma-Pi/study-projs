import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import datetime as dt

data = pd.read_csv('hockey_players.csv', encoding="ISO-8859-1", header = 0) #чтение csv-шника
data1 = data.copy() #копируем, имея 2 переменные будет проще работать
data1.drop_duplicates(subset=['name'], keep='first', inplace=True) #удаление дубликатов в столбце "name" (кроме первого) и вернуть копию



matplotlib.rc("font", family="Calibri") #задем шрифт
fig, ([ax1, ax2], [ax3, ax4]) = plt.subplots(ncols=2, nrows=2, figsize=(10,10)) #характеристики всего изображения
fig.tight_layout(h_pad=7)
plt.subplots_adjust(top=0.85)
fig.canvas.manager.set_window_title("Визуализация данных") #имя окошка
fig.suptitle("Хоккейная статистика ЧМ: (2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2014, 2015, 2016)", fontsize=16) #заголовок окошка

x1=data['name'].value_counts()  #сортировка по к-ву вхождений

#groupby для сбори информации только по росту и году игр
x21=data[data['position']=='G'].groupby('year')['height'].mean() #вратари
x22=data[data['position']=='D'].groupby('year')['height'].mean() #защитники
x23=data[data['position']=='F'].groupby('year')['height'].mean() #нападающие
xx = pd.DataFrame() #создаем пустой многомерный массив с метками для строк и столбцов
xx['height'] = x21.copy() #копируем значение роста
xx['year'] = x21.index #для индексa указываем год
xx2 = pd.DataFrame() #создаем пустой многомерный массив с метками для строк и столбцов
xx2['height'] = x22.copy() #копируем значение роста
xx2['year'] = x22.index #для индексa указываем год
xx3 = pd.DataFrame() #создаем пустой многомерный массив с метками для строк и столбцов
xx3['height'] = x23.copy() #копируем значение роста
xx3['year'] = x23.index #для индексa указываем год

data1["month"] = pd.DatetimeIndex(data1['birth']).month.sort_values()#берет месяц и конвентирует в дату
x3=data1.value_counts('month').sort_index() #сортировка относительно месяца

#размеры столбцов для 3-его графика
size = [y for y in x3]
nums = [x + 1 for x in range(len(size))]

x4 = data['position'].value_counts() #сортировка по к-ву вхождений

#1 ГРАФИК
ax1.set_title(u'Распределение хоккеистов по количеству участий в ЧМ', fontsize=16) #заголовок и размер
ax1.set_xlabel("Количество ЧМ", fontsize=14) # заголовок по x
ax1.set_ylabel("Доля", fontsize=14) # заголовок по y
ax1.hist(x1, color='r', edgecolor='black') #рисуем гистограмму
ax1.set_yticks(ticks = range(500,2501, 500), labels = ['0.1', '0.2', '0.3', '0.4', '0.5'], fontsize=14) #подпись по y
#ax1..tick_params(ticks, fontsize=14) axis = 'both'

#2 ГРАФИК
ax2.set_title(u'Тренды изменения роста игрока для каждой позиции', fontsize=16) #заголовок и размер
ax2.set_xlabel("Год ЧМ", fontsize=14) # заголовок по x
ax2.set_ylabel("Рост (см.)", fontsize=14) # заголовок по y


#вычисления делаюие из кривых линий- прямые
z1 = np.polyfit(xx['year'], xx['height'], 1)
p1 = np.poly1d(z1)
z2 = np.polyfit(xx2['year'], xx2['height'], 1)
p2 = np.poly1d(z2)
z3 = np.polyfit(xx3['year'], xx3['height'], 1)
p3 = np.poly1d(z3)


ax2.plot(xx['year'], p1(xx['year']), linestyle='dashed') #рисует одну линию
ax2.plot(xx2['year'], p2(xx2['year']), linestyle='dashed') #рисует другую линию
ax2.plot(xx3['year'], p3(xx3['year']), linestyle='dashed') #рисует третью линию
ax2.legend(['Вратарь', 'Защитник', 'Нападающий'], fontsize=14) #пояснение что к чему относится(соттветсвенно)
ax2.tick_params(axis = 'both', labelsize = 14) # немножко меняем метки по обеим осям



#3
ax3.set_title(u'Распределение хоккеистов по месяцам рождения', fontsize=16) #заголовок и размер
ax3.set_ylabel("Чел", fontsize=14) # заголовок по y
ax3.bar(nums, size)#размер столбцов
ax3.set_xticks(ticks = range(1,13) ,labels = ['Янв', 'Фев', 'Мар', 'Апр', 'Май', 'Июн', 'Июл', 'Авг', 'Сен', 'Окт', 'Ноя', 'Дек']) #подпись по оси x
ax3.tick_params(axis = 'both', labelsize = 14) # немножко меняем метки по обеим осям

#4
ax4.set_title(u'Распределение позиций междк хоккеистами', fontsize=16) #заголовок и размер
ax4.pie(x4, autopct='%1.1f%%', labels=['Нападающий', 'Защитник', 'Вратарь'], textprops={'fontsize': 14})
#рисуем круговую диаграмму
# autopct добавляет в центр каждой части текст с соответствующим значением. (%)
# autopct='%1.1f%%' заклинание-формат вывода числа-округление до десятых

#plt.xticks(fontsize = 40)
plt.savefig("my_image.png") #сохраняем магию
plt.show() #показать магию





