from base_dao import BaseDAO
from db import db_instance as db
from bson import ObjectId

class UserDAO(BaseDAO):
    def __init__(self):
        super().__init__(db.get_collection("users"))
    
    def find_by_id(self, user_id: ObjectId):
        return self.find_one({"_id": user_id})
    
    def find_by_account(self, account: str):
        return self.find_one({"account": account})
    
    def find_by_name(self, name: str):
        return self.find_many({"name": name})
    
    def find_users(self):
        return self.find_many({})
    
    def find_student_by_account(self, account: str):
        return self.find_one({"account": account,"type":"1"})
    
    def find_students(self):
        return self.find_many({"type":"1"})

    
    def update_user(self,account,name,type,password):
        return self.update_one({"account": account,}, {"$set": {
            "name": name,
            "type": type,
            "password": password
        }})
    
    def delete_user(self, account):
        return self.delete_one({"account": account})
    
    def add_user(self, account, name, type, password):
        return self.insert_one({
            "account": account,
            "name": name,
            "type": type,
            "password": password
        })
    


    