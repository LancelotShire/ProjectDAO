from pymongo import MongoClient

class MongoDB:
    def __init__(self, uri="mongodb://localhost:27017/", db_name="smart_education_system"):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]

    def get_collection(self, collection_name):
        return self.db[collection_name]

# 获取数据库实例
db_instance = MongoDB()