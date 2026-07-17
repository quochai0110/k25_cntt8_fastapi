from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from services import get_all_product, get_product_detail,add_new_product, update_new_product, delete_product
from schema import ProductCreate, ProductUpdate
# TẠO CÁC API 

router = APIRouter(
    prefix="/products",
    tags= ["Product"]
)
# VIẾT API LẤY CẢ SẢN PHẨM
@router.get("")
def get_products(db:Session= Depends(get_db)):
    return {
        "message":"lấy danh sách sản phẩm thành công",
        "data"   : get_all_product(db)
    }
    
# VIẾT API LẤY CHI TIẾT SẢN PHẨM
@router.get("/{product_id}")
def get_product_by_id(product_id: int, db: Session= Depends(get_db)):
    return get_product_detail(product_id, db)

#VIẾT API THÊM SẢN PHẨM

@router.post("")
def add_product(product:ProductCreate,db:Session=Depends(get_db)):
    return add_new_product(product,db)

@router.put("/{product_id}")
def update_product(product_id: int,product:ProductCreate,db:Session=Depends(get_db)):
    return update_new_product(product_id,product,db)

@router.delete("/{product_id}")
def delete_product_by_id(product_id: int, db:Session=Depends(get_db)):
    return delete_product(product_id, db)