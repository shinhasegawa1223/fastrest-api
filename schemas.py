from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field


class ItemStatus(Enum):
    ON_SALE = "ON_SALE"
    SOLD_OUT = "SOLD_OUT"


class ItemCreate(BaseModel):
    name: str = Field(min_length=2, max_length=20, examples=["PC"])
    price: int = Field(gt=0, examples=[10000])
    # Todo: Optional型について調査
    description: Optional[str] = Field(None, examples=["new"])


class ItemUpdate(BaseModel):
    name: Optional[str] = Field(
        None, min_length=2, max_length=20, examples=["pc"])
    price: Optional[int] = Field(None, gt=0, examples=["10000"])
    description: Optional[str] = Field(None, examples=["new"])
    status: Optional[ItemStatus] = Field(None, examples=[ItemStatus.SOLD_OUT])


class ItemResponse(BaseModel):
    id: int = Field(ge=0, examples=[1])
    name: str = Field(min_length=2, max_length=20, examples=["PC]"])
    price: int = Field(gt=0, examples=[10000])
    description: Optional[str] = Field(None, examples=["new"])
    status: ItemStatus = Field(examples=[ItemStatus.ON_SALE])
