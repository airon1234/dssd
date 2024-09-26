import math

print("0. 6-scian i kwadrat")
print("1. prostopadło i prostokąt")
print("2. graniasto i równoległo")
print("3. ostroslup i trapez")
print("4. Walce i Trójkąt")
print("5. Stożek i trj Równoboczny")
print("6. Kula i kolo")
print("7. Rombu")
print("8.")
print("9.")
rzecz = int(input())
if rzecz == 0:
    print("0. pole powierzchni 6-scianu")
    print("1. obj 6-scianu")
    print("2. obw kwadratu")
    print("3. P kwadratu")
    print("wybierz")
    zmiennaA = int(input())
    if zmiennaA == 0:
     print("dlugosc boku")
     x = float(input("x: "))
     odp = 6*x**2
     print("odp to", odp)
    if zmiennaA == 1:
     print("dlugosc boku")
     x1 = float(input("x: "))
     odp1 = x1**3
     print("odp to", odp1)
    if zmiennaA == 2:
     print("dlugosc boku")
     x2 = float(input("x: "))
     odp2 = 4*x2
     print("odp to", odp2)
    if zmiennaA == 3:
     print("dlugosc boku")
     x3 = float(input("x: "))
     odp3 = x3**2
     print("odp to", odp3)
else:
    print("nie to od 0-3")

if rzecz == 1:
    print("0. P prostopadłościanu")
    print("1. obj prostopadłościanu")
    print("2. obw pro-kat")
    print("3. P pro-kat")
    print("wybierz")
    zmiennaB = int(input())
    if zmiennaB == 0:
     print("dlugosc bokow")
     a = float(input("a: "))
     b = float(input("b: "))
     c = float(input("b: "))
     odp = (2*a)*(2*b) + (2*a)*(2*c) + (2*b)*(2*c)
     print("odp to", odp)
    if zmiennaB == 1:
     print("dlugosci bokow")
     a = float(input("a: "))
     b = float(input("b: "))
     c = float(input("b: "))
     odp1 = a*b*c
     print("odp to", odp1)
    if zmiennaB == 2:
     print("dlugosci bokow")
     a = float(input("a: "))
     b = float(input("b: "))
     odp2 = (2*a) + (2*b)
     print("odp to", odp2)
    if zmiennaB == 3:
     print("dlugosci bokow")
     a = float(input("a: "))
     b = float(input("b: "))
     odp3 = a*b
     print("odp to", odp3)
else:
    print("nie to od 0-3")

if rzecz == 2:
    print("0. pole powierzchni Graniastosłupa")
    print("1. obj Graniastosłupa")
    print("2. obw Równoległobok")
    print("3. P Równoległobok")
    print("wybierz")
    zmiennaC = int(input())
    if zmiennaC == 0:
     print("dlugosc boku")
     x = float(input("x: "))
     odp = 6*x**2
     print("odp to", odp)
    if zmiennaC == 1:
     print("dlugosc boku")
     x1 = float(input("x: "))
     odp1 = x1**3
     print("odp to", odp1)
    if zmiennaC == 2:
     print("dlugosc boku")
     x2 = float(input("x: "))
     odp2 = 4*x2
     print("odp to", odp2)
    if zmiennaC == 3:
     print("dlugosc boku")
     x3 = float(input("x: "))
     odp3 = x3**2
     print("odp to", odp3)
else:
    print("nie to od 0-3")

if rzecz == 3:
    print("0. P Ostrosłup")
    print("1. obj Ostrosłup")
    print("2. obw Trapezu")
    print("3. P Trapezu")
    print("wybierz")
    zmiennaD = int(input())
    if zmiennaD == 0:
     print("dlugosc bokow")
     a = float(input("a: "))
     b = float(input("b: "))
     c = float(input("b: "))
     odp = (2*a)*(2*b) + (2*a)*(2*c) + (2*b)*(2*c)
     print("odp to", odp)
    if zmiennaD == 1:
     print("dlugosci bokow")
     a = float(input("a: "))
     b = float(input("b: "))
     c = float(input("b: "))
     odp1 = a*b*c
     print("odp to", odp1)
    if zmiennaD == 2:
     print("dlugosci bokow")
     a = float(input("a: "))
     b = float(input("b: "))
     odp2 = (2*a) + (2*b)
     print("odp to", odp2)
    if zmiennaD == 3:
     print("dlugosci bokow")
     a = float(input("a: "))
     b = float(input("b: "))
     odp3 = a*b
     print("odp to", odp3)
else:
    print("nie to od 0-3")

