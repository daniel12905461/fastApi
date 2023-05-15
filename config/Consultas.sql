-- a.	Asistencia
-- Req1: Seleccionando un estudiante, mostrar del mes su Asistencia y Falta y en qué fecha fue.
--             Un reporte de cada día que asistió del inicio hasta el final de mes.
-- (Basado en el requerimiento 9, 19h)

SELECT CONCAT(e.apellidoPaterno,' ', e.primerNombre) as NombreEstudiantes ,e.IdEstudiante
FROM Estudiante e;

SELECT a.FechaHoraLlegada,a.EstadoAsistencia,CONCAT(e.apellidoPaterno,' ', e.primerNombre) as NombreEstudiantes 
FROM asistencia a JOIN estudiante e ON a.IdEstudiante=e.IdEstudiante
AND e.IdEstudiante=1
AND a.FechaHoraLlegada BETWEEN "2019-03-01 00:00:00" AND "2019-03-31 00:00:00"
ORDER BY a.FechaHoraLlegada;


SELECT a.FechaHoraLlegada,a.EstadoAsistencia,CONCAT(e.apellidoPaterno,' ', e.primerNombre) as NombreEstudiante
FROM asistencia a JOIN estudiante e ON a.IdEstudiante=e.IdEstudiante
AND e.IdEstudiante=1
AND YEAR(a.FechaHoraLlegada) = '2019'
AND MONTH(a.FechaHoraLlegada) = '04'
ORDER BY a.FechaHoraLlegada;


SELECT a.FechaHoraLlegada,DATE(a.FechaHoraLlegada) AS Fecha, TIME(a.FechaHoraLlegada) AS Hora,a.EstadoAsistencia,CONCAT(e.apellidoPaterno,' ', e.primerNombre) as NombreEstudiante
FROM asistencia a JOIN estudiante e ON a.IdEstudiante=e.IdEstudiante
AND e.IdEstudiante=1
AND YEAR(a.FechaHoraLlegada) = '2019'
AND MONTH(a.FechaHoraLlegada) = '04'
ORDER BY a.FechaHoraLlegada;


SELECT a.FechaHoraLlegada, IF(a.Retraso =1, 'Retraso','Asistencia') as Estado
FROM asistencia a JOIN estudiante e ON a.IdEstudiante=e.IdEstudiante
AND e.IdEstudiante=1
AND YEAR(a.FechaHoraLlegada) = '2019'
AND MONTH(a.FechaHoraLlegada) = '04'
ORDER BY a.FechaHoraLlegada;


-- Req2: Mostrar un reporte estadístico comparativo de un mes seleccionado por el usuario. Del conjunto 
--            de estudiantes que pertenecen a una clase, mostrar de cada uno de ellos asistencia y faltas. 
--            (Basado en el requerimiento 9)

SELECT tn.nivel,g.IdGrupo
FROM Grupo g JOIN TipoNivel tn ON g.IdTipoNivel=tn.IdTipoNivel;

SELECT CONCAT(e.apellidoPaterno,' ', e.primerNombre) as NombreEstudiantes,a.Retraso,a.Falta
FROM Grupo g JOIN Estudiante e ON g.IdGrupo=e.IdGrupo
AND g.IdGrupo='1'
JOIN Asistencia a ON e.IdEstudiante=a.IdEstudiante
AND YEAR(a.FechaHoraLlegada) = '2019'
AND MONTH(a.FechaHoraLlegada) = '03';

-- b.	Instructor
-- Req1: Mostrar horario en el cual imparte clases, de este mostrar por día, y hora


SELECT CONCAT(i.apellidoPaterno,' ', i.primerNombre) as NombreUsuario,i.CiInstructor
FROM Instructor i
ORDER BY i.apellidoPaterno,' ', i.primerNombre;

SELECT CONCAT(i.apellidoPaterno,' ', i.primerNombre) as NombreInstructor,ho.HoraIngreso,ho.HoraSalida,tn.Nivel,d.Dia,m.mes,a.anio
FROM Instructor i join Grupo g ON i.CiInstructor=g.CiInstructor
join TipoNivel tn ON g.IdTipoNivel=tn.IdTipoNivel
AND i.CiInstructor='321'
join Horario h ON g.IdGrupo=h.IdGrupo
join Dia d ON h.IdDia=d.IdDia
join Hora ho ON h.IdHora=ho.IdHora
join Mes m ON h.IdMes=m.IdMes
join Anio a ON h.IdAnio=a.IdAnio; 

