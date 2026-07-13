from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()
""" 
    METHOD:
    get: lấy dữ liệu
    post: thêm dữ liệu
    put, patch : cập nhật
    delete: xóa dữ liệu 
    
"""
students = [
    {
        "id":1,
        "name":"Bích Ngọc",
        "email":"ngoc@gmail.com"
    },
    {
        "id":2,
        "name":"Khắc Hưng",
        "email":"hung@gmail.com"
    }
]

class StudentCreate(BaseModel):

    name: str 
    email: str
    
    
@app.get("/")
def home():
    return {
        "message": "api đang chạy"
    }
#  lấy danh sách sinh viên của lớp CNTT8
# VIẾT API LẤY TẤT CẢ DANH SÁCH SINH VIÊN LỚP CNTT8
@app.get("/students")
def get_students():
    return {
        "message":"lấy danh sách sinh viên thành công!",
        "data"   : students
    }
# VIẾT API LẤY CHI TIẾT 1 SINH VIÊN THÔI
@app.get("/students/{student_id}")
def get_student_detail(student_id:int):
    print("id sinh viên là", student_id)
    for student in students:
        if student["id"] == student_id:
            return {
                "message":"lấy chi tiết sinh viên thành công",
                "data"   : student
            }
    return {
        "message":"không tìm thấy sinh viên",
        "data"   : None
    }
# VIẾT API THÊM MỚI SINH VIÊN
@app.post("/students")
def add_student(new_student: StudentCreate):
    print("new_student",new_student)
    new_id=len(students)+1
    add_new_student = {
        "id": new_id,
        "name": new_student.name,
        "email": new_student.email
    }
    students.append(add_new_student)
    return {
        "message":"thêm sinh viên thành công",
        "data"   : students
    }

#  VIẾT API XÓA SINH VIÊN 
@app.delete("/students/{student_id}")
def delete_student(student_id:int):
    print("id sinh viên cần xóa", student_id)
    for std in students:
        if std["id"]== student_id:
            students.remove(std)
            return{
                "message":"xóa sinh viên thành công!",
                "data"   : std
            }
    return {
        "message":"không tìm thấy sinh viên",
        "data"   : None
    }
# API CẬP NHẬT THÔNG TIN SINH VIÊN
@app.put("/students/{student_id}")
def update_student(student_id:int, update_student:StudentCreate):
    for std in students:
        if std["id"] == student_id:
            std["name"] = update_student.name
            std["email"] = update_student.email
            return{
                "message":"cập nhật sinh viên thành công",
                "data"   : students 
            }
    return{
        "message":"không tìm thấy sinh viên",
        "data"   : None
    }
              


