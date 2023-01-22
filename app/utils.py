import asyncio

import aioredis
import async_timeout
from aioredis import Redis
from fastapi import WebSocket

__all__ = [
    'get_redis',
    'reader',
]


def get_redis() -> Redis:
    return aioredis.from_url(url='redis://redis')


async def reader(
        websocket: WebSocket,
        channel: aioredis.client.PubSub,
) -> None:
    while True:
        try:
            async with async_timeout.timeout(1):
                message = await channel.get_message(
                    ignore_subscribe_messages=True,
                )
                if message is not None:
                    if message['data'] == b'STOP':
                        print('[Reader] STOP')
                        break

                    else:
                        print(f'[Reader] Message Received: {message}')
                        await websocket.send_text(str(message))

                await asyncio.sleep(0.01)
        except asyncio.TimeoutError:
            pass
