import requests
from typing import Literal
from pydantic import BaseModel, validator


class RequestModel(BaseModel):
    endpoint: str
    method: Literal[('GET', 'POST', 'PATCH', 'DELETE')]
    data: dict = {}
    url: str = "http://localhost:3000"

    @validator('url')
    def validate_url(cls, url):
        if url.endswith('/'):
            raise ValueError("URL cannot end with '/'")
        return url


def make_request(request: RequestModel) -> requests.Response:
    '''
    Lightweight wrapper for requests library that only supports Content-Type: application/json.
    '''
    url = f"{request.url}/{request.endpoint}"
    if request.method == 'GET':
        return requests.get(url)
    if request.method == 'POST':
        return requests.post(url, json=data)
    if request.method == 'PATCH':
        return requests.patch(url, json=data)
    if request.method == 'DELETE':
        return requests.delete(url, json=data)