-- Req2: Por cada clase el instructor verifica su lista de estudiantes que está a su cargo.
--             (Basado en el requerimiento 7)

SELECT tn.Nivel,g.IdGrupo
fROM Instructor i join Grupo g ON i.CiInstructor=g.CiInstructor
AND i.CiInstructor='321'
join TipoNivel tn ON g.IdTipoNivel=tn.IdTipoNivel
join Horario h ON g.IdGrupo=h.IdGrupo
join Mes m ON h.IdMes=m.IdMes
AND m.Mes='Enero'
join Anio a ON h.IdAnio=a.IdAnio
AND a.Anio='2010';

SELECT CONCAT(e.apellidoPaterno,' ', e.primerNombre) as NombreEstudiantes
fROM Grupo g join Estudiante e ON g.IdGrupo = e.IdGrupo
AND g.IdGrupo='3';

-- c.	Horarios
-- Req1: Mostrar horario en el cual imparte clases los instructores, mostrando horarios por día y hora.
--            (Basado en el requerimiento 7, 19a)

SELECT CONCAT(i.apellidoPaterno,' ', i.primerNombre) as NombreUsuario,ho.HoraIngreso,ho.HoraSalida,tn.Nivel,d.Dia,m.mes,a.anio
FROM Instructor i join Grupo g ON i.CiInstructor=g.CiInstructor
join TipoNivel tn ON g.IdTipoNivel=tn.IdTipoNivel
join Horario h ON g.IdGrupo=h.IdGrupo
join Dia d ON h.IdDia=d.IdDia
join Hora ho ON h.IdHora=ho.IdHora 
join Mes m ON h.IdMes=m.IdMes
join Anio a ON h.IdAnio=a.IdAnio; 


-- Req2: Dado un nivel por ejemplo inicial, mostrar las clases sus horarios y en qué días se imparte y con que 
--            instructor.
--           Esto debe suceder con cualquier parámetro ingresado: intermedio, avanzado, etc.
--            (Basado en el requerimiento 19.b)

SELECT g.IdGrupo,tn.Nivel
FROM Grupo g join TipoNivel tn ON g.IdTipoNivel=tn.IdTipoNivel;


SELECT ho.HoraIngreso,ho.HoraSalida,d.Dia,m.mes,a.anio,CONCAT(i.apellidoPaterno,' ', i.primerNombre) as NombreInstructor
fROM Dia d join Horario h ON d.IdDia=h.IdDia
join Hora ho ON h.IdHora=ho.IdHora
join Mes m ON h.IdMes=m.IdMes
join Anio a ON h.IdAnio=a.IdAnio
join Grupo g ON h.IdGrupo=g.IdGrupo
AND g.IdGrupo='3'
join Instructor i ON g.CiInstructor=i.CiInstructor;



-- d.	Inscritos
-- Req1: Mostrar reporte estadístico del año cantidad de inscritos por mes. (2018) 
--                                          (Basado en el requerimiento 19.c)



-- Req2: Mostrar reporte estadístico de los últimos cinco años cantidad de inscritos, hasta un año antes del 
--             actual.
--            (Basado en el requerimiento 19.d)
-- Req3: Mostrar cantidad de inscritos por mes hasta el mes actual (refiriéndonos hasta el presente año)
--            (Basado en el requerimiento 19.g)












SELECT u.activo
FROM Usuario u join Rol r ON u.IdRol = r.IdRol
AND u.usuario='ei'
AND u.contrasenia='ei';

SELECT g.IdGrupo,tn.nivel
FROM Grupo g join TipoNivel tn ON g.IdTipoNivel = tn.IdTipoNivel;




SELECT CONCAT(e.apellidoPaterno,' ',e.apellidoMaterno,' ',e.primerNombre,' ',e.segundoNombre) as NombreEstudiantes ,e.IdEstudiante,e.fechaNacimiento
								FROM Estudiante e 
								WHERE primerNombre LIKE 'd%' 
								ORDER BY e.apellidoPaterno, e.primerNombre;



								SELECT CONCAT(i.apellidoPaterno,' ',i.apellidoMaterno,' ',i.primerNombre,' ',i.segundoNombre) as NombreInstructor ,i.CiInstructor,i.fechaNacimiento
									FROM Instructor i 
									WHERE primerNombre LIKE 'd%' 
									ORDER BY i.apellidoPaterno, i.primerNombre;


