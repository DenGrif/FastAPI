from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def welcome() -> dict:
    return {"message": "Hello World"}

@app.get("/user/A/B")
async def news() -> dict:
    return {"message": f"Hello, Tester"} # чтоб вывести пишется: http://127.0.0.1:8000/id?username=user&age=44

@app.get("/id")
async def id_paginator(username: str = "Den", age: int = 44) -> dict:
    return {"User": username, "Age": age}

# @app.get("/user/{first_name}/{last_name}")
# async def news(first_name: str, last_name: str) -> dict:
#     return {"message": f"Здорова товарищ, {first_name}/{last_name}"}

