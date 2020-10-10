from typing import Optional, List

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None

class Page(BaseModel):
    title: str
    description: str
    text: str

class Folder(BaseModel):
    title: str
    description: str
    pages: List[Page]

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}

@app.post("/printcontent")
def print_folder(content: Folder):
    print(content.title)
    return {"Hello": "World"}
