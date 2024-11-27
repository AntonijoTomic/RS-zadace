# Definirajte korutinu provjeri_parnost koja će simulirati "super zahtjevnu operaciju" provjere
# parnosti broja putem vanjskog API-ja. Korutina prima kao argument broj za koji treba provjeriti
# parnost, a vraća poruku "Broj {broj} je paran." ili "Broj {broj} je neparan." nakon 2 sekunde.
# Unutar main funkcije definirajte listu 10 nasumičnih brojeva u rasponu od 1 do 100 (koristite random
# modul). Listu brojeva izgradite kroz list comprehension sintaksu. Nakon toga, pohranite u listu zadaci
# 10 Task objekata koji će izvršavati korutinu provjeri_parnost za svaki broj iz liste (također kroz list
# comprehension). Na kraju, koristeći asyncio.gather() , pokrenite sve korutine konkurentno i ispišite
# rezultate


import asyncio
import random

async def provjeri_parnost(broj):
    await asyncio.sleep(2) 
    
    if broj % 2 == 0:
        return f"Broj {broj} je paran."
    else:
        return f"Broj {broj} je neparan."

# Glavna funkcija koja poziva korutinu
async def main():
    lista_brojeva = [random.randint(1,100) for x in range(1, 11)]
    tasks = [asyncio.create_task(provjeri_parnost(i)) for i in lista_brojeva]
    results = await asyncio.gather(*tasks)
    print(results)

        
asyncio.run(main())   