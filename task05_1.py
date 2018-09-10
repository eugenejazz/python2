# coding: utf-8
# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала для каждого предприятия. 
# Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести наименования предприятий, 
# чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже среднего.
# Примечание: 4 квартала - это 4 разных прибыли ;-)

company = {}
s = 0

n = int(input("Введите количество предприятий: "))

for i in range(n):
	comp_name = str(input("Введите название предприятия: "))
	comp_profit_1 = int(input("Введите прибыль за 1-й квартал: "))
	comp_profit_2 = int(input("Введите прибыль за 2-й квартал: "))
	comp_profit_3 = int(input("Введите прибыль за 3-й квартал: "))
	comp_profit_4 = int(input("Введите прибыль за 4-й квартал: "))
	comp_profit = comp_profit_1 + comp_profit_2 + comp_profit_3 + comp_profit_4
	company[comp_name] = comp_profit
	s += comp_profit

avrg = s / n

print(f'Средняя прибыль предприятий: {avrg}')
print(f'Предприятия с прибылью выше среднего: ')
for i in company:
    if company[i] > avrg:
        print(i)
print(f'Предприятия с прибылью ниже среднего: ')
for i in company:
    if company[i] < avrg:
        print(i)