-- consulta de horario por tipo nivel

SELECT ho.HoraIngreso,ho.HoraSalida,d.Dia,m.mes,a.anio,CONCAT(i.apellidoPaterno,' ', i.primerNombre) as NombreInstructor,tn.Nivel
fROM Dia d join Horario h ON d.IdDia=h.IdDia
join Hora ho ON h.IdHora=ho.IdHora
join Mes m ON h.IdMes=m.IdMes
join Anio a ON h.IdAnio=a.IdAnio
join Grupo g ON h.IdGrupo=g.IdGrupo
AND g.IdTipoNivel = 2
join Instructor i ON g.CiInstructor=i.CiInstructor
join TipoNivel tn ON g.IdTipoNivel=tn.IdTipoNivel;


-- SELECT CONCAT(i.apellidoPaterno,' ', i.primerNombre) as NombreInstructor,tn.Nivel,count(IdEstudiante) CantidadEstu
-- fROM TipoNivel tn JOIN Grupo g ON tn.IdTipoNivel = g.IdTipoNivel
-- AND tn.IdTipoNivel = 2
-- join Instructor i ON g.CiInstructor=i.CiInstructor
-- join GrupoEstudiante ge ON g.IdGrupo=ge.IdGrupo;

-- muentra la cantidad de estudiantes por gruppo
SELECT count(IdEstudiante) CantidadEstu
fROM TipoNivel tn JOIN Grupo g ON tn.IdTipoNivel = g.IdTipoNivel
AND g.IdGrupo = 3
join Instructor i ON g.CiInstructor=i.CiInstructor
join GrupoEstudiante ge ON g.IdGrupo=ge.IdGrupo;
 
-- muestra los grupos que hay por nivel 
SELECT CONCAT(i.apellidoPaterno,' ', i.primerNombre) as NombreInstructor,tn.Nivel,g.IdGrupo
fROM TipoNivel tn JOIN Grupo g ON tn.IdTipoNivel = g.IdTipoNivel
AND tn.IdTipoNivel = 2
join Instructor i ON g.CiInstructor=i.CiInstructor; 

--muestra las horas y dias de cada grupo
SELECT hi.HoraIngreso,hs.HoraSalida,d.Dia,m.mes,a.anio,tn.Nivel
fROM Dia d join Horario h ON d.IdDia=h.IdDia
join HoraIngreso hi ON h.IdHoraIngreso=hi.IdHoraIngreso
join HoraSalida hs ON h.IdHoraSalida=hs.IdHoraSalida
join Mes m ON h.IdMes=m.IdMes
join Anio a ON h.IdAnio=a.IdAnio
join Grupo g ON h.IdGrupo=g.IdGrupo
AND g.IdGrupo = 1
join Instructor i ON g.CiInstructor=i.CiInstructor
join TipoNivel tn ON g.IdTipoNivel=tn.IdTipoNivel;


-- muesstra cuantas clases ogrupos hay por nivel

SELECT count(g.IdGrupo) CantidadGrupo
FROM Grupo g JOIN TipoNivel tn ON g.IdTipoNivel=tn.IdTipoNivel
AND tn.IdTipoNivel = 2;



-- muesstra las clases o grupos que o tengan instructor

SELECT g.IdGrupo
fROM TipoNivel tn JOIN Grupo g ON tn.IdTipoNivel = g.IdTipoNivel
join Instructor i ON g.CiInstructor = i.CiInstructor
AND i.CiInstructor="567";


-- muesstra las cuantos grupos hay
SELECT count(g.IdGrupo) fROM grupo g;


-- muestra las horas y dias que pasa un estudiante
SELECT hi.HoraIngreso,hs.HoraSalida,d.Dia,m.mes,a.anio,e.IdEstudiante
fROM Dia d join Horario h ON d.IdDia=h.IdDia
join HoraIngreso hi ON h.IdHoraIngreso=hi.IdHoraIngreso
join HoraSalida hs ON h.IdHoraSalida=hs.IdHoraSalida
join Mes m ON h.IdMes=m.IdMes
join Anio a ON h.IdAnio=a.IdAnio
join Grupo g ON h.IdGrupo=g.IdGrupo
AND g.IdGrupo = 6
join Instructor i ON g.CiInstructor=i.CiInstructor
join TipoNivel tn ON g.IdTipoNivel=tn.IdTipoNivel;


