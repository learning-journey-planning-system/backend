import json
from app.core.config import settings

class LoadDataBase:

    def __init__(self, model_name: str):
        self.model_name = model_name.lower()
        self.base_url = f"{settings.API_V1_STR}/{self.model_name}/"
        self.base_data = json.load(open("app/tests/db/test_data/%s/base.json" % self.model_name))
        self.create_one_data = json.load(open("app/tests/db/test_data/%s/create_one.json" % self.model_name))
        self.update_one_data = json.load(open("app/tests/db/test_data/%s/update_one.json" % self.model_name))


load_course = LoadDataBase("course")
load_jobrole = LoadDataBase("jobrole")
load_learningjourney = LoadDataBase("learningjourney")
load_registration = LoadDataBase("registration")
load_role = LoadDataBase("role")
load_skill = LoadDataBase("skill")
load_staff = LoadDataBase("staff")