from geopy import distance
from fastapi import APIRouter
from config.db import conectar_db
from schemas.dia import Dia
from schemas.hora import Hora
import json
import mysql.connector
import math
import datetime
import locale

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
async def getbyid(id: int):
  cnx = conectar_db()

  cursor = cnx.cursor()

  consulta = ("SELECT nombre, numero, estado, detalle, fecha, hora_inicio, hora_inicio_reseso, hora_fin_reseso, hora_fin, posicion, hora_retrasos, id_funcionarios, id_mes, id FROM dia WHERE id = "+str(id))
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
      "hora_inicio": str(fila[5]),
      "hora_inicio_reseso": str(fila[6]),
      "hora_fin_reseso": str(fila[7]),
      "hora_fin": str(fila[8]),
      "posicion": fila[9],
      "hora_retrasos": str(fila[10]),
      "id_funcionarios": fila[11],
      "id_mes": fila[12],
      "id": fila[13]
    }
    json_resultados["ok"] = True

    consulta = ("SELECT id, hora, latitud, longitud, id_dia FROM ubicacion_hora WHERE id_dia = "+str(fila[13]))
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

@dias.get("/dias/funcionario/{id}")
async def getallfuncionario(id: int):
  cnx = conectar_db()

  cursor = cnx.cursor()

  consulta = ("SELECT nombre, numero, estado, detalle, fecha, hora_inicio, hora_inicio_reseso, hora_fin_reseso, hora_fin, id_funcionarios, id_mes FROM dia WHERE id_funcionarios = "+str(id))
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
      "hora_inicio": str(fila[5]),
      "hora_inicio_reseso": str(fila[6]),
      "hora_fin_reseso": str(fila[7]),
      "hora_fin": str(fila[8]),
      "id_funcionarios": fila[9],
      "id_mes": fila[10]
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
    coordenada1 = (fila[2], fila[1])
    coordenada2 = (hora.latitud, hora.longitud)
    rango_deseado = 50.0

    # if not verificar_rango(coordenada1, coordenada2, rango_deseado):
    print(fila[2], fila[1], hora.latitud, hora.longitud);
    if not verificar_rango(fila[2], fila[1], hora.latitud, hora.longitud, rango_deseado):
      print("Las ubicacion están fuera del rango deseado.")
      json_resultados["mensaje"] = "Las coordenadas están fuera del rango desaedo."
      json_resultados["ok"] = False
      return json_resultados

    respuestaDia =  createOrUpdateDia(dia)

    json_resultados = {"mensaje": "Inserción exitosa."}
    json_resultados["ok"] = True
    json_resultados["dia"] = respuestaDia
    # json_resultados["parecido"] = True

  cursor.close()
  cnx.close()

  return json_resultados

# def calcular_distancia(coord1, coord2):
#   x1, y1 = coord1
#   x2, y2 = coord2
#   distancia = math.sqrt((float(x2) - float(x1)) ** 2 + (float(y2) - float(y1)) ** 2)
#   return distancia

def calcular_distancia_entre_coordenadas(lat1, lon1, lat2, lon2):
    # Convertir las coordenadas de grados a radianes
    lat1_rad = math.radians(float(lat1))
    lon1_rad = math.radians(float(lon1))
    lat2_rad = math.radians(float(lat2))
    lon2_rad = math.radians(float(lon2))

    # # Calcular la diferencia de longitud y latitud
    # dlat = lat2_rad - lat1_rad
    # dlon = lon2_rad - lon1_rad

    # # Calcular la distancia utilizando la fórmula de la distancia euclidiana
    # distancia = math.sqrt(dlat**2 + dlon**2) * 6371000  # Radio medio de la Tierra en metros

    # return distancia
    # Radio de la Tierra en metros
    radio_tierra = 6371000

    # Diferencia de latitud y longitud
    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad
 # Verificar si las coordenadas son prácticamente idénticas
    if abs(dlat) < 1e-8 and abs(dlon) < 1e-8:
        return 0.0
    # Calcular la distancia utilizando la fórmula del haversine
    a = math.sin(dlat/2)*2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon/2)*2
    # Ajustar el valor de 'a' si está fuera del rango válido
    if a > 1.0:
        a = 1.0
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    distancia = radio_tierra * c

    return distancia

# def verificar_rango(coord1, coord2, rango):
def verificar_rango(lat1, lon1, lat2, lon2, rango):
  # distancia = calcular_distancia(coord1, coord2)
  # distancia = calcular_distancia_entre_coordenadas(lat1, lon1, lat2, lon2)
  coord1 = (float(lat1), float(lon1))
  coord2 = (float(lat2), float(lon2))

  distancia = distance.distance(coord1, coord2).meters
  print("La distancia entre las coordenadas es de", distancia, "metros.")
  
  if distancia <= rango:
    return True
  else:
    return False

