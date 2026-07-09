#!/usr/bin/env python3
"""WebSocket server that broadcasts each message to all connected clients"""

import asyncio

from websockets.asyncio.server import ServerConnection, serve
from websockets.exceptions import ConnectionClosed


connected_clients = set()


async def connection_handler(websocket: ServerConnection) -> None:
    """Track the client and broadcast each message to everyone connected"""

    connected_clients.add(websocket)
    try:
        async for message in websocket:
            for client in connected_clients:
                await client.send("B:" + message)
    except ConnectionClosed:
        pass
    finally:
        connected_clients.remove(websocket)


async def main() -> None:
    """Start the broadcast server and keep it running forever"""

    async with serve(connection_handler, "localhost", 8765) as server:
        await server.serve_forever()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
