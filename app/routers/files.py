# app/routers/files.py
from fastapi import APIRouter, File, UploadFile, Depends, HTTPException
from fastapi.responses import FileResponse
from ..services.file_service import upload_file, get_file_path

import os

router = APIRouter()
# to be implmented get user function in .auth folder
get_current_user = None

@router.post("/upload")
async def upload_media(
    file: UploadFile = File(...),
    current_user: dict = Depends(get_current_user)
):
    try:
        file_url = await upload_file(file)
        return {"file_url": file_url}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"File upload failed: {str(e)}")

@router.get("/download/{filename}")
async def download_media(
    filename: str,
    current_user: dict = Depends(get_current_user)
):
    try:
        file_path = await get_file_path(filename)
        if os.path.exists(file_path):
            return FileResponse(file_path, filename=filename)
        else:
            raise HTTPException(status_code=404, detail="File not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"File download failed: {str(e)}")