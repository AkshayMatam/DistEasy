from fastapi import APIRouter
from services.product_service import get_all_products

router = APIRouter()


@router.get("/products")
def products():
    return {
        "products": get_all_products()
    }