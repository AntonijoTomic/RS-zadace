# Treći mikroservis pozovite nakon konkurentnog izvršavanja prvog i drugog mikroservisa. Dakle treći ide
# sekvencijalno jer mora čekati rezultati prethodna 2. Ovaj mikroservis neka sluša na portu 8085 te na
# endpointu /kolicnik očekuje JSON s podacima prva dva servisa. Kao odgovor mora vratiti količnik
# umnoška i zbroja. Dodajte provjeru i vratite odgovarajući statusni kod ako se pokuša umnožak dijeliti s 0.

import aiohttp
import asyncio
from aiohttp import web


async def kolicnik(request):
    data = await request.json()
    data_brojevi = data.get("brojevi")
    print(data_brojevi)
    
    async with aiohttp.ClientSession() as session:
        response = await session.post('http://localhost:8083/zbroj', json={"brojevi": data_brojevi})
       # microservice_sum_data = await response.json()
        microservice_sum_data = await response.json()
        zbroj = microservice_sum_data.get("zbroj")
        print(zbroj)
         
        responsezbroj = await session.post('http://localhost:8084/umnozak', json={"brojevi": data_brojevi})
       # microservice_sum_data = await response.json()
        microservice_sum_data = await responsezbroj.json()
        umnozak = microservice_sum_data.get("Umnozak")
        print(umnozak)
        if zbroj == 0:
            return web.json_response({"Error":"Ne djelimo s 0!"}, status=400)
        kolicnik_umnozak_zbroj = umnozak / zbroj
    return web.json_response({"kolicnik": kolicnik_umnozak_zbroj}, status=200)

    

    
app = web.Application()
app.router.add_post('/kolicnik', kolicnik)

if __name__ == "__main__":
    web.run_app(app, port=8085)
    
