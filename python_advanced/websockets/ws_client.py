#!/usr/bin/env python3
"""WebSocket client that sends one message and returns the echo"""

import asyncio
import os

from websockets.asyncio.client import connect


async def connect_and_send(ws_server_url: str, msg_to_send: str) -> str:
    """Connect to the server, send one message and return the reply"""

    async with connect(ws_server_url) as websocket:
        await websocket.send(msg_to_send)
        response = await websocket.recv()
        return response


if __name__ == "__main__":
    ws_uri = os.environ.get("WS_URI", "ws://localhost:8765")
    ws_message = os.environ.get("WS_MESSAGE", "demo")
    reply = asyncio.run(connect_and_send(ws_uri, ws_message))
    print(reply, end="")
