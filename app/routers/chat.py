# app/routers/chat.py
from fastapi import APIRouter, Depends
from ..services.chat_service import (
    create_chat_room, get_chat_room, add_message_to_chat
)
from ..models import ChatRoom, Message

# to be implmented in .auth
get_current_user = None

router = APIRouter()

@router.post("/rooms", response_model=ChatRoom)
async def create_room(room: ChatRoom, user: dict = Depends(get_current_user)):
    return await create_chat_room(
        name=room.name, type=room.type, participants=[str(user["id"])]
    )

@router.get("/rooms/{room_id}", response_model=ChatRoom)
async def get_room(room_id: str):
    return await get_chat_room(room_id)

@router.post("/rooms/{room_id}/messages", response_model=Message)
async def send_message(room_id: str, message: Message, user: dict = Depends(get_current_user)):
    message.sender = user["id"]
    await add_message_to_chat(room_id, message)
    return message