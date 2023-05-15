# import os
# from fastapi import APIRouter, File, Form, UploadFile
# import cv2
# from matplotlib import pyplot
# from mtcnn.mtcnn import MTCNN
# import numpy as np

# asistencia = APIRouter()

# PATH = "public/"

# @asistencia.post("/asistencia/registrar")
# async def registrarAsistencia(image: UploadFile = File(...), name: str = Form(...), id: str = Form(...)):
#   contents = await image.read()
#   # cv2.imwrite(PATH+id+"_"+name+".jpg",contents)

#   # Decode image to NumPy array
#   np_img = cv2.imdecode(np.frombuffer(contents, np.uint8), cv2.IMREAD_UNCHANGED)

#   # Save image to directory
#   cv2.imwrite(os.path.join(PATH, id + "_" + name + ".jpg"), np_img)

#   pixeles = pyplot.imread(PATH + id + "_" + name + ".jpg")
#   detector = MTCNN()
#   caras = detector.detect_faces(pixeles)
#   reg_rostro(id + "_" + name + ".jpg", caras)

#   return {"ok": True, "mensaje": "Imagen Registrada correctamente."}

# def reg_rostro(img, lista_resultados):
#   data = pyplot.imread(PATH + img)
#   for i in range(len(lista_resultados)):
#     x1,y1,ancho,alto = lista_resultados[i]['box']
#     x2,y2 = x1+ancho, y1+alto
#     pyplot.subplot(1,len(lista_resultados), i+1)
#     pyplot.axis('off')
#     cara_reg = data[y1:y2, x1:x2]
#     cara_reg = cv2.resize(cara_reg,(150,200), interpolation=cv2.INTER_CUBIC)
#     cv2.imwrite(PATH +"cara_" + img, cara_reg)
#     pyplot.imshow(data[y1:y2, x1:x2])
#   # pyplot.show()

# @asistencia.post("/asistencia/login")
# async def registrarAsistencia(image: UploadFile = File(...), name: str = Form(...), id: str = Form(...)):
#   contents = await image.read()

#   # Decode image to NumPy array
#   np_img = cv2.imdecode(np.frombuffer(contents, np.uint8), cv2.IMREAD_UNCHANGED)

#   # Save image to directory
#   cv2.imwrite(os.path.join(PATH, id + "_" + name + "_LOG.jpg"), np_img)

#   pixeles = pyplot.imread(PATH + id + "_" + name + "_LOG.jpg")
#   detector = MTCNN()
#   caras = detector.detect_faces(pixeles)
#   log_rostro(PATH + id + "_" + name + "_LOG.jpg", caras)

#   rostro_reg = cv2.imread(PATH +"cara_"+ id + "_" + name + ".jpg", 0)
#   rostro_log = cv2.imread(PATH + id + "_" + name + "_LOG.jpg", 0)

#   json_resultados = {"ok": True}

#   similitud = orb_sim(rostro_reg,rostro_log)
#   if similitud >= 0.9:
#       print("welcome!!!")
#       json_resultados["mensaje"] = "Bienbenido."
#       json_resultados["parecido"] = True
#   else:
#       json_resultados["mensaje"] = "Me la pelas no te pareses."
#       json_resultados["parecido"] = False

#   return json_resultados

# def log_rostro(img, lista_resultados):
#   data = pyplot.imread(img)
#   for i in range(len(lista_resultados)):
#     x1,y1,ancho,alto = lista_resultados[i]['box']
#     x2,y2 = x1+ancho, y1+alto
#     pyplot.subplot(1,len(lista_resultados), i+1)
#     pyplot.axis('off')
#     cara_reg = data[y1:y2, x1:x2]
#     cara_reg = cv2.resize(cara_reg,(150,200), interpolation=cv2.INTER_CUBIC)
#     cv2.imwrite(img, cara_reg)
#     pyplot.imshow(data[y1:y2, x1:x2])
#   # pyplot.show()

# def orb_sim(img1, img2):
#   orb = cv2.ORB_create()

#   kpa, descr_a = orb.detectAndCompute(img1, None)
#   kpb, descr_b = orb.detectAndCompute(img2, None)

#   comp = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck = True)

#   matches = comp.match(descr_a, descr_b)

#   regiones_similares = [i for  i in matches if i.distance < 70]

#   if len(matches) == 0:
#     return 0
#   return len(regiones_similares)/len(matches)
