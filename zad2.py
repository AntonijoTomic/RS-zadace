# Definirajte dvije korutine koje će simulirati dohvaćanje podataka s weba. Prva korutina neka vrati
# listu proizvoljnih rječnika (npr. koji reprezentiraju podatke o korisnicima) nakon 3 sekunde, a druga
# korutina neka vrati listu proizvoljnih rječnika (npr. koji reprezentiraju podatke o proizvodima) nakon 5
# sekundi. Korutine pozovite konkurentno korištenjem asyncio.gather() i ispišite rezultate. Program
# se mora izvršavati ~5 sekundi.
# 

import asyncio

 
async def fetch_api_1():
    korisnici = [
        {"Ime":"Antonijo", "Prezime": "Tomic", "Godine":22},
         {"Ime":"Dominik", "Prezime": "Tomic", "Godine":19},
    ]
    await asyncio.sleep(3)
    return korisnici

async def fetch_api_2():
    proizvodi = [
            {"Naziv":"Miš", "Cijena": 100, "Kolicina":22},
            {"Naziv":"Tipkovnica", "Cijena":68, "Kolicina":19},
        ]
    await asyncio.sleep(5)
    return proizvodi

async def main():
    results = await asyncio.gather(fetch_api_1(),fetch_api_2())
   
    print(results)
asyncio.run(main())