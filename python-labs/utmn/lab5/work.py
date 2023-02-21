import numpy as np
import pandas as pd
# pd.options.display.width = None
# pd.options.display.max_columns = None
# pd.set_option('display.max_rows', 3000)
# pd.set_option('display.max_columns', 3000)

# 1. Число детей (все пациенты из источника – женщины не моложе 21 года).
#   (Kids)
# 2. Концентрация глюкозы в плазме через 2 часа после введения в пероральном глюкозотолерантном тесте.
#   (GCP - Glucose Concentration in Plasma)
# 3. Диастолическое артериальное давление (мм рт. ст.).
#   (DAT - Diastolic Arterial Tension)
# 4. Толщина кожной складки в районе трицепса (мм).
#   (TST - Triceps Skinfold Thickness)
# 5. Концентрация инсулина в сыворотке крови (мкЕд/мл).
#   (ICBS - Insulin Concentration in Blood Serum)
# 6. Индекс массы тела (вес в кг/(рост в м)2).
#   (BWI - Body-Weight Index)
# 7. Функция, описывающая генетическую предрасположенность к диабету (diabetes pedegree).
#   (GPF - Genetic Predispotion Function)
# 8. Возраст (годы).
#   (Years)
# 9. Метка 1 или 0: результат диагностики диабета (диагностирован или нет).
#   (Result)

colnames = ['Kids', 'GCP', 'DAT', 'TST', 'ICBS', 'BWI', 'GPF', 'Years', 'Result']
data = pd.read_csv('prima-indians-diabetes.csv', names=colnames, header=None)

print('Входные данные:\n', data, '\n')

dc = data.corr()
np.fill_diagonal(dc.values, 0)

print('1. Максимальный возраст людей с установленным диабетом:', data['Years'].where(data['Result'] == 1).max(),
      '\nСредний возраст людей с установленным диабетом:', np.floor(data['Years'].where(data['Result'] == 1).mean()),
      '\n\n2. Параметры максимальной корреляции между собой:')
print(pd.DataFrame({'Kids': dc.eq(dc.max().max())['Kids']}))
print(round(dc.max().max(), 2))
print('\n3. Доля бездетных среди пациентов с неустановленным диабетом:',
      str(data['Result'].where(data['Result'] == 0).where(data['Kids'] < 1).count()/data['Result']
      .where(data['Result'] == 0).count() * 100) + '%',
      '\n\n4. Максимальная концентрация глюкозы у пациентов старше 50 лет:',
      data['GCP'].where(data['Years'] > 50).max(),
      '\n\n5. Средний возраст пациентов с диастолическим давлением выше 80:',
      round(data['Years'].where(data['DAT'] > 80).mean(), 2),
      '\n\n6. Список пациентов старше 60 с уровнем инсулина выше среднего, отсортированные по возрасту по возрастанию:')
print(data.where(data['Years'] > 60).where(data['ICBS'] > data['ICBS'].mean()).sort_values('Years').dropna())
print('\n7.	Список записей с нулевыми значениями хотя бы одного параметра (без первого и последнего столбцов):')
# print(data[data.where(data['Kids'] != 0).where(data['Result'] != 0).any(axis=1)])
print(data.loc[(data['GCP'] == 0) | (data['DAT'] == 0) | (data['TST'] == 0) | (data['ICBS'] == 0) | (data['BWI'] == 0)
               | (data['GPF'] == 0) | (data['Years'] == 0)])
# print(data[data.where(data['GCP'] == 0).where(data['DAT'] == 0).where(data['TST'] == 0).where(data['ICBS'] == 0)
#       .where(data['BWI'] == 0).where(data['GPF'] == 0).where(data['Years'] == 0).all(axis=1)])
