from base_dao import BaseDAO
from db import db_instance as db
from bson import ObjectId
from datetime import datetime

class HistoryDAO(BaseDAO):
    def __init__(self):
        super().__init__(db.get_collection('history'))
    
    def find_histories(self, student_id: ObjectId):
        return self.find_many({'student_id': student_id})
    
    def find_by_id(self, id: ObjectId):
        return self.find_one({'_id': id})
    
    def add_history(self, student_id: ObjectId, time: datetime, dialogs: list):
        return self.insert_one({
            'student_id': student_id,
            'time': time,
            'dialogs': dialogs
        })

    def update_history(self, history_id: ObjectId, dialogs: list):
        return self.update_one({'_id': history_id}, {'$set': {
            'dialogs': dialogs
        }})