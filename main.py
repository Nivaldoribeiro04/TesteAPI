from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello word"}

@app.get("/admin")
async def admin():
    return{"Admin": "Tela admin"}