from pydantic import BaseModel
from typing import List

class OrderSchema(BaseModel):
    user_id: str
    product_ids: List[str]

class OrderResponse(OrderSchema):
    id: str
