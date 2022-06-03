```
print(5 + 10)
print(5 - 2)
print(2 * 3)
print(2 ** 3)
print(9 / 2)
print(37 // 3)
print(37 % 3)
```
```
age = 20

print("Befor", age)
i = 1
while i < 27:
    i += 1
    age += 1

print("After", age)
```
```
n = 0
s = 0

while True:
    n = int(input())
    s += n
    if n == 0:
        break

print(s)
```
```
n = int(input())
i = 0

while 2 ** i < n:
    i += 1

print(i - 1)
```
Вводится такая же последовательность.
Нужно вывести среднее арифметическое этой последовательности, ее максимальное и минимальное значения
```
while True:
    n = int(input())
    if n == 0:
        break

print("The end")
```
2. Определить количество парных элементов в завершающей последовательности
числом 0
```
counter = 0

while True:
    n = int(input())
    if n == 0:
        break
    if n % 2 == 0:
        counter += 1

print(counter)
```
В первый день спортсмен пробежал x километров, а затем он каждый день увеличивал пробег на 10% от предыдущего значения. По данному числу y определите номер дня, на который пробег спортсмена составит не менее y километров.
Программа получает на вход действительные числа x и y и должна вывести одно натуральное число.
```
x = float(input('Enter start distance: '))
y = float(input('Enter goal: '))
days = 0

while x <= y:
    print(f'day {days}, distance = {x}')
    x += 0.1 * x
    days += 1

print(x, days)
```
