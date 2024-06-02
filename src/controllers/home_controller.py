from typing import Union
from fastapi import APIRouter;

from ..models.GenResponse import GenResponse;
from ..models.ItemModel import ItemModel
from  ..config.appsettings import AppSettings
from ..main import app;


class HomeController:
    router = APIRouter()

    @router.get("/")
    async def read_root():
        app_name: str = AppSettings.APP_NAME.value;
        return {"Hello": f"World {app_name} with type {type(AppSettings)} - {AppSettings.__members__}"}


    @router.get("/items/{item_id}")
    async def read_item(item_id: int, q: Union[str, None] = None) -> GenResponse[Union[ItemModel, None]]:
        item: ItemModel = ItemModel(item_id=item_id, q=q)
        return GenResponse().success(data=item, message="Item retrieved successfully");

    @router.get("/list/{item_id}")
    async def read_item(item_id: str, q: str | None = None, short: bool = False):
        item = {"item_id": item_id}
        if q:
            item.update({"q": q})
        if not short:
            item.update(
                {"description": "This is an amazing item that has a long description"}
            )
        return item

    @router.get("/users/{user_id}/items/{item_id}")
    async def read_user_item(
        user_id: int, item_id: str, q: str | None = None, short: bool = False
    ):
        '''
        This function reads a user list of items.\n
        You want to pass the user_id and item_id as path parameters.
        '''
        item = {"item_id": item_id, "owner_id": user_id}
        if q:
            item.update({"q": q})
        if not short:
            item.update(
                {"description": "This is an amazing item that has a long description"}
            )
        return item
