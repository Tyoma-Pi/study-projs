import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
# G - вратарь (goalkeeper), D - защитник (defender), F - нападающий (fighter)


def fullPrint(x):
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', 5000)
    pd.set_option('display.float_format', '{:20,.2f}'.format)
    pd.set_option('display.max_colwidth', None)
    print(x)
    pd.reset_option('display.max_rows')
    pd.reset_option('display.max_columns')
    pd.reset_option('display.width')
    pd.reset_option('display.float_format')
    pd.reset_option('display.max_colwidth')


my_csv = pd.read_csv('hockey_players.csv', low_memory=False, encoding='iso8859-1')
df_year_times = my_csv.groupby(['name'])['year'].count()
df_heights_G = my_csv[my_csv['position'] == 'G'].groupby(['year'], as_index=False)['height'].mean()
df_heights_D = my_csv[my_csv['position'] == 'D'].groupby(['year'], as_index=False)['height'].mean()
df_heights_F = my_csv[my_csv['position'] == 'F'].groupby(['year'], as_index=False)['height'].mean()
df_hockeyist_months = pd.DatetimeIndex(my_csv['birth']).month.value_counts().sort_index()
DFHM_counts = list(df_hockeyist_months)
DFHM_nums = [x for x in range(1, 13)]
hockeyists_roles = my_csv['position'].value_counts()

fullPrint(hockeyists_roles)

fig, ([dia1, dia2], [dia3, dia4]) = plt.subplots(nrows=2, ncols=2)
fig.canvas.manager.set_window_title('Данные')
fig.suptitle('Хоккейная статистика ЧМ: 2001 — 2016')
fig.tight_layout()

dia1.set_title('Распределение хоккеистов по количеству участий в ЧМ')
dia1.set_xlabel('Количество ЧМ')
dia1.set_ylabel('Доля')
dia1.set_xticks(np.arange(1, 16))
dia1.hist(df_year_times, bins=range(1, 16), range=(1, 15), density=True, color='red', edgecolor='black')

dia2.set_title('Тренды изменения роста игрока для каждой позии')
dia2.set_xlabel('Год ЧМ')
dia2.set_ylabel('Рост (см.)')
year_G = df_heights_G['year']
height_G = df_heights_G['height']
z_G = np.polyfit(year_G, height_G, 1)
p_G = np.poly1d(z_G)
year_D = df_heights_D['year']
height_D = df_heights_D['height']
z_D = np.polyfit(year_D, height_D, 1)
p_D = np.poly1d(z_D)
year_F = df_heights_F['year']
height_F = df_heights_F['height']
z_F = np.polyfit(year_F, height_F, 1)
p_F = np.poly1d(z_F)
dia2.plot(year_G, p_G(year_G), '--', color='blue')
dia2.plot(year_D, p_D(year_D), '--', color='orange')
dia2.plot(year_F, p_F(year_F), '--', color='green')
dia2.legend(['Вратарь', 'Защитник', 'Нападающий'], loc='lower right')

dia3.set_title('Распределение хоккеистов по месяцам рождения')
dia3.set_ylabel('Чел.')
dia3.bar(DFHM_nums, DFHM_counts, tick_label=['янв', 'фев', 'мар', 'апр', 'май', 'июн', 'июл', 'авг', 'сен', 'окт', 'ноя', 'дек'])

dia4.set_title('Распределение позиций между хоккеистами')
dia4.pie(hockeyists_roles, labels=['Нападающий', 'Защитник', 'Вратарь'], autopct='%.1f%%')

plt.show()
