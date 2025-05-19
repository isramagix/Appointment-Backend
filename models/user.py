from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime, timezone

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    full_name = Column(String)
    role = Column(String, default="user")  # "user" o "admin"
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    appointments = relationship("Appointment", back_populates="user")