if rzecz == 4:
    print("0. pole powierzchni Walca")
    print("1. obj Walca")
    print("2. obw Trójkąt")
    print("3. P Trójkąt")
    print("wybierz")
    zmiennaE = int(input())
    if zmiennaE == 0:
     print("dlugosc boku")
     x = float(input("x: "))
     odp = 6*x**2
     print("odp to", odp)
    if zmiennaE == 1:
     print("dlugosc boku")
     x1 = float(input("x: "))
     odp1 = x1**3
     print("odp to", odp1)
    if zmiennaE == 2:
     print("dlugosc boku")
     x2 = float(input("x: "))
     odp2 = 4*x2
     print("odp to", odp2)
    if zmiennaE == 3:
     print("dlugosc boku")
     x3 = float(input("x: "))
     odp3 = x3**2
     print("odp to", odp3)
else:
    print("nie to od 0-3")

if rzecz == 5:
    print("0. P Stożka")
    print("1. obj Stożka")
    print("2. obw trj rownobocz")
    print("3. P trj rownobocz")
    print("wybierz")
    zmiennaF = int(input())
    if zmiennaF == 0:
     print("dlugosc bokow")
     a = float(input("a: "))
     b = float(input("b: "))
     c = float(input("b: "))
     odp = (2*a)*(2*b) + (2*a)*(2*c) + (2*b)*(2*c)
     print("odp to", odp)
    if zmiennaF == 1:
     print("dlugosci bokow")
     a = float(input("a: "))
     b = float(input("b: "))
     c = float(input("b: "))
     odp1 = a*b*c
     print("odp to", odp1)
    if zmiennaF == 2:
     print("dlugosci bokow")
     a = float(input("a: "))
     b = float(input("b: "))
     odp2 = (2*a) + (2*b)
     print("odp to", odp2)
    if zmiennaF == 3:
     print("dlugosci bokow")
     a = float(input("a: "))
     b = float(input("b: "))
     odp3 = a*b
     print("odp to", odp3)
else:
    print("nie to od 0-3")

 if rzecz == 6:
    print("0. P powierzchni Kuli")
    print("1. obj Kuli")
    print("2. obw koła")
    print("3. P koła")
    print("wybierz")
    zmiennaG = int(input())
    if zmiennaG == 0:
     print("dlugosc boku")
     x = float(input("x: "))
     odp = 6*x**2
     print("odp to", odp)
    if zmiennaG == 1:
     print("dlugosc boku")
     x1 = float(input("x: "))
     odp1 = x1**3
     print("odp to", odp1)
    if zmiennaG == 2:
     print("dlugosc boku")
     x2 = float(input("x: "))
     odp2 = 4*x2
     print("odp to", odp2)
    if zmiennaG == 3:
     print("dlugosc boku")
     x3 = float(input("x: "))
     odp3 = x3**2
     print("odp to", odp3)
else:
    print("nie to od 0-3")

if rzecz == 7:
    print("0. obw rombu")
    print("1. P rombu")
    print("wybierz")
    zmiennaH = int(input())
    if zmiennaH == 0:
     print("dlugosc bokow")
     a = float(input("a: "))
     b = float(input("b: "))
     c = float(input("b: "))
     odp = (2*a)*(2*b) + (2*a)*(2*c) + (2*b)*(2*c)
     print("odp to", odp)
    if zmiennaH == 1:
     print("dlugosci bokow")
     a = float(input("a: "))
     b = float(input("b: "))
     c = float(input("b: "))
     odp1 = a*b*c
     print("odp to", odp1)
else:
    print("nie to od 0-1")

if rzecz == 8:
    print("0. Wysokość Trójkąta Równobocznego")
    print("1. Przękatna Kwadratu")
    print("2. Twierdzenie Pitagorasa")
    print("3. P rombu")
    print("wybierz")
    zmiennaI = int(input())
    if zmiennaI == 0:
     print("dlugosc boku")
     x = float(input("x: "))
     odp = 6*x**2
     print("odp to", odp)
    if zmiennaI == 1:
     print("dlugosc boku")
     x1 = float(input("x: "))
     odp1 = x1**3
     print("odp to", odp1)
    if zmiennaI == 2:
     print("dlugosc boku")
     x2 = float(input("x: "))
     odp2 = 4*x2
     print("odp to", odp2)
    if zmiennaI == 3:
     print("dlugosc boku")
     x3 = float(input("x: "))
     odp3 = x3**2
     print("odp to", odp3)
else:
    print("nie to od 0-3")

    