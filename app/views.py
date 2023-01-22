import asyncio

from aioredis import Redis
from fastapi import APIRouter, Depends, WebSocket
from fastapi.responses import HTMLResponse
from starlette.responses import Response

from app.resources import HTML, REDIS_CHANNEL
from app.utils import get_redis, reader

__all__ = [
    'router',
]

router = APIRouter()


@router.get('/')
async def get() -> HTMLResponse:
    return HTMLResponse(HTML)


@router.websocket('/ws')
async def websocket_endpoint(
        websocket: WebSocket,
        redis_client: Redis = Depends(get_redis),
) -> None:

    # Open connection...
    await websocket.accept()
    pubsub = redis_client.pubsub()
    await pubsub.subscribe(REDIS_CHANNEL)

    # Run logic...
    future = asyncio.create_task(reader(websocket=websocket, channel=pubsub))
    await future

    # Closing all open connections
    await pubsub.unsubscribe(REDIS_CHANNEL)
    await pubsub.close()
    await websocket.close()


@router.get('/message/')
async def send_msg(
        m: str,
        redis_client: Redis = Depends(get_redis),
) -> Response:
    """
    Публикация сообщения.
    """
    await redis_client.publish(REDIS_CHANNEL, m)
    await redis_client.close()

    return Response(status_code=202, content=m)
