from fastapi import APIRouter,Form
from config.db import conectar_db
from schemas.permiso import Permiso
import json
import mysql.connector
from schemas.dia import Dia
from routes.mes import getIdMes
from routes.dia import quitar_acentos
import datetime
import locale

permiso = APIRouter()

@permiso.get("/permisos")
async def getall(ubicacion_id: int = 0, mes_id: int = 0):
  cnx = conectar_db()

  cursor = cnx.cursor()

  consulta = "SELECT p.motivo, p.id_dia, p.id_funcionarios, p.id, p.aprobado FROM permisos p "
  
  if ubicacion_id != 0:
    consulta = consulta + ("JOIN funcionarios f ON p.id_funcionarios = f.id " +
      "JOIN ubicaciones u ON f.id_ubicaciones = u.id " +
      "AND u.id = " + str(ubicacion_id) + " ")

  if mes_id != 0:
    consulta = consulta + ("JOIN dia d ON p.id_dia = d.id " +
      "JOIN mes m ON d.id_mes = m.id " +
      "AND m.id = " + str(mes_id) + " ")
    
  consulta = consulta + "ORDER BY id DESC"
  cursor.execute(consulta)
  resultados = cursor.fetchall()

  json_resultados = {"data": []}

  i=0
  for fila in resultados:
    json_resultados["data"].append({
      "motivo": fila[0], 
      "id_dia": fila[1], 
      "id_funcionarios": fila[2], 
      "id": fila[3], 
      "aprobado": fila[4]
    })
    json_resultados["ok"] = True

    
    consulta = ("SELECT nombre, numero, estado, detalle, fecha, hora_inicio, hora_inicio_reseso, hora_fin_reseso, hora_fin, posicion, hora_retrasos, id_funcionarios, id_mes, id FROM dia WHERE id = "+str(fila[1]))
    cursor.execute(consulta)
    resultados_aux = cursor.fetchall()

    json_resultados["data"][i]["dia"] = {}
    for fila_aux in resultados_aux:
      json_resultados["data"][i]["dia"] = {
        "nombre": fila_aux[0],
        "numero": fila_aux[1],
        "estado": fila_aux[2],
        "detalle": fila_aux[3],
        "fecha": fila_aux[4],
        "hora_inicio": str(fila_aux[5]),
        "hora_inicio_reseso": str(fila_aux[6]),
        "hora_fin_reseso": str(fila_aux[7]),
        "hora_fin": str(fila_aux[8]),
        "posicion": fila_aux[9],
        "hora_retrasos": str(fila_aux[10]),
        "id_funcionarios": fila_aux[11],
        "id_mes": fila_aux[12],
        "id": fila_aux[13]
      }
    
    consulta = ("SELECT nombres, apellidos, ci, foto, celular, fecha_nac, id, user, password, id_rols, id_ubicaciones FROM funcionarios WHERE id = "+str(fila[2]))
    cursor.execute(consulta)
    resultados_aux = cursor.fetchall()

    json_resultados["data"][i]["funcionario"] = {}
    for fila_aux in resultados_aux:
      json_resultados["data"][i]["funcionario"] = {
        "nombres": fila_aux[0], 
        "apellidos": fila_aux[1], 
        "ci": fila_aux[2], 
        "foto": fila_aux[3], 
        "celular": fila_aux[4], 
        "fecha_nac": fila_aux[5], 
        "id": fila_aux[6], 
        "user": fila_aux[7], 
        "password": fila_aux[8], 
        "id_rols": fila_aux[9], 
        "id_ubicaciones": fila_aux[10]
      }
    
    i=i+1

  if len(json_resultados["data"]) == 0:
    json_resultados["mensaje"] = "No se encontraron resultados para la consulta."
    json_resultados["ok"] = False

  cursor.close()
  cnx.close()

  return json_resultados

@permiso.get("/permisos/{id}")
async def getbyid(id: int):
  cnx = conectar_db()

  cursor = cnx.cursor()

  consulta = ("SELECT motivo, id_dia, id_funcionarios, id FROM permisos WHERE id = "+str(id))
  # valores = (id)
  cursor.execute(consulta)
  resultados = cursor.fetchall()

  json_resultados = {"data": []}

  for fila in resultados:
    json_resultados["data"] = {"motivo": fila[0], "id_dia": fila[1], "id_funcionarios": fila[2], "id": fila[3]}
    json_resultados["ok"] = True

  if len(json_resultados["data"]) == 0:
    json_resultados["mensaje"] = "No se encontraron resultados para la consulta."
    json_resultados["ok"] = False

  cursor.close()
  cnx.close()

  return json_resultados

