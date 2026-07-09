# Python - WebSockets

Real-time, bidirectional communication between clients and a server, built with
the [`websockets`](https://websockets.readthedocs.io/) library and Python's
`asyncio`.

Unlike the HTTP request-response model, a WebSocket keeps the connection open,
so both sides can send messages at any time. This project builds a real-time
communication system step by step.

## Requirements

- Ubuntu 20.04
- Python 3.x
- The `websockets` library (version 13 or newer: this code uses the modern
  `websockets.asyncio` API)
- `starlette` (ASGI web framework) and `uvicorn` (ASGI server), used in task 5
- Asynchronous programming with `async` / `await`

## Setup

The dependencies are installed in a local virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
pip install websockets starlette uvicorn
```

Check the installed version:

```bash
python3 -c "import websockets; print(websockets.__version__)"
```

## Files

| File | Task | Description |
| --- | --- | --- |
| `echo_server.py` | 0 | WebSocket server on `localhost:8765` that echoes back every message it receives, while keeping the connection open |
| `ws_client.py` | 1 | WebSocket client that connects to the echo server, sends one message, prints the reply, and closes the connection |
| `validation_server.py` | 2 | WebSocket server that replies `OK:<message>` for a valid message or `ERR:EMPTY` for a blank one, keeping the connection open |
| `unicast_server.py` | 3 | WebSocket server that tracks connected clients in a set and unicasts each reply (prefixed `U:`) only to its sender |
| `broadcast_server.py` | 4 | WebSocket server that broadcasts each message (prefixed `B:`) to every connected client |
| `asgi_server.py` | 5 | Starlette ASGI app serving an HTML page at `/` and a WebSocket echo endpoint at `/ws`, run with Uvicorn on port 8000 |

## Usage

Start the server (virtual environment activated):

```bash
python3 echo_server.py
```

The server listens on `localhost`, port `8765`, and accepts multiple concurrent
clients.

With the server running, the client sends one message and prints the reply:

```bash
python3 ws_client.py
```

The validation server checks each message and replies `OK:<message>`, or
`ERR:EMPTY` when the message is empty or blank:

```bash
python3 validation_server.py
```

The unicast server tracks connected clients and sends each reply (prefixed
`U:`) only to the client that sent the message:

```bash
python3 unicast_server.py
```

The broadcast server sends each message (prefixed `B:`) to every connected
client, like a chat room:

```bash
python3 broadcast_server.py
```

The ASGI app (task 5) is different: it serves an HTML page at `/` and a
WebSocket echo at `/ws`, and it is started with Uvicorn on port 8000:

```bash
uvicorn asgi_server:app --host 0.0.0.0 --port 8000 --reload
```

Then open http://localhost:8000 in a browser, and connect a WebSocket client to
`ws://localhost:8000/ws`.

## Testing

In a second terminal, use the interactive client provided by `websockets`:

```bash
websockets ws://localhost:8765/
```

Example session:

```
Connected to ws://localhost:8765/.
> Hello world!
< Hello world!
```

Whatever you type is sent back unchanged. Press `Ctrl+C` to close the client,
and `Ctrl+C` again in the server terminal to stop the server.

## Author

David Lengellé
