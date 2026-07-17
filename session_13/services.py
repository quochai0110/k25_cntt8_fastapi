from fastapi import HTTPException
from models import Product
from schema import ProductCreate, ProductUpdate
# CÁC HÀM TƯƠNG TÁC VỚI DỮ LIỆU TRONG DB

# HÀM LẤY TẤT CẢ DANH SÁCH SẢN PHẨM

def get_all_product(db):
    return db.query(Product).all()
def get_product_detail(id: int, db):
    product = db.query(Product).filter(Product.id == id).first()
    if product is None:
        raise HTTPException(
            status_code=404,
            detail= "Không tìm thấy sản phẩm"
        )
    return {
        "message" : "Tìm thấy chi tiết sản phẩm thành công",
        "data": product
    }
    
# Hàm thêm sản phẩm vào database
def add_new_product(product:ProductCreate,db):
    new_product=Product(
        name=product.name,
        price=product.price
    )
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return{
        "message":"thêm sp thành công",
        "data":new_product
    }
    
def update_new_product(product_id:int, UpdateProduct:ProductUpdate, db):
    
    product =  db.query(Product).filter(Product.id == product_id).first()
    
    if product is None:
        raise HTTPException(
            status_code=404,
            detail=f"Không tìm thấy sản phẩm có id là {product_id}"
        )
        
    product.name = UpdateProduct.name
    product.price = UpdateProduct.price
    
    db.commit()
    db.refresh(product)
    
    return {
        "message": "Cập nhập thành công!",
        "Data": product
    }
    
def delete_product(product_id:int, db):
    product = db.query(Product).filter(Product.id == product_id).first()
    if product is None:
        raise HTTPException (
            status_code=404,
            detail="Không tìm thấy sản phâm để xóa"
        )
    db.delete(product)
    db.commit()
    return {
        "message": "Xóa sản phẩm thành công",
        "data": product
    }