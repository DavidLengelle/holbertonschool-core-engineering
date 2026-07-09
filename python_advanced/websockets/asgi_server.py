#!/usr/bin/env python3
"""ASGI app serving the chat client and a WebSocket echo endpoint"""

import os

from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import FileResponse
from starlette.routing import Route, WebSocketRoute
from starlette.websockets import WebSocket, WebSocketDisconnect


BASE_DIR = os.path.dirname(os.path.abspath(__file__))


async def homepage(request: Request) -> FileResponse:
    """Serve the chat client home page"""

    return FileResponse(os.path.join(BASE_DIR, "index.html"))


async def styles(request: Request) -> FileResponse:
    """Serve the stylesheet"""

    return FileResponse(os.path.join(BASE_DIR, "styles.css"))


async def chat_script(request: Request) -> FileResponse:
    """Serve the client JavaScript"""

    return FileResponse(os.path.join(BASE_DIR, "chat.js"))


async def websocket_endpoint(websocket: WebSocket) -> None:
    """Accept the connection and echo every text message back"""

    await websocket.accept()
    try:
        while True:
            message = await websocket.receive_text()
            await websocket.send_text(message)
    except WebSocketDisconnect:
        pass


app = Starlette(routes=[
    Route("/", homepage),
    Route("/styles.css", styles),
    Route("/chat.js", chat_script),
    WebSocketRoute("/ws", websocket_endpoint),
])
