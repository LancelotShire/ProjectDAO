from pymongo import collection as collection

class BaseDAO:
    def __init__(self, collection: collection.Collection):
        self.collection = collection

    def insert_one(self, data):
        return self.collection.insert_one(data).inserted_id

    def insert_many(self, data_list):
        return self.collection.insert_many(data_list).inserted_ids

    def find_one(self, query):
        return self.collection.find_one(query)

    def find_many(self, query, limit=10):
        return list(self.collection.find(query).limit(limit))

    def update_one(self, query, update_data):
        return self.collection.update_one(query, {"$set": update_data}).modified_count

    def delete_one(self, query):
        return self.collection.delete_one(query).deleted_count

    def delete_many(self, query):
        return self.collection.delete_many(query).deleted_count
    
    @staticmethod
    def map(x):
        x['id'] = str(x['_id'])
        del x['_id']
        return x

