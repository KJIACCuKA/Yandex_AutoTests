import user_requests as user_requests
import user_data as user_data

# POST /user

# Проверка, что пользователь создается
def test_user_created():
    responce = user_requests.create_user(user_data.user_body)
    assert responce.status_code == 200
    assert responce.json()["code"] == 200
    assert responce.json()["type"] == "unknown"
    assert responce.json()["message"] == f'{user_data.user_body["id"]}'

# В документации позволено создать пользователя без данных
def test_user_created_with_body_without_params():
    responce = user_requests.create_user(user_data.user_body_without_params)
    assert responce.status_code == 200
    assert responce.json()["code"] == 200
    assert responce.json()["type"] == "unknown"
    assert responce.json()["message"] == '0'
def test_user_created_with_body_without_username():
    responce = user_requests.create_user(user_data.user_body_without_username)
    assert responce.status_code == 200
    assert responce.json()["code"] == 200
    assert responce.json()["type"] == "unknown"
    assert responce.json()["message"] == f'{user_data.user_body_without_username["id"]}'

def test_user_created_with_body_without_first_name():
    responce = user_requests.create_user(user_data.user_body_without_first_name)
    assert responce.status_code == 200
    assert responce.json()["code"] == 200
    assert responce.json()["type"] == "unknown"
    assert responce.json()["message"] == f'{user_data.user_body_without_first_name["id"]}'

def test_user_created_with_body_without_last_name():
    responce = user_requests.create_user(user_data.user_body_without_last_name)
    assert responce.status_code == 200
    assert responce.json()["code"] == 200
    assert responce.json()["type"] == "unknown"
    assert responce.json()["message"] == f'{user_data.user_body_without_last_name["id"]}'

def test_user_created_with_body_without_email():
    responce = user_requests.create_user(user_data.user_body_without_email)
    assert responce.status_code == 200
    assert responce.json()["code"] == 200
    assert responce.json()["type"] == "unknown"
    assert responce.json()["message"] == f'{user_data.user_body_without_email["id"]}'

def test_user_created_with_body_without_password():
    responce = user_requests.create_user(user_data.user_body_without_password)
    assert responce.status_code == 200
    assert responce.json()["code"] == 200
    assert responce.json()["type"] == "unknown"
    assert responce.json()["message"] == f'{user_data.user_body_without_password["id"]}'

def test_user_created_with_body_without_phone():
    responce = user_requests.create_user(user_data.user_body_without_phone)
    assert responce.status_code == 200
    assert responce.json()["code"] == 200
    assert responce.json()["type"] == "unknown"
    assert responce.json()["message"] == f'{user_data.user_body_without_phone["id"]}'

def test_user_created_with_body_without_userStatus():
    responce = user_requests.create_user(user_data.user_body_without_userStatus)
    assert responce.status_code == 200
    assert responce.json()["code"] == 200
    assert responce.json()["type"] == "unknown"
    assert responce.json()["message"] == f'{user_data.user_body_without_userStatus["id"]}'

# POST /user/createWithList

# Проверка, что создается несколько пользователей
def test_users_created():
    responce = user_requests.create_list_of_users(user_data.list_of_users)
    assert responce.status_code == 200