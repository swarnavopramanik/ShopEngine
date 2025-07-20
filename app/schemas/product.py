from pydantic import BaseModel, Field
from typing import Optional, List

class ProductSchema(BaseModel):
    name: str
    description: Optional[str] = ""
    price: float
    sizes: List[str]

class ProductResponse(ProductSchema):
    id: str
