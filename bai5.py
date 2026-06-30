from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

students = [
    {
    "full_name": "Nguyen Van A",
    "email": "vana@gmail.com",
    "age": 20,
    "course": "python",
    "phone": "0987654321"
    }
]

class CreateStudent(BaseModel):
    full_name: str = Field(min_length=3)
    email: str = Field(pattern=r'^[^\s@]+@[^\s@]+\.[^\s@]+$')
    age: int = Field(ge = 15, le = 60)
    phone: str = Field(pattern='^(0|\+84)(3|5|7|8|9)\d{8}$', min_length=10, max_length=11)
    course: str
    note: str | None = Field(max_length=200)
    
    
@app.post('/students/register')
def create_students(student: CreateStudent):
    for stu in students:
        if student.email == stu.get('email'): 
            return {
                    "detail": "Email đã tồn tại trong hệ thống"
                    }
            
    new_stu = {
        'full_name': student.full_name,
        'email': student.email,
        'age': student.age,
        'phone': student.phone,
        'course': student.course,
        'note': student.note
    }
    students.append(new_stu)
    return {
        "message": "Đăng ký học viên thành công",
        "data": new_stu
}