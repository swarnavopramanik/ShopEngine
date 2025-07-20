from fastapi import APIRouter, Query
from app.database import product_collection
from app.schemas.product import ProductSchema
from app.models.product import product_serializer
from bson import ObjectId
from typing import List

router = APIRouter()

@router.post("/products", status_code=201)
async def create_product(product: ProductSchema):
    result = await product_collection.insert_one(product.dict())
    new_product = await product_collection.find_one({"_id": result.inserted_id})
    return product_serializer(new_product)

@router.get("/products")
async def list_products(
    name: str = None,
    size: str = None,
    limit: int = 10,
    offset: int = 0
):
    query = {}
    if name:
        query["name"] = {"$regex": name, "$options": "i"}
    if size:
        query["sizes"] = size

    products = product_collection.find(query).skip(offset).limit(limit)
    return [product_serializer(p) async for p in products]
