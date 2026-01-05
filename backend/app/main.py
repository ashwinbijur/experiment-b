from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "EU Banking RAG Assistant backend is running"}

