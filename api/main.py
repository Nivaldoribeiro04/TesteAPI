from io import BytesIO
from fastapi import FastAPI, File, UploadFile
from typing import Annotated
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd


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
    return {"Message":"Página Admin"}


@app.post("/files/")
async def create_file(file: Annotated[bytes, File()]):
    return{"file_size": len(file)}

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    if file.content_type != "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet":
         return{"Erro": "Aquivo não é valido, por favor coloque um no formato xlsx ou xls"}
    
    else:
        df =pd.DataFrame()
        file_content = await file.read()
        # Converte os bytes em um objeto BytesIO (buffer)
        excel_data = BytesIO(file_content)
        # Usa pandas para ler o Excel
        df = pd.read_excel(excel_data, engine='openpyxl')

        result = []
        for index, row in df.iterrows():
            if row.dropna().any():  # Verifica se há algum valor não nulo
                result.append(row.to_dict())  # Adiciona a linha se não for vazia
                
        # Se o resultado não estiver vazio, converter para JSON
        if result:
            df_filtered = pd.DataFrame(result)  # Cria um novo dataframe com as linhas filtradas
            json_result = df_filtered.to_json(orient="records")  # Converte para JSON
            return {"Retorno Arquivo Json": json_result}
