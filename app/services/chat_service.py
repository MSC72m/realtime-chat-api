from bson import ObjectId
from ..utils.mongo_client import db
from ..models import ChatRoom, Message

async def create_chat_room(name: str, type: str, participants: list[str]) -> ChatRoom:
    room = ChatRoom(name=name, type=type, participants=[ObjectId(p) for p in participants], messages=[])
    result = await db.chat_rooms.insert_one(room.dict())
    room.id = result.inserted_id
    return room

async def get_chat_room(room_id: str) -> ChatRoom:
    room = await db.chat_rooms.find_one({"_id": ObjectId(room_id)})
    return ChatRoom(**room)

async def add_message_to_chat(room_id: str, message: Message) -> bool:
    result = await db.chat_rooms.update_one(
        {"_id": ObjectId(room_id)},
        {"$push": {"messages": message.dict()}}
    )
    return result.modified_count > 0