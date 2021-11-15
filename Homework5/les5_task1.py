"""
1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль
за четыре квартала для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий)
и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.
"""

from collections import Counter
from collections import OrderedDict

companies = Counter()
num_company = int(input("Введите количество предприятий :"))
for i in range(num_company):
    name = input(f"Введите наименование компании N{i + 1} :")
    companies[name] = 0
    for q in range(4):
        q_summa = float(input(f"Введите прибыль для {name} за Q{q + 1} :"))
        companies[name] += q_summa

average_income = sum(companies.values()) / num_company
companies_lead = OrderedDict(sorted(companies.items(), key=lambda x: x[1]))
print("Средняя прибыль: ", average_income)
print("Предприятия, чья прибыль ниже среднего :", [x for x, y in companies_lead.items() if y < average_income])
print("Предприятия, чья прибыль выше среднего :", [x for x, y in companies_lead.items() if y > average_income])
