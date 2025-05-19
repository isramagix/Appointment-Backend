from sqlalchemy.orm import Session
from models.appointment import Appointment
from schemas.appointment import AppointmentCreate, AppointmentBase
from datetime import datetime, timezone

def create_appointment(db: Session, data: AppointmentCreate):
    new_appointment = Appointment(
        **data.model_dump(),
        created_at=datetime.now(timezone.utc)
    )
    db.add(new_appointment)
    db.commit()
    db.refresh(new_appointment)
    return new_appointment

def get_appointment_by_id(db: Session, appointment_id: int):
    return db.query(Appointment).filter(Appointment.id == appointment_id).first()

def get_appointments(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Appointment).offset(skip).limit(limit).all()

def update_appointment(db: Session, appointment_id: int, data: AppointmentBase):
    appointment = get_appointment_by_id(db, appointment_id)
    if not appointment:
        return None
    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(appointment, field, value)
    db.commit()
    db.refresh(appointment)
    return appointment

def delete_appointment(db: Session, appointment_id: int):
    appointment = get_appointment_by_id(db, appointment_id)
    if not appointment:
        return None
    db.delete(appointment)
    db.commit()
    return appointment
