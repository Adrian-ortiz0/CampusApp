# Campuslands App

## Descripción

Campuslands app es un software encargado de gestionar todas las operaciones tanto como de administrativos como de campers, permitiendo asi una mayor eficiencia y orden dentro de la empresa campuslands

**Estado del Proyecto**: ![Estado](https://img.shields.io/badge/estado-en%20progreso-yellow)

## Tabla de Contenidos

| Sección                             | Descripción                            |
| ----------------------------------- | -------------------------------------- |
| [Descripción](#descripción)         | Descripción general del proyecto       |
| [Características](#características) | Funcionalidades principales            |
| [Instalación](#instalación)         | Cómo instalar y configurar el proyecto |
| [Uso](#uso)                         | Instrucciones para usar el proyecto    |
| [Contato](#contacto)                | Contacto                               |

## Descripción

Este es un proyecto para campuslands, un software capaz de controlar la gestion de todas las tareas dentro de la organización, este incluye las siguiente caracteristicas.

## Características

### Administrador

- **Registrar campers**: Esta función permite al administrador registrar campers y posteriormente realizarles pruebas para poder saber si estos aprueban o no y asi modificar su estado dentro del proceso.
- **Aprobar campers**: Esta función permite al usuario aprobar campers una vez realizadas las pruebas de admisión
- **Registrar trainers**: Esta función permite registrar nuevos trainers en la base de datos de la organización
- **Asignar campers a trainers**: Con esta funcionalidad de le permite al administrador asignar campers a trainers, solo pueden ser maximo 30 campers por trainer.
- **Asignar trainers a rutas**: Esta funcion permite asignar una ruta a cada trainer.
- **Asignar trainers a salones**: Esta funcionalidad permite asignar trainers a salones, esto toma en cuenta los horarios del trainer.
- **Reporte de campers**: El administrador también tomará en cuenta el estado de los campers para poder ver un reporte de todos estos.
- **Asignar notas a campers**: El administrador será el encargado de asignar notas a los campers y con base a esto cambiar el estado de estos.
- **Modificar el estado de los campers**: Esta función permite al admin modificar el estado de los campers en caso de ser necesario.
- **Crear rutas**: Esta función permite al administrador crear nuevas rutas junto con nuevos skills.

### Trainers

- **Presentar pruebas**: El trainer tiene la capacidad de realizar pruebas a sus alumnos en cada skill

### Campers

- **Ver notas**: Los campers podrán ingresar al sistema y ver unicamente las notas en cada skill.

## Instalación

1. **Clona el Repositorio**

   Primero, necesitarás clonar el repositorio del proyecto en tu máquina local. Abre una terminal y ejecuta el siguiente comando:

   ```bash
   git clone https://github.com/Adrian-ortiz0/CampusApp

   ```

2. Navega al Directorio del Proyecto

   Después de clonar el repositorio, cambia al directorio del proyecto con el siguiente comando:

   ```bash
   cd CampusApp
   ```

3. Proceso de Abrir:
   una vez ubicado dentro de tu carpetas se puede utilizar
   ```bash
   code .
   ```

## Uso

### Acceso al sistema

1. Iniciar la aplicación desde el main.py

## Panel de Administrador

Aquí puedes gestionar todas las operaciones administrativas. Las funciones disponibles son:

### Registrar Campers

1. Accede a la sección "Registrar Campers".
2. Completa el formulario con la información del camper.
3. Haz clic en "Guardar" para registrar el camper en la base de datos.

### Aprobar Campers

1. Ve a la sección "Campers Pendientes".
2. Revisa las pruebas realizadas por cada camper.
3. Haz clic en "Aprobar" para cambiar el estado del camper a aprobado.

### Registrar Trainers

1. Dirígete a "Registrar Trainers".
2. Introduce los detalles del trainer y haz clic en "Guardar".

### Asignar Campers a Trainers

1. Ve a "Asignar Campers a Trainers".
2. Selecciona un trainer y asigna hasta 30 campers a dicho trainer.

### Asignar Trainers a Rutas

1. En la sección "Asignar Trainers a Rutas", elige un trainer y una ruta y confirma la asignación.

### Asignar Trainers a Salones

1. Accede a "Asignar Trainers a Salones".
2. Elige un trainer y un salón, asegurándote de que los horarios coincidan.

### Reporte de Campers

1. Navega a "Reporte de Campers".
2. Consulta el estado de todos los campers y genera reportes según sea necesario.

### Asignar Notas a Campers

1. En "Asignar Notas", selecciona el camper y el skill.
2. Introduce la nota y haz clic en "Guardar".

### Modificar el Estado de los Campers

1. Dirígete a "Modificar Estado".
2. Selecciona el camper cuyo estado deseas cambiar y ajusta según sea necesario.

### Crear Rutas

1. Accede a "Crear Rutas".
2. Introduce los detalles de la nueva ruta y los skills asociados.
3. Haz clic en "Guardar" para añadir la ruta a la base de datos.

## Panel de Trainers

Los trainers pueden realizar las siguientes tareas:

### Presentar Pruebas

1. Ve a "Presentar Pruebas".
2. Selecciona el skill y el camper al que se le va a realizar la prueba.
3. Introduce los resultados y haz clic en "Guardar".

## Panel de Campers

Los campers tienen acceso a las siguientes funcionalidades:

### Ver Notas

1. Accede a la sección "Ver Notas".
2. Consulta las notas en cada skill que hayas completado.

## Contacto

- dxniel7328gmail.com
