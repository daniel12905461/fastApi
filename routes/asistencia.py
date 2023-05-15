import os
import shutil
from fastapi import APIRouter, File, Form, UploadFile
# import cv2
import torch
# from matplotlib import pyplot
# from mtcnn.mtcnn import MTCNN
import numpy as np
from PIL import Image
from facenet_pytorch import MTCNN, InceptionResnetV1

asistencia = APIRouter()

# Cargar el modelo MTCNN para detección de rostros
mtcnn = MTCNN(image_size=160, margin=0)

PATH = "public/"

@asistencia.post("/asistencia/registrar")
async def registrarAsistencia(image: UploadFile = File(...), name: str = Form(...), id: str = Form(...)):
  # Definimos el nombre del archivo con el que se guardará la imagen
  nombre_archivo = f"{id}_{name}.jpg"

  # Definimos la ruta de la carpeta donde se guardará la imagen
  ruta_carpeta = "public"

  # Creamos la carpeta si no existe
  if not os.path.exists(ruta_carpeta):
      os.makedirs(ruta_carpeta)

  # Unimos la ruta de la carpeta y el nombre del archivo para obtener la ruta completa
  ruta_archivo = os.path.join(ruta_carpeta, nombre_archivo)

  # Guardamos la imagen en la ubicación deseada con el nombre especificado
  with open(ruta_archivo, "wb") as buffer:
    shutil.copyfileobj(image.file, buffer)

  # Realizamos alguna operación adicional, como enviar una respuesta al cliente
  return {"ok": True, "mensaje": "La imagen se ha guardado correctamente."}

@asistencia.post("/asistencia/login")
async def registrarAsistencia(image: UploadFile = File(...), name: str = Form(...), id: str = Form(...)):
  # Definimos el nombre del archivo que estamos buscando
  nombre_archivo = f"{id}_{name}.jpg"

  # Definimos la ruta de la carpeta donde se encuentra la imagen
  ruta_carpeta = "public"

  # Unimos la ruta de la carpeta y el nombre del archivo para obtener la ruta completa
  ruta_archivo = os.path.join(ruta_carpeta, nombre_archivo)

  # Verificamos si el archivo existe en la ubicación especificada
  if not os.path.exists(ruta_archivo):
    return {"ok": False, "parecido": False, "mensaje": "Suba primero una Imagen suya."}

  # Definimos el nombre del archivo que estamos buscando
  nombre_archivo = f"{id}_{name}_LOG.jpg"

  # Unimos la ruta de la carpeta y el nombre del archivo para obtener la ruta completa
  ruta_archivo = os.path.join(ruta_carpeta, nombre_archivo)

  # Guardamos la imagen en la ubicación deseada con el nombre especificado
  with open(ruta_archivo, "wb") as buffer:
    shutil.copyfileobj(image.file, buffer)

  # Cargar el modelo InceptionResnetV1 para extracción de características
  model = InceptionResnetV1(pretrained='vggface2').eval()

  # Cargar y preprocesar las dos imágenes que se quieren comparar
  image1 = load_and_preprocess_image(PATH + id + "_" + name + ".jpg")
  image2 = load_and_preprocess_image(PATH + id + "_" + name + "_LOG.jpg")

  json_resultados = {"ok": True}
  # Si no se detecta ningún rostro en alguna de las imágenes, mostrar un mensaje de error
  if image1 is None or image2 is None:
    print('No se detectó un rostro en alguna de las imágenes.')
    json_resultados["mensaje"] = "No se detectó un rostro en alguna de las imágenes."
    json_resultados["parecido"] = False
  else:
    # Obtener las características de los rostros en ambas imágenes
    embeddings1 = model(image1).detach().numpy()
    embeddings2 = model(image2).detach().numpy()
    # Calcular la distancia euclidiana entre las características de los rostros
    distance = np.linalg.norm(embeddings1 - embeddings2)
    # Definir un umbral de distancia para determinar si corresponden a la misma persona o no
    threshold = 1.1
    if distance < threshold:
      print('Las imágenes corresponden a la misma persona.')
      json_resultados["mensaje"] = "Las imágenes corresponden a la misma persona."
      json_resultados["parecido"] = True
    else:
      print('Las imágenes no corresponden a la misma persona.')
      json_resultados["mensaje"] = "Las imágenes no corresponden a la misma persona."
      json_resultados["parecido"] = False

  return json_resultados

# Función para cargar y preprocesar una imagen
def load_and_preprocess_image(image_path):
  # Cargar la imagen y convertirla a RGB
  image = Image.open(image_path).convert('RGB')
  # Detectar el rostro en la imagen y recortar la región del rostro
  face = mtcnn(image)
  # Si no se detecta ningún rostro, devolver None
  if face is None:
      return None
  # Preprocesar la imagen para que sea compatible con el modelo
  face = np.transpose(face.numpy(), (1, 2, 0))
  face = np.expand_dims(face, axis=0)
  face = torch.from_numpy(face).permute(0, 3, 1, 2).float()
  # Devolver la imagen preprocesada
  return face
