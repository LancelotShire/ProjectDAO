from base_dao import BaseDAO
from db import db_instance as db
from bson import ObjectId

class StudentHomeworkDAO(BaseDAO):
    def __init__(self):
        super().__init__(db.get_collection("student_homework"))
    
    def find_by_student_id(self, student_id):
        return self.find_many({"student_id": student_id})
    
    def find_by_id(self, id):
        return self.find_one({"_id": ObjectId(id)})
    
