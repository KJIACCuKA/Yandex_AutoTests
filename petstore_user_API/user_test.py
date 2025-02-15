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

# Проверка, что пользователь создается
def test_user_created():
    responce = user_requests.create_user(user_data.user_body)
    assert responce.status_code == 200
    assert responce.json()["code"] == 200
    assert responce.json()["type"] == "unknown"
    assert responce.json()["message"] == "1"

# В документации позволено создать пользователя без данных
def test_user_created_with_body_without_params():
    responce = user_requests.create_user(user_data.user_body_without_params)
    assert responce.status_code == 200
    assert responce.json()["code"] == 200
    assert responce.json()["type"] == "unknown"
    assert responce.json()["message"] == "0"

# Проверка, что можно удалить существующего пользователя
def test_user_deleted():
    user_requests.create_user(user_data.user_body_for_delete)
    responce = user_requests.delete_user('GarryPotterDelete')
    assert responce.status_code == 200
    assert responce.json()["code"] == 200
    assert responce.json()["type"] == "unknown"
    assert responce.json()["message"] == "GarryPotterDelete"

# Проверка, что данные пользователя изменяются
def test_user_data_changed():
    user_requests.create_user(user_data.user_body_for_change)
    responce = user_requests.change_user_data(user_data.changed_user_body, 'FirstSecond')
    assert responce.status_code == 200
    assert responce.json()["code"] == 200
    assert responce.json()["type"] == "unknown"
    assert responce.json()["message"] == "12"

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

# Проверка, что данные пользователя изменились? а не создался новый пользователь с новыми даными
def test_old_user_data_not_found():
    responce = user_requests.get_user('FirstSecond')
    assert responce.json()["id"] == 12
    assert responce.json()["username"] == user_data.user_body_for_change["username"]
    assert responce.json()["firstName"] != user_data.user_body_for_change["firstName"]
    assert responce.json()["lastName"] != user_data.user_body_for_change["lastName"]
    assert responce.json()["email"] != user_data.user_body_for_change["email"]
    assert responce.json()["password"] != user_data.user_body_for_change["password"]
    assert responce.json()["phone"] != user_data.user_body_for_change["phone"]
    assert responce.json()["userStatus"] != user_data.user_body_for_change["userStatus"]

# Проверка, что удаленный пользователь не найден
def test_deleted_user_not_found():
    user_requests.create_user(user_data.user_body_for_delete)
    user_requests.delete_user('GarryPotterDelete')
    responce = user_requests.get_user('GarryPotterDelete')
    assert responce.status_code == 404