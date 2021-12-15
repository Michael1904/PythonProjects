from math import sqrt
import numpy as np
def nthroot(a,n):
    return np.power(a,(1/c))
print('''Enter 1 for english version/wpisz 1 dla angielskiej wersji
Enter 2 for polish version/wpisz 2 dla polskiej wersji''')
p = int(input("[Number/Cyfra]: "))
if p < 0 or p > 2:
    while p < 0:
        p = int(input("Enter correct number/Wpisz poprawną liczbę"))
    while p > 2:
        p = int(input("Enter correct number/Wpisz poprawną liczbę"))
elif p == 1:
    print("Calculator")
    print('''Enter 1 if you want the simple calculator
    Enter 2 if you want scientific calculator''')
    x = int(input("Awaiting choice... "))
    if x < 0 or x > 2:
        while x < 0:
            x = int(input("Enter correct number"))
        while x > 2:
            x = int(input("Enter correct number"))
    elif x == 1:
        print("Simple Calculator: ")
        a = int(input("FirstNumber: "))
        print('''+ is for plusing
    - is for substracting
    * is for multiplying
    / is for dividing''')
        b = str(input("What to do: "))
        while b != "+" or b != "-" or b != "*" or b != "/":
            if b == "+" or b == "-" or b == "*" or b == "/":
                break
            elif b != "+" or b != "-" or b != "*" or b != "/":
                print("There was an error, please try again")
                b = str(input("What to do: "))   
        c = int(input("SecondNumber:"))
        if b == "/":
            print(a, ":", c, "=", a/c)
        elif b == "*":
            print(a, "*", c, "=", a*c)
        elif b == "-":
            print(a, "-", c, "=", a-c)
        elif b == "+":
            print(a, "+", c, "=", a+c)
    elif x == 2:
    #(Potęgi, pierwiastki, wartość bezwględna, logarytmy)
        print("Scientific Calculator")
        a = int(input("FirstNumber: "))
        print('''^ is for ########
    @ is for ########''')
        b = str(input("What to do: "))
        while b != "^" or b != "@":
            if b == "^" or b == "@":
                break
            elif b != "^" or b != "@":
                print("There was an error, please try again")
                b = str(input("What to do: "))
        c = int(input("SecondNumber: "))
        if b == "^":
           print(a,"to the power of",c,"is",a**c)
        elif b == "@":
            d = nthroot(a,b)
            e = round(d)
            print("The ",c,"th root of ",a,"is",e)#pierwiastek...
elif p == 2:
    print("Kalkulator")
    print('''Wpisz 1 dla kalkulatora prostego
    Wpisz 2 dla kalkulatora naukowego''')
    x = int(input("[Wpisz cyfrę] "))
    if x < 0 or x > 2:
        while x < 0:
            x = int(input("[Wpisz poprawny numer]"))
        while x > 2:
            x = int(input("[Wpisz poprawny numer]"))
    elif x == 1:
        print("Prosty Kalkulator")
        a = int(input("[Cyfra1]: "))
        print('''+ dla dodawania
    - dla odejmowania
    * dla mnożenia
    / dla dzielenia''')
        b = str(input("[Znak czynności]: "))
        while b != "+" or b != "-" or b != "*" or b != "/":
            if b == "+" or b == "-" or b == "*" or b == "/":
                break
            elif b != "+" or b != "-" or b != "*" or b != "/":
                print("Pojawił się błąd, proszę spróbować ponownie")
                b = str(input("[Znak czynności]: "))   
        c = int(input("Cyfra2:"))
        if b == "/":
            print(a, ":", c, "=", a/c)
        elif b == "*":
            print(a, "*", c, "=", a*c)
        elif b == "-":
            print(a, "-", c, "=", a-c)
        elif b == "+":
            print(a, "+", c, "=", a+c)
    elif x == 2:
    #(Potęgi, pierwiastki, wartość bezwględna, logarytmy)
        print("Kalkulator Naukowy")
        a = int(input("[Cyfra1]: "))
        print('''^ is for potęgowanie
    @ is for pierwiastkowanie''')
        b = str(input("[Znak czynności]: "))
        while b != "^" or b != "@":
            if b == "^" or b == "@":
                break
            elif b != "^" or b != "@":
                print("Pojawił się błąd, proszę spróbować ponownie")
                b = str(input("[Znak czynności]: "))
        c = int(input("[Cyfra2]: "))
        if b == "^":
           print(a,"do potęgi stopnia",c,"to",a**c)
        elif b == "@":
            d = nthroot(a,b)
            e=round(d)
            print("Pierwiastek",c,"stopnia z",a,"to",e)#pierwiastek...
