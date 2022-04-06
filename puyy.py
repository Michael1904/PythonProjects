import sys
Qwer=int(input("Aby uruchomić kalkulator wpisz 1: "))
while Qwer != 2:
    print("Instrukcje: \n Wpisz {Liczba}{znak}{Liczba}\n możesz dać wiele znaków oraz liczb.")
    a = str(input("Kalkulator ver.1 (+-*/) \nWpisz równanie: "))
    k, oo, b, t, pp=0, 0, 0, 0, 0
    kk=[]
    num=[]
    c = d = zz = 0
    for el in a:
        pp+=1
        if str(el) == "-" or "+" or "*" or "/":
            if el.isnumeric() == False:
                kk.append(el)
            elif el.isnumeric() == True:
                num.append(el)
        else:
            print("The fuck!?")
    dd1=a.replace("+", " ")
    dd2=dd1.replace("-"," ")
    dd3=dd2.replace("*"," ")
    Licb=dd3.replace("/"," ")
    liczby=Licb.split(" ")
    licznik=0
    Lp=0
    Ld=0
    wynik=0
    mnoże=0
    noże=[]
    dziele=0
    ziele=[]
    for x in kk:
        c+=1
        if x == "+" or "-":
            CPP=1+1
        if x == "*":
            kk.pop(c-1)
            mnoże=int(liczby[c])*int(liczby[c-1])
            liczby.pop(c)
            liczby[c-1] = mnoże
    for x in kk:
        d+=1
        if x == "+" or "-":
            CPP=1+1 
        if x == "/":
            kk.pop(d-1)
            dziele=int(liczby[c-1])/int(liczby[c])
            liczby.pop(d)
            liczby[d-1]=dziele
    for x in liczby:
        if len(kk)-1 == licznik:
            zz=kk[licznik]
        else:
            if len(kk) > 1:
                zz=kk[licznik-1]
            elif len(kk) == 0:
                cpppp=1+1
        if zz !=0:
            if zz =="+":
                Lp=int(x)
                wynik=Lp+Ld
                Ld=wynik
            elif zz =="-":
                Lp=int(x)
                wynik=Lp-Ld
                Ld=wynik
        else:
            wynik=int(liczby[0])
        
        licznik+=1
    print(f"Wynik {a} to {wynik}")
    Qwer = int(input("Aby kontynuować wpisz cyfrę: "))
        
        