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
- Asynchronous programming with `async` / `await`

## Setup

The `websockets` library is installed in a local virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
pip install websockets
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
