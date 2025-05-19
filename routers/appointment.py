from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from schemas.appointment import AppointmentCreate, AppointmentOut, AppointmentBase
from controllers import appointment_controller

router = APIRouter(prefix="/appointments", tags=["Appointments"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=AppointmentOut)
def create_appointment(data: AppointmentCreate, db: Session = Depends(get_db)):
    return appointment_controller.create(data, db)

@router.get("/", response_model=list[AppointmentOut])
def list_appointments(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return appointment_controller.list_all(db, skip, limit)

@router.get("/{appointment_id}", response_model=AppointmentOut)
def get_appointment(appointment_id: int, db: Session = Depends(get_db)):
    return appointment_controller.get(appointment_id, db)

@router.put("/{appointment_id}", response_model=AppointmentOut)
def update_appointment(appointment_id: int, data: AppointmentBase, db: Session = Depends(get_db)):
    return appointment_controller.update(appointment_id, data, db)

@router.delete("/{appointment_id}")
def delete_appointment(appointment_id: int, db: Session = Depends(get_db)):
    return appointment_controller.delete(appointment_id, db)
