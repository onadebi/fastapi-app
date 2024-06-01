from typing import Union
import json;

from fastapi import FastAPI
from models.GenResponse import GenResponse
from models.ItemModel import ItemModel

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None) -> GenResponse[Union[ItemModel, None]]:
    item: ItemModel = ItemModel(item_id=item_id, q=q)
    return GenResponse().success(data=item, message="Item retrieved successfully");

if __name__ == "__main__":
    print(f"Running {__file__}...")