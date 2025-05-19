from pydantic import BaseModel
from datetime import datetime

class AppointmentBase(BaseModel):
    title: str
    description: str | None = None
    date_start: datetime
    date_end: datetime
    status: str = "pending"  # Opcional: "pending", "confirmed", "cancelled"

class AppointmentCreate(AppointmentBase):
    user_id: int  # Enlaza con el usuario que crea la cita

class AppointmentOut(AppointmentBase):
    id: int
    created_at: datetime
    user_id: int

    class Config:
        orm_mode = True
 