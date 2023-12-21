import uvicorn
from fastapi import FastAPI, Body
from pydantic import EmailStr, BaseModel


class CreateUser(BaseModel):
    email: EmailStr


app = FastAPI()

items = [
    "item 1",
    "item 2",
    "item 3",
]


@app.get("/")
def hello_index():
    return {
        "Message": "Hello index!",
    }


@app.get("/hello/")
def hello(name: str = "World") -> dict:
    return {
        "Message": f"Hello {name.strip().title()}!",
    }


@app.post("/users/")
def create_user(user: CreateUser):
    return {
        "message": "success",
        "email": user.email,
    }


@app.get("/items/")
def list_items() -> list[str]:
    return items


@app.get("/items/latest")
def get_item_latest() -> list[str]:
    return [items[-1]]


@app.get("/items/{item_id}/")
def get_item_(item_id: int):
    return {
        items[item_id]: {"id": item_id},
    }


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
