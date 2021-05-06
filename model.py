from pydantic import BaseModel
from typing import List


class Image(BaseModel):
    url: str
    # TODO, add the missing `attribute` for this class to pass the unittest


class Product(BaseModel):
    uid: str  # unique id to identify product
    # TODO, add the rest of Product information like: gender, images, product url and etc
    # images: List[Image]
    
