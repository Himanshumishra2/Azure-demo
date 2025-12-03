from app import app

def test_health():
    client = app.test_client()
    r = client.get('/health')
    assert r.status_code == 200

def test_get_order():
    client = app.test_client()
    r = client.get('/order/42')
    assert r.status_code == 200
    assert r.json['id'] == '42'