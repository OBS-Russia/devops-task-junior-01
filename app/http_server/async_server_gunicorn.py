import logging

from aiohttp import web

from app.http_server.routes import routes
from app.settings import LOGGING

logger = logging.getLogger("web_api")

from logging.config import dictConfig


def setup_logger(config):
    dictConfig(config)


setup_logger(LOGGING)

app = web.Application()

for route in routes:
    logger.info("Add route {}".format(route[1]))
    app.router.add_route(route[0], route[1], route[2], name=route[3])
