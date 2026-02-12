from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "hi"}

@app.get("/hi")
def read_item():
    return "hi"