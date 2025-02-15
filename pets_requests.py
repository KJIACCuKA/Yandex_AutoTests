import requests
import pets_data as pets_data
import petstore_docs as petstore_docs

pet_path = '/v2/pet'

# Добавить питомца в магазин
def add_new_pet_to_the_store(body):
    return requests.post(petstore_docs.petstore_docs_url + pet_path, json=body, headers=pets_data.headers)

# Удалить питомца
def delete_pet(pet_id):
    return requests.delete(f'{petstore_docs.petstore_docs_url}/{pet_path}/{pet_id}')

# Найти питомца по id
def find_pet_by_id(pet_id):
    return requests.get(f'{petstore_docs.petstore_docs_url}/{pet_path}/{pet_id}')

#Найти питомца по статусу
def find_pet_by_status(status):
    params = {
        "status": status
    }
    return requests.get(f'{petstore_docs.petstore_docs_url}/{pet_path}/findByStatus', params=params)

# Изменить данные о питомце
def update_pet_data(change_body):
    return requests.put(petstore_docs.petstore_docs_url + pet_path, json=change_body, headers=pets_data.headers)

# Обновить имя и статус питомца
def update_pet_name_and_status(pet_id, name):
    current_body = pets_data.pet_data.copy()
    current_body["name"] = name
    return requests.post(f'{petstore_docs.petstore_docs_url}/{pet_path}/{pet_id}', json=current_body, headers=pets_data.headers)

responce = update_pet_name_and_status(1, "test")
print(responce.status_code)