from app import app

def test_health():
    client = app.test_client()
    r = client.get('/health')
    assert r.status_code == 200
    assert r.json['status'] == 'ok'

def test_get_user():
    client = app.test_client()
    r = client.get('/user/1')
    assert r.status_code == 200
    assert r.json['id'] == '1'