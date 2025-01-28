from pydantic import BaseModel, Field
from typing import List

class Item(BaseModel):
    shortDescription: str = Field(..., pattern=r"^[\w\s\-]+$", example="Mountain Dew 12PK")
    price: str = Field(..., pattern=r"^\d+\.\d{2}$", example="6.49")

class Receipt(BaseModel):
    retailer: str = Field(..., pattern=r"^[\w\s\-&]+$", example="M&M Corner Market")
    purchaseDate: str = Field(..., pattern=r"^\d{4}-\d{2}-\d{2}$", example="2022-01-01")
    purchaseTime: str = Field(..., pattern=r"^\d{2}:\d{2}$", example="13:01")
    items: List[Item]
    total: str = Field(..., pattern=r"^\d+\.\d{2}$", example="6.49")
