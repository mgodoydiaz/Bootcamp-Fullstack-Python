#!/bin/bash

echo "Creando base de datos..."
createdb -U postgres clinica_veterinaria

echo "Ejecutando schema..."
psql -U postgres -d clinica_veterinaria -f database.sql

echo "Cargando datos de prueba..."
psql -U postgres -d clinica_veterinaria -f seed.sql

echo "Listo."