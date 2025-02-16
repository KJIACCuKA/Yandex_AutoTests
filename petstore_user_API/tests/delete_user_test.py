import user_requests as user_requests
import user_data as user_data

# DELETE /user/{username}

# Проверка, что можно удалить существующего пользователя
def test_user_deleted():
    user_requests.create_user(user_data.user_body_for_delete)
    responce = user_requests.delete_user('GarryPotterDelete')
    assert responce.status_code == 200
    assert responce.json()["code"] == 200
    assert responce.json()["type"] == "unknown"
    assert responce.json()["message"] == "GarryPotterDelete"

# Проверка, что удаленный пользователь не найден
def test_deleted_user_not_found():
    user_requests.create_user(user_data.user_body_for_delete)
    user_requests.delete_user('GarryPotterDelete')
    responce = user_requests.get_user('GarryPotterDelete')
    assert responce.status_code == 404

# Проверка, что нельзя удалить несуществующего пользователя
def test_cant_deleted_doesnt_exist_user():
    responce = user_requests.delete_user('GarryPotterDelete123232323')
    assert responce.status_code == 404