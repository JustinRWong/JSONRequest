import requests
from jsonrequest.RequestModel import RequestModel

def make_request(request: RequestModel) -> requests.Response:
    '''
    Lightweight wrapper for requests library that only supports Content-Type: application/json.
    '''
    url = f"{request.url}/{request.endpoint}"
    if request.method == 'GET':
        return requests.get(url)
    if request.method == 'POST':
        return requests.post(url, json=request.data)
    if request.method == 'PATCH':
        return requests.patch(url, json=request.data)
    if request.method == 'DELETE':
        return requests.delete(url, json=request.data)
