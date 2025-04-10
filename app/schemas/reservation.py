import datetime
from pydantic import BaseModel
from .table import Table as TableSchema


class ReservationBase(BaseModel):
    customer_name: str
    reservation_time: datetime.datetime
    duration_minutes: int
    table_id: int


class ReservationCreate(ReservationBase):
    pass


class Reservation(ReservationBase):
    id: int
    table: TableSchema

    class Config:
        from_attributes = True