def createOrUpdateDia(dia: Dia):
  cnx = conectar_db()
  cursor = cnx.cursor()


  consulta = ("SELECT hora_inicio, hora_inicio_reseso, hora_fin_reseso, hora_fin, domingo, lunes, martes, miercoles, jueves, viernes, sabado FROM funcionarios f JOIN rols r ON f.id_rols = r.id JOIN horarios h ON r.id_horarios = h.id AND f.id = " + dia.id_funcionarios)
  cursor.execute(consulta)
  resultados = cursor.fetchall()

  json_resultados = {"data": []}

  for fila in resultados:
    locale.setlocale(locale.LC_TIME, 'es_ES')

    fecha = datetime.date.today()

    if(fecha.strftime("%A") == 'domingo'):
      if not fila[4]:
        return False

    if(fecha.strftime("%A") == 'lunes'):
      if not fila[5]:
        return False

    if(fecha.strftime("%A") == 'martes'):
      if not fila[6]:
        return False

    if(fecha.strftime("%A") == 'miércoles'):
      if not fila[7]:
        return False

    if(fecha.strftime("%A") == 'jueves'):
      if not fila[8]:
        return False

    if(fecha.strftime("%A") == 'viernes'):
      if not fila[9]:
        return False

    if(fecha.strftime("%A") == 'sábado'):
      if not fila[10]:
        return False

    json_resultados["data"] = {
      "hora_inicio": str(fila[0]),
      "hora_inicio_reseso": str(fila[1]),
      "hora_fin_reseso": str(fila[2]),
      "hora_fin": str(fila[3])}

  if len(json_resultados["data"]) == 0:
    return False

  consulta = ("SELECT posicion, id FROM dia WHERE id_funcionarios = "+dia.id_funcionarios+" AND posicion != 0 ")
  cursor.execute(consulta)
  resultados_aux = cursor.fetchall()

  for fila_aux in resultados_aux:
    if(fila_aux[0] == 1):

      # resMetodo = comparacionHoras(json_resultados["data"]["hora_inicio_reseso"], dia.hora_inicio_reseso)

      sentencia = "UPDATE dia SET posicion = 2, hora_inicio_reseso = '"+dia.hora_inicio_reseso+"' WHERE id = "+str(fila_aux[1])

      cursor.execute(sentencia)
      cnx.commit()

      cursor.close()
      cnx.close()
      return {"id": fila_aux[1], "posicion": "2" }

    if(fila_aux[0] == 2):
      sentencia = "UPDATE dia SET posicion = 3, hora_fin_reseso = '"+dia.hora_fin_reseso+"' WHERE id = "+str(fila_aux[1])

      cursor.execute(sentencia)
      cnx.commit()

      cursor.close()
      cnx.close()
      return {"id": fila_aux[1], "posicion": "3" }

    if(fila_aux[0] == 3):
      sentencia = "UPDATE dia SET posicion = 0, hora_fin = '"+dia.hora_fin+"' WHERE id = "+str(fila_aux[1])

      cursor.execute(sentencia)
      cnx.commit()

      cursor.close()
      cnx.close()
      return {"id": fila_aux[1], "posicion": "0" }

  hora1 = datetime.datetime.strptime(json_resultados["data"]["hora_inicio"], '%H:%M:%S')
  hora2 = datetime.datetime.strptime(dia.hora_inicio, '%H:%M:%S')

  hora_retrasos = '00:00:00'
  estado = 'Presente'

  if hora1 < hora2:
    hora_retrasos = hora2 - hora1
    estado = 'Tarde'

  sentencia = "INSERT INTO dia (nombre, numero, estado, detalle, fecha, hora_inicio, hora_inicio_reseso, hora_fin_reseso, hora_fin, posicion, hora_retrasos, id_funcionarios, id_mes) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
  valores = (quitar_acentos(dia.nombre), dia.numero, estado, dia.detalle, dia.fecha, dia.hora_inicio, '00:00:00', '00:00:00', '00:00:00', dia.posicion, hora_retrasos, dia.id_funcionarios, dia.id_mes)

  cursor.execute(sentencia, valores)
  cnx.commit()

  return {"id": cursor.lastrowid, "posicion": dia.posicion }

def comparacionHoras(hora1_aux, hora2_aux):
  hora1 = datetime.datetime.strptime(hora1_aux, '%H:%M:%S')
  hora2 = datetime.datetime.strptime(hora2_aux, '%H:%M:%S')

  json_resultados = {"hora_retrasos": '00:00:00', "estado": 'Presente'}

  if hora1 < hora2:
    # hora_retrasos = hora2 - hora1
    # estado = 'Tarde'
    json_resultados = {"hora_retrasos": hora2 - hora1, "estado": 'Tarde'}

def quitar_acentos(texto):
  acentuadas = ["á", "é", "í", "ó", "ú", "ñ"]
  sin_acento = ["a", "e", "i", "o", "u", "n"]
  for i in range(len(acentuadas)):
      texto = texto.replace(acentuadas[i], sin_acento[i])
  return texto
