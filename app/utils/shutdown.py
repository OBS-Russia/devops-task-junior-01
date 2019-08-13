import asyncio
import logging
import signal
import sys

from app.settings import MAX_ASYNC_TASK_CLOSE_TIME

logger = logging.getLogger('web_api')


def async_exception_handler(loop, context):
    if "exception" not in context \
            or not isinstance(context["exception"], asyncio.CancelledError):
        logger.error(f'Unexpected exception during shutdown, context: {context}')


async def cancel_async_tasks_and_stop(loop, wait_time=3):
    loop.set_exception_handler(async_exception_handler)
    tasks = asyncio.gather(*asyncio.Task.all_tasks(), return_exceptions=True)
    tasks.cancel()
    try:
        while not tasks.done() and not loop.is_closed():
            await asyncio.sleep(0)
    except asyncio.CancelledError:
        pass
    wt = 0
    # Only single task (self) can be pending
    while len(list(t for t in asyncio.Task.all_tasks() if not t.done())) > 1:
        await asyncio.sleep(wt)
        wt += 1
        if wt > wait_time:
            break
    try:
        loop.stop()
    except RuntimeError:
        loop.stop()
        logger.warning(f'Some async tasks are still pending: '
                       f'{list(t for t in asyncio.Task.all_tasks() if not t.done())}, '
                       f'wait_time expired, stopping the loop')
    logger.info('All async tasks are canceled')


async def shutdown_on_signal(signal, loop, wait_time):
    logger.warning(f'Received exit signal {signal.name}, terminating...')
    loop.remove_signal_handler(signal)
    loop.create_task(cancel_async_tasks_and_stop(loop, wait_time))


def add_signals(loop):
    if sys.platform == 'win32':
        # There are no signals on Windows
        pass
    else:
        signals = (signal.SIGTERM, signal.SIGINT)
        for s in signals:
            loop.add_signal_handler(s, lambda:
            asyncio.create_task(shutdown_on_signal(s, loop, MAX_ASYNC_TASK_CLOSE_TIME)))
    return loop
