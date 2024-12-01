import aiohttp
import asyncio
import requests
import time

response1 = requests.get("https://catfact.ninja/fact")
print(response1.text)

def send_request():
    response = requests.get("https://catfact.ninja/fact")
    fact = response.json()["fact"]
    print(fact)
    
start = time.time()    
print("Šaljemo 1. zahtjev...")
send_request()
print("Šaljemo 2. zahtjev...")
send_request()
print("Šaljemo 3. zahtjev...")
send_request()
print("Šaljemo 4. zahtjev...")
send_request()
print("Šaljemo 5. zahtjev...")
send_request()
end = time.time()
print(f"Izvršavanje programa traje {end - start:.2f} sekundi.")

import requests
import time
def send_request():
    response = requests.get("https://catfact.ninja/fact")
    fact = response.json()["fact"]
    print(fact)
start = time.time()
for i in range(15):
    print(f"Šaljemo {i + 1}. zahtjev...")
    send_request()
end = time.time()
print(f"Izvršavanje programa traje {end - start:.2f} sekundi.")


import aiohttp
import asyncio
import time

try:
    file = open("datoteka.txt", "r")
    sadržaj = file.read()
    print(sadržaj)
except Exception as e:
    print(f"Greška: {e}")
finally:
    file.close()
    
import aiohttp
import asyncio
import time
    
    
async def main(): # definiramo main korutinu
    async with aiohttp.ClientSession() as session: # otvaramo HTTP sesiju koristeći context manager "with"
       for i in range(5): 
        response = await session.get("https://catfact.ninja/fact")
        fact_dict = await response.json()
        print(f"{i + 1}: {fact_dict["fact"]}")
# pokrećemo main korutinu koristeći asyncio.run()
asyncio.run(main())


import aiohttp
import asyncio
import time
    
async def get_cat_fact(session):
    response = await session.get("https://catfact.ninja/fact")
    fact_dict = await response.json()
    return (fact_dict['fact'])    

async def main():
     async with aiohttp.ClientSession() as session:
        cat_fact_korutine = [get_cat_fact(session) for i in range(5)]
        await asyncio.gather(*cat_fact_korutine)   
         
asyncio.run(main())    