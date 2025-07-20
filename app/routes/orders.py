from fastapi import APIRouter
from app.database import order_collection
from app.schemas.order import OrderSchema
from app.models.order import order_serializer
from bson import ObjectId

router = APIRouter()

@router.post("/orders", status_code=201)
async def create_order(order: OrderSchema):
    result = await order_collection.insert_one(order.dict())
    new_order = await order_collection.find_one({"_id": result.inserted_id})
    return order_serializer(new_order)

@router.get("/orders", summary="Get all orders")
async def get_all_orders(limit: int = 10, offset: int = 0):
    orders = order_collection.find().skip(offset).limit(limit)
    return [order_serializer(order) async for order in orders]

@router.get("/orders/{user_id}", summary="Get orders for a user")
async def get_orders(user_id: str, limit: int = 10, offset: int = 0):
    orders = order_collection.find({"user_id": user_id}).skip(offset).limit(limit)
    return [order_serializer(order) async for order in orders]
