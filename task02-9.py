# coding: utf-8
# Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.

n = int(input("Введите число или '0' для завершения ввода: "))

sm = 0
nm = 0

while n != 0:
    m = n
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    if s > sm:
        sm = s
        nm = m
    n = int(input("Введите число или '0' для завершения ввода: "))

print(f'Число - {nm}, сумма - {sm}')