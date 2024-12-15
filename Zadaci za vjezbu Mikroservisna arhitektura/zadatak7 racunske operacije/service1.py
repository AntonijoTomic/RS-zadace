# Definirajte 3 mikroservisa unutar direktorija microservice_calculations . Prvi mikroservis neka sluša na
# portu 8083 i na endpointu /zbroj vraća JSON bez čekanja. Ulazni podatak u tijelu zahtjeva neka bude lista
# brojeva, a odgovor neka bude zbroj svih brojeva. Dodajte provjeru ako brojevi nisu proslijeđeni, vratite
# odgovarajući HTTP odgovor i statusni kod.
from aiohttp import web


async def zbroj(request):
    data = await request.json()
    data_brojevi = data.get("brojevi")
    zbroj = sum(data_brojevi)
    if len(data_brojevi) <=0:
        return web.json_response({"Error": "prazna lista"}, status=400)
    return web.json_response({"zbroj": zbroj}, status=200)
   

app = web.Application()
app.router.add_post('/zbroj', zbroj)

if __name__ == "__main__":
    web.run_app(app, port=8083)
