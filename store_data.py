import json

store_data = '{ "id": 1, "petId": 1, "quantity": 1, "shipDate": "2025-02-15T18:31:32.287Z", "status": "placed", "complete": true}'
store_data_without_id = '{"petId": 1, "quantity": 1, "shipDate": "2025-02-15T18:31:32.287Z", "status": "placed", "complete": true}'
store_data_without_body = {}

data = json.loads(store_data)
data_without_id = json.loads(store_data_without_id)