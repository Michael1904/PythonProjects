from math import sqrt
import numpy as np
def nthroot(a,n):
    return np.power(a,(1/c))
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
        print("Pierwiastek",c,"stopnia z",a,"to",e)
