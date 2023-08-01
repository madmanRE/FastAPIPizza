from fastapi import APIRouter


order_router = APIRouter(
    prefix='/orders',
    tags=['Orders'],
)


@order_router.get("/")
async def hello():
    return {"message": "Hellow World!"}