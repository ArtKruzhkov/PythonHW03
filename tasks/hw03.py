# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка с нечетными индексами.
# print('How many elements:')
# n = int(input())
# numbers = []
# for i in range(1, n + 1):
#     print('Enter element:')
#     b = int(input())
#     numbers.append(b)
# print(f'List = {numbers}')
# sum = 0
# for i in range (len(numbers)):
#     if i % 2 != 0:
#         print(f'This element({numbers[i]}) is on odd position i = ({i})')
#         sum = sum + numbers[i]
# print(f'Sum for elements on odd positions = {sum}')



# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# print('How many elements:')
# n = int(input())
# numbers = []
# product = 0
# for i in range(1, n + 1):
#     print('Enter element:')
#     b = int(input())
#     numbers.append(b)
# print(f'List = {numbers}')
# if (len(numbers)) % 2 == 0:
#     for i in range (len(numbers) // 2):
#         product = numbers[i] * numbers[(len(numbers)) - 1 - i]
#         print(f'The product for pair is {numbers[i]} * {numbers[(len(numbers)) - 1 - i]} = {product}')
# else:
#     for i in range (len(numbers) // 2 ):
#         product = numbers[i] * numbers[(len(numbers)) - 1 - i]
#         print(f'The product for pair is {numbers[i]} * {numbers[(len(numbers)) - 1 - i]} = {product}')
#     for i in range (len(numbers) // 2 + 1):
#         if i == (len(numbers) // 2 ) and (len(numbers)) % 2 != 0:
#             product = numbers[i] * numbers[i]
#             print(f'The product for mid element = {product}')



# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# print('How many elements:')
# n = int(input())
# list = []
# for i in range(1 , n + 1):
#     b = float(input('Enter number:'))
#     list.append(b)
# print(list)
# new_list = []
# for i in list:                                      # Не работает, но не могу понять почему. Логика у меня такая, из первого списка
#     if list[i] % 1 != 0:                            # берем те элементы, у которых остаток от деления на 1 не равен 0. То есть
#         new_list[i] = list[i] % 1                   # берем все числа у которых есть числа после запятой. В новый массив 
#         round(new_list[i], 2)                       # поэлементно записываем остатки от деления на 1 элементов исходного массива
# print(new_list)                                     # например из массива [1.1, 1.2, 3.1, 5, 10.01] получился бы массив 
# print(max(new_list) - min(new_list))                # [0.1, 0.2, 0.1, 0.01] после чего просто делаем вычитание мин. эл. из макс. эл



# Напишите программу, которая будет преобразовывать десятичное число в двоичное. Без применения встроеных методов (арифметически)
# print('Enter number:')
# a = int(input())
# b = ""
# while a > 0:
#     b = str(a % 2) + b
#     a = a // 2
# print(b)



# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов (Негафибоначчи).
# print('How many elements:')
# a = int(input())
# def Fibo(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return Fibo(n - 1) + Fibo(n - 2)
# fiboList = [0]
# i = 1
# while i < a + 1:
#     fiboList.append(Fibo(i))
#     fiboList.insert(0, Fibo(i) * ((-1) ** (i + 1)))
#     i = i + 1
# print(fiboList)

