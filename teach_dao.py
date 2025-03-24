from base_dao import BaseDAO
from db import db_instance as db
from bson import ObjectId

class TeachDAO(BaseDAO):
    def __init__(self):
        super().__init__(db.get_collection("teach"))
    
    def add_teach(self,student_id:ObjectId,teacher_id:ObjectId):
        return self.insert_one({"student":student_id,"teacher":teacher_id})
    