-- muestra las horas y dias que pasa un estudiante
SELECT hi.HoraIngreso,hs.HoraSalida,d.Dia,m.mes,a.anio,e.IdEstudiante,i.IdInscripcion
fROM Dia d join Horario h ON d.IdDia=h.IdDia
AND d.Dia="lunes"
join HoraIngreso hi ON h.IdHoraIngreso=hi.IdHoraIngreso
join HoraSalida hs ON h.IdHoraSalida=hs.IdHoraSalida
join Mes m ON h.IdMes=m.IdMes
AND m.mes="febrero"
join Anio a ON h.IdAnio=a.IdAnio
AND a.anio = "2019"
join Grupo g ON h.IdGrupo=g.IdGrupo
join Inscripcion i ON g.IdGrupo=i.IdGrupo
JOIN estudiante e ON i.IdEstudiante=e.IdEstudiante
join RFID rf ON e.IdEstudiante=rf.IdEstudiante
AND rf.RFID='4362547';

-- muestra los estudiantes y sus RFID
SELECT CONCAT(e.apellidoPaterno,' ',e.apellidoMaterno,' ',e.primerNombre,' ',e.segundoNombre) as NombreEstudiantes ,e.IdEstudiante,e.fechaNacimiento,rf.RFID
FROM Estudiante e JOIN rfid rf ON e.IdEstudiante=rf.IdEstudiante
ORDER BY e.apellidoPaterno, e.primerNombre;

-- Cambiar el balor de rfid
UPDATE rfid SET rfid = '567890', WHERE IdEstudiante='28';


-- muestra todas las clases del estudiante
SELECT g.IdGrupo, tn.nivel, i.IdInscripcion
FROM estudiante e JOIN Inscripcion i ON e.IdEstudiante = i.IdEstudiante
AND e.IdEstudiante=1
JOIN Grupo g ON i.IdGrupo = g.IdGrupo
JOIN TipoNivel tn ON g.IdTipoNivel=tn.IdTipoNivel;



-- muestra si facturocadagrupo
SELECT *
FROM Inscripcion i JOIN factura f  ON i.IdInscripcion = f.IdInscripcion
AND i.IdInscripcion=1;


-- EL id DE LA ULTIMA FACTURA
SELECT MAX(IdFactura) AS IdFactura FROM factura; 



-- muestra las Mes el nivel y Costo
SELECT m.mes,tn.nivel,h.Monto
fROM Mes m JOIN Horario h ON m.IdMes = h.IdMes
join Grupo g ON h.IdGrupo=g.IdGrupo
join TipoNivel tn ON g.IdTipoNivel=tn.IdTipoNivel
JOIN Inscripcion i ON g.IdGrupo=i.IdGrupo
AND i.IdInscripcion=1;


-- muentra la lista de estudiantes por grupo
SELECT CONCAT(e.apellidoPaterno,' ', e.primerNombre) as NombreEstudiante
fROM Grupo g join Inscripcion i ON g.IdGrupo=i.IdInscripcion
AND g.IdGrupo = 1
JOIN Estudiante e ON i.IdEstudiante=e.IdEstudiante;


-- muentra todos los datos de n studiante por su id
SELECT *
fROM Estudiante e WHERE e.IdEstudiante=3;

-- muentra el nombre del usuario segun su ci
SELECT CONCAT(u.primerNombre,' ',u.segundoNombre,' ',u.apellidoPaterno,' ',u.apellidoMaterno) as NombreUsuario
fROM Usuario u WHERE u.ciUsuario='123-A';

-- muestra los ultimos 14 
SELECT * 
FROM asistencia
ORDER BY IdAsistencia DESC
LIMIT 5;

-- muestra los datos del estudante pos id de asistencia
SELECT CONCAT(e.apellidoPaterno,' ',e.apellidoMaterno,' ',e.primerNombre,' ',e.segundoNombre) as NombreEstudiantes ,e.fotografia,tn.Nivel,hi.HoraIngreso,hs.HoraSalida,a.EstadoAsistencia
FROM Asistencia a JOIN rfid rf ON a.IdRFID=rf.IdRFID
AND a.IdAsistencia = 1
JOIN Estudiante e ON rf.IdEstudiante=e.IdEstudiante
JOIN Inscripcion i ON e.IdEstudiante=i.IdEstudiante
JOIN Grupo g ON i.IdGrupo=g.IdGrupo
JOIN TipoNivel tn ON g.IdTipoNivel=tn.IdTipoNivel
JOIN Horario h ON g.IdGrupo=h.IdGrupo
JOIN HoraIngreso hi ON h.IdHoraIngreso=hi.IdHoraIngreso
JOIN HoraSalida hs ON h.IdHoraSalida = hs.IdHoraSalida
JOIN Dia d ON h.IdDia=d.IdDia
AND d.Dia="Lunes"
JOIN Mes m ON h.IdMes = m.IdMes
AND m.mes="Febrero"
JOIN Anio an ON h.IdAnio = an.IdAnio
AND an.anio="2019";




