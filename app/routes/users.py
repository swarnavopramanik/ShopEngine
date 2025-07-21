# app/routes/users.py

from fastapi import APIRouter
import pandas as pd

router = APIRouter()

@router.get("/users", summary="Get all users from CSV")
def get_users():
    try:
        df = pd.read_csv("users.csv")
        users = df.to_dict(orient="records")
        return {"status": "success", "users": users}
    except FileNotFoundError:
        return {"status": "error", "message": "users.csv file not found"}
