from fastapi import FastAPI

app = FastAPI()

my_list = []

@app.get("/{index}")
def get_function(index: int) -> str:
    if index < len(my_list):
        return my_list[index]
    else:
        return "Error: The index you requested doesn't exist"

@app.post("/")
def post_function(content: str) -> bool:
    my_list.append(content)
    return True

@app.put("/{index}")
def put_function(index: int, content: str) -> bool:
    if index < len(my_list):
        my_list[index] = content
        return True
    else:
        return False

@app.delete("/{index}")
def delete_function(index: int):
    if index < len(my_list):
        my_list.pop(index)
        return True
    else:
        return False