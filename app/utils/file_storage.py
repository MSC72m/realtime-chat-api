import os
from fastapi import UploadFile

UPLOAD_DIR = "uploads/"

async def save_file(file: UploadFile, filename: str) -> str:
    file_path = await get_file_path(filename)
    with open(file_path, "wb") as f:
        content = await file.read()
        f.write(content)
    return file_path

async def get_file_path(filename: str) -> str:
    return os.path.join(UPLOAD_DIR, filename)