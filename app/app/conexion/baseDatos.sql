CREATE DATABASE IF NOT EXISTS ecotech_db11;
USE ecotech_db11;

-- === TABLA USUARIO (Login y roles) ===
CREATE TABLE IF NOT EXISTS usuario(
    idUsuario INT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    direccion VARCHAR(150) NOT NULL,
    telefono VARCHAR(20) NOT NULL,
    correo VARCHAR(100) UNIQUE NOT NULL,
    rol VARCHAR(20) NOT NULL,
    hashContrasena VARCHAR(255),
    salt VARCHAR(255)
);

-- === TABLA EMPLEADO (datos laborales) ===
CREATE TABLE IF NOT EXISTS empleado(
    idUsuario INT PRIMARY KEY,
    salario DECIMAL(10,2) NOT NULL,
    fecha_inicio DATE NOT NULL,
    idDepartamento INT,
    FOREIGN KEY(idUsuario) REFERENCES usuario(idUsuario)
);

-- === TABLA DEPARTAMENTO ===
CREATE TABLE IF NOT EXISTS departamento(
    idDepartamento INT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    idGerente INT,
    FOREIGN KEY(idGerente) REFERENCES empleado(idUsuario)
);

-- === TABLA GERENTE (relación entre usuario/empleado y departamento) ===
CREATE TABLE IF NOT EXISTS gerente(
    idGerente INT PRIMARY KEY AUTO_INCREMENT,
    idUsuario INT NOT NULL,
    idDepartamento INT NOT NULL,
    UNIQUE KEY uq_gerente_usuario (idUsuario),
    FOREIGN KEY(idUsuario) REFERENCES usuario(idUsuario),
    FOREIGN KEY(idDepartamento) REFERENCES departamento(idDepartamento)
);

-- === TABLA PROYECTO ===
CREATE TABLE IF NOT EXISTS proyecto(
    idProyecto INT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion VARCHAR(255),
    fecha_inicio DATE NOT NULL
);

CREATE TABLE IF NOT EXISTS registroTiempo(
    idRegistro INT PRIMARY KEY,
    fecha DATE NOT NULL,
    horas DECIMAL(5,2) NOT NULL,
    descripcion VARCHAR(255),
    idEmpleado INT NOT NULL,
    idProyecto INT NOT NULL,
    FOREIGN KEY(idEmpleado) REFERENCES empleado(idUsuario),
    FOREIGN KEY(idProyecto) REFERENCES proyecto(idProyecto)
);
COMMIT;
