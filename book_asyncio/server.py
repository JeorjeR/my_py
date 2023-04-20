import asyncio
from aiohttp import web


async def handle(request):
    await asyncio.sleep(2)
    text = 'Я очень медленный сервер'
    return web.Response(text=text)

app = web.Application()
app.add_routes(
    [web.route('*', '/', handle)]
)

if __name__ == '__main__':
    web.run_app(app)
