from fastapi import FastAPI, UploadFile, File

# import uvicorn

app = FastAPI()

@app.get("/ping")
async def ping():
    return "hello, i am alive"

@app.post("/predict")
async def predict(
    file: UploadFile = File(...)
):
    bytes = await file.read()

    return
    
