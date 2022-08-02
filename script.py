per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
n = int(input('Введите сумму депозита: '))
for i in per_cent:
    per_cent[i] = per_cent[i]*n/100
print(*per_cent.items())
print('Максимальная сумма, которую вы можете заработать — ', max(per_cent.values()))