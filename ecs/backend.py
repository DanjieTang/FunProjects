from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def say_smt_funny() -> str:
    return "Lmfao"
