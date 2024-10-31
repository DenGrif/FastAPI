from fastapi import FastAPI

app = FastAPI

@app.get("/")
async def welcome() -> dict:
    return {"message": "Hello World"}

# @app.get("/main")
# async def welcome() -> dict:
#     return {"message": "Main page"}


# Get - адрес в строке: ?переменная=значение
# Post - формы - оформить заказ в магазине
# Put - Обновляет
# Delete - удаляет

# @app.get("/")
# async def welcome() -> dict:
#     return {"message": "Hello World"}