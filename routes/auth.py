from fastapi import APIRouter
from config.db import conectar_db
from schemas.user import User
# import json
# import mysql.connector

auth = APIRouter()

@auth.post("/auth/login")
async def login(user: User):
  cnx = conectar_db()

  cursor = cnx.cursor()

  consulta = ("SELECT nombres, apellidos, ci, foto, celular, fecha_nac, id, user, password FROM funcionarios WHERE user = '"+user.user+"' AND password = '"+user.password+"'")
  cursor.execute(consulta)
  resultados = cursor.fetchall()

  json_resultados = {"data": []}

  for fila in resultados:
    json_resultados["data"] = {"nombres": fila[0], "apellidos": fila[1], "ci": fila[2], "foto": fila[3], "celular": fila[4], "fecha_nac": fila[5], "id": fila[6], "user": fila[7], "password": fila[8]}
    json_resultados["ok"] = True
    json_resultados["token"] = "daniel"

  if len(json_resultados["data"]) == 0:
    json_resultados["mensaje"] = "Usuario o ontraseña incorrectos."
    json_resultados["ok"] = False

  cursor.close()
  cnx.close()

  return json_resultados

