from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import Base, engine
from routers import user

# 👇 Esta función se ejecuta al iniciar y cerrar la app
@asynccontextmanager
async def lifespan(app: FastAPI):
    print("⏳ Iniciando aplicación...")
    Base.metadata.create_all(bind=engine)
    yield
    print("🛑 Cerrando aplicación...")

# 👇 Aquí vinculamos el lifespan al FastAPI
app = FastAPI(lifespan=lifespan)

@app.get("/")
def root():
    return {"message": "API funcionando correctamente"}

app.include_router(user.router)
