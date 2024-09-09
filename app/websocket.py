from fastapi import FastAPI, WebSocket
from .utils.socket_events import handle_connect, handle_disconnect, handle_chat_message

app = FastAPI()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await handle_connect(websocket)

    try:
        async for message in websocket.iter_text():
            await handle_chat_message(websocket, message)
    except:
        await handle_disconnect(websocket)