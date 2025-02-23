from app import app

def test_home():
    res = app.test_client().get('/')

    assert res.status_code == 200
    assert res.data == b'Hello World!'
