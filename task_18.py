# Задача 18: Требуется найти в массиве A[N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# Ввод: 5
# Ввод: 1 2 6 4 9
# Ввод: 8
# -> 9

count=0
print()
n=int(input('Введите кол-во элементов - '))
print()
list=[]
for i in range(1,n+1):
    a=int(input('Введите значение элемента - '))
    list.append(a)
print()
print(list)
print()
x= int(input('Введите искомый элемент - '))

min=list[0]-x
num=list[0]
print()

for i in range(1, n):
        count = n - list[i]
        if count < min:
            min = count
            index = i
            
print(f'к элементу {x} самый близкий элемент {i} равный {list[i]}')