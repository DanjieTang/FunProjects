from fastapi import FastAPI
from time import sleep

app = FastAPI()

@app.get("/api/user")
def loading():
    sleep(5)
    return "Thanks"