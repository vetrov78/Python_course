#Задачи на циклы и оператор условия------
#----------------------------------------

'''
Задача 1

Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована.
'''
str = '00000000000000000000000000000000'

for i in range(1,6):
    print(i, '. ',str)

'''
Задача 2

Пользователь в цикле вводит 10 цифр. Найти количество введеных пользователем цифр 5.
'''
print('Task_2')

it = 1
num = 0
while (it<11):
    a = input(f'Введите число {it} ')
    if (int(a)==5): num+=1
    it+=1

print(num, '\n')
'''
Задача 3

Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран.
'''
sum = 0
for i in range(1,101):
    sum+=i
print('Task_3')
print(sum, '\n')

'''
Задача 4

Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран.
'''
mult = 1
for i in range(1,11):
    mult*=i
print('Task_4')
print(mult, '\n')

'''
Задача 5

Вывести цифры числа на каждой строчке.
'''
print('Task_5')
integer_number = 2129
while integer_number>0:
    print(integer_number%10)
    integer_number = integer_number//10
print('\n')
'''
Задача 6

Найти сумму цифр числа.
'''
print('Task_6')
integer_number = 23291
sum = 0
while integer_number>0:
    sum+=integer_number%10
    integer_number = integer_number//10
print('Sum is: ', sum)
print('\n')

'''
Задача 7

Найти произведение цифр числа.
'''
print('Task_7')
integer_number = 23210
mult = 1

while integer_number>0:
    mult*=integer_number%10
    integer_number = integer_number//10
print('Mult is: ', mult)
print('\n')
'''
Задача 8

Дать ответ на вопрос: есть ли среди цифр числа 5?
'''
print('Task_8')
integer_number = 2134513
while integer_number>0:
    if integer_number%10 == 5:
        print('Yes')
        break
    integer_number = integer_number//10
else: print('No')
print('\n')

'''
Задача 9

Найти максимальную цифру в числе
'''
print('Task_6')

integer_number = 9232718
print('The number is:', integer_number)

max = 0

while integer_number>0:
    max = integer_number%10 if max < integer_number%10 else max
    integer_number = integer_number//10
print('Max is: ', max)
print('\n')

'''
Задача 10

Найти количество цифр 5 в числе
'''
integer_number = 592375185
print('The number is:', integer_number)

num = 0

while integer_number>0:
    if integer_number%10==5: num+=1
    integer_number = integer_number//10
print('Num is: ', num)
print('\n')