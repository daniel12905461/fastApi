from fastapi import APIRouter,Form
from config.db import conectar_db
from schemas.ubicacionhora import UbicacionHora
import mysql.connector
import datetime
import locale

ubicacionHoras = APIRouter()

@ubicacionHoras.get("/ubicacion-horas")
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

@ubicacionHoras.get("/ubicacion-horas/{id}")
async def getbyid(id: int):
  cnx = conectar_db()

  cursor = cnx.cursor()

  consulta = ("SELECT nombre, numero, estado, detalle, fecha, id_funcionarios, id_mes, id FROM dia WHERE id = "+str(id))
  cursor.execute(consulta)
  resultados = cursor.fetchall()

  json_resultados = {"data": {}}

  for fila in resultados:
    json_resultados["data"] = {
      "nombre": fila[0],
      "numero": fila[1],
      "estado": fila[2],
      "detalle": fila[3],
      "fecha": fila[4],
      "id_funcionarios": fila[5],
      "id_mes": fila[6]
    }
    json_resultados["ok"] = True

    consulta = ("SELECT id, hora, latitud, longitud, id_dia FROM ubicacion_hora WHERE id_dia = "+str(fila[7]))
    cursor.execute(consulta)
    resultados_aux = cursor.fetchall()

    json_resultados["data"]["horas"] = []

    for fila_aux in resultados_aux:
      json_resultados["data"]["horas"].append({
        "id": fila_aux[0],
        "hora": fila_aux[1],
        "latitud": fila_aux[2],
        "longitud": fila_aux[3],
        "id_dia": fila_aux[4]
      })

  if len(json_resultados["data"]) == 0:
    json_resultados["mensaje"] = "No se encontraron resultados para la consulta."
    json_resultados["ok"] = False

  cursor.close()
  cnx.close()

  return json_resultados


@ubicacionHoras.post("/ubicacion-horas")
async def create(latitud: str = Form(...), longitud: str = Form(...), id_dia: str = Form(...)):
  cnx = conectar_db()
  cursor = cnx.cursor()

  # Establecer el idioma español
  locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')

  # Obtener la fecha y hora actual
  fecha_actual = datetime.datetime.now()

  sentencia = "INSERT INTO ubicacion_hora (hora, latitud, longitud, id_dia) VALUES (%s, %s, %s, %s)"
  valores = (fecha_actual.strftime('%H:%M:%S'), float(latitud), float(longitud), id_dia)

  try:
    cursor.execute(sentencia, valores)
    cnx.commit()

    num_filas_afectadas = cursor.rowcount

    json_respuesta = {"mensaje": "Inserción exitosa.", "filas_afectadas": num_filas_afectadas}

  except mysql.connector.Error as error:
    json_respuesta = {"mensaje": "Error al insertar en la base de datos: {}".format(error.msg)}

  finally:
    cursor.close()
    cnx.close()

  return json_respuesta
