from fastapi import FastAPI
from app.routes import products, orders, users

app = FastAPI()

app.include_router(products.router)
app.include_router(orders.router)
app.include_router(users.router)
