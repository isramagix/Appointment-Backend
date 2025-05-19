from sqlalchemy.orm import Session
from fastapi import HTTPException
from schemas.user import UserCreate, UserUpdate
from CRUDs.user import (
    get_user_by_id,
    get_user_by_email,
    get_users,
    create_user,
    update_user,
    delete_user
)


def register_user(user: UserCreate, db: Session):
    """
    Registra un nuevo usuario si no existe ya.
    """
    existing_user = get_user_by_email(db, user.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email ya registrado")
    return create_user(db, user)


def get_user(user_id: int, db: Session):
    """
    Devuelve un usuario por ID o lanza 404 si no existe.
    """
    user = get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return user


def list_users(db: Session, skip: int = 0, limit: int = 10):
    """
    Lista usuarios con paginación.
    """
    return get_users(db, skip=skip, limit=limit)


def update_user_data(user_id: int, user_data: UserUpdate, db: Session):
    """
    Actualiza un usuario si existe.
    """
    user = update_user(db, user_id, user_data)
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return user


def delete_user_data(user_id: int, db: Session):
    """
    Elimina un usuario por ID.
    """
    user = delete_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return {"detail": "Usuario eliminado correctamente"}
