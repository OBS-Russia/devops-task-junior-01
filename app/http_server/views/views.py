import functools
import json
import logging

from aiohttp.web import View, json_response

logger = logging.getLogger("web_api")


class HelloView(View):
    async def get(self):
        logger.info(f"Incoming request {self.request} from {self.request.remote}")
        return json_response({'data': "Hello from Python!"}, dumps=functools.partial(json.dumps, indent=4))
