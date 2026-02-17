# Projecte odoo
 Midnight Customs - Proyecto Modular SGE
Este repositorio contiene el desarrollo del módulo personalizado para Odoo 17 enfocado en la gestión integral de un taller de personalización de vehículos de alta gama. El proyecto forma parte de la evaluación modular del IES Benigasló.


Sobre el Proyecto
Midnight Customs es un sistema ERP diseñado para controlar el flujo de trabajo de un taller de tuning. Permite gestionar desde la entrada del vehículo hasta la entrega final, asegurando que los mecánicos asignados tengan las certificaciones adecuadas y optimizando los tiempos de entrega.


Nota: Este repositorio es privado para evitar copias externas y se utiliza como entorno de trabajo real.


 Requisitos Técnicos Implementados
Siguiendo las directrices de la guía docente, el módulo incluye:


Modelos Relacionados: Definición de clases para vehículos y reparaciones con relaciones Many2one y One2many.


Vistas Personalizadas: Implementación de vistas tipo Formulario, Árbol (Lista), Kanban para estados y Calendario de citas.

Lógica de Negocio (Python):

Métodos computados para el cálculo de presupuestos.

Constraints para validar que el mecánico tenga el carnet necesario para el vehículo.

Interfaz Avanzada:

Uso de colores dinámicos en las listas según la urgencia del trabajo.


Buscador avanzado con filtros de "Alta Prioridad".



Wizard: Asistente rápido para la asignación masiva de mecánicos a partes de trabajo.



Reporting: Generación de fichas técnicas y facturas en PDF.



Web Controller: Endpoint externo para consultar el estado del vehículo mediante un código único.


📂 Estructura del Repositorio
Organizado de forma clara para facilitar la navegación y revisión:

Bash

├── models/             # Lógica de Python (clases y métodos)
├── views/              # Definiciones XML de la interfaz
├── wizards/            # Lógica y vistas del asistente de asignación
├── report/             # Plantillas QWeb para los PDF
├── controllers/        # Rutas para el acceso web externo
├── security/           # Reglas de acceso y grupos
├── static/             # Imágenes y recursos visuales
└── __manifest__.py     # Declaración oficial del módulo Odoo
🛠️ Instalación y Uso
Clonar el repositorio en tu carpeta de addons.

Asegurarse de tener Docker configurado con la imagen privada correspondiente.

Actualizar la lista de aplicaciones en Odoo e instalar Midnight Customs.

👤 Autor
Nombre: Diego Martín García


Curso: 2º DAW - IES Benigasló 



Fecha: Febrero 2026 


Licencia: CC BY-NC-SA (Reconocimiento - No Comercial - CompartirIgual).
