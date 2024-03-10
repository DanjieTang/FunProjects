from fastapi import FastAPI

app = FastAPI()


@app.get("/hello")
def my_func() -> str:
    with open("storage/hey.txt", 'w') as file:
        file.write("Yo what's up")
    return "I love docker -- not, sike! loll. hahhaha. djdj"
