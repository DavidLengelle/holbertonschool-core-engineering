#!/usr/bin/env python3
"""WebSocket echo server listening on localhost port 8765"""

import asyncio

from websockets.asyncio.server import ServerConnection, serve


async def connection_handler(websocket: ServerConnection) -> None:
    """Echo back every text message received on the connection"""

    async for message in websocket:
        await websocket.send(message)


async def main() -> None:
    """Start the echo server and keep it running forever"""

    async with serve(connection_handler, "localhost", 8765) as server:
        await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(main())
