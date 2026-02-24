-- 1. Creacion de la base de datos en postgreSQL

CREATE DATABASE clinica_veterinaria;

-- 2. Creacion de tablas

CREATE TABLE duenos (
    id_dueno SERIAL PRIMARY KEY, -- Serial es un tipo de dato que se auto incrementa
    nombre VARCHAR(100),
    direccion VARCHAR(200),
    telefono VARCHAR(20) 
);


CREATE TABLE mascotas (
    id_mascota SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    tipo VARCHAR(50),
    fecha_nacimiento DATE,
    id_dueno INT,
    FOREIGN KEY (id_dueno) REFERENCES duenos(id_dueno) -- Relacion con la tabla duenos
);


CREATE TABLE profesionales (
    id_profesional SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    especialidad VARCHAR(100)
);


CREATE TABLE atenciones (
    id_atencion SERIAL PRIMARY KEY,
    fecha_atencion DATE,
    descripcion TEXT,
    id_mascota INT,
    id_profesional INT,
    FOREIGN KEY (id_mascota) REFERENCES mascotas(id_mascota), -- Relacion con la tabla mascotas
    FOREIGN KEY (id_profesional) REFERENCES profesionales(id_profesional) -- Relacion con la tabla profesionales
);


