# . Definirajte korutinu koja će simulirati dohvaćanje podataka s weba. Podaci neka budu lista
# brojeva od 1 do 10 koju ćete vratiti nakon 3 sekunde. Listu brojeva definirajte comprehensionom.
# Nakon isteka vremena, u korutinu ispišite poruku "Podaci dohvaćeni." i vratite podatke. Riješite bez
# korištenja asyncio.gather() i asyncio.create_task() funkcija.

import asyncio
  

async def fetch_api():
    print('Dohvaćam podatke s API-ja 1...')
    lista_brojeva = [x for x in range(1, 11)]
    await asyncio.sleep(3)
    print('Podaci dohvaćeni.')
    return lista_brojeva


async def main():
    podaci_1 = await fetch_api()
    print(f'Podaci s API-ja: {podaci_1}')
asyncio.run(main())