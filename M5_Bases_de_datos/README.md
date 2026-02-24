# Evaluación Modular - Fundamentos Base de Datos
## Clínica Veterinaria

### Descripción del proyecto

Existen dos archivos .sql, ```database.sql``` y ```seed.sql```, el primero contiene la estructura de la base de datos, mientras que el segundo contiene los datos de prueba para poblar la base de datos.

El archivo ```create_db.bat``` es un script de Windows que automatiza el proceso de creación de la base de datos, ejecutando los comandos necesarios para crear la base de datos y cargar los archivos .sql.

En caso de estar trabajando en linux, correr el archivo ```create_db.sh``` para lograr el mismo resultado. Ojo que es posible tener que darle permisos de ejecución al archivo con el comando ```chmod +x create_db.sh```.

### Ejemplos de ejecución

Para conectar a la base de datos, se puede usar el siguiente comando en la terminal:

```bash
psql -U postgres -d clinicaveterinaria
```
Una vez conectado, se pueden ejecutar consultas SQL para interactuar con la base de datos. Por ejemplo, para obtener una lista de todas las mascotas:

```sql
SELECT * FROM mascotas;
```
```bash
 id_mascota | nombre | tipo  | fecha_nacimiento | id_dueno
------------+--------+-------+------------------+----------
          1 | Rex    | Perro | 2020-05-10       |        1
          2 | Luna   | Gato  | 2019-02-20       |        2
          3 | Fido   | Perro | 2021-03-15       |        3
(3 filas)
```

### Consultas solicitadas

1. Obtener todos los dueños y sus mascotas:

```sql
SELECT 
    d.nombre AS nombre_dueno
    ,m.nombre AS nombre_mascota
FROM duenos d
JOIN mascotas m ON d.id_dueno = m.id_dueno;
```

| nombre_dueno | nombre_mascota |
|--------------|----------------|
| Juan Pérez   | Rex            |
| Ana Gómez    | Luna           |
| Carlos Ruiz  | Fido           |

2. Obtener las atenciones realizadas a las mascotas con los detalles del profesional que atendió:

```sql
SELECT
	a.fecha_atencion AS "Fecha",
	a.descripcion AS "Descripción",
	p.nombre AS "Profesional",
	p.especialidad AS "Especialidad",
	m.nombre AS "Mascota",
	m.tipo AS "Tipo"
	
FROM atenciones a
JOIN profesionales p ON p.id_profesional = a.id_profesional
JOIN mascotas m ON a.id_mascota = m.id_mascota;
```


| Fecha       | Descripción                | Profesional   | Especialidad                   | Mascota | Tipo  |
|-------------|----------------------------|---------------|--------------------------------|---------|-------|
| 2025-03-01  | Chequeo general            | Dr. Martínez  | Veterinario                    | Rex     | Perro |
| 2025-03-05  | Tratamiento dermatológico  | Dr. Pérez     | Especialista en dermatología   | Luna    | Gato  |
| 2025-03-07  | Consulta cardiológica      | Dr. López     | Cardiólogo veterinario         | Fido    | Perro |

3. Contar la cantidad de atenciones por profesional

```sql
SELECT
	p.nombre as "Profesional",
	COUNT(id_atencion) as "Nro Atenciones"
FROM atenciones a
JOIN profesionales p ON p.id_profesional = a.id_profesional
GROUP BY p.nombre;
```

| Profesional   | Nro Atenciones |
|---------------|----------------|
| Dr. Martínez  | 1              |
| Dr. Pérez     | 1              |
| Dr. López     | 1              |

4. Actualizar la dirección de un dueño.
En este caso se actualizará la dirección del dueño con id 1, Juan Pérez.

```sql
UPDATE duenos
SET direccion = 'Calle Imaginaria 234'
WHERE id_dueno = 1;
```
```sql
SELECT * FROM duenos;
```

| id_dueno | nombre | direccion |telefono |
|-----|------|-|-|
| 2 |Ana Gómez | Avenida Siempre Viva 456 | 555-5678 |
| 3 |Carlos Ruiz | Calle 8 de Octubre 789 | 555-8765 |
| 1 |Juan Pérez | Calle Imaginaria 234 | 555-1234 |

5. Eliminar una atención, en este caso se eliminará la atención con id 2, correspondiente a la mascota Luna.

```sql
DELETE FROM atenciones
WHERE id_atencion = 2;
```
```sql
SELECT * FROM atenciones;
```

| id_atencion | fecha_atencion | descripcion | id_mascota | id_profesional |
|-------------|----------------|-------------|------------|----------------|
| 1           | 2025-03-01     | Chequeo general | 1          | 1              |
| 3           | 2025-03-07     | Consulta cardiológica | 3          | 3              |

7. Realizar una transacción para agregar una nueva mascota, atención y actualización de información.

```sql
BEGIN;

WITH 
nuevo_dueno AS (
	INSERT INTO duenos (nombre, direccion, telefono)
	VALUES ('Miguel Godoy', 'Av. Los Leones 1555 Dep 1601', '555-5945')
	RETURNING id_dueno
),
nueva_mascota AS (
    INSERT INTO mascotas (nombre, tipo, fecha_nacimiento, id_dueno) 
    SELECT 'Andy', 'Gato', '2022-01-10', id_dueno
	FROM nuevo_dueno
    RETURNING id_mascota
),
nueva_atencion AS (
	INSERT INTO atenciones (fecha_atencion, descripcion, id_mascota, id_profesional)
	SELECT '2025-03-10', 'Vacunación anual', id_mascota, 1
	FROM nueva_mascota
)

UPDATE duenos
SET telefono = '555-0001'
WHERE id_dueno IN (SELECT id_dueno FROM nuevo_dueno);

COMMIT;
```