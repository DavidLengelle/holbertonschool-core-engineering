#!/usr/bin/env python3
"""WebSocket server that validates messages before echoing them back"""

import asyncio

from websockets.asyncio.server import ServerConnection, serve


async def connection_handler(websocket: ServerConnection) -> None:
    """Reply OK: with the message, or ERR:EMPTY when it is blank"""

    async for message in websocket:
        cleaned = message.strip()
        if cleaned == "":
            await websocket.send("ERR:EMPTY")
        else:
            await websocket.send("OK:" + message)


async def main() -> None:
    """Start the validation server and keep it running forever"""

    async with serve(connection_handler, "localhost", 8765) as server:
        await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(main())
