import requests
import json

headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json',
    'X-CSRFToken': 'hvaGHJuv7S2FBFkaPUrYnkDTlT3OFJz4IkaaAdwfRJ7BZIxhfTo8r0Bg7yVnMECk',
}

data = '{ "tags": [ "string" ], "protocol": "string", "host": "string", "fqdn": "string", "port": 0, "path": "string", "query": "string", "fragment": "string", "mitigated": true, "product": 0, "endpoint_status": [ 0 ]}'

response = requests.post('http://localhost:8080/api/v2/endpoints/', headers=headers, data=data)

print (response.status_code)
