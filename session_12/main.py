""" 
VIẾT CÁC API

1. TEST API TRƯỚC
2. TẠO FILE CHỨA CẤU HÌNH DATABASE

"""
from fastapi import FastAPI,Depends
from sqlalchemy.orm import Session
from database import get_db
from models import Product
from services import get_all_product, get_product_detail
app = FastAPI()

@app.get("/")
def home():
    return{
        "message":"API đang chạy!"
    }

# API LẤY DANH SÁCH SẢN PHẨM
@app.get("/products")
def get_products(db:Session = Depends(get_db)):
    return get_all_product(db)

# API LẤY CHI TIẾT SẢN PHẨM
@app.get("products/{product_id}")
def get_product_by_id(product_id:int, db:Session=Depends(get_db)):
    return get_product_detail(product_id,db)