import requests
import Petstore_API.petstore_pet_API.data.pets_data as pets_data
import petstore_docs as petstore_docs
import url_paths.url_paths as url_paths
import headers.headers as headers

# Добавить питомца в магазин
def add_new_pet_to_the_store(body):
    return requests.post(petstore_docs.petstore_docs_url + url_paths.pet_path, json=body, headers=headers.headers)

# Удалить питомца
def delete_pet(pet_id):
    return requests.delete(f'{petstore_docs.petstore_docs_url}/{url_paths.pet_path}/{pet_id}')

# Найти питомца по id
def find_pet_by_id(pet_id):
    return requests.get(f'{petstore_docs.petstore_docs_url}/{url_paths.pet_path}/{pet_id}')

#Найти питомца по статусу
def find_pet_by_status(status):
    params = {
        "status": status
    }
    return requests.get(f'{petstore_docs.petstore_docs_url}/{url_paths.pet_path}/findByStatus', params=params)
