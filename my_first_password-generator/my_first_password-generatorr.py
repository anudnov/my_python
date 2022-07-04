import random

num_count = int(input('How much numbers: '))
s_let_count = int(input('How much small characters: '))
b_let_count = int(input('How much Uppercase characters: '))
sym_count = int(input('How much symbols: '))

pas = []
lst = [i for i in range(1, 10)]
lst_s = ['@', '#', '$', '%', '!', '&']
s = 'abcdefgh'
lst_let = list(s)
lst_b = list(s.upper())

for i in range(num_count):
    pas.append(random.choice(lst))

for i in range(s_let_count):
    pas.append(random.choice(lst_let))

for i in range(b_let_count):
    pas.append(random.choice(lst_b))

for i in range(sym_count):
    pas.append(random.choice(lst_s))

random.shuffle(pas)
print('Your password is: ', end='')
for i in pas:
    print(i, end='')

