DROP DATABASE IF EXISTS proyecto_caleb;
CREATE DATABASE proyecto_caleb;
USE proyecto_caleb;

-- -----------------------------------------------------
-- Table `funcionarios`.`AcuaticClub`
-- -----------------------------------------------------
CREATE TABLE horarios(
  id INT PRIMARY KEY AUTO_INCREMENT,
  hora_inicio TIME NOT NULL,
  hora_inicio_reseso TIME NOT NULL,
  hora_fin_reseso TIME NOT NULL,
  hora_fin TIME NOT NULL,
  domingo TINYINT NOT NULL,
  lunes TINYINT NOT NULL,
  martes TINYINT NOT NULL,
  miercoles TINYINT NOT NULL,
  jueves TINYINT NOT NULL,
  viernes TINYINT NOT NULL,
  sabado TINYINT NOT NULL
);

-- -----------------------------------------------------
-- Table `funcionarios`.`AcuaticClub`
-- -----------------------------------------------------
CREATE TABLE rols(
  id INT PRIMARY KEY AUTO_INCREMENT,
  nombre VARCHAR(45) NOT NULL,
  id_horarios INT NOT NULL,
  FOREIGN KEY (id_horarios) REFERENCES horarios(id)
);


-- -----------------------------------------------------
-- Table `biblioteca`.`TipoTutor`
-- -----------------------------------------------------
CREATE TABLE ubicaciones (
  id INT PRIMARY KEY  AUTO_INCREMENT,
  nombre VARCHAR(45) NOT NULL,
  latitud DECIMAL(10, 8) NOT NULL,
  longitud DECIMAL(11, 8) NOT NULL
);

-- -----------------------------------------------------
-- Table `funcionarios`.`AcuaticClub`
-- -----------------------------------------------------
CREATE TABLE funcionarios(
  id INT PRIMARY KEY AUTO_INCREMENT,
  nombres VARCHAR(45) NOT NULL,
  apellidos VARCHAR(45) NOT NULL,
  ci VARCHAR(45) NOT NULL,
  foto VARCHAR(45) NOT NULL,
  celular VARCHAR(45) NULL,
  fecha_nac DATE NOT NULL,
  user VARCHAR(45) NULL,
  password VARCHAR(45) NULL,
  id_rols INT NOT NULL,
  FOREIGN KEY (id_rols) REFERENCES rols(id),
  id_ubicaciones INT NOT NULL,
  FOREIGN KEY (id_ubicaciones) REFERENCES ubicaciones(id)
);

CREATE TABLE gestion(
  id INT PRIMARY KEY AUTO_INCREMENT,
  nombre VARCHAR(45) NOT NULL
);

CREATE TABLE mes(
  id INT PRIMARY KEY AUTO_INCREMENT,
  nombre VARCHAR(45) NOT NULL,
  numero INT NOT NULL,
  id_gestion INT NOT NULL,
  FOREIGN KEY (id_gestion) REFERENCES gestion(id)
);

CREATE TABLE dia(
  id INT PRIMARY KEY AUTO_INCREMENT,
  nombre VARCHAR(45) NOT NULL,
  numero INT NOT NULL,
  estado VARCHAR(45) NOT NULL,
  detalle VARCHAR(45) NULL,
  fecha DATE NOT NULL,
  hora_inicio TIME NOT NULL,
  hora_inicio_reseso TIME NOT NULL,
  hora_fin_reseso TIME NOT NULL,
  hora_fin TIME NOT NULL,
  posicion INT NOT NULL,
  hora_retrasos TIME NOT NULL,
  id_funcionarios INT NOT NULL,
  FOREIGN KEY (id_funcionarios) REFERENCES funcionarios(id),
  id_mes INT NOT NULL,
  FOREIGN KEY (id_mes) REFERENCES mes(id)
);

CREATE TABLE ubicacion_hora(
  id INT PRIMARY KEY AUTO_INCREMENT,
  hora TIME NOT NULL,
  latitud DECIMAL(10, 8) NOT NULL,
  longitud DECIMAL(11, 8) NOT NULL,
  id_dia INT NOT NULL,
  FOREIGN KEY (id_dia) REFERENCES dia(id)
);


