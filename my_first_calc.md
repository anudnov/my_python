```
def plus(a, b):
    return a + b


def minus(a, b):
    return a - b


def dev(a, b):
    return a // b


def mult(a, b):
    return a * b


opper = input('What calculation do you want to do? +, -, //, *: ')
print('Hello to my first calculator')
for i in opper.split(' '):
    if opper == '+':
        x = int(input('Now add you first number: '))
        y = int(input('Now add you secondary number: '))
        my_answer = plus(x, y)
        print('Your answer is: ', my_answer)
    elif opper == '-':
        x1 = int(input('Now add you first number: '))
        y1 = int(input('Now add you secondary number: '))
        my_answer1 = minus(x1, y1)
        print('Your answer is: ', my_answer1)
    elif opper == '//':
        x2 = int(input('Now add you first number: '))
        y2 = int(input('Now add you secondary number: '))
        my_answer2 = dev(x2, y2)
        print('Your answer is: ', my_answer2)
    elif opper == '*':
        x3 = int(input('Now add you first number: '))
        y3 = int(input('Now add you secondary number: '))
        my_answer3 = dev(x3, y3)
        print('Your answer is: ', my_answer3)

print('--------Calculation was finish------')
```
