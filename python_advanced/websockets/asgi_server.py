#!/usr/bin/env python3
"""ASGI app serving an HTML page and a WebSocket echo endpoint"""

from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import HTMLResponse
from starlette.routing import Route, WebSocketRoute
from starlette.websockets import WebSocket, WebSocketDisconnect


async def homepage(request: Request) -> HTMLResponse:
    """Return the HTML home page"""

    return HTMLResponse("<h1>WebSocket App</h1>")


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
    WebSocketRoute("/ws", websocket_endpoint),
])
