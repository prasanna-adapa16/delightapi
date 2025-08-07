import requests
from config import API_BASE

def register_user(data):
    return requests.post(f"{API_BASE}/register/", json=data)

def login_user(data):
    return requests.post(f"{API_BASE}/login/", json=data)

def get_cakes():
    try:
        res = requests.get(f"{API_BASE}/cakes/")
        if res.status_code == 200:
            return res.json()
        return []
    except Exception as e:
        print("Error:", e)
        return []




