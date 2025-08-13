from fastapi import FastAPI, File, UploadFile
from typing import Annotated
from fastapi.middleware.cors import CORSMiddleware




app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos os métodos HTTP
    allow_headers=["*"],  # Permite todos os cabeçalhos
)


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
