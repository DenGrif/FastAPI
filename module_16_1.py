from fastapi import FastAPI
from typing import Optional

app = FastAPI()

# Главная страница
@app.get("/")
async def read_main():
    return {"message": "Главная страница"}

# Администратор
@app.get("/user/admin")
async def read_admin():
    return {"message": "Вы вошли как администратор"}

# Пользователь с № user_id
@app.get("/user/{user_id}")
async def read_user(user_id: int):
    return {"message": f"Вы вошли как пользователь № {user_id}"}

# Пользователь с вводом данных в адресной строке
@app.get("/user")
async def read_user_info(username: Optional[str] = None, age: Optional[int] = None):
    return {"message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}
