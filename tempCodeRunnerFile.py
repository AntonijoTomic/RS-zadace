# Definirajte korutinu get_dog_fact koja dohvaća činjenice o psima sa DOG API.
# Korutina get_dog_fact neka dohvaća činjenicu o psima na URL-u: https://dogapi.dog/api/v2/facts .
# Nakon toga, definirajte korutinu get_cat_fact koja dohvaća činjenicu o mačkama slanjem zahtjeva na
# URL: https://catfact.ninja/fact .
# Istovremeno pohranite rezultate izvršavanja ovih Taskova koristeći asyncio.gather(*dog_facts_tasks,
# *cat_facts_tasks) funkciju u listu dog_cat_facts , a zatim ih koristeći list slicing odvojite u dvije liste
# obzirom da znate da je prvih 5 činjenica o psima, a drugih 5 o mačkama.
# Na kraju, definirajte i treću korutinu mix_facts koja prima liste dog_facts i cat_facts i vraća novu
# listu koja za vrijednost indeksa i sadrži činjenicu o psima ako je duljina činjenice o psima veća od duljine
# činjenice o mačkama na istom indeksu, inače vraća činjenicu o mački. Na kraju ispišite rezultate filtriranog
# niza činjenica. Liste možete paralelno iterirati koristeći zip funkciju, npr. for dog_fact, cat_fact in
# zip(dog_facts, cat_facts) .

import asyncio
import aiohttp

async def get_dog_fact(session):
    response = await session.get("https://dogapi.dog/api/v2/facts")
    fact_dict = await response.json()
    return fact_dict['data'][0]['attributes']['body']  
    
async def get_cat_fact(session):
    response = await session.get("https://catfact.ninja/fact")
    fact_dict = await response.json()
    return fact_dict['fact']    

async def mix_facts(dog_facts, cat_facts):
    mixed_facts = []
    for dog_fact, cat_fact in zip(dog_facts, cat_facts):
        if len(dog_fact) > len(cat_fact):
            mixed_facts.append(dog_fact)
        else:
            mixed_facts.append(cat_fact)
    return mixed_facts

async def main():
    async with aiohttp.ClientSession() as session:
        cat_fact_tasks  = [asyncio.create_task(get_cat_fact(session)) for i in range(5)] # u
        dog_fact_tasks  = [asyncio.create_task(get_dog_fact(session)) for i in range(5)]
        mix = await asyncio.gather(*dog_fact_tasks, *cat_fact_tasks)
    dog_facts = mix[:5]  # Prvih 5 činjenica su o psima
    cat_facts = mix[5:]    
    mixed_facts = await mix_facts(dog_facts, cat_facts)   
    for fact in mixed_facts:
            print(f"- {fact}")


    
asyncio.run(main())    