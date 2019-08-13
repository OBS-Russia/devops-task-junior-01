import logging

from aiohttp import web

from app.http_server.routes import routes
from app.settings import HTTP_SERVER_HOST, HTTP_SERVER_PORT

logger = logging.getLogger("web_api")

async def run_server():
    logger.info("Setup http server ...")
    app = web.Application()

    for route in routes:
        app.router.add_route(route[0], route[1], route[2], name=route[3])

    runner = web.AppRunner(app)
    await runner.setup()
    logger.info("Starting http server ...")
    site = web.TCPSite(runner, HTTP_SERVER_HOST, HTTP_SERVER_PORT)
    await site.start()
    logger.info("Http server is ready")
