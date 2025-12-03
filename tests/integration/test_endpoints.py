import requests

BASE = 'http://REPLACE_INGRESS_HOST'

def test_user_health():
    r = requests.get(f'{BASE}/user/health')
    assert r.status_code == 200

def test_order_health():
    r = requests.get(f'{BASE}/order/health')
    assert r.status_code == 200