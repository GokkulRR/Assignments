from fastapi import FastAPI
from pydantic import BaseModel

student_list = {}


class Name(BaseModel):
    Student_Name: str
    Course_Name: str
    Enroll_Month: str
    Duration: str
    Price: int


app = FastAPI()


@app.get("/")
async def get_input():
    return {"Welcome to Course Registering Platform!"}

@app.get("/get_all")
def get_all():
    return {"Student List": student_list}

@app.post("/course/{Application_no}")
async def sel_course(Application_no: int, request: Name):
    student_list[Application_no] = (request.dict())
    return student_list

@app.put("/update_course/{Application_no}")
def update_course(Application_no: int, update_course: Name):
    student_list.update({Application_no: update_course})
    return student_list

@app.delete("/delete_course/{Application_no}")
def delete_course(Application_no: int):
    del student_list[Application_no]
    return student_list