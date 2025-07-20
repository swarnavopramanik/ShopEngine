from motor.motor_asyncio import AsyncIOMotorClient
from .config import MONGO_DETAILS, DATABASE_NAME

client = AsyncIOMotorClient(MONGO_DETAILS)
db = client[DATABASE_NAME]

product_collection = db.get_collection("products")
order_collection = db.get_collection("orders")
