import user_requests
import user_data
import requests

# Проверка, что пользователь найден
def test_user_finded():
    responce = user_requests.get_user('GarryPotter')
    assert responce.status_code == 200
    assert responce.json()["id"] == user_data.user_body["id"]
    assert responce.json()["username"] == user_data.user_body["username"]
    assert responce.json()["firstName"] == user_data.user_body["firstName"]
    assert responce.json()["lastName"] == user_data.user_body["lastName"]
    assert responce.json()["email"] == user_data.user_body["email"]
    assert responce.json()["password"] == user_data.user_body["password"]
    assert responce.json()["phone"] == user_data.user_body["phone"]
    assert responce.json()["userStatus"] == user_data.user_body["userStatus"]

# Проверка, что пользователь не найден
def test_user_not_founded():
    responce = user_requests.get_user('Garry')
    assert responce.status_code == 404
    assert responce.json()["code"] == 1
    assert responce.json()["type"] == "error"
    assert responce.json()["message"] == "User not found"