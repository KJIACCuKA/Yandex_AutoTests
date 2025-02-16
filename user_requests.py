import petstore_docs
import Petstore_API.petstore_user_API.data.user_data as user_data
import requests
import url_paths.url_paths as url_paths
import headers.headers as headers



# Создаем пользователя
def create_user(body):
    return requests.post(petstore_docs.petstore_docs_url + url_paths.user_path, json=body, headers=headers.headers)

# Создаем нескольких пользователей
def create_list_of_users(body):
    return requests.post(petstore_docs.petstore_docs_url + url_paths.user_path + '/createWithList', json=body, headers=headers.headers)


# Проверяем наличие пользователя
def get_user(username):
    return requests.get(petstore_docs.petstore_docs_url + url_paths.user_path + '/' + username)


# Авторизация пользователя
def user_login(username, password):
    params = {
        'username': username,
        'password': password

    }
    return requests.get(petstore_docs.petstore_docs_url + url_paths.user_path + '/login?', params=params)

# Выход из аккаунта пользователя
def user_logout():
    return requests.get(petstore_docs.petstore_docs_url + url_paths.user_path + '/logout')

# Изменяем данные пользователя
def change_user_data(changed_body, username):
    create_user(user_data.user_body_for_change)
    return requests.put(petstore_docs.petstore_docs_url + url_paths.user_path + '/' + username, json=changed_body, headers=headers.headers)

# Удаляем пользователя
def delete_user(username):
    return requests.delete(petstore_docs.petstore_docs_url + url_paths.user_path + '/' + username)
