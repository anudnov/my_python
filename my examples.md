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

    w1 = 1000
    w2 = 1200
    w3 = 7800
    w4 = 12000
    w5 = 2100
    w6 = 3500
    salary_lst = [1000, 1200, 7800, 12000, 2100, 3500]

    for i in salary_lst:
        print(i, end=' ')

    print(w1, w2, w3, w4, w5, w6)

```
for i in range(1, 11):
         print(i)
```
```
s = 0

for i in range(1, 7):
    n = int(input(f'Enter number {i}: '))
    s += n

print(s/6)
```
```
n = int(input("How many digits u want to enter: "))  # вводится количесвто чисел
counter = 0

for i in range(n):  # вводится ровно n чисел
    x = int(input())
    if x == 0:
        counter += 1

print(counter)
```
```
import random

lst = []
lst.append(random.randint(1, 10))
lst.append(random.randint(1, 10))
lst.append(random.randint(1, 10))
lst.append(random.randint(1, 10))
lst.append(random.randint(1, 10))
lst.append(random.randint(1, 10))
lst.append(random.randint(1, 10))
lst.append(random.randint(1, 10))
lst.append(random.randint(1, 10))
lst.append(random.randint(1, 10))
print(lst)
```
```
import random

lst = [3, 10, 4, 10, 1, 8, 10, 9, 3, 2]
print(lst)
print(lst[-1::-1])
```
```
remove min element from list

lst = [3, 10, 4, 10, 1, 8, 10, 9, 3, 2]
print(lst)
min_el = min(lst)
lst.remove(min_el)
print(lst)
```
```
lst = ['химия', 'физика', 'биология', 'астрономия', 'информатика', 'общество и право', 'мировая художественная литература']
print(lst)

n = int(input('Сколько предметов тебе не нравится? '))
for i in range(n):
    subject = str(input(f'Введи {i + 1} предмет, который тебе не нравиться: '))
    lst.remove(subject)

print(lst)
```
```
nums = []

for i in range(1, 4):
    if i == 3:
        q = input("Do you w to save third value (yes/no)? ")
        if q == 'no':
            break

    n = int(input('Please insert number: '))
    nums.append(n)
    print("Номер ввода: ", i)

print(nums)
```
```
nums = []

for i in range(1, 4):
    if i == 3:
        q = input("Do you w to save third value (yes/no)? ")
        if q == 'no':
            break

    n = int(input('Please insert number: '))
    nums.append(n)
    print("Номер ввода: ", i)

print(nums)
```
```
lst = [1, 23, 20, 38, 98, 20, 17, 20]
print(lst)

print('If y see number 20, I will change it to 200')

for i in range(len(lst)):
    if lst[i] == 20:
        lst[i] = 200

print(lst)
```
```
str_list = [x for x in str_list if x != '']
```
2. Необходимо удалить пустые строки из списка строк.
```
string_lst = ['', 'u', 'ere', '', 'hello', 'no']
print(string_lst)

string_lst = [i for i in string_lst if i]

print(string_lst)a
```
```

```




