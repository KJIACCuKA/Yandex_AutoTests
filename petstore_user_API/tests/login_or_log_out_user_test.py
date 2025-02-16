import user_requests as user_requests
import user_data as user_data

# GET /user/login

# Проверка, что пользователь может зайти в систему
def test_user_can_login_in_system():
    responce = user_requests.user_login('GarryPotter', '123')
    assert responce.status_code == 200
    assert responce.json()["code"] == 200
    assert responce.json()["type"] == "unknown"
    assert responce.json()["message"] == responce.json()["message"]

# Проверка, что пользователь не может зайти в систему в неккоректным именем
def test_user_cant_login_in_system_with_incorrect_name():
    responce = user_requests.user_login('GarryPotter1380', '123')
    assert responce.status_code == 400

# Проверка, что пользователь не может зайти в систему в неккоректным паролем
def test_user_can_login_in_system_with_incorrect_password():
    responce = user_requests.user_login('GarryPotter', '123434343443')
    assert responce.status_code == 400

# GET /user/logout

# Проверка, что пользователь может выйти из системы
def test_user_can_logout_in_system():
    responce = user_requests.user_logout()
    assert responce.status_code == 200
    assert responce.json()["code"] == 200
    assert responce.json()["type"] == "unknown"
    assert responce.json()["message"] == responce.json()["message"]