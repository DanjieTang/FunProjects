from fastapi import FastAPI

app = FastAPI()

@app.get("/funny_words")
def say_smt_funny() -> str:
    return "Hahaha"