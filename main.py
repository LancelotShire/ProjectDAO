from fastapi import FastAPI
from pydantic import BaseModel
from user_dao import UserDAO
from history_dao import HistoryDAO
from teach_dao import TeachDAO
from student_homework_dao import StudentHomeworkDAO
from homework_dao import HomeworkDAO
from question_dao import QuestionDAO
from bson import ObjectId
from datetime import datetime,timezone

app = FastAPI(docs_url="/docs",
              redoc_url="/redoc",
              openapi_url="/openapi.json")

# 学生DAO操作
# @app.get("/dao/student/getHomeworkList")
# def get_homework_list(student_id: str):
#     homeworks = StudentHomeworkDAO().find_by_student_id(ObjectId(student_id))
#     if homeworks is not None:
#         results = []
#         for h in homeworks:
#             dic = {'id':h['_id'], 'homeworkId': h['homework_id'], 'status': h['status'],'date':h['time']}
#             results.append(dic)
#     return {"code": 0, "message": "查询成功", "data": {'homeworkList': results}}

@app.get("/dao/student/getHomework")
def get_homework(homework_id: str):
    pass

class StudentHomeworkUpdate(BaseModel):
    id: str
    status: int
    scoreList: list
    answerList: list
    analysis: str
    recommendationList: list

@app.put("/dao/student/updateHomework")
def update_homework(homework: StudentHomeworkUpdate):
    id = homework.id
    status = homework.status
    scoreList = homework.scoreList
    answerList = homework.answerList
    analysis = homework.analysis
    recommendationList = homework.recommendationList
    count = StudentHomeworkDAO().update_student_homework(ObjectId(id), status, scoreList, recommendationList, analysis, answerList)
    if count == 0:
        return {"code": 1, "message": "更新失败，记录不存在"}
    else:
        return {"code": 0, "message": "更新成功"}

class DialogAdd(BaseModel):
    studentId: str

@app.post("/dao/student/addDialog")
def add_dialog(history: DialogAdd):
    student_id = history.studentId
    time = datetime.now(timezone.utc)
    id = HistoryDAO().add_history(ObjectId(student_id), time, [])
    return {"code": 0, "message": "添加成功，记录id为{}".format(id)}

class DialogUpdate(BaseModel):
    id: str
    dialog: list

@app.put("/dao/student/updateDialog")
def update_dialog(history: DialogUpdate):
    id = history.id
    dialog = history.dialog
    count = HistoryDAO().update_history(ObjectId(id), dialog)
    if count == 0:
        return {"code": 1, "message": "更新失败，记录不存在"}
    else:
        return {"code": 0, "message": "更新成功"}

@app.get("/dao/student/getDialogList")
def get_dialog_list(studentId: str):
    dialogs = HistoryDAO().find_histories(ObjectId(studentId))
    if dialogs is not None:
        results = []
        for d in dialogs:
            dic = {'id': d['_id'], 'studentId': d['student_id'], 'time': d['time'], 'dialog': d['dialogs']}
        results.append(dic)
    return {"code": 0, "message": "查询成功", "data": {'dialogList': results}}

@app.get("/dao/student/getDialog")
def get_dialog(dialogId: str):
    dialog = HistoryDAO().find_by_id(ObjectId(dialogId))
    if dialog is not None:
        dic = {'id': dialog['_id'], 'studentId': dialog['student_id'], 'time': dialog['time'], 'dialog': dialog['dialogs']}
    return {"code": 0, "message": "查询成功", "data": dic}

@app.get("/dao/student/getTeacherList")
def get_teacher_list(studentId: str):
    teachers = TeachDAO().find_teacher_by_student_id(ObjectId(studentId))
    if len(teachers) != 0:
        teachers = map(UserDAO.map, teachers)
    return {"code": 0, "message": "查询成功", "data": {'teacherList': teachers}}

# 教师DAO操作



# 基础人员管理
class UserAdd(BaseModel):
    account: str
    name: str
    type: int
    password: str

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
    
class UserUpdate(BaseModel):
    id: str
    name: str
    type: int
    password: str

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



