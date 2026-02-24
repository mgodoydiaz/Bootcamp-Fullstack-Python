@echo off

echo Creando la base de datos ....
createdb -U postgres clinica_veterinaria

echo Creando el esquema de la base de datos ....
psql -U postgres -d clinica_veterinaria -f database.sql

echo Poblando la base de datos con datos de prueba ....
psql -U postgres -d clinica_veterinaria -f seed.sql

echo Base de datos creada y poblada exitosamente.
pause