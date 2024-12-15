
import asyncio, aiohttp
from aiohttp import web

proizvodi = [
 {"id": 1, "naziv": "Laptop", "cijena": 5000},
 {"id": 2, "naziv": "Miš", "cijena": 100},
 {"id": 3, "naziv": "Tipkovnica", "cijena": 200},
 {"id": 4, "naziv": "Monitor", "cijena": 1000},
 {"id": 5, "naziv": "Slušalice", "cijena": 50}
]

narudzbe = []

async def post_proizvod(request):
    postoji = False 
    data = await request.json() 
    proizvod_id = data.get('proizvod_id')
    kolicina = data.get('kolicina')
    for proizvod in proizvodi:
        if proizvod['id'] == int(proizvod_id):
            postoji = True
            narudzba = {
                "proizvod_id": proizvod_id,
                "kolicina": kolicina,
                }
            narudzbe.append(narudzba)
            return web.json_response(narudzbe, status=200)
    if postoji != True:
        return web.json_response({"error": "Proizvod s traženim ID-em ne postoji"}, status=404) 
    print(data) 
    return web.json_response(data) 

async def svi_proizvodi(request):
    return web.json_response(proizvodi)

async def get_proizvod(request):
    id = request.match_info['id']
    postoji = False 
    for proizvod in proizvodi:
        if proizvod['id'] == int(id):
            postoji = True
            return web.json_response(proizvod, status=200)
    if postoji != True:
        return web.json_response({"error": "Proizvod s traženim ID-em ne postoji"}, status=404) 
app = web.Application()
app.router.add_get('/proizvodi/{id}', get_proizvod)
app.router.add_get('/proizvodi', svi_proizvodi)
app.router.add_post('/narudzbe', post_proizvod)
web.run_app(app, port=8081)


