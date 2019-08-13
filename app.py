import asyncio
from logging.config import dictConfig
import sys

from app.http_server.async_server import run_server
from app.settings import LOGGING
from app.utils.shutdown import add_signals


def setup_logger(config):
    dictConfig(config)


def main():
    loop = asyncio.get_event_loop()

    if sys.platform == 'win32':
        loop = asyncio.ProactorEventLoop()
        asyncio.set_event_loop(loop)

    loop = add_signals(loop)
    loop.run_until_complete(run_server())
    loop.run_forever()


if __name__ == '__main__':
    setup_logger(LOGGING)
    main()
