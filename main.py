
from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    id:int
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/items/{item_id}")
async def write_item(items:Item):
    return {"item_id": items.id}

@app.get("/items/{item_id}")
async def read_item(item_id:int):
    return {"item_id": item_id}