from fastapi import FastAPI
from langcorn import create_service
from decouple import config

app: FastAPI = create_service(
    "api.llm_chain:chain",
    "api.conversation_chain:conversation"
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/secret")
async def root():
    return {"secret": config("YOUR_SECRET_NAME")}


@app.post("/")
async def root():
    return {"message": "Hello World"}
