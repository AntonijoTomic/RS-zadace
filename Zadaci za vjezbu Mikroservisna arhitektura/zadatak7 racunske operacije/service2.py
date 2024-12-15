
# Drugi mikroservis neka sluša na portu 8084 te kao ulazni podataka prima iste podatke. Na endpointu
# /umnozak neka vraća JSON odgovor s umnoškom svih brojeva. Dodajte provjeru ako brojevi nisu
# proslijeđeni, vratite odgovarajući HTTP odgovor i statusni kod.


from aiohttp import web


async def umnozak(request):
    data = await request.json()
    data_brojevi = data.get("brojevi")
    umnozak_rezultat = 1
    for i in data_brojevi:
        umnozak_rezultat *= i    
    if len(data_brojevi) <=0:
        return web.json_response({"Error": "prazna lista"}, status=400)
    return web.json_response({"Umnozak": umnozak_rezultat}, status=200)
   

app = web.Application()
app.router.add_post('/umnozak', umnozak)

if __name__ == "__main__":
    web.run_app(app, port=8084)
