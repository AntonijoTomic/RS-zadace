#region Prvi zdatak

num1 = float (input("Unesite prvi broj: "))
num2 = float (input("Unesite drugi broj: "))

val = input("Unesite operaciju koju želite izvršiti (+, -, /, *) \n")

if val == '*':
    print("Rezultat operacije ",num1, " * ", num2, " je ", num1*num2)
elif  val == '+':
    print("Rezultat operacije ",num1, " + ", num2, " je ", num1+num2)    
elif  val == '-':
    print("Rezultat operacije ",num1, " - ", num2, " je ", num1-num2)    
elif  val == '/':
    if num2 == 0:
     print("Ne može se djeliti s nulom")
    else:
     print("Rezultat operacije ", num1, " / ", num2, " je ", num1 / num2)
else:
    print("Nepoznata operacija")

#endregion

#region drugi zadatak

godina = int(input("Unesite godinu: "))

if (godina % 4 == 0 and godina % 100 != 0) or (godina % 400 == 0):
     print("Godina ", godina,". je prijestupna." )
else:
     print("Godina ", godina,". nije prijestupna." )    

#endregion

#region treci zadatak

import random

nasumicniBroj = (random.randint(1, 100))
brojac=01
x=0
broj_je_pogoden = False;
while not broj_je_pogoden:
  brojac += 1;   
  x=int(input("Unesite broj: "))
  if nasumicniBroj > x:
    print("Vaš uneseni broj je manji od broja koji tražimo!")
  elif nasumicniBroj < x:  
     print("Vaš uneseni broj je veci od broja koji tražimo!")
  else:
      broj_je_pogoden = True 

print("Bravo, pogodio si broj u ", brojac,"pokusaja.")          

#endregion

#region cetvrti zadatak

"""
U prvoj while petlji će broj biti 6.

Petlja je beskonačna jer se nikad ne izvrši povećanje broja.

U trecem whileu ne valja to da kada broj bude manji od 5 će se stalno povećati za 2 i onda ispisati i tako će se stvoriti beskonačna petlja
"""

#endregion

#region peti zadatak

broj = int(input("Unesite broj za izračunavanje faktorijela: "))

faktorijel = 1
c=1

for i in range(1, broj + 1):
    faktorijel *= i

print("Faktorijel broja", broj, "je:", faktorijel)
faktorijel = 1
while c <= broj:
    faktorijel *=c
    c+=1
    
print("Faktorijel broja", broj, "je:", faktorijel)

#end region

#region sesti zadatak
"""
Nema smisla raditi petlju za jedan broj

1 3 5 7 9

10,9,8,7,6,5,4,3,2

"""

#end region