-- -- -- -----------------------------------------------------
-- -- -- Table `biblioteca`.`Tutor`
-- -- -- -----------------------------------------------------
-- -- CREATE TABLE Tutor (
-- -- CiTutor VARCHAR(45) UNIQUE PRIMARY KEY,
-- -- PrimerNombre VARCHAR(45) NOT NULL,
-- -- SegundoNombre VARCHAR(45) NULL,
-- -- ApellidoPaterno VARCHAR(45) NOT NULL,
-- -- ApellidoMaterno VARCHAR(45) NOT NULL,
-- -- NumeroCelular VARCHAR(45) NOT NULL,
-- -- Direccion VARCHAR(45) NOT NULL,
-- -- Foto VARCHAR(45) NOT NULL,
-- -- IdTipoTutor InT NOT NULL,
-- -- FOREIGN KEY (IdTipoTutor) REFERENCES TipoTutor(IdTipoTutor)
-- -- );


-- -- -----------------------------------------------------
-- -- Table `biblioteca`.`TipoNivel`
-- -- -----------------------------------------------------
-- CREATE TABLE TipoNivel (
-- IdTipoNivel INT PRIMARY KEY  AUTO_INCREMENT,
-- Nivel VARCHAR(45) NOT NULL
-- );

-- -- -----------------------------------------------------
-- -- Table `biblioteca`.`Dia`
-- -- -----------------------------------------------------
-- CREATE TABLE Dia (
-- IdDia INT PRIMARY KEY AUTO_INCREMENT,
-- Dia VARCHAR(45) NOT NULL
-- );



-- -- -----------------------------------------------------
-- -- Table `biblioteca`.`Dia`
-- -- -----------------------------------------------------
-- CREATE TABLE Mes (
-- IdMes INT PRIMARY KEY AUTO_INCREMENT,
-- Mes VARCHAR(45) NOT NULL
-- );



-- -- -----------------------------------------------------
-- -- Table `biblioteca`.`Dia`
-- -- -----------------------------------------------------
-- CREATE TABLE Anio (
-- IdAnio INT PRIMARY KEY AUTO_INCREMENT,
-- Anio VARCHAR(45) NOT NULL
-- );



-- -- -----------------------------------------------------
-- -- Table `biblioteca`.`HoraAM`
-- -- -----------------------------------------------------
-- CREATE TABLE HoraIngreso (
-- IdHoraIngreso INT PRIMARY KEY AUTO_INCREMENT,
-- HoraIngreso TIME NOT NULL
-- );

-- -- -----------------------------------------------------
-- -- Table `biblioteca`.`HoraAM`
-- -- -----------------------------------------------------
-- CREATE TABLE HoraSalida (
-- IdHoraSalida INT PRIMARY KEY AUTO_INCREMENT,
-- HoraSalida TIME NOT NULL
-- );

-- -- -- -----------------------------------------------------
-- -- -- Table `biblioteca`.`Referencia`
-- -- -- -----------------------------------------------------
-- -- CREATE TABLE Referencia  (
-- -- CiReferencia VARCHAR(45) UNIQUE PRIMARY KEY,
-- -- PrimerNombre VARCHAR(45) NOT NULL,
-- -- SegundoNombre VARCHAR(45) NULL,
-- -- ApellidoPaterno VARCHAR(45) NOT NULL,
-- -- ApellidoMaterno VARCHAR(45) NOT NULL,
-- -- Direccion VARCHAR(45) NOT NULL,
-- -- FechaNacimiento DATE NOT NULL,
-- -- NumeroCelular VARCHAR(45) NOT NULL
-- -- );


-- -- -----------------------------------------------------
-- -- Table `biblioteca`.`Instructor`
-- -- -----------------------------------------------------
-- CREATE TABLE Instructor  (
-- CiInstructor VARCHAR(45) UNIQUE PRIMARY KEY,
-- PrimerNombre VARCHAR(45) NOT NULL,
-- SegundoNombre VARCHAR(45) NULL,
-- ApellidoPaterno VARCHAR(45) NOT NULL,
-- ApellidoMaterno VARCHAR(45) NOT NULL,
-- Fotografia VARCHAR(45) NOT NULL,
-- Direccion VARCHAR(45) NOT NULL,
-- FotoCarnetAmverso VARCHAR(45) NOT NULL,
-- FotoCarnetReverso VARCHAR(45) NOT NULL,
-- FechaNacimiento DATE NOT NULL,
-- NumeroCelular VARCHAR(45) NOT NULL,
-- Usuario VARCHAR(45) NOT NULL,
-- Contrasenia VARCHAR(45) NOT NULL,
-- Activo TINYINT NOT NULL,
-- Genero VARCHAR(45) NOT NULL,
-- PrimerNombreRef VARCHAR(45) NOT NULL,
-- SegundoNombreRef VARCHAR(45) NULL,
-- ApellidoPaternoRef VARCHAR(45) NOT NULL,
-- ApellidoMaternoRef VARCHAR(45) NOT NULL,
-- DireccionRef VARCHAR(45) NOT NULL,
-- FechaNacimientoRef DATE NOT NULL,
-- NumeroCelularRef VARCHAR(45) NOT NULL
-- );


