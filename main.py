from aiohttp import web
import aiohttp_jinja2
import jinja2
import os

app = web.Application()
aiohttp_jinja2.setup(
    app,
    loader=jinja2.FileSystemLoader('./templates')
)

async def index(request):
    context = {"name":"Tariqul Hasan"}
    return aiohttp_jinja2.render_template(
        'index.jinja2', request, context
    )

app.add_routes(
    [web.get('/',index)]
)

web.run_app(app, port=os.environ['PORT'])


async def start_site(self, app, address='localhost', port=8080, usessl=False):
    runner = web.AppRunner(app)
    self.runners.append(runner)
    await runner.setup()
    if usessl:
        ssl_ctx = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
        ssl_ctx.load_cert_chain(bumper.server_cert, bumper.server_key)
        site = web.TCPSite(
            runner,
            host=address,
            port=port,
            ssl_context=ssl_ctx,
        )

    else:
        site = web.TCPSite(
            runner, host=address, port=port
        )

    await site.start() 