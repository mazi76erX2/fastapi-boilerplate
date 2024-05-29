from typing import Optional
from datetime import datetime

from pydantic import BaseModel, Field

# Example of a Pydantic model CRUD schema
# class ItemBase(BaseModel):
#     name: str = Field(..., description="The item name")
#     description: str = Field(None, description="The item description (optional)")
#     stock: int = Field(..., description="The current stock level")
#     category_id: int = Field(..., description="The ID of the associated category")
#     supplier_id: int = Field(..., description="The ID of the associated supplier")


# class ItemCreate(ItemBase):
#     pass


# class ItemUpdate(ItemBase):
#     id: int


# class ItemResponse(ItemBase):
#     id: int
#     created_at: datetime
#     updated_at: datetime

#     class Config:
#         from_attributes = True
