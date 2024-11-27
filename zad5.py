# Definirajte korutinu secure_data koja će simulirati enkripciju osjetljivih podataka. Kako se u
# praksi enkripcija radi na poslužiteljskoj strani, korutina će simulirati enkripciju podataka u trajanju od 3
# sekunde. Korutina prima kao argument rječnik osjetljivih podataka koji se sastoji od ključeva prezime ,
# broj_kartice i CVV . Definirajte listu s 3 rječnika osjetljivih podataka. Pohranite u listu zadaci kao u
# prethodnom zadatku te pozovite zadatke koristeći asyncio.gather() . Korutina secure_data mora za
# svaki rječnik vratiti novi rječnik u obliku: {'prezime': prezime , 'broj_kartice': 'enkriptirano',
# 'CVV': 'enkriptirano'} . Za fake enkripciju koristite funkciju hash(str) koja samo vraća hash
# vrijednost ulaznog stringa.

import asyncio

async def secure_data(osjetljivi_podaci):
    asyncio.sleep(3)
    enkriptirani_podaci = {
        'prezime': osjetljivi_podaci['Prezime'],
        'broj_kartice': hash(str(osjetljivi_podaci['Broj_kartice'])), 
        'CVV': hash(str(osjetljivi_podaci['CVV']))  
    }
    return enkriptirani_podaci  

async def main():
    osjetljivi_podaci = [
        {"Prezime":"Tomic","Broj_kartice":123,"CVV":123},
        {"Prezime":"Cosic","Broj_kartice":213,"CVV":321},
        {"Prezime":"Duvnjak","Broj_kartice":313,"CVV":222}
    ]
    zadaci = [asyncio.create_task(secure_data(podaci)) for podaci in osjetljivi_podaci]
    
    rezultati = await asyncio.gather(*zadaci)
    print(rezultati)
    
asyncio.run(main())