import petstore_user_API.petstore_docs as petstore_docs
import requests

def get_docs():
    return requests.get(petstore_docs.petstore_docs_url)

responce = get_docs()
print(responce.status_code)