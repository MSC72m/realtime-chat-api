# app/services/user_service.py
from bson import ObjectId
from datetime import datetime
from ..utils.mongo_client import db
from ..models import User

# verify_password and get_passwrod_hash are yet to be implmeneted in .auth folder
verify_password = None
get_password_hash =None
async def get_user_by_id(user_id: str) -> User:
    user = await db.users.find_one({"_id": ObjectId(user_id)})
    if user:
        return User(**user)
    return None

async def get_user_by_username(username: str) -> User:
    user = await db.users.find_one({"username": username})
    return User(**user) if user else None

async def create_user(user: User) -> User:
    user.password = get_password_hash(user.password)
    result = await db.users.insert_one(user.dict())
    user.id = result.inserted_id
    return user

async def authenticate_user(username: str, password: str) -> User:
    user = await get_user_by_username(username)
    if not user or not verify_password(password, user.password):
        return None
    return user

async def update_user_online_status(user_id: str, online: bool):
    await db.users.update_one(
        {"_id": ObjectId(user_id)},
        {"$set": {"online": online, "last_seen": datetime.utcnow()}}
    )

async def get_all_users() -> list[User]:
    users = await db.users.find().to_list(None)
    return [User(**user) for user in users]

async def update_user(user_id: str, update_data: dict) -> User:
    await db.users.update_one({"_id": ObjectId(user_id)}, {"$set": update_data})
    return await get_user_by_id(user_id)

async def delete_user(user_id: str) -> bool:
    result = await db.users.delete_one({"_id": ObjectId(user_id)})
    return result.deleted_count > 0