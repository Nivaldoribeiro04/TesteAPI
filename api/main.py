from fastapi import FastAPI, File, UploadFile
from typing import Annotated



app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello word"}

@app.get("/admin")
async def admin():
    return{"Admin": "Tela admin"}


@app.post("/files/")
async def create_file(file: Annotated[bytes, File()]):
    return{"file_size": len(file)}

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    return {"Tipo do arquivo": file.content_type}
