from fastapi import FastAPI
from pydantic import BaseModel
from user_dao import UserDAO
from history_dao import HistoryDAO
from teach_dao import TeachDAO
from bson import ObjectId
from datetime import datetime,timezone

app = FastAPI(docs_url="/docs",
              redoc_url="/redoc",
              openapi_url="/openapi.json")

class UserAdd(BaseModel):
    account: str
    name: str
    type: int
    password: str

class UserUpdate(BaseModel):
    id: str
    name: str
    type: int
    password: str

class DialogAdd(BaseModel):
    student_id: str
    dialog: list

# 学生DAO操作
@app.post("/dao/student/addDialog")
def add_dialog(history: DialogAdd):
    student_id = history.student_id
    dialog = history.dialog
    time = datetime.now(timezone.utc)
    id = HistoryDAO().add_history(ObjectId(student_id), time, dialog)
    return {"code": 0, "message": "添加成功，记录id为{}".format(id)}

@app.get("/dao/student/getDialogList")
def get_dialog_list(student_id: str):
    dialogs = HistoryDAO().find_histories(ObjectId(student_id))
    if dialogs is not None:
        dialogs = map(HistoryDAO.map, dialogs)
    return {"code": 0, "message": "查询成功", "data": {'dialogList': dialogs}}

@app.get("/dao/student/getDialog")
def get_dialog(dialog_id: str):
    dialog = HistoryDAO().find_by_id(ObjectId(dialog_id))
    if dialog is not None:
        dialog = HistoryDAO.map(dialog)
    return {"code": 0, "message": "查询成功", "data": dialog}

@app.get("/dao/student/getTeacherList")
def get_teacher_list(student_id: str):
    teachers = TeachDAO().find_teacher_by_student_id(ObjectId(student_id))
    if len(teachers) != 0:
        teachers = map(UserDAO.map, teachers)
    return {"code": 0, "message": "查询成功", "data": {'teacherList': teachers}}

# 教师DAO操作



# 基础人员管理
@app.post("/dao/user")
def add_user(user: UserAdd):
    account = user.account
    name = user.name
    type = user.type
    password = user.password
    if UserDAO().find_by_account(account) is not None:
        return {"code": 1, "message": "添加失败，用户已存在"}
    else:
        id = UserDAO().add_user(account, name, type, password)
        return {"code": 0, "message": "添加成功，记录id为{}".format(id)}

@app.delete("/dao/user")
def delete_user(id: str):
    count = UserDAO().delete_user(ObjectId(id))
    if count == 0:
        return {"code": 1, "message": "删除失败，记录不存在"}
    else:
        return {"code": 0, "message": "删除成功"}

@app.put("/dao/user")
def update_user(user: UserUpdate):
    id = user.id
    name = user.name
    type = user.type
    password = user.password
    count = UserDAO().update_user(ObjectId(id), name, type, password)
    if count == 0:
        return {"code": 1, "message": "更新失败，记录不存在"}
    else:
        return {"code": 0, "message": "更新成功"}

@app.get("/dao/user")
def find_user(id: str):
    user = UserDAO().find_by_account(ObjectId(id))
    if user is not None:
        user = UserDAO.map(user)
    return {"code": 0, "message": "查询成功", "data": user}


@app.get("/dao/user/getUserList")
def get_user_list():
    users = UserDAO().find_users()
    if len(users) != 0:
        users = map(UserDAO.map, users)
    return {"code": 0, "message": "查询成功", "data": {'userList': users}}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)



