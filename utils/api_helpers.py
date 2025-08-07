import requests

BASE_URL = "http://127.0.0.1:8000/api"

def get_cart(token):
    headers = {"Authorization": f"Token {token}"}
    return requests.get(f"{BASE_URL}/cart/", headers=headers).json()

def remove_item(item_id, token):
    headers = {"Authorization": f"Token {token}"}
    return requests.delete(f"{BASE_URL}/cart/remove/{item_id}/", headers=headers)

def place_order(token):
    headers = {"Authorization": f"Token {token}"}
    return requests.post(f"{BASE_URL}/orders/", headers=headers).json()
