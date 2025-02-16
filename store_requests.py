import requests
import Petstore_API.petstore_store_API.data.store_data as store_data
import petstore_docs
import url_paths.url_paths as url_paths
import headers.headers as headers

# Оформить заказ на домашнее животное
def place_an_order_for_a_pet(body):
    return requests.post(petstore_docs.petstore_docs_url + url_paths.store_path + '/order', json=body, headers=headers.headers)

# Возвращает инвентарь питомцев по статусу
def return_pet_inventories_by_status():
    return requests.get(petstore_docs.petstore_docs_url + url_paths.store_path + '/inventory')

# Найти заказ на покупку в магазине
def find_purchase_order_in_store(order_id):
    return requests.get(f'{petstore_docs.petstore_docs_url}/{url_paths.store_path}/order/{order_id}')

# Удалить заказ на покупку в магазине
def delete_purchase_order_in_store(order_id):
    return requests.delete(f'{petstore_docs.petstore_docs_url}/{url_paths.store_path}/order/{order_id}')