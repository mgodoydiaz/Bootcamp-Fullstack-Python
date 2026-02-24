# 🏥 Evaluación Modular 3

## Clínica "Doctor Python"

## 📌 Problema

En esta evaluación se solicita desarrollar un programa en Python que
simule la gestión de horas médicas en una clínica llamada **Doctor
Python**.

El sistema debe permitir:

-   Registrar horas médicas\
-   Listar horas registradas\
-   Buscar una hora por RUT\
-   Modificar una hora existente\
-   Eliminar una hora\
-   Mostrar un menú interactivo hasta que el usuario decida salir

El programa debe:

-   Utilizar funciones definidas por el usuario\
-   Utilizar `input()` para capturar datos\
-   Usar listas para almacenar la información\
-   Implementar estructuras `while`, `for` e `if`\
-   Trabajar completamente en memoria RAM

------------------------------------------------------------------------

## 🧠 Enfoque de la Solución

El programa fue desarrollado utilizando programación estructurada en
Python.

Se definió una lista global llamada `horas`, la cual almacena cada hora
médica como un diccionario con los siguientes datos:

-   rut\
-   nombre\
-   direccion\
-   edad\
-   comuna\
-   celular\
-   correo\
-   prevision\
-   fecha\
-   hora

Cada registro corresponde a un paciente con su hora médica asociada.

------------------------------------------------------------------------

## ⚙️ Funcionalidades Implementadas

### 1️⃣ Registrar hora

Se solicita al usuario ingresar todos los datos del paciente mediante
`input()` y se almacenan en un diccionario que se agrega a la lista
`horas`.

### 2️⃣ Listar horas

Recorre la lista con un ciclo `for` y muestra todos los registros
almacenados.

### 3️⃣ Buscar hora

Solicita un RUT y recorre la lista para encontrar coincidencia.\
Si existe, muestra los datos.\
Si no, informa que el paciente no fue encontrado.

### 4️⃣ Eliminar hora

Busca por RUT y elimina el registro usando `pop()`.

### 5️⃣ Modificar hora

Busca por RUT y permite modificar todos o algunos campos.\
Si el usuario deja un campo vacío, el valor original se mantiene.

### 6️⃣ Menú interactivo

Se implementa un ciclo `while True` que mantiene el programa en
ejecución hasta que el usuario seleccione la opción salir.

------------------------------------------------------------------------

## 🏗️ Estructura Técnica

Principales elementos utilizados:

-   Lista como estructura de almacenamiento\
-   Diccionarios para representar cada hora\
-   Funciones definidas por el usuario\
-   Ciclos `while` y `for`\
-   Condicionales `if`\
-   Función `input()`

------------------------------------------------------------------------

## 💡 Decisiones de Diseño

-   Se trabajó completamente en memoria RAM\
-   La edad se almacena como string ya que no se realizan operaciones
    matemáticas\
-   Se utilizó búsqueda secuencial para simplificar la lógica\
-   Se mantuvo enfoque en fundamentos de Python

------------------------------------------------------------------------

## 🚀 Cómo Ejecutar

``` bash
python evaluacion_modular.py
```

------------------------------------------------------------------------

## 🎯 Conclusión

La solución cumple con los criterios solicitados en la evaluación y
demuestra el uso correcto de estructuras básicas de Python aplicadas a
un caso práctico.
