# Nadogradite poslužitelj iz prethodnog zadatka na način da na istoj putanji /proizvodi prima POST zahtjeve
# s podacima o proizvodu. Podaci se šalju u JSON formatu i sadrže ključeve naziv , cijena i količina .
# Handler funkcija treba ispisati primljene podatke u terminalu, dodati novi proizvod u listu proizvoda i vratiti
# odgovor s novom listom proizvoda u JSON formatu.

from aiohttp import web

def handler_function(request):
    data = [{'naziv': 'Laptop', 'cijena': 1000, 'kolicina': 25},{'naziv': 'Monitor', 'cijena': 100, 'kolicina': 20}]
    return web.json_response(data)

async def post_handler(request):
    data = await request.json() 
    print(data) 
    return web.json_response(data) 

app = web.Application()
app.router.add_get('/proizvodi', handler_function)
app.router.add_post('/proizvodi', post_handler)
web.run_app(app, host='localhost', port=8080)
