from fastapi import FastAPI
from pydantic import BaseModel
from user_dao import UserDAO

app = FastAPI()

class User(BaseModel):
    account: str
    name: str
    type: int
    password: str

@app.post("/dao/user")
def add_user(user: User):
    account = user.account
    name = user.name
    type = user.type
    password = user.password
    if UserDAO().find_by_account(account) is not None:
        return {"code": 1, "message": "添加失败，用户已存在"}
    else:
        id = UserDAO().add_user(account, name, type, password)
        return {"code": 0, "message": "添加成功，记录id为{}".format(id)}

@app.delete("/dao/user/")
def delete_user(account: str):
    count = UserDAO().delete_user(account)
    if count == 0:
        return {"code": 1, "message": "删除失败，记录不存在"}
    else:
        return {"code": 0, "message": "删除成功"}

@app.put("/dao/user")
def update_user(user: User):
    account = user.account
    name = user.name
    type = user.type
    password = user.password
    count = UserDAO().update_user(account, name, type, password)
    if count == 0:
        return {"code": 1, "message": "更新失败，记录不存在"}
    else:
        return {"code": 0, "message": "更新成功"}

@app.get("/dao/user/")
def find_user(account: str):
    user = UserDAO.map(UserDAO().find_by_account(account))
    if user is None:
        return {"code": 1, "message": "查询失败，记录不存在"}
    else:
        return {"code": 0, "message": "查询成功", "data": user}


@app.get("/dao/user/getUserList")
def find_all():
    users = map(UserDAO.map,UserDAO().find_users())
    return {"code": 0, "message": "查询成功", "data": {'userList': users}}





