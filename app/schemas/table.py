from pydantic import BaseModel
from typing import Optional


class TableBase(BaseModel):
    name: str
    seats: int
    location: Optional[str] = None


class TableCreate(TableBase):
    pass


class Table(TableBase):
    id: int

    class Config:
        from_attributes = True
