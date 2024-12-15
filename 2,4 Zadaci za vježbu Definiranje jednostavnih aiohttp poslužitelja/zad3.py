# Definirajte poslužitelj koji sluša na portu 8082 i na putanji /punoljetni vraća listu korisnika starijih od 18
# godina. Svaki korisnik je rječnik koji sadrži ključeve ime i godine . Pošaljite zahtjev na adresu
# http://localhost:8082/stariji_korisnici i provjerite odgovor. Novu listu korisnika definirajte koristeći
# funkciju filter ili list comprehension

from aiohttp import web

korisnici = [
 {'ime': 'Ivo', 'godine': 25},
 {'ime': 'Ana', 'godine': 17},
 {'ime': 'Marko', 'godine': 19},
 {'ime': 'Maja', 'godine': 16},
 {'ime': 'Iva', 'godine': 22}
]

async def get_users(request): # korutina za GET zahtjev
    punoljetni = [x for x in korisnici if x["godine"] > 17]
    return web.json_response(punoljetni)


app = web.Application()
app.router.add_get('/stariji_korisnici', get_users)
#app.router.add_post('/proizvodi', post_handler)
web.run_app(app, host='localhost', port=8082)