@permiso.post("/permisos")
async def create(motivo: str = Form(...), id_funcionarios: str = Form(...)):

  cnx = conectar_db()
  cursor = cnx.cursor()
  
  # Establecer el idioma español
  locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')

  # Obtener la fecha y hora actual
  fecha_actual = datetime.datetime.now()

  consulta = "SELECT * FROM dia WHERE fecha = %s AND id_funcionarios = %s"
  cursor.execute(consulta, (fecha_actual.strftime('%Y-%m-%d'), id_funcionarios))
  resultados = cursor.fetchall()

  if resultados:
    json_respuesta = {"mensaje": "Este Dia ya se registro"}
    json_respuesta["ok"] = False

    cursor.close()
    cnx.close()

    return json_respuesta

  dia = Dia(
    nombre = fecha_actual.strftime('%A'),
    numero = fecha_actual.strftime('%d'),
    estado = "Permiso",
    detalle = "",
    fecha = fecha_actual.strftime('%Y-%m-%d'),
    hora_inicio = fecha_actual.strftime('%H:%M:%S'),
    hora_inicio_reseso = fecha_actual.strftime('%H:%M:%S'),
    hora_fin_reseso = fecha_actual.strftime('%H:%M:%S'),
    hora_fin = fecha_actual.strftime('%H:%M:%S'),
    posicion = "1",
    id_funcionarios = id_funcionarios,
    id_mes = str(await getIdMes( str(fecha_actual.strftime('%m')), str(1))),
    id = ""
  )

  print(motivo,id_funcionarios)

  sentencia = "INSERT INTO dia (nombre, numero, estado, detalle, fecha, hora_inicio, hora_inicio_reseso, hora_fin_reseso, hora_fin, posicion, hora_retrasos, id_funcionarios, id_mes) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
  valores = (quitar_acentos(dia.nombre), dia.numero,  "Permiso", dia.detalle, dia.fecha, dia.hora_inicio, '00:00:00', '00:00:00', '00:00:00', dia.posicion, '00:00:00', dia.id_funcionarios, dia.id_mes)

  cursor.execute(sentencia, valores)
  # Obtener el ID del día recién creado
  id_dia = cursor.lastrowid
  
  sentencia = "INSERT INTO permisos (motivo, aprobado, id_dia, id_funcionarios) VALUES (%s, %s, %s, %s)"
  valores = (motivo, False, id_dia, id_funcionarios)

  try:
    cursor.execute(sentencia, valores)
    cnx.commit()

    num_filas_afectadas = cursor.rowcount

    json_respuesta = {"mensaje": "Inserción exitosa.", "filas_afectadas": num_filas_afectadas}
    json_respuesta["ok"] = True

  except mysql.connector.Error as error:
    json_respuesta = {"mensaje": "Error al insertar en la base de datos: {}".format(error.msg)}
    json_respuesta["ok"] = False

  finally:
    cursor.close()
    cnx.close()

  return json_respuesta

@permiso.put("/permisos/{id}")
async def update(id: int, permiso: Permiso):
  cnx = conectar_db()
  cursor = cnx.cursor()

  sentencia = "UPDATE permisos SET motivo = '"+permiso.motivo+"', id_dia = "+str(permiso.id_dia)+", id_funcionarios = "+str(permiso.id_funcionarios)+" WHERE id = "+str(id)

  cursor.execute(sentencia)
  cnx.commit()

  cnx.close()

  return 'dda'

@permiso.delete("/permisos/{id}")
async def delete(id: int):
  cnx = conectar_db()
  cursor = cnx.cursor()

  sentencia = "DELETE FROM permisos WHERE id = "+str(id)

  cursor.execute(sentencia)
  cnx.commit()

  cursor.close()
  cnx.close()

  return cursor

@permiso.get("/permisos/habilitar/{id}")
async def delete(id: int):
  cnx = conectar_db()
  cursor = cnx.cursor()

  sentencia = "UPDATE permisos SET aprobado = 1 WHERE id = "+str(id)

  cursor.execute(sentencia)
  cnx.commit()

  cursor.close()
  cnx.close()

  return cursor