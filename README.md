# Sistema de Gestión de Inventario - INPORTADORA_GR

## 1. Descripción del sistema

INPORTADORA_GR es un proyecto de sistema de gestión de inventario diseñado para organizar la información de productos y facilitar el control de las existencias, las compras y las ventas.

## 2. Objetivo

Desarrollar un sistema que permita administrar los productos y mantener un mejor control del inventario, reduciendo errores en los registros y facilitando la consulta de información.

## 3. Problema que busca resolver

El control manual del inventario puede provocar diferencias en las existencias, dificultades para localizar productos y retrasos al registrar compras y ventas. El sistema propone centralizar estas operaciones para facilitar el seguimiento de los movimientos del inventario.

## 4. Funcionalidades principales

- Registrar productos.
- Consultar las existencias.
- Buscar productos por nombre o código.
- Actualizar las cantidades del inventario.
- Registrar compras y ventas.
- Organizar la información de los productos.

## 5. Requisitos del sistema

### Requisitos funcionales

- RF-01: Permitir el registro y la clasificación de productos.
- RF-02: Permitir la consulta de las existencias.
- RF-03: Actualizar el inventario a partir de los movimientos registrados.
- RF-04: Facilitar la búsqueda de productos.

### Requisitos no funcionales

- RNF-01: Proteger el acceso a la información mediante controles de seguridad.
- RNF-02: Ofrecer tiempos de respuesta adecuados para las consultas habituales.

## 6. Arquitectura del sistema

Se propone una arquitectura por capas que separa las responsabilidades de los componentes:

- **Interfaz de usuario:** presenta los formularios y las opciones de interacción.
- **Lógica de negocio:** aplica las reglas para registrar y controlar las operaciones del inventario.
- **Servicios del sistema:** coordinan las solicitudes y las operaciones entre los componentes.
- **Base de datos:** almacena los datos de productos y movimientos.

### Responsabilidades del frontend y backend

**Frontend:** corresponde a la interfaz con la que interactúa el usuario para registrar productos, consultar existencias y realizar búsquedas.

**Backend:** se encargará de procesar las solicitudes, validar los datos y aplicar las reglas del negocio.

**Comunicación:** el frontend enviará las solicitudes al backend, que procesará la información y devolverá los resultados. La tecnología y el mecanismo de comunicación deberán confirmarse durante la implementación.

## 7. Modelado y diseño

El proyecto contempla el uso de diagramas UML para representar la estructura y el comportamiento del sistema. Estos modelos sirven como guía para organizar sus componentes antes de completar la implementación.

Herramienta de modelado: Visual Paradigm Online.

## 8. Herramientas de trabajo

- GitHub: alojamiento del repositorio y control de versiones.
- GitHub Issues: registro y seguimiento de tareas.
- GitHub Projects: organización del trabajo mediante un tablero Kanban.
- Visual Paradigm Online: elaboración de diagramas UML.

## 9. Gestión del proyecto

El seguimiento de las tareas se organiza mediante las siguientes columnas:

- Reserva (Backlog).
- Por hacer.
- En progreso.
- En revisión.
- Finalizado.

El estado de cada tarea debe actualizarse según el avance real del proyecto.

## 10. Estado actual

El proyecto cuenta con un repositorio de GitHub, documentación inicial de la arquitectura y tareas registradas para organizar el desarrollo. La documentación, la revisión de los modelos, las pruebas y la validación de las funcionalidades deben completarse y verificarse según el avance real.

## 11. Próximos pasos

- Revisar y completar los diagramas UML.
- Verificar la documentación técnica.
- Revisar el estado de las tareas e incidencias.
- Validar las funcionalidades cuando estén implementadas.
- Registrar los cambios relevantes en el repositorio.
