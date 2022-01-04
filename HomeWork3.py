#Задача 1

def div(a, b):
    try:
        res = a / b
        return res
    except ZeroDivisionError:
        print("Делить на ноль нельзя")


print(div(10, 0))

#Задача 2

# def personal_data (name, surname, year_of_birth, city, email, phone_number):
#     print(name, surname, year_of_birth, city, email, phone_number)
#
# personal_data(name= input("Введите имя: "), surname=input("Фамилия: "), year_of_birth= input("Год рождения: "), city=input("Город: "), email= input("Email: "), phone_number=input("Номер телефона: ")  )

#Задача 3

# def my_func (num1, num2, num3):
#     sum1 = num1 + num2
#     sum2 = num2 + num3
#     sum3 = num1 + num3
#     if sum1 > sum3 and sum2:
#         return sum1
#     elif sum2 > sum1 and sum3:
#         return sum2
#     elif sum3 > sum2 and sum1:
#         return sum3
# print(my_func(10, 20, 25))

#Задача 4
# 1 вариант
# def my_functwo (numone, numtwo):
#     exp = numone ** numtwo
#     return  exp
# print(my_functwo(10, -3))

# 2 вариант

#Задача 5
#Не смог сделать


#Задача 6

def int_func():
    st = input("Введите строку: ").split()
    for i in st:
        print(i.title())

int_func()


