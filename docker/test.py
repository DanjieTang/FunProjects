from fastapi import FastAPI

app = FastAPI()


@app.get("/hello")
def my_func() -> str:
    return "I love docker -- not, sike! loll. hahhaha. djdj"
