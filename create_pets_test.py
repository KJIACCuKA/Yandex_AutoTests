import pets_requests
import pets_data
import requests

# Если создать питомца без id в теле запроса, то id ему присвоится автоматически
def test_create_pet_without_id_in_body():
    responce = pets_requests.add_new_pet_to_the_store(pets_data.pet_data_without_id)
    assert responce.status_code == 200
    assert responce.json()["id"] != None
    assert responce.json()["id"] == responce.json()["id"]

# Создание питомца с корректными данными
def test_create_pet_with_correct_data():
    responce = pets_requests.add_new_pet_to_the_store(pets_data.pet_data)
    assert responce.status_code == 200
    assert responce.json()["id"] == pets_data.pet_data["id"]
    assert responce.json()["category"] == pets_data.pet_data["category"]
    assert responce.json()["name"] == pets_data.pet_data["name"]
    assert responce.json()["photoUrls"] == pets_data.pet_data["photoUrls"]
    assert responce.json()["tags"] == pets_data.pet_data["tags"]
    assert responce.json()["status"] == pets_data.pet_data["status"]

# Создание питомца с телом без параметров
def test_create_pet_without_params_in_body():
    responce = pets_requests.add_new_pet_to_the_store(pets_data.pet_data_without_id)
    assert responce.status_code == 200
    assert responce.json()["id"] != None
    assert responce.json()["id"] == responce.json()["id"]