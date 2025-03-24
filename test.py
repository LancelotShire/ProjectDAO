from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test():
    response = client.get("/hello")  # 发送 GET 请求
    assert response.status_code == 200  # 断言状态码
    assert response.json() == {"message": "Hello, FastAPI"}  # 断言返回数据

