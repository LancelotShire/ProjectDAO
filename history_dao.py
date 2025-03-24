from base_dao import BaseDAO
from db import db_instance as db
from bson import ObjectId

class historyDAO(BaseDAO):
    def __init__(self):
        super().__init__(db.get_collection('history'))
    
    def find_histories(self, user_id: ObjectId):
        return self.find_many({'user_id': user_id})
    
    def find_by_id(self, id: ObjectId):
        return self.find_one({'_id': id})