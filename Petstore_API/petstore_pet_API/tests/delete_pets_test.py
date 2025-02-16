import pets_requests as pets_requests
import Petstore_API.petstore_pet_API.data.pets_data as pets_data


# DELETE /pet/{petId}


# Проверка, что можно удалить питомца
def test_delete_pet():
    pets_requests.add_new_pet_to_the_store(pets_data.pet_data_for_delete)
    responce = pets_requests.delete_pet(pets_data.pet_data_for_delete["id"])
    assert responce.status_code == 200

# Проверка, что удаленного питомца нельзя найти
def test_deleted_pet_cant_be_founded():
    pets_requests.add_new_pet_to_the_store(pets_data.pet_data_for_delete)
    pets_requests.delete_pet(pets_data.pet_data_for_delete["id"])
    responce = pets_requests.find_pet_by_id(pets_data.pet_data_for_delete["id"])
    assert responce.status_code == 404
    assert responce.json()["code"] == 1
    assert responce.json()["type"] == "error"
    assert responce.json()["message"] == "Pet not found"

# Проверка, что нельзя удалить несуществующего питомца
def test_cant_delete_doesnt_exist_pet():
    responce = pets_requests.delete_pet(4234234242)
    assert responce.status_code == 404