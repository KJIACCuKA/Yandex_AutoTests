import petstore_user_API.requests.user_requests as user_requests
import petstore_user_API.data.user_data as user_data
import requests

# Проверка, что данные пользователя изменяются
def test_user_data_changed():
    user_requests.create_user(user_data.user_body_for_change)
    responce = user_requests.change_user_data(user_data.changed_user_body, 'FirstSecond')
    assert responce.status_code == 200
    assert responce.json()["code"] == 200
    assert responce.json()["type"] == "unknown"
    assert responce.json()["message"] == f'{user_data.changed_user_body["id"]}'

# Проверка, что измененный пользователь найден
def test_changed_user_finded():
    responce = user_requests.get_user('FirstSecond')
    assert responce.status_code == 200

# Проверка, что измененный пользователь имеет корректные данные в теле
def test_changed_user_data():
    responce = user_requests.get_user('FirstSecond')
    assert responce.status_code == 200
    assert responce.json()["id"] == user_data.changed_user_body["id"]
    assert responce.json()["username"] == user_data.changed_user_body["username"]
    assert responce.json()["firstName"] == user_data.changed_user_body["firstName"]
    assert responce.json()["lastName"] == user_data.changed_user_body["lastName"]

# Проверка, что данные пользователя изменились, а не создался новый пользователь с новыми даными
def test_old_user_data_not_found():
    responce = user_requests.get_user('FirstSecond')
    assert responce.json()["id"] == user_data.user_body_for_change["id"]
    assert responce.json()["username"] == user_data.user_body_for_change["username"]
    assert responce.json()["firstName"] != user_data.user_body_for_change["firstName"]
    assert responce.json()["lastName"] != user_data.user_body_for_change["lastName"]
    assert responce.json()["email"] != user_data.user_body_for_change["email"]
    assert responce.json()["password"] != user_data.user_body_for_change["password"]
    assert responce.json()["phone"] != user_data.user_body_for_change["phone"]
    assert responce.json()["userStatus"] != user_data.user_body_for_change["userStatus"]