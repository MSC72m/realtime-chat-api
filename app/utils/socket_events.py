from starlette.websockets import WebSocket
from ..services.chat_service import add_message_to_chat
from ..models import Message

async def handle_connect(websocket: WebSocket):
    await websocket.accept()
    # todo: Notify other users about the new connection

async def handle_disconnect(websocket: WebSocket):
    await websocket.close()
    # todo: Notify other users about the disconnection

async def handle_chat_message(websocket: WebSocket, message_data: str):
    message = Message.parse_raw(message_data)
    await add_message_to_chat(message.room_id, message)
    # todo : Broadcast the new message to all participants in the room