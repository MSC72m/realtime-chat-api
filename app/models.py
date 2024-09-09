from pydantic import BaseModel, Field
from bson import ObjectId
from datetime import datetime

class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not isinstance(v, ObjectId):
            raise TypeError('ObjectId required')
        return str(v)

class User(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias='_id')
    username: str
    email: str
    password: str
    online: bool
    last_seen: datetime

class Message(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias='_id')
    sender: PyObjectId
    content: str | None
    timestamp: datetime
    media: dict | None

class ChatRoom(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias='_id')
    name: str
    type: str
    participants: list[PyObjectId]
    messages: list[Message]

class PrivateMessage(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias='_id')
    participants: list[PyObjectId]
    messages: list[Message]