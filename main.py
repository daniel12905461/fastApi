from fastapi import FastAPI
from routes.user import user
from routes.funcionario import funcionario
from routes.horario import horario
from routes.rol import rol
from routes.auth import auth
from routes.asistencia import asistencia
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user)
app.include_router(funcionario)
app.include_router(horario)
app.include_router(rol)
app.include_router(auth)
app.include_router(asistencia)
