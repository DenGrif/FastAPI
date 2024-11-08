from fastapi import FastAPI, status, Body, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

message_db = []

class Message(BaseModel):
    id: int = None
    text: str

@app.get("/")
def get_all_message() -> List[Message]:
    return message_db

@app.get(path="/message/{message_id}")
def get_message(message_id: int) -> Message:
    try:
        return message_db[message_id]
    except IndexError:
        raise HTTPException(status_code=404, detail="Message not found")

@app.post("/message")
def create_message(message: Message) -> str:
    message.id = len(message_db)
    message_db.append(message)
    return f"Message created!"

@app.put("message/{message_id}")
def update_message(message_id: int, message: str = Body()) -> str:
    try:
        edit_message = message_db[message_id]
        edit_message.text = message
        return f"Message updated!"
    except IndexError:
        raise HTTPException(status_code=404, detail="Message not found")

@app.delete("message/{message_id}")
def delete_message(message_id: int) -> str:
    try:
        message_db.pop(message_id)
        return f"Message ID={message_id} deleted!"
    except IndexError:
        raise HTTPException(status_code=404, detail="Message not found")

@app.delete("/")
def kill_message_all() -> str:
    message_db.clear()
    return "ALL messages deleted!"
