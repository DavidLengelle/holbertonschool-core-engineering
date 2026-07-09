#!/usr/bin/env python3
"""WebSocket server that unicasts each reply back to its sender"""

import asyncio

from websockets.asyncio.server import ServerConnection, serve
from websockets.exceptions import ConnectionClosed


connected_clients = set()


async def connection_handler(websocket: ServerConnection) -> None:
    """Track the client and send each message back only to its sender"""

    connected_clients.add(websocket)
    try:
        async for message in websocket:
            await websocket.send("U:" + message)
    except ConnectionClosed:
        pass
    finally:
        connected_clients.remove(websocket)


async def main() -> None:
    """Start the unicast server and keep it running forever"""

    async with serve(connection_handler, "localhost", 8765) as server:
        await server.serve_forever()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