-- -- -----------------------------------------------------
-- -- Table `biblioteca`.`Grupo`
-- -- -----------------------------------------------------
-- CREATE TABLE Grupo (
-- IdGrupo INT PRIMARY KEY AUTO_INCREMENT,
-- IdTipoNivel INT NOT NULL,
-- CiInstructor VARCHAR(45) NOT NULL,
-- FOREIGN KEY (IdTipoNivel) REFERENCES TipoNivel(IdTipoNivel),
-- FOREIGN KEY (CiInstructor) REFERENCES Instructor(CiInstructor)
-- );


-- -- -----------------------------------------------------
-- -- Table `biblioteca`.`Horario`
-- -- -----------------------------------------------------
-- CREATE TABLE Horario (
-- IdHorario INT PRIMARY KEY AUTO_INCREMENT,
-- Monto VARCHAR(45) NOT NULL,
-- Cantidad INT(45) NOT NULL,
-- IdDia INT NOT NULL,
-- IdMes INT NOT NULL,
-- IdAnio INT NOT NULL,
-- IdGrupo INT NOT NULL,
-- IdHoraIngreso INT NOT NULL,
-- IdHoraSalida INT NOT NULL,
-- FOREIGN KEY (IdDia) REFERENCES Dia(IdDia),
-- FOREIGN KEY (IdMes) REFERENCES Mes(IdMes),
-- FOREIGN KEY (IdAnio) REFERENCES Anio(IdAnio),
-- FOREIGN KEY (IdGrupo) REFERENCES Grupo(IdGrupo),
-- FOREIGN KEY (IdHoraIngreso) REFERENCES HoraIngreso(IdHoraIngreso),
-- FOREIGN KEY (IdHoraSalida) REFERENCES HoraSalida(IdHoraSalida)
-- );



-- -- -----------------------------------------------------
-- -- Table `biblioteca`.`Estudiante`
-- -- -----------------------------------------------------
-- CREATE TABLE Estudiante (
-- IdEstudiante INT AUTO_INCREMENT PRIMARY KEY,
-- PrimerNombre VARCHAR(45) NOT NULL,
-- SegundoNombre VARCHAR(45) NULL,
-- ApellidoPaterno VARCHAR(45) NOT NULL,
-- ApellidoMaterno VARCHAR(45) NOT NULL,
-- Ci VARCHAR(45) NULL,
-- Fotografia VARCHAR(200) NOT NULL,
-- Direccion VARCHAR(45) NOT NULL,
-- FotoCarnetAmverso VARCHAR(200) NULL,
-- FotoCarnetReverso VARCHAR(200) NULL,
-- FechaNacimiento DATE NOT NULL,
-- Activo TINYINT NOT NULL,
-- Genero VARCHAR(45) NOT NULL,
-- CiTutor VARCHAR(45) NULL,
-- PrimerNombreTutor VARCHAR(45) NOT NULL,
-- SegundoNombreTutor VARCHAR(45) NULL,
-- ApellidoPaternoTutor VARCHAR(45) NOT NULL,
-- ApellidoMaternoTutor VARCHAR(45) NOT NULL,
-- NumeroCelularTutor VARCHAR(45) NOT NULL,
-- DireccionTutor VARCHAR(45) NOT NULL,
-- FotoTutor VARCHAR(200) NOT NULL,
-- TipoTutor VARCHAR(45) NOT NULL
-- );


-- -- -----------------------------------------------------
-- -- Table `biblioteca`.`Grupo`
-- -- -----------------------------------------------------
-- CREATE TABLE Inscripcion (
-- IdInscripcion INT AUTO_INCREMENT PRIMARY KEY,
-- IdEstudiante INT NOT NULL,
-- IdGrupo INT NOT NULL,
-- FOREIGN KEY (IdEstudiante) REFERENCES Estudiante(IdEstudiante),
-- FOREIGN KEY (IdGrupo) REFERENCES Grupo(IdGrupo)
-- );


-- -- -- -----------------------------------------------------
-- -- -- Table `biblioteca`.`Gestion`
-- -- -- -----------------------------------------------------
-- -- CREATE TABLE Gestion (
-- -- IdGestion INT AUTO_INCREMENT PRIMARY KEY,
-- -- Gestion VARCHAR(45) NOT NULL,
-- -- Monto VARCHAR(45) NOT NULL,
-- -- Activo TINYINT NOT NULL
-- -- );



-- -- -- -----------------------------------------------------
-- -- -- Table `biblioteca`.`InscripcionMensualidad`
-- -- -- -----------------------------------------------------
-- -- CREATE TABLE InscripcionMensualidad (
-- -- IdInscripcionMensualidad INT AUTO_INCREMENT PRIMARY KEY,
-- -- Mes VARCHAR(45) NOT NULL,
-- -- FechaHora DATETIME NOT NULL,
-- -- IdEstudiante INT NOT NULL,
-- -- IdGestion INT NOT NULL,
-- -- FOREIGN KEY (IdEstudiante) REFERENCES Estudiante(IdEstudiante),
-- -- FOREIGN KEY (IdGestion) REFERENCES Gestion(IdGestion)
-- -- );


-- -- -----------------------------------------------------
-- -- Table `biblioteca`.`RFID`
-- -- -----------------------------------------------------
-- CREATE TABLE RFID (
-- IdRFID INT AUTO_INCREMENT PRIMARY KEY,
-- IdEstudiante INT NOT NULL,
-- RFID VARCHAR(45) NOT NULL,
-- FOREIGN KEY (IdEstudiante) REFERENCES Estudiante(IdEstudiante)
-- );


-- -- -----------------------------------------------------
-- -- Table `biblioteca`.`Asistencia`
-- -- -----------------------------------------------------
-- CREATE TABLE Asistencia (
-- IdAsistencia INT AUTO_INCREMENT PRIMARY KEY,
-- FechaHoraLlegada DATETIME NOT NULL,
-- EstadoAsistencia TINYINT NOT NULL,
-- IdRFID INT NOT NULL,
-- FOREIGN KEY (IdRFID) REFERENCES RFID(IdRFID)
-- );


-- -- -----------------------------------------------------
-- -- Table `biblioteca`.`Rol`
-- -- -----------------------------------------------------
-- CREATE TABLE Rol (
-- IdRol INT AUTO_INCREMENT PRIMARY KEY,
-- Rol VARCHAR(45) NOT NULL
-- );


-- -- -----------------------------------------------------
-- -- Table `biblioteca`.`Usuario`
-- -- -----------------------------------------------------
-- CREATE TABLE Usuario (
-- CiUsuario VARCHAR(45) UNIQUE PRIMARY KEY ,
-- PrimerNombre VARCHAR(45) NOT NULL,
-- SegundoNombre VARCHAR(45) NULL,
-- ApellidoPaterno VARCHAR(45) NOT NULL,
-- ApellidoMaterno VARCHAR(45) NOT NULL,
-- Fotografia VARCHAR(200) NOT NULL,
-- Direccion VARCHAR(45) NOT NULL,
-- FotoCarnetAmverso VARCHAR(200) NOT NULL,
-- FotoCarnetReverso VARCHAR(200) NOT NULL,
-- FechaNacimiento DATE NOT NULL,
-- Usuario VARCHAR(45) NOT NULL,
-- Contrasenia VARCHAR(45) NOT NULL,
-- Activo TINYINT NOT NULL,
-- IdRol INT NOT NULL,
-- FOREIGN KEY (IdRol) REFERENCES Rol(IdRol)
-- );



-- -- -----------------------------------------------------
-- -- Table `biblioteca`.`Factura`
-- -- -----------------------------------------------------
-- CREATE TABLE Factura (
-- IdFactura INT AUTO_INCREMENT PRIMARY KEY,
-- FechaHoraEmision DATETIME NOT NULL,
-- NombreCliente VARCHAR(45) NOT NULL,
-- QR VARCHAR(45) NOT NULL,
-- Nit VARCHAR(45) NOT NULL,
-- IdInscripcion INT NOT NULL,
-- CiUsuario VARCHAR(45) NOT NULL,
-- FOREIGN KEY (Nit) REFERENCES AcuaticClub(Nit),
-- FOREIGN KEY (IdInscripcion) REFERENCES Inscripcion(IdInscripcion),
-- FOREIGN KEY (CiUsuario) REFERENCES Usuario(CiUsuario)
-- );
