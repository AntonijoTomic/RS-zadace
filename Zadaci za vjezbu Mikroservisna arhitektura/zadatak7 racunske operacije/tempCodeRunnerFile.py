import aiohttp
import asyncio
from aiohttp import web

async def main():
    data_brojevi = {"brojevi": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]}
    print(f"Zbroj: {data_brojevi}")
    async with aiohttp.ClientSession() as session:
      
        zbroj_task = session.post('http://localhost:8083/zbroj', json=data_brojevi)
        umnozak_task = session.post('http://localhost:8084/umnozak', json=data_brojevi)
        print(f"zbroj_task: {zbroj_task}")
  
        zbroj_response, umnozak_response = await asyncio.gather(zbroj_task, umnozak_task)
        
       
        zbroj = (await zbroj_response.json()).get("zbroj")
        umnozak = (await umnozak_response.json()).get("Umnozak")
        print(f"Zbroj: {zbroj}")
        print(f"Umnožak: {umnozak}")
       
        kolicnik_request = {"brojevi": data_brojevi["brojevi"]} 
        kolicnik_response = await session.post('http://localhost:8085/kolicnik', json=kolicnik_request)
        kolicnik_data = await kolicnik_response.json()
        print(f"Količnik: {kolicnik_data.get('kolicnik')}")
 
        

if __name__ == "__main__":
    asyncio.run(main())