import math
import numpy as np
def nthroot(a,n):
    return np.power(a,(1/c))
print("Calculator")
print('''Enter 1 if you want the simple calculator
Enter 2 if you want scientific calculator''')
x = int(input("Awaiting choice... "))
while x < 0 or x > 2:
    x = int(input("Enter correct number: "))
if x == 1:
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
    a = float(input("FirstNumber: "))
    print('''^ is for exponentiation
@ is for rooting
& is for absolute values
# is for logarythms''')
    b = str(input("What to do: "))
    while b != "^" or b != "@" or b != "&" or b != "#":
        if b == "^" or b == "@" or b == "&" or b == "#":
            break
        elif b != "^" or b != "@" or b != "&" or b != "#":
            print("There was an error, please try again")
            print('''^ is for exponentiation
@ is for rooting
& is for absolute values
# is for logarythms''')
            b = str(input("What to do: "))
    if b == "^":
        c = int(input("SecondNumber: "))
        print(a,"to the power of",c,"is",a**c)
    elif b == "@":
        c = int(input("SecondNumber: "))
        d = nthroot(a,b)
        e=round(d)
        print("The ",c,"th root of ",a,"is",e)
    elif b == "&":
        print('''Option 1 is for absolute value of first number
Option 2 is for absolute value of first number and second number
Option 3 is for substracting the first number with second number
Option 4 is for deviding those numbers
Option 5 is for multiplying''')
        d = int(input("Awaiting choice..."))
        while d != 1 or d != 2 or d != 3 or d != 4 or d != 5:
            if d == 1 or d == 2 or d == 3 or d == 4 or d == 5:
                break
            elif d != 1 or d != 2 or d != 3 or d != 4 or d != 5:
                d = int(input("Awaiting correct choice..."))
                print("There was an error, please try again")
        if d == 1:
            print(abs(a))
        elif d == 2:
            c = int(input("Second number: "))
            print(f"|",a,"-",b, "|=",abs(a-b))
        elif d == 3:
            c = int(input("Second number: "))
            print(f"|",a,"+",b, "|=",abs(a+b))
        elif d == 4:
            c = int(input("Second number: "))
            print(f"|",a,"/",b, "|=",abs(a/b))
        elif d == 5:
            c = int(input("Second number: "))
            print(f"|",a,"*",b, "|=",abs(a*b))
    elif b =="#":
        c = int(input("Second number: "))
        l = math.log(a,c)
        print("Logarythm with base ",c,"of",a,"is",l)
        
        
        

