import numpy as np
import pandas as pd

df = pd.read_csv("https://pycourse.s3.amazonaws.com/bike-sharing.csv")
'''a) Qual o tamanho desse dataset? #17379 x 17
# R: 17379 x 17 '''

# print(df.info())

'''b) Qual a média da coluna windspeed?
#R: 0.1900976'''

value = df['windspeed'].mean()
#print(value)

'''c) Qual a média da coluna temp?
# R: 0.4969871'''

value2 = df['temp'].mean()
#print(value2)

'''d. Quantos registros existem para o ano de 2011?
# R: 8645'''

# reg_2011 = df.loc[df['year'] == 0].value_counts()
# print(reg_2011)

'''e. Quantos registros existem para o ano de 2012?
# R: 8734'''

# print(df.year.value_counts())

######################################################
'''#f. Quantas locações de bicicletas foram efetuadas em 2011?
# R: #1243103'''

'''À partir do valor do year(0 ou 1) devo pegar o valor do total_count correspondente
e somá-lo para depois retornar.
'''

bike_2011 = df.loc[df['year'] == 0]['total_count'].sum()
#print(bike_2011)


'''g. Quantas locações de bicicletas foram efetuadas em 2012?'''
# R: 2049576

bike_2012 = df.loc[df['year'] == 1]['total_count'].sum()
#print(bike_2012)

#################################################################
'''h. Qual estação do ano contém a maior média de locações de bicicletas?
# R: Verão/3

#i. Qual estação do ano contém a menor média de locações de bicicletas?

# R: Inverno/1'''

'''estação do ano (1: inverno, 2: primevera, 3: verão, 4: outono).'''

# RESOLUÇÃO
# seasons = ("inverno", "primavera", "verão", "outono")
# for i in range(0, 4):
#     season_mean = df.loc[df['season'] == i + 1]['total_count'].mean()
#     print(f"{seasons[i]}: {season_mean:.2f}")


################################################################
'''j. Qual horário do dia contém a maior média de locações de bicicletas?
# R: 16 ou 17

# k. Qual horário do dia contém a menor média de locações de bicicletas?
#R: 3 ou 4'''

# min = 100
# max = 0
# for i in range(24):
#     y = df.loc[df['hour'] == i]['total_count'].mean()
#     if y > max:
#         max = y
#     if y < min:
#         min = y
#     print(f"{i} {y:.2f}")
# print(f"Minimo: {min:.2f} Máximo: {max:.2f}")


#################################################################################
''' QUESTÃO 12-- l. Que dia da semana contém a maior média de locações de bicicletas?
#R: 4/Quinta

# QUESTÃO 13-- m. Que dia da semana contém a menor média de locações de bicicletas?
#R: 0/Domingo'''


#BASEADO NO DIA DA SEMANA, FAZER A MÉDIA DE LOCAÇÃO DE BICICLETAS DO RESPECTIVO DIA
# for i in range(7):
#     we = df.loc[df['weekday'] == i]['total_count'].mean()
#     print(f"{i} {we:.2f}")

###################################################################################


'''14-- n. Às quartas-feiras (weekday = 3), qual o horário do dia contém a maior média de locações de bicicletas?
R: 17h
15-- o. Aos sábados (weekday = 6), qual o horário do dia contém a maior média de locações de bicicletas?
R: 13h'''

# Em determinado dia (quarta-feira), capturar todos os horários(0 à 23) e verificar qual dentre possui a maior média  '''

# max = 0
# for i in range(0, 24):
#     global media, minimo
#     media_wednesday = df.loc[df['weekday'] == 6]
#     hour_loc = media_wednesday.loc[df['hour'] == i]
#     media = hour_loc['total_count'].mean()
#     if media > max:
#         max = media
#         i_max = i
#     print(f"{i} {media:.2f}")



