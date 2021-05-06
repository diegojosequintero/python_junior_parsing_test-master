from pydantic import BaseModel
from typing import List


class Image(BaseModel):
    url: str
    etag: str=None
    # TODO, add the missing `attribute` for this class to pass the unittest


class Product(BaseModel):
    uid: str  # unique id to identify product
    images: list=None
    gender: str
    url: str
    price: float
    size: str
    category: str
    description: str
    # TODO, add the rest of Product information like: gender, images, product url and etc
    # images: List[Image]
    
