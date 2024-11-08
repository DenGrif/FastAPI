from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# Пустой список
users = []

# Модель User
class User(BaseModel):
    id: int
    username: str
    age: int

# GET запрос для получения всех пользователей
@app.get("/users", response_model=List[User])
def get_all_users():
    return users

# POST запрос для добавления нового пользователя
@app.post("/user/{username}/{age}", response_model=User)
def create_user(username: str, age: int):
    # Установка ID: если список пуст, то ID будет 1, иначе ID будет на 1 больше, чем у последнего пользователя
    new_id = users[-1].id + 1 if users else 1
    new_user = User(id=new_id, username=username, age=age)
    users.append(new_user)
    return new_user

# PUT запрос для обновления данных пользователя по user_id
@app.put("/user/{user_id}/{username}/{age}", response_model=User)
def update_user(user_id: int, username: str, age: int):
    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return user
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User was not found")

# DELETE запрос для удаления пользователя по user_id
@app.delete("/user/{user_id}", response_model=User)
def delete_user(user_id: int):
    for index, user in enumerate(users):
        if user.id == user_id:
            return users.pop(index)
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User was not found")
