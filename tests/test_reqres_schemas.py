import json
from jsonschema.validators import validate
import requests
import os

resources_path = os.path.join(os.path.dirname((os.path.abspath(__file__))), 'resources')
base_url = 'https://reqres.in/'


def test_schema_list_resource():
    with open(os.path.join(resources_path, 'schema_list_resource.json')) as file:
        schema = json.loads(file.read())
    response = requests.get(url=f"{base_url}api/unknown")

    validate(instance=response.json(), schema=schema)


def test_schema_single_user():
    with open(os.path.join(resources_path, 'schema_single_user.json')) as file:
        schema = json.loads(file.read())
    response = requests.get(url=f"{base_url}api/users/2")

    validate(instance=response.json(), schema=schema)
