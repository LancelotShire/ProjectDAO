from base_dao import BaseDAO
from db import db_instance as db
from bson import ObjectId

class QuestionDAO(BaseDAO):
    def __init__(self):
        super().__init__(db.get_collection("questions"))