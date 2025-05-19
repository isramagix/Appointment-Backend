from sqlalchemy.orm import Session
from fastapi import HTTPException
from schemas.appointment import AppointmentCreate, AppointmentBase
from CRUDs.appointment import (
    create_appointment,
    get_appointment_by_id,
    get_appointments,
    update_appointment,
    delete_appointment
)

def create(data: AppointmentCreate, db: Session):
    return create_appointment(db, data)

def get(appointment_id: int, db: Session):
    appt = get_appointment_by_id(db, appointment_id)
    if not appt:
        raise HTTPException(status_code=404, detail="Cita no encontrada")
    return appt

def list_all(db: Session, skip: int = 0, limit: int = 10):
    return get_appointments(db, skip, limit)

def update(appointment_id: int, data: AppointmentBase, db: Session):
    appt = update_appointment(db, appointment_id, data)
    if not appt:
        raise HTTPException(status_code=404, detail="Cita no encontrada")
    return appt

def delete(appointment_id: int, db: Session):
    appt =delete_appointment(db, appointment_id)
    if not appt:
        raise HTTPException(status_code=404, detail="Cita no encontrada")
    return {"detail": "Cita eliminada correctamente"}
