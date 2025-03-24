from base_dao import BaseDAO
from db import db_instance as db
from bson import ObjectId

class StudentHomeworkDAO(BaseDAO):
    def __init__(self):
        super().__init__(db.get_collection("student_homework"))
    
    def find_by_student_id(self, student_id):
        return self.find_many({"student_id": student_id})
    
    def find_by_id(self, id: ObjectId):
        return self.find_one({"_id": id})
    
    def update_student_homework(self, id: ObjectId, status, scores, recommended_questions, analysis, answers):
        return self.update_one({"_id": id}, {
            "$set": {"status": status, "scores": scores, "recommended_questions": recommended_questions, "analysis": analysis, "answers": answers}
        })
    
