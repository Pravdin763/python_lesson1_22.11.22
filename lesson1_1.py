#  Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

x = int(input('Введите день недели (от 1 до 7): '))

if x in (6, 7):
    print('ДА')
else:
    print('НЕТ')
