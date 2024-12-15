# Unutar client.py datoteke definirajte 1 korutinu koja može slati zahtjev na oba mikroservisa, mora
# # primati argumente url i port . Korutina neka vraća JSON odgovor.

import aiohttp
import asyncio

async def fetch(url, port):
    full_url = f"{url}{port}/pozdrav"
    async with aiohttp.ClientSession() as session:
            response = await session.get(full_url)
            return await response.json()
async def main():
    url = "http://localhost:"

    # Sekvencijalno slanje zahtjeva
    print("Sekvencijalno slanje zahtjeva:")
    response1 = await fetch(url, 8081)
    print(f"Odgovor sa mikroservisa 1: {response1}")
    response2 = await fetch(url, 8082)
    print(f"Odgovor sa mikroservisa 2: {response2}")

    # Konkurentno slanje zahtjeva
    print("\nKonkurentno slanje zahtjeva:")
    task1 = asyncio.create_task(fetch(url, 8081))
    task2 = asyncio.create_task(fetch(url, 8082))
    
    response1, response2 = await asyncio.gather(task1, task2)
    print(f"Odgovor sa mikroservisa 1: {response1}")
    print(f"Odgovor sa mikroservisa 2: {response2}")

if __name__ == "__main__":
    asyncio.run(main())
