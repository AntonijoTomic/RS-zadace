# Definirajte korutinu autentifikacija() koja će simulirati autentifikaciju korisnika na
# poslužiteljskoj strani. Korutina kao ulazni parametar prima rječnik koji opisuje korisnika, a sastoji se
# od ključeva korisnicko_ime , email i lozinka . Unutar korutine simulirajte provjeru korisničkog
# imena na način da ćete provjeriti nalaze li se par korisnicko_ime i email u bazi korisnika. Ova
# provjera traje 3 sekunde.

import asyncio
import time

async def autentifikacija(korisnik):

    nema = True
    baza_korisnika = [
 {'korisnicko_ime': 'mirko123', 'email': 'mirko123@gmail.com'},
 {'korisnicko_ime': 'ana_anic', 'email': 'aanic@gmail.com'},
 {'korisnicko_ime': 'maja_0x', 'email': 'majaaaaa@gmail.com'},
 {'korisnicko_ime': 'zdeslav032', 'email': 'deso032@gmail.com'}
]
    await asyncio.sleep(3)
    for k in baza_korisnika:
        if korisnik['korisnicko_ime'] == k['korisnicko_ime'] and korisnik['email'] == k['email']:
            nema = False
            await autorizacija(korisnik)
            
    if nema:
         print(f"Korisnik {korisnik}: nije pronađen.")
         
         
#    Ako se korisnik nalazi u bazi, potrebno je pozvati vanjsku korutinu autorizacija() koja će simulirati
# autorizaciju korisnika u trajanju od 2 sekunde. Funkcija kao ulazni parametar prima rječnik korisnika iz baze
# i lozinku proslijeđenu iz korutine autentifikacija() . Autorizacija simulira dekripciju lozinke (samo
# provjerite podudaranje stringova) i provjeru s lozinkom iz baze_lozinka. Ako su lozinke jednake, korutine
# vraća poruku "Korisnik {korisnik}: Autorizacija uspješna." , a u suprotnom "Korisnik
# {korisnik}: Autorizacija neuspješna." .    

async def autorizacija(korisnik):  
    nema = True
    baza_lozinka = [
 {'korisnicko_ime': 'mirko123', 'lozinka': 'lozinka123'},
 {'korisnicko_ime': 'ana_anic', 'lozinka': 'super_teska_lozinka'},
 {'korisnicko_ime': 'maja_0x', 'lozinka': 's324SDFfdsj234'},
 {'korisnicko_ime': 'zdeslav032', 'lozinka': 'deso123'}
]
    await asyncio.sleep(2)
    for k in baza_lozinka:
        if korisnik['lozinka'] == k['lozinka']:
            nema = False
            print(f"Korisnik {korisnik}: Autorizacija uspješna.")
     
    if nema:
         print(f"Korisnik {korisnik}: Autorizacija neuspješna.")       
            
         
async def main():
    korisnik = {
       "korisnicko_ime":input("Unesite korisničko ime: "),
       "email":input("Unesite email: "),
       "lozinka":input("Unesite lozinku: ")
    }
    
    await autentifikacija(korisnik)
 
asyncio.run(main())
    