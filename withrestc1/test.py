import requests
import json

BASE_URL = 'http://127.0.0.1:8000/'
ENDPOINT = 'api/'


# def get_ressource(id=None):
#     data = {}
#     if id is not None:
#         data = {
#             'id': id
#         }
#     r = requests.get(BASE_URL + ENDPOINT, data=json.dumps(data))
#     print(r.status_code)
#     print(r.json())
#
#
# get_ressource(1)


# def create_resource():
#     new_emp = {
#         'eno': 687,
#         'ename': 'vishal',
#         'esal': 8521,
#         'eaddr': "goregaon",
#     }
#     r = requests.post(BASE_URL + ENDPOINT, data=json.dumps(new_emp))
#     print(r.status_code)
#     print(r.json())
#
#
# create_resource()


def update_resource(id):
    new_data = {
        'id': id,

        'esal': 650,

    }
    r = requests.put(BASE_URL + ENDPOINT, data=json.dumps(new_data))
    print(r.status_code)
    print(r.json())


update_resource(1)
#
# def delete_resource(id):
#     data = {
#         'id': id,
#     }
#     r = requests.delete(BASE_URL + ENDPOINT, data=json.dumps(data))
#     print(r.status_code)
#     print(r.json())
#
#
# delete_resource(2)
