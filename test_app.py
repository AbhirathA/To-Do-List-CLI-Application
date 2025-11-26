from app import app

def test_home():
    client = app.test_client()
    res = client.get("/")
    assert res.status_code == 200
    assert res.json["message"] == "ToDo List App is running"

def test_greet():
    client = app.test_client()
    res = client.get("/hello/Pratham")
    assert res.status_code == 200
    assert res.json["greeting"] == "Hello, Pratham!"
