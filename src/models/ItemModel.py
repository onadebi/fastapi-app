from typing import Optional

from pydantic import BaseModel


class ItemModel(BaseModel):
    item_id: int
    q: Optional[str] = None