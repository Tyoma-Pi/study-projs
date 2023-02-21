    # import numpy as np
# import matplotlib.pyplot as plt
# import re
# from selenium import webdriver
# from selenium.common.exceptions import NoSuchElementException
# from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
from bs4 import BeautifulSoup
import requests as rq


def fullPrint(x):
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', 2000)
    pd.set_option('display.float_format', '{:20,.2f}'.format)
    pd.set_option('display.max_colwidth', None)
    print(x)
    pd.reset_option('display.max_rows')
    pd.reset_option('display.max_columns')
    pd.reset_option('display.width')
    pd.reset_option('display.float_format')
    pd.reset_option('display.max_colwidth')


fp_tables = pd.read_html("https://soccer365.ru/competitions/13/https://soccer365.ru/competitions/13/")
fp_tables[0].rename({'Unnamed: 0': '№', 'Unnamed: 1': 'Команда', 'И': 'Игры', 'В': 'Выиграно', 'Н': 'Ничьи',
                     'П': 'Проиграно', 'З': 'Забито', 'П.1': 'Пропущено', '+/-': 'Разница', 'О': 'Общее'},
                    axis=1, inplace=True)
fp_tables[1].rename({'Unnamed: 1': 'Голы', 'Unnamed: 2': 'Пенальти', 'Unnamed: 3': 'Матчи'}, axis=1, inplace=True)
fp_tables[2].rename({'Unnamed: 1': 'Пасы', 'Unnamed: 2': 'Матчи'}, axis=1, inplace=True)
fp_tables[3].rename({'Unnamed: 1': 'Fair play', 'Unnamed: 2': 'ЖК', 'Unnamed: 3': '2ЖК', 'Unnamed: 4': 'Штрафные',
                     'Unnamed: 5': 'Матчи'}, axis=1, inplace=True)
fb = fp_tables[0]

resp_text = rq.get("https://soccer365.ru/competitions/13/https://soccer365.ru/competitions/13/").text
soup_images = BeautifulSoup(resp_text, 'lxml').find_all('img', {'class': 'has-tip'})

SI = []
for i in soup_images:
    SI.append(i['title'])

SI1 = pd.Series(SI[:12])
fp_tables[1].insert(0, 'Команда', SI1)
SI2 = pd.Series(SI[12:24])
fp_tables[2].insert(0, 'Команда', SI2)
SI3 = pd.Series(SI[24:])
fp_tables[3].insert(0, 'Команда', SI3)

df = pd.DataFrame(columns=['Команда', 'ФИ игрока', 'Роль', 'Матчи',
                           'Голы', 'Пенальти', 'Пасы',
                           'Fair play', 'ЖК', '2ЖК', 'Штрафные'])

df['Команда'] = pd.concat([fp_tables[1]['Команда'], fp_tables[2]['Команда'], fp_tables[3]['Команда']],
                          ignore_index=True)
df['ФИ игрока'] = pd.concat([fp_tables[1]['Бомбардиры'], fp_tables[2]['Ассистенты'], fp_tables[3]['Штрафники']],
                            ignore_index=True)
df['Матчи'] = pd.concat([fp_tables[1]['Матчи'], fp_tables[2]['Матчи'], fp_tables[3]['Матчи']],
                        ignore_index=True)

df.drop_duplicates(inplace=True)
df = df.reset_index(drop=True)

df['Роль'] = ''
df2 = df.loc[:, ['Роль', 'Пенальти', 'Голы', 'Пасы', 'Fair play', 'ЖК', '2ЖК', 'Штрафные']]
for i in range(df['ФИ игрока'].count()):
    for j in range(fp_tables[1]['Бомбардиры'].count()):
        if df['ФИ игрока'][i] in fp_tables[1]['Бомбардиры'][j]:
            df2['Роль'][i] += ', Бомбардир'
            df2['Голы'][i] = fp_tables[1]['Голы'][j]
            df2['Пенальти'][i] = fp_tables[1]['Пенальти'][j]
    for j in range(fp_tables[2]['Ассистенты'].count()):
        if df['ФИ игрока'][i] in fp_tables[2]['Ассистенты'][j]:
            df2['Роль'][i] += ', Ассистент'
            df2['Пасы'][i] = fp_tables[2]['Пасы'][j]
    for j in range(fp_tables[3]['Штрафники'].count()):
        if df['ФИ игрока'][i] in fp_tables[3]['Штрафники'][j]:
            df2['Роль'][i] += ', Штрафник'
            df2['Fair play'][i] = fp_tables[3]['Fair play'][j]
            df2['ЖК'][i] = fp_tables[3]['ЖК'][j]
            df2['2ЖК'][i] = fp_tables[3]['2ЖК'][j]
            df2['Штрафные'][i] = fp_tables[3]['Штрафные'][j]

df['Роль'] = df2['Роль']
df['Роль'].replace(r'^, ', '', regex=True, inplace=True)
df['Пенальти'] = df2['Пенальти']
df['Голы'] = df2['Голы']
df['Пасы'] = df2['Пасы']
df['Fair play'] = df2['Fair play']
df['ЖК'] = df2['ЖК']
df['2ЖК'] = df2['2ЖК']
df['Штрафные'] = df2['Штрафные']
del df2

print('Данные по командам:')
fullPrint(fb)
print('\nДанные по футболистам:')
fullPrint(df)
print('\n1. Топ-3 команд по числу забитых голов:')
fullPrint(fb.loc[:2, ['Команда', 'Забито']])
print('\n2. Топ-3 команд по числу жёлтых карточек:')
yc = df.loc[:, ['Команда', 'ЖК']]
yc['ЖК'] = pd.to_numeric(yc['ЖК'])
fullPrint(yc.nlargest(3, 'ЖК'))
print('\n3. Игроки, участвовавшие не во всех играх команды (по максимуму матчей игроков):')
df['ММИ'] = df.groupby(['Команда'])['Матчи'].transform(max)
fullPrint(df.loc[:, ['Команда', 'ФИ игрока', 'Матчи', 'ММИ']].where(df['Матчи'] != df['ММИ']).dropna())
del df['ММИ']
print('\n4. Доля пенальти по отношению к числу голов у каждой команды:')
df['СП'] = df.groupby(['Команда'])['Пенальти'].transform(sum)
df['СГ'] = df.groupby(['Команда'])['Голы'].transform(sum)
for i in range(df['Команда'].count()):
    df.loc[i, 'ДПкГ (%)'] = df.loc[i, 'СП'] / df.loc[i, 'СГ'] if df.loc[i, 'СГ'] != 0 else 0
df['ДПкГ (%)'] = df['ДПкГ (%)'] * 100
fullPrint(df.loc[:, ['Команда', 'Пенальти', 'Голы', 'СП', 'СГ', 'ДПкГ (%)']].dropna(subset='Голы'))
del df['СП']
del df['СГ']
del df['ДПкГ (%)']
print('\n5. Корреляция числа голов с количеством очков команды:', round(fb['Забито'].corr(fb['Общее']), 2))
# print(pd.concat([fp_tables[1], fp_tables[2]], axis=1))  .merge(fp_tables[3])
# fp_tables[0].loc[int]['col']
