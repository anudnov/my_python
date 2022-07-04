import tkinter as tk
import random



def display_password():
    password=gen_my_password()
    print(password)
    pole.delete(0, tk.END)
    pole.insert(0, password)



def gen_my_password():
    numbers_count = numbers_input.get()
    small_letters_count = small_letters_input.get()
    big_letters_count = big_letters_input.get()
    symbols_count = symbols_input.get()
    pas = []
    lst = [i for i in range(1, 10)]
    lst_s = ['@', '#', '$', '%', '!', '&']
    s = 'abcdefgh'
    lst_let = list(s)
    lst_b = list(s.upper())

    for i in range(int(numbers_count)):
        pas.append(random.choice(lst))

    for i in range(int(small_letters_count)):
        pas.append(random.choice(lst_let))

    for i in range(int(big_letters_count)):
        pas.append(random.choice(lst_b))

    for i in range(int(symbols_count)):
        pas.append(random.choice(lst_s))

    random.shuffle(pas)
    prol = ''
    for i in pas:
        prol += str(i)
    return prol


root = tk.Tk()
root.title('password generator')
root.geometry('400x300+540+200')

greetings = tk.Label(text='Enter params for password (with coma)\n'
                          'num count, s_letter, b_letter, symb_counnt', bg='yellow', font=30)
greetings.pack(fill=tk.X)

pole = tk.Entry(bg='gray', fg='blue', width=50, font=30)
pole.pack()

gen = tk.Button(width=20, text='Gen password', command=display_password)
gen.pack()

big_letters=tk.Label(text='Big Letters:')
big_letters.place(x=10, y=150)
big_letters_input=tk.Spinbox(width=5, from_=0, to=100)
big_letters_input.place(x=100, y=150)

small_letters=tk.Label(text='Small Letters:')
small_letters.place(x=10, y=180)
small_letters_input=tk.Spinbox(width=5, from_=0, to=100)
small_letters_input.place(x=100, y=180)

numbers=tk.Label(text='Numbers:')
numbers.place(x=10, y=210)
numbers_input=tk.Spinbox(width=5, from_=0, to=100)
numbers_input.place(x=100, y=210)

symbols=tk.Label(text='Symbols:')
symbols.place(x=10, y=240)
symbols_input=tk.Spinbox(width=5, from_=0, to=100)
symbols_input.place(x=100, y=240)

exit_end = tk.Button(width=20, text='END')
exit_end.place(x=10, y=270)
exit_end.config(command=root.destroy)


root.mainloop()
