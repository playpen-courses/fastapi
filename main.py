from fastapi import FastAPI, Path

from typing import Optional

from pydantic import BaseModel

app = FastAPI()

students = {
 1: {
  "name": "john",
  "age": "18",
  "year": "year 12"
 },
 2: {
  "name": "abadi",
  "age": "32",
  "year": "year21"
 }
}

class Students(BaseModel):
 name: str
 age: int
 year: str

class UpdateStudents(BaseModel):
 name: Optional[str] = None
 age: Optional[int] = None
 year: Optional[str] = None

@app.get("/")
def index():
 return {"name": "First Data"}

@app.get("/get-students")
def get_students():
 return students

@app.get("/get-students/{student_id}")
def get_student(student_id: int):
 return students[student_id]

@app.get("/get-student-name")
def get_student(*, name: Optional[str] = None, test: int):
 for student_id in students:
  print(student_id)
  if students[student_id]["name"] == name:
   return students[student_id]
  
 return {"data": "Student doesn't exist"}

@app.get("/get-students/{student_id}")
def get_students_query(student_id: int, name: Optional[str] = None):
 if student_id:
  return 
 
@app.post("/create-student")
def create_student(student: Students):
 # name = student.name
 # for stu_id in students:
 #  if students[stu_id]["name"] == name:
 #   return {"Error": "Student is already exist"}
 
 student_id = len(students)
 students[student_id] = student

 return {"Status": "User Created", "Data": students[student_id]}

@app.put("/update-student/{student_id}")
def update_student(student_id: int, student : UpdateStudents):
 if student_id not in students:
  return {"Error": "Student doesn't exist"}
 
 if student.name != None: 
  students[student_id]["name"] = student.name
 if student.age != None:
  students[student_id]["age"] = student.age
 if student.year != None:
  students[student_id]["year"] = student.year

 return {"Status": "Student Updated", "Date": students[student_id]}

@app.delete("/delete-student/{student_id}")
def delete_student(student_id: int):
 if student_id not in students:
  return {"Error": "Student doesn't exist"}
 
 students.pop(student_id)

 return students