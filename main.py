from fastapi import FastAPI, HTTPException
from pyairtable import Api
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

TOKEN = os.getenv("AIRTABLE_TOKEN")
BASE_ID = os.getenv("AIRTABLE_BASE_ID")
TABLE_NAME = os.getenv("TABLE_NAME")

api = Api(TOKEN)
table = api.table(BASE_ID, TABLE_NAME)


# Home Route
@app.get("/")
def home():
    return {"message": "FastAPI Airtable CRUD API"}


# GET ALL RECORDS
@app.get("/students")
def get_students():
    return table.all()


# GET ONE RECORD
@app.get("/students/{record_id}")
def get_student(record_id: str):
    try:
        return table.get(record_id)
    except:
        raise HTTPException(status_code=404, detail="Record not found")


# CREATE RECORD
@app.post("/students")
def create_student(name: str, course: str):

    record = table.create(
        {
            "NAME": name,
            "Course": course
        }
    )

    return {
        "message": "Student added successfully",
        "record": record
    }


# UPDATE RECORD
@app.put("/students/{record_id}")
def update_student(record_id: str, name: str, course: str):

    record = table.update(
        record_id,
        {
            "NAME": name,
            "Course": course
        }
    )

    return {
        "message": "Student updated successfully",
        "record": record
    }


# DELETE RECORD
@app.delete("/students/{record_id}")
def delete_student(record_id: str):

    table.delete(record_id)

    return {
        "message": "Student deleted successfully"
    }