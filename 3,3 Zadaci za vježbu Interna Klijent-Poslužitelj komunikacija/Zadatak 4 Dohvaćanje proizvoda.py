# Definirajte aiohttp poslužitelj koji radi na portu 8081 . Poslužitelj mora imati dvije rute: /proizvodi i
# /proizvodi/{id} . Prva ruta vraća listu proizvoda u JSON formatu, a druga rutu vraća točno jedan proizvod
# prema ID-u. Ako proizvod s traženim ID-em ne postoji, vratite odgovor s statusom 404 i porukom
# {'error': 'Proizvod s traženim ID-em ne postoji'} .
import asyncio, aiohttp
from aiohttp import web

proizvodi = [
 {"id": 1, "naziv": "Laptop", "cijena": 5000},
 {"id": 2, "naziv": "Miš", "cijena": 100},
 {"id": 3, "naziv": "Tipkovnica", "cijena": 200},
 {"id": 4, "naziv": "Monitor", "cijena": 1000},
 {"id": 5, "naziv": "Slušalice", "cijena": 50}
]

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
web.run_app(app, port=8081)