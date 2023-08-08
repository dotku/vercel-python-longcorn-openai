from fastapi import FastAPI
from langcorn import create_service

app: FastAPI = create_service(
    "api.llm_chain:chain",
    "api.conversation_chain:conversation"
)


@app.get("/")
async def root():
    return {"message": "Hello World"}
