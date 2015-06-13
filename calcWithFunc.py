# -*- coding utf-8 -*-
def menu():
    print("""
	      ВЫбери:+\
		  1 - сложить+\
		  2 - умножить+\
		  3 - отнять+\
		  4 - поделить+\
		  5 - выйти из калькулятора+\
		  """),
    op = int(input())
    return op
   
def add(a,b):
    print(a, '+', b, '=', a + b)
def subt(a,b):
    print(a, '-', b, '=', a - b)
def multiply(a,b):
    print(a, '*', b, '=', a * b)
def divide(a,b):
    print(a, '/', b, '=', a / b)

stop = True
while stop == True:
    print('Привет, я калькулятор. Введите первое число:'),
    a = int(input())
    print('Введите второе число:'),
    b = int(input())
    choice = menu()
    if choice == 4 and b == 0:
        print('На ноль делить нельзя!')
    else:
        if choice == 1:
            add(a,b)
        elif choice == 2:
            multiply(a,b)
        elif choice == 3:
            subt(a,b)
        elif choice == 4:
            divide(a,b)
        elif choice == 5:
            stop = False
        
