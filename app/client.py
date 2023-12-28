import requests

# response = requests.post(
#     "http://127.0.0.1:5000/advertisements",
#     json={"title": "test",
#           "description": "test advertisement",
#           "owner": "test"
#           }
# )

response = requests.get(
    'http://127.0.0.1:5000/advertisements/1',
)

# response = requests.patch(
#     'http://127.0.0.1:5000/advertisements/1',
#     json={"description": "new description"},
# )
#
# response = requests.delete(
#     'http://127.0.0.1:5000/advertisements/1',
# )
print(response.status_code)
print(response.json())
