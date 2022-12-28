from typing import Optional, List, Dict
from pydantic import BaseModel

class Shops(BaseModel):
    id: int 
    name: str
    type: str
    rating: float
    review: int 
    price: int
    delivery: bool
    dinein: bool
    takeout: bool
    country: str
    area_code: int