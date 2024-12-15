# Definirajte aiohttp poslužitelj koji radi na portu 8081 koji na putanji /proizvodi vraća listu proizvoda u
# JSON formatu. Svaki proizvod je rječnik koji sadrži ključeve naziv , cijena i količina . Pošaljite zahtjev na
# adresu http://localhost:8080/proizvodi koristeći neki od HTTP klijenata ili curl i provjerite odgovor.

from aiohttp import web

def handler_function(request):
    data = [{'naziv': 'Laptop', 'cijena': 1000, 'kolicina': 25},{'naziv': 'Monitor', 'cijena': 100, 'kolicina': 20}]
    return web.json_response(data)

app = web.Application()
app.router.add_get('/proizvodi', handler_function)
web.run_app(app, host='localhost', port=8080)