-- muestra los datos del Instructor ppor Ci
SELECT * FROM Instructor WHERE CiInstructor=321;



-- muestra los datos de Asistencia del  estudante por mes y anio
SELECT a.FechaHoraLlegada,DATE(a.FechaHoraLlegada) AS Fecha, TIME(a.FechaHoraLlegada) AS Hora,a.EstadoAsistencia
FROM Asistencia a JOIN rfid rf ON a.IdRFID=rf.IdRFID
AND MONTH( a.FechaHoraLlegada ) = '3'
AND YEAR( a.FechaHoraLlegada ) = '2019'
JOIN Estudiante e ON rf.IdEstudiante=e.IdEstudiante
AND E.IdEstudiante=1;

SELECT a.FechaHoraLlegada,DATE(a.FechaHoraLlegada) AS Fecha, TIME(a.FechaHoraLlegada) AS Hora,a.EstadoAsistencia
									FROM Asistencia a JOIN rfid rf ON a.IdRFID=rf.IdRFID
									AND MONTH( a.FechaHoraLlegada ) = '3'
									AND YEAR( a.FechaHoraLlegada ) = '2019'
									JOIN Estudiante e ON rf.IdEstudiante=e.IdEstudiante
									AND e.IdEstudiante='1';





	-- actualixzar un estudiante
UPDATE estudiante SET 
PrimerNombre ="",
SegundoNombre ="",
ApellidoPaterno ="",
ApellidoMaterno ="",
Ci ="",
Fotografia ="",
Direccion ="",
FotoCarnetAmverso ="",
FotoCarnetReverso ="",
FechaNacimiento ="",
Activo =,
Genero ="",
CiTutor ="",
PrimerNombreTutor ="",
SegundoNombreTutor ="",
ApellidoPaternoTutor ="",
ApellidoMaternoTutor ="",
NumeroCelularTutor ="",
DireccionTutor ="",
FotoTutor ="",
TipoTutor =""
WHERE IdEstudiante='1';

DELETE FROM estudiante WHERE IdEstudiante = 1;






	-- actualixzar un Instructor
UPDATE Instructor SET 
PrimerNombre ='',
SegundoNombre ='',
ApellidoPaterno ='',
ApellidoMaterno ='',
Fotografia ='',
Direccion ='',
FotoCarnetAmverso ='',
FotoCarnetReverso ='',
FechaNacimiento ='',
NumeroCelular ='',
Usuario ='',
Contrasenia ='',
Activo =,
Genero ='',
PrimerNombreRef ='',
SegundoNombreRef ='',
ApellidoPaternoRef ='',
ApellidoMaternoRef ='',
DireccionRef ='',
FechaNacimientoRef ='',
NumeroCelularRef =''
WHERE CiInstructor='321';

DELETE FROM estudiante WHERE IdEstudiante = 1;


-- muestra que horas tiene clase los dias lunes
SELECT hi.IdHoraIngreso,hs.IdHoraSalida
FROM  Instructor i JOIN Grupo g ON i.CiInstructor=g.CiInstructor
AND i.CiInstructor  = 321
JOIN Horario h ON g.IdGrupo=h.IdGrupo
JOIN HoraIngreso hi ON h.IdHoraIngreso=hi.IdHoraIngreso
JOIN HoraSalida hs ON h.IdHoraSalida = hs.IdHoraSalida
JOIN Dia d ON h.IdDia=d.IdDia
AND d.Dia="Lunes"
JOIN Mes m ON h.IdMes = m.IdMes
AND m.mes="Julio"
JOIN Anio an ON h.IdAnio = an.IdAnio
AND an.anio="2019";




SELECT u.ciUsuario,u.IdRol,u.primerNombre,u.segundoNombre,u.apellidoPaterno,u.apellidoMaterno,u.usuario,u.contrasenia,u.activo 
FROM Usuario u join Rol r ON u.IdRol = r.IdRol
AND u.usuario='' or '1'='1';
