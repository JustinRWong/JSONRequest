from typing import Literal
from pydantic import BaseModel, validator


class RequestModel(BaseModel):
    endpoint: str
    method: Literal[("GET", "POST", "PATCH", "DELETE")]
    data: dict = {}
    url: str = "http://localhost:3000"

    @validator('url')
    def validate_url(cls, url):
        if url.endswith('/'):
            raise ValueError("URL cannot end with '/'")
        return url
