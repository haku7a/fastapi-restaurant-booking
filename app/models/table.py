from typing import List
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from . import Base


class Table(Base):
    __tablename__ = "tables"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    seats: Mapped[int] = mapped_column(Integer)
    location: Mapped[str] = mapped_column(String(100), nullable=True)

    reservations: Mapped[List['Reservation']
                         ] = relationship(back_populates="table")
