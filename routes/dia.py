from fastapi import APIRouter
from config.db import conectar_db
from schemas.dia import Dia
from schemas.hora import Hora
import json
import mysql.connector
import math

dias = APIRouter()

@dias.get("/dias")
async def getall():
  cnx = conectar_db()

  cursor = cnx.cursor()

  consulta = ("SELECT nombre, numero, estado, detalle, fecha, id_funcionarios, id_mes FROM dia")
  cursor.execute(consulta)
  resultados = cursor.fetchall()

  json_resultados = {"data": []}

  for fila in resultados:
    json_resultados["data"].append({
      "nombre": fila[0],
      "numero": fila[1],
      "estado": fila[2],
      "detalle": fila[3],
      "fecha": fila[4],
      "id_funcionarios": fila[5],
      "id_mes": fila[6]
    })
    json_resultados["ok"] = True

  if len(json_resultados["data"]) == 0:
    json_resultados["mensaje"] = "No se encontraron resultados para la consulta."
    json_resultados["ok"] = False

  cursor.close()
  cnx.close()

  return json_resultados

@dias.get("/dias/{id}")
async def getallfuncionario(id: int):
  cnx = conectar_db()

  cursor = cnx.cursor()

  consulta = ("SELECT nombre, numero, estado, detalle, fecha, id_funcionarios, id_mes FROM dia WHERE id_funcionarios = "+str(id))
  cursor.execute(consulta)
  resultados = cursor.fetchall()

  json_resultados = {"data": []}

  for fila in resultados:
    json_resultados["data"].append({
      "nombre": fila[0],
      "numero": fila[1],
      "estado": fila[2],
      "detalle": fila[3],
      "fecha": fila[4],
      "id_funcionarios": fila[5],
      "id_mes": fila[6]
    })
    json_resultados["ok"] = True

  if len(json_resultados["data"]) == 0:
    json_resultados["mensaje"] = "No se encontraron resultados para la consulta."
    json_resultados["ok"] = False

  cursor.close()
  cnx.close()

  return json_resultados

async def create(dia: Dia, hora: Hora):
  cnx = conectar_db()
  cursor = cnx.cursor()

  consulta = ("SELECT u.nombre, u.latitud, u.longitud, u.id FROM ubicaciones u JOIN funcionarios f ON u.id = f.id_ubicaciones AND f.id = " + dia.id_funcionarios)
  cursor.execute(consulta)
  resultados = cursor.fetchall()

  json_resultados = {"data": []}

  for fila in resultados:
    coordenada1 = (fila[1], fila[2])
    coordenada2 = (hora.latitud, hora.longitud)
    rango_deseado = 100

    if not verificar_rango(coordenada1, coordenada2, rango_deseado):
      print("Las coordenadas están fuera del rango deseado.")
      json_resultados["mensaje"] = "Las coordenadas están fuera del rango deseado."
      json_resultados["ok"] = False
      return json_resultados

    sentencia = "INSERT INTO dia (nombre, numero, estado, detalle, fecha, id_funcionarios, id_mes) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    valores = (dia.nombre, dia.numero, dia.estado, dia.detalle, dia.fecha, dia.id_funcionarios, dia.id_mes)

    cursor.execute(sentencia, valores)
    cnx.commit()

    sentencia = "INSERT INTO ubicacion_hora (hora, latitud, longitud, id_dia) VALUES (%s, %s, %s, %s)"
    valores = (hora.hora, hora.latitud, hora.longitud, cursor.lastrowid)

    cursor.execute(sentencia, valores)
    cnx.commit()

    json_resultados = {"mensaje": "Inserción exitosa."}
    json_resultados["ok"] = True
    # json_resultados["parecido"] = True

  cursor.close()
  cnx.close()

  return json_resultados

def calcular_distancia(coord1, coord2):
  x1, y1 = coord1
  x2, y2 = coord2
  distancia = math.sqrt((float(x2) - float(x1)) ** 2 + (float(y2) - float(y1)) ** 2)
  return distancia

def verificar_rango(coord1, coord2, rango):
  distancia = calcular_distancia(coord1, coord2)
  print(distancia)
  if distancia <= rango:
    return True
  else:
    return False
