from base_dao import BaseDAO
from db import db_instance as db
from bson import ObjectId

class UserDAO(BaseDAO):
    def __init__(self):
        super().__init__(db.get_collection("users"))
    
    def find_by_id(self, id: ObjectId):
        return self.find_one({"_id": id})
    
    def find_by_account(self, account: str):
        return self.find_one({"account": account})
    
    def find_users(self):
        return self.find_many({})
    
    def update_user(self,id:ObjectId,name,type,password):
        return self.update_one({"_id": id}, {"$set": {
            "name": name,
            "type": type,
            "password": password
        }})
    
    def delete_user(self, id:ObjectId):
        return self.delete_one({"_id": id})
    
    def add_user(self, account, name, type, password):
        return self.insert_one({
            "account": account,
            "name": name,
            "type": type,
            "password": password
        })
    


    