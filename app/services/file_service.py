import os
from fastapi import UploadFile
from ..utils.file_storage import save_file, get_file_path

UPLOAD_DIR = "uploads/"

async def upload_file(file: UploadFile) -> str:
    filename = file.filename
    file_path = await save_file(file, filename)
    file_url = get_file_url(file_path)
    return file_url

def get_file_url(file_path: str) -> str:
    return f"/files/download/{os.path.basename(file_path)}"

async def get_file_path(filename: str) -> str:
    return os.path.join(UPLOAD_DIR, filename)