# app/routers/users.py
from fastapi import APIRouter, Depends
from ..services.user_service import (
    get_user_by_id, update_user_online_status
)
from ..models import User

# to be implmented in .auth file
get_current_user = None
router = APIRouter()

@router.get("/me", response_model=User)
async def get_me(user: dict = Depends(get_current_user)):
    return await get_user_by_id(str(user["id"]))

@router.put("/me/online")
async def set_online(user: dict = Depends(get_current_user)):
    await update_user_online_status(str(user["id"]), True)
    return {"status": "online"}

@router.put("/me/offline")
async def set_offline(user: dict = Depends(get_current_user)):
    await update_user_online_status(str(user["id"]), False)
    return {"status": "offline"}