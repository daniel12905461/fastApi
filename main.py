from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routes.user import user
from routes.funcionario import funcionario
from routes.horario import horario
from routes.rol import rol
from routes.auth import auth
from routes.asistencia import asistencia
from routes.ubicacion import ubicacion
from routes.gestion import gestion
from routes.dia import dias
from routes.ubicacionhora import ubicacionHoras
from routes.permiso import permiso
from fastapi.middleware.cors import CORSMiddleware
from sockets.sockets import sio_app

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
app.include_router(ubicacion)
app.include_router(gestion)
app.include_router(dias)
app.include_router(ubicacionHoras)
app.include_router(permiso)

app.mount('/sio', app=sio_app)
app.mount("/public", StaticFiles(directory="public"), name="public")
