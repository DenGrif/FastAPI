from fastapi import FastAPI, Path, HTTPException, status
from typing import Annotated

app = FastAPI()

# Инициализируем словарь пользователей
users = {'1': 'Имя: Example, возраст: 18'}

# GET запрос для получения всех пользователей
@app.get("/users")
async def get_users():
    if not users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No users found")
    return users

# POST запрос для добавления нового пользователя
@app.post("/user/{username}/{age}")
async def create_user(
    username: Annotated[str, Path(title="Enter username", min_length=5, max_length=20)],
    age: Annotated[int, Path(title="Enter age", ge=18, le=120)]
):
    new_id = str(int(max(users.keys(), key=int)) + 1)  # Генерируем новый ID
    users[new_id] = f"Имя: {username}, возраст: {age}"
    return {"message": f"User {new_id} is registered"}

# PUT запрос для обновления данных пользователя по user_id
@app.put("/user/{user_id}/{username}/{age}")
async def update_user(
    user_id: Annotated[str, Path(title="Enter User ID")],
    username: Annotated[str, Path(title="Enter username", min_length=5, max_length=20)],
    age: Annotated[int, Path(title="Enter age", ge=18, le=120)]
):
    if user_id not in users:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with ID {user_id} not found"
        )
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return {"message": f"User {user_id} has been updated"}

# DELETE запрос для удаления пользователя по user_id
@app.delete("/user/{user_id}")
async def delete_user(user_id: Annotated[str, Path(title="Enter User ID")]):
    if user_id not in users:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with ID {user_id} not found"
        )
    del users[user_id]
    return {"message": f"User {user_id} has been deleted"}
