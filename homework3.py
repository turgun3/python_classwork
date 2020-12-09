while True:
    x = float(input("x="))
    y = float(input("y="))
    s = input("Какое дейсвие выполнить (+,-,*,/): ")
    if s == '0':
        break
    if s in ('+', '-', '*', '/'):       
        if s == '+':
            print("%.2f" % (x+y))
        elif s == '-':
            print("%.2f" % (x-y))
        elif s == '*':
            print("%.2f" % (x*y))
        elif s == '/':
            if y != 0:
                print("%.2f" % (x/y))
            else:
                print("Деление на ноль!")
    else:
        print("Ошибка, проверьте ввод")