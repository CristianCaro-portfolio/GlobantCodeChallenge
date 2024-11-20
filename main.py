from fastapi import FastAPI
from routes import data_upload  # import module manage load of data

app = FastAPI()

app.include_router(data_upload.router)

@app.get("/")
async def root():
    return {"message": "Hello, World! The API is running."}
