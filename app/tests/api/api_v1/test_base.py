import json
from app.core.config import settings

class LoadDataBase:

    def __init__(self, model_name: str):
        self.model_name = model_name.lower()
        self.base_url = f"{settings.API_V1_STR}/{self.model_name}/"
        self.base_data = json.load(open("app/tests/db/test_data/%s/base.json" % self.model_name))
        self.create_one_data = json.load(open("app/tests/db/test_data/%s/create_one.json" % self.model_name))
        self.update_one_data = json.load(open("app/tests/db/test_data/%s/update_one.json" % self.model_name))
        # self.len_base_data = len(self.base_data)

# class TestBase(Generic[ModelType]):

#     def __init__(self, client: TestClient, model: Type[ModelType]):
#         self.client = client
#         self.model = model
#         self.base_url = f"{settings.API_V1_STR}/{self.model.__name__.lower()}/"
#         self.base_data = json.load("app/tests/test_data/%s/base.json" % self.model.__name__.lower())
#         self.create_one_data = json.load("app/tests/test_data/%s/create_one.json" % self.model.__name__.lower())
#         self.update_one_data = json.load("app/tests/test_data/%s/update_one.json" % self.model.__name__.lower())
#         self.len_base_data = len(self.base_data)
    
#     def test_read_all(self):
#         response = self.client.get(f"{self.base_url}/")
#         assert response.status_code == 200
#         assert response.json() == self.base_data

#     def test_create_one(self):
#         response = self.client.post(f"{self.base_url}/", json=self.create_one_data)
#         assert response.status_code == 200
#         assert response.json() == self.create_one_data
        
#     def test_read_one(self):
#         rand_record = random_num(self.len_base_data-1)
#         id = self.base_data[rand_record]["id"]
#         response = self.client.get(f"{self.base_url}/{id}")
#         assert response.status_code == 200
#         assert response.json() == self.base_data[rand_record]

#     def test_update_one(self):
#         rand_record = random_num(self.len_base_data-1)
#         id = self.base_data[rand_record]["id"]
#         response = self.client.put(f"{self.base_url}/{id}", json=self.update_one_data)
#         self.update_one_data["id"] = id
#         assert response.status_code == 200
#         assert response.json() == self.update_one_data

#     def test_delete_one(self):
#         rand_record = random_num(self.len_base_data-1)
#         record = self.base_data[rand_record]
#         id = record["id"]
#         response = self.client.delete(f"{self.base_url}/{id}")
#         assert response.status_code == 200
#         assert record not in json.loads(response.json())