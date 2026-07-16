# TẠO CÁC BẢNG GIỐNG NHƯ CÁC BẢNG TRONG MYSQL
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import declarative_base

Base = declarative_base()
class Product (Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name= Column(String(50), nullable=False)
    price= Column(Float, nullable=False)
# class User (Base)
# class Order 
# class Cart


    
    