INSERT INTO horarios
(hora_inicio, hora_inicio_reseso, hora_fin_reseso, hora_fin, domingo, lunes, martes, miercoles, jueves, viernes, sabado)
VALUES
('07:00:00', '07:00:00', '07:00:00', '07:00:00', 0, 1, 1, 1, 1, 1, 0);

INSERT INTO rols
(nombre, id_horarios)
VALUES
('administrador', 1);

INSERT INTO ubicaciones
(nombre, latitud, longitud)
VALUES
('alcaldia', 12.3434, 12.123123);

INSERT INTO funcionarios
(nombres, apellidos, ci, foto, celular, fecha_nac, user, password, id_rols, id_ubicaciones)
VALUES
('daniel', 'delgado', '123', '', '321', '1999-10-19', 'daniel', 'daniel', 1, 1);

INSERT INTO gestion
(nombre)
VALUES
('2023');

INSERT INTO mes
(nombre, numero, id_gestion)
VALUES
('Enero',1,1),
('Febrero',2,1),
('Marzo',3,1),
('Abril',4,1),
('Mayo',5,1),
('Junio',6,1),
('Julio',7,1),
('Agosto',8,1),
('Septiembre',9,1),
('Octubre',10,1),
('Noviembre',11,1),
('Diciembre',12,1);


INSERT INTO dia
(nombre, numero, estado, detalle, fecha, hora_inicio, hora_inicio_reseso, hora_fin_reseso, hora_fin, posicion, hora_retrasos, id_funcionarios, id_mes)
VALUES
('Lunes', 5, 'Presente', '', '2023-06-05', '07:00:00', '07:00:00', '07:00:00', '07:00:00', 1, '00:00:00', 1, 1);


-- INSERT INTO Anio
-- (Anio)
-- VALUES
-- ('2010'),
-- ('2011'),
-- ('2012'),
-- ('2013'),
-- ('2014'),
-- ('2015'),
-- ('2016'),
-- ('2017'),
-- ('2018'),
-- ('2019'),
-- ('2020'),
-- ('2021'),
-- ('2022'),
-- ('2023'),
-- ('2024');



-- INSERT INTO HoraIngreso
-- (HoraIngreso)
-- VALUES
-- ('07:00:00'),
-- ('08:00:00'),
-- ('09:00:00'),
-- ('10:00:00'),
-- ('11:00:00'),
-- ('14:00:00'),
-- ('15:00:00'),
-- ('16:00:00'),
-- ('17:00:00'),
-- ('18:00:00'),
-- ('19:00:00');

-- INSERT INTO HoraSalida
-- (HoraSalida)
-- VALUES
-- ('08:00:00'),
-- ('09:00:00'),
-- ('10:00:00'),
-- ('11:00:00'),
-- ('12:00:00'),
-- ('15:00:00'),
-- ('16:00:00'),
-- ('17:00:00'),
-- ('18:00:00'),
-- ('19:00:00'),
-- ('20:00:00');



-- -- INSERT INTO Referencia
-- -- (CiReferencia,primerNombre ,segundoNombre ,apellidoPaterno,apellidoMaterno,direccion ,FechaNacimiento,NumeroCelular)
-- -- VALUES
-- -- ('456','maria','','gonzales','suarez','c.primero de mayo','1999-10-19','60771615');


-- INSERT INTO Instructor
-- (CiInstructor ,primerNombre ,segundoNombre ,apellidoPaterno,apellidoMaterno,Fotografia ,Direccion,FotoCarnetAmverso,FotoCarnetReverso ,FechaNacimiento,NumeroCelular,Usuario,Contrasenia,Activo,Genero,PrimerNombreRef,SegundoNombreRef,ApellidoPaternoRef,ApellidoMaternoRef,DireccionRef,FechaNacimientoRef,NumeroCelularRef)
-- VALUES
-- ('321','Daniel','','delgado','Camacho','foto','c.primero de mayo','FotoCarnetAmverso','FotoCarnetReverso','1999-10-19','60771615','ddelgado321','321',1,'M','maria','','gonzales','suarez','c.primero de mayo','1999-10-19','60771615'),
-- ('567','Maria','','Melisa','Gonsales','foto','c.primero de mayo','FotoCarnetAmverso','FotoCarnetReverso','1999-10-19','60771615','mgonsales567','567',1,'F','maria','','gonzales','suarez','c.primero de mayo','1999-10-19','60771615'),
-- ('678','juan','','delgado','Camacho','foto','c.primero de mayo','FotoCarnetAmverso','FotoCarnetReverso','1999-10-19','60771615','ddelgado321','321',1,'M','maria','','gonzales','suarez','c.primero de mayo','1999-10-19','60771615');



-- INSERT INTO Grupo
-- (IdTipoNivel,CiInstructor)
-- VALUES
-- (1,'321'),
-- (3,'321'),
-- (2,'567'),
-- (4,'567'),
-- (2,'321');



-- -- INSERT INTO InstructorGrupo
-- -- (IdGrupo,CiInstructor)
-- -- VALUES
-- -- ("1-A",'321'),
-- -- ("3-A",'321'),
-- -- ("2-A",'567'),
-- -- ("4-A",'567'),
-- -- ("2-b",'321');



-- INSERT INTO Horario
-- (Monto,Cantidad,IdDia,IdMes,IdAnio,IdGrupo,IdHoraIngreso,IdHoraSalida)
-- VALUES
-- ("100",20,2,2,10,1,1,1),
-- ("100",20,3,2,10,1,1,1),
-- ("100",20,5,2,10,1,1,1),
-- ("100",20,4,2,10,1,1,1),
-- ("100",20,5,2,10,1,1,1),
-- ("100",20,6,2,10,1,1,1),
-- ("100",20,2,2,10,2,1,1),
-- ("100",20,3,2,10,2,1,1),
-- ("100",20,4,2,10,2,1,1),
-- ("100",20,5,2,10,2,1,1),
-- ("100",20,6,2,10,2,1,1),
-- ("100",20,2,2,10,3,1,1),
-- ("100",20,3,2,10,3,1,1),
-- ("100",20,4,2,10,3,1,1),
-- ("100",20,5,2,10,3,1,1),
-- ("100",20,6,2,10,3,1,1),
-- ("100",20,2,2,10,5,1,1),
-- ("100",20,3,2,10,5,1,1),
-- ("100",20,4,2,10,5,1,1),
-- ("100",20,5,2,10,5,1,1),
-- ("100",20,6,2,10,5,1,1),
-- ("100",20,2,2,10,4,3,4),
-- ("100",20,4,2,10,4,3,4),
-- ("100",20,6,2,10,4,3,4);




-- INSERT INTO estudiante
-- (primerNombre ,segundoNombre ,apellidoPaterno,apellidoMaterno,Ci,Fotografia,Direccion,FotoCarnetAmverso,FotoCarnetReverso,FechaNacimiento,Activo,Genero,CiTutor,PrimerNombreTutor,SegundoNombreTutor,ApellidoPaternoTutor,ApellidoMaternoTutor,NumeroCelularTutor,DireccionTutor,FotoTutor,TipoTutor)
-- VALUES
-- ('Nelly','','Delgado','Camacho','','foto','c. Aurora','FotoCarnetAmverso','FotoCarnetReverso','2004-04-04',1,'F','123','maria','','gonzales','suarez','6847459','c.primero de mayo','foto','Mama'),
-- ('Martin','','Moales','Camacho','','foto','c. Aurora','FotoCarnetAmverso','FotoCarnetReverso','1999-04-04',1,'M','123','maria','','gonzales','suarez','6847459','c.primero de mayo','foto','Mama'),
-- ('Marlene','','Apaza','Camacho','','foto','c. Aurora','FotoCarnetAmverso','FotoCarnetReverso','1994-04-04',1,'F','123','maria','','gonzales','suarez','6847459','c.primero de mayo','foto','Mama'),
-- ('Maira','','Delgado','Camacho','','foto','c. Aurora','FotoCarnetAmverso','FotoCarnetReverso','2004-04-04',1,'F','123','maria','','gonzales','suarez','6847459','c.primero de mayo','foto','Mama'),
-- ('Avigail','','Moales','Camacho','','foto','c. Aurora','FotoCarnetAmverso','FotoCarnetReverso','1999-04-04',1,'F','123','maria','','gonzales','suarez','6847459','c.primero de mayo','foto','Mama'),
-- ('Samuel','','Apaza','Camacho','','foto','c. Aurora',null,null,'1994-04-04',1,'M','123','maria','','gonzales','suarez','6847459','c.primero de mayo','foto','Mama');


-- INSERT INTO Inscripcion
-- (IdEstudiante,IdGrupo)
-- VALUES
-- (1,1),
-- (2,2),
-- (3,3),
-- (4,3),
-- (5,4),
-- (6,4),
-- (6,5);



-- -- INSERT INTO Gestion
-- -- (Gestion,Monto,Activo)
-- -- VALUES
-- -- ('2010','300',1);



-- -- INSERT INTO InscripcionMensualidad
-- -- (Mes,FechaHora,IdEstudiante,IdGestion)
-- -- VALUES
-- -- ('Mayo','2019-03-26 07:00:00',1,1),
-- -- ('Mayo','2019-03-26 07:00:00',2,1),
-- -- ('Mayo','2019-03-26 07:00:00',3,1),
-- -- ('Mayo','2019-03-26 07:00:00',4,1),
-- -- ('Mayo','2019-03-26 07:00:00',5,1),
-- -- ('Mayo','2019-03-26 07:00:00',6,1);


-- INSERT INTO RFID
-- (RFID,IdEstudiante)
-- VALUES
-- ('678910',1),
-- ('101112',2),
-- ('131415',3),
-- ('161718',4),
-- ('192021',5),
-- ('222324',6);


-- INSERT INTO Asistencia
-- (FechaHoraLlegada,EstadoAsistencia,IdRFID)
-- VALUES
-- ('2019-03-25 00:00:00',3,1),
-- ('2019-03-26 07:00:00',1,1),
-- ('2019-03-27 08:00:00',2,1),
-- ('2019-03-28 07:00:00',1,1),
-- ('2019-03-29 07:00:00',1,1),
-- ('2019-03-30 08:00:00',2,1),
-- ('2019-04-01 00:00:00',3,1),
-- ('2019-03-26 07:00:00',1,2),
-- ('2019-03-26 07:00:00',1,3),
-- ('2019-03-26 07:00:00',1,4),
-- ('2019-03-26 07:00:00',1,5),
-- ('2019-03-26 07:00:00',1,6);


-- INSERT INTO Rol
-- (Rol)
-- VALUES
-- ('EncargadoInscripcion'),
-- ('AsistenteControlAsistencia'),
-- ('AdministradorNatación');


-- INSERT INTO Usuario
-- (CiUsuario,primerNombre ,segundoNombre ,apellidoPaterno,apellidoMaterno,Fotografia,Direccion,FotoCarnetAmverso,FotoCarnetReverso,FechaNacimiento,Usuario,Contrasenia,Activo,IdRol)
-- VALUES
-- ('123-A','Marta','','Mercado','Camacho','foto','c. Aurora','FotoCarnetAmverso','FotoCarnetReverso','2004-04-04','a','a',1,1),
-- ('123-B','Julian','','Delgado','Camacho','foto','c. Aurora','FotoCarnetAmverso','FotoCarnetReverso','1995-04-04','b','b',1,2),
-- ('123-C','Daniel','','Delgado','Camacho','foto','c. Aurora','FotoCarnetAmverso','FotoCarnetReverso','1995-04-04','c','c',1,3);


-- INSERT INTO Factura
-- (FechaHoraEmision ,NombreCliente,QR,IdInscripcion,Nit,CiUsuario)
-- VALUES
-- ('2019-03-26 20:28:00','Daniel Delgado Camacho','QR',1,'12345','123-A');


