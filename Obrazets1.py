from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

@app.get("/")
async def welcome() -> dict:
    return {"message": "Hello World"}

@app.get("/user/A/B")
async def news() -> dict:
    return {"message": f"Hello, Tester!"}


@app.get("/user/{username}/{id}")
async def news(username: Annotated[str,Path(min_length=3, max_length=15, description="Enter your username", example="montes")]
               , id:int = Path(ge=80, le=100, description="Enter your id", example="75")) -> dict:
    return {"message": f"Hello, {username} {id}"} # чтоб вывести пишется: http://127.0.0.1:8000/id?username=user&age=44



# @app.get("/user/{first_name}/{last_name}")
# async def news(first_name: str, last_name: str) -> dict:
#     return {"message": f"Здорова товарищ, {first_name}/{last_name}"}

# @app.get("/id")
# async def id_paginator(username: str = "Den", age: int = 44) -> dict:
#     return {"User": username, "Age": age}
