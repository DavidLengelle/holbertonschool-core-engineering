#!/usr/bin/env python3
"""WebSocket client that sends one message and prints the echo"""

import asyncio

from websockets.asyncio.client import connect


async def main() -> None:
    """Connect to the echo server, send one message and print the reply"""

    async with connect("ws://localhost:8765") as websocket:
        await websocket.send("Hello WebSocket")
        response = await websocket.recv()
        print(response)


if __name__ == "__main__":
    asyncio.run(main())
