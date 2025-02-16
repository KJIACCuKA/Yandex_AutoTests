import pets_requests

# GET /pet/{petId}

# Проверка, что питомца можно найти по id
def test_find_pets_by_id():
    responce = pets_requests.find_pet_by_id(1)
    assert responce.status_code == 200

# Проверка, что питомца нельзя найти по несуществующему id
def test_cant_find_pets_by_doesnt_exist_id():
    responce = pets_requests.find_pet_by_id(112343434)
    assert responce.status_code == 404
    assert responce.json()["code"] == 1
    assert responce.json()["type"] == "error"
    assert responce.json()["message"] == "Pet not found"

# GET /pet/findByStatus

# Проверка, что питомца можно найти по статусу 'sold'
def test_find_pet_by_status_sold():
    responce = pets_requests.find_pet_by_status("sold")
    assert responce.status_code == 200

# Проверка, что питомца можно найти по статусу 'pending'
def test_find_pet_by_status_pending():
    responce = pets_requests.find_pet_by_status("pending")
    assert responce.status_code == 200

# Проверка, что питомца можно найти по статусу 'available'
def test_find_pet_by_status_available():
    responce = pets_requests.find_pet_by_status("available")
    assert responce.status_code == 200

# Проверка, что питомца нельзя найти по несуществующему статусу
def test_find_pet_by_doesnt_exist_status():
    responce = pets_requests.find_pet_by_status("123")
    assert responce.status_code != 200