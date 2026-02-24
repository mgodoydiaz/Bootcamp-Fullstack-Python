-- Datos de ejemplo para database clinica_veterinaria

-- Insertar duenos
INSERT INTO duenos (nombre, direccion, telefono) VALUES 
('Juan Pérez', 'Calle Falsa 123', '555-1234'),
('Ana Gémez', 'Avenida Siempre Viva 456', '555-5678'),
('Carlos Ruiz', 'Calle 8 de Octubre 789', '555-8765');


-- Insertar mascotas
INSERT INTO mascotas (nombre, tipo, fecha_nacimiento, id_dueno) VALUES 
('Rex', 'Perro', '2020-05-10', 1),
('Luna', 'Gato', '2019-02-20', 2),
('Fido', 'Perro', '2021-03-15', 3);


-- Insertar profesionales
INSERT INTO profesionales (nombre, especialidad) VALUES 
('Dr. Martínez', 'Veterinario'),
('Dr. Pérez', 'Especialista en dermatología'),
('Dr. López', 'Cardiólogo veterinario');


-- Insertar atenciones
INSERT INTO atenciones (fecha_atencion, descripcion, id_mascota, id_profesional) VALUES 
('2025-03-01', 'Chequeo general', 1, 1),
('2025-03-05', 'Tratamiento dermatológico', 2, 2),
('2025-03-07', 'Consulta cardiológica', 3, 3);