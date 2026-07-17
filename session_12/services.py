# Viết hàm lấy dữ liệu từ database

# hàm lấy danh sách sản phẩm
from fastapi import HTTPException
from models import Product
def get_all_product(db):
    products = db.query(Product).all()
    return {
        "message":"lấy danh sách sản phẩm thành công!",
        "data"   :products
    }

# hàm lấy chi tiết sản phẩm
def get_product_detail(product_id:int,db):
    product = db.query(Product).filter(Product.id== product_id).first()
    if product is None:
        raise HTTPException(
            status_code= 404,
            detail="không tìm thấy sản phẩm"
        )
    return {
        "message":"tìm thấy sản phẩm thành công!",
        "data"   : product
    }
# hàm thêm sản phẩm

# hàm xóa sản phẩm

# hàm cập nhật sản phẩm


    