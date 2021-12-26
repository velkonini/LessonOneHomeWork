#Домашнее задание к 1 уроку
#Задача 1
#name = input("Введите имя: ")
#age = int(input("Введите свой возраст: "))
#weight  = float(input("Введите свой вес :) "))

#print(name, age, weight)

#Задача 2
# time = int(input("Веедите время в секундах: "))
# hours = time // 3600
# if hours > 0:
#     minutes = (time - hours * 3600) // 60
#     secs = (time % 60) % 60
#     print(str(time) + " это " + str(hours) + " часов " + str(minutes) + " минут " + str(secs) + " секунд")
# else:
#     minutes = time // 60
#     secs = time % 60
#     print(str(time) + " это " + str(minutes) + " минут " + str(secs) + " секунд")

#Задача 3
# number = int(input("Введите число: "))
# print(number + int(str(number) + str(number)) + int(str(number) + str(number) + str(number)))

#Задача 4

#Задача 5
costs = int(input("Введите издержки компании в этом месяце: "))
proceeds = int(input("Введите выручку компании в этом месяце: "))
if proceeds > costs:
    print("Молодцы, наша фирма приносит прибыль")
    profitability = proceeds / costs
    print("Рентабильность: " + str(profitability))
    employees = int(input("Введите количество сотрудников: "))
    profit = proceeds - costs
    profit_for_employee = profit / employees
    print("Каждому сотруднику полагается " + str(profit_for_employee) + " от общей суммы прибыли")
else:
    print("Надо лучше работать, наша компания не приносит прибыль")

