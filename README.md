# 🛠️ Midnight Customs - Proyecto Modular SGE

[cite_start]Este repositorio contiene el desarrollo del módulo personalizado para **Odoo 17** enfocado en la gestión integral de un taller de personalización de vehículos de alta gama[cite: 17, 18]. [cite_start]El proyecto forma parte de la evaluación modular del **IES Benigasló**[cite: 12, 25].

## 📌 Sobre el Proyecto
**Midnight Customs** es un sistema ERP diseñado para controlar el flujo de trabajo de un taller de tuning. [cite_start]Permite gestionar desde la entrada del vehículo hasta la entrega final, asegurando que los mecánicos asignados tengan las certificaciones adecuadas y optimizando los tiempos de entrega[cite: 108, 111].

> [cite_start]**Nota:** Este repositorio es privado para evitar copias externas y se utiliza como entorno de trabajo real[cite: 61, 63, 69].

---

## 🚀 Requisitos Técnicos Implementados
[cite_start]Siguiendo las directrices de la guía docente, el módulo incluye[cite: 82, 83]:

* [cite_start]**Modelos Relacionados**: Definición de clases para vehículos y reparaciones con relaciones `Many2one` y `One2many`[cite: 87].
* [cite_start]**Vistas Personalizadas**: Implementación de vistas tipo Formulario, Árbol (Lista), Kanban para estados y Calendario de citas[cite: 84].
* **Lógica de Negocio (Python)**:
    * [cite_start]Métodos computados para el cálculo de presupuestos[cite: 85].
    * [cite_start]`Constraints` para validar que el mecánico tenga el carnet necesario para el vehículo[cite: 85, 108].
* **Interfaz Avanzada**:
    * [cite_start]Uso de colores dinámicos en las listas según la urgencia del trabajo[cite: 89, 114].
    * [cite_start]Buscador avanzado con filtros de "Alta Prioridad" y procesos de ordenación[cite: 86, 110].
* [cite_start]**Wizard**: Asistente rápido para la asignación masiva de mecánicos a partes de trabajo[cite: 88, 116].
* [cite_start]**Reporting**: Generación de fichas técnicas y facturas en PDF[cite: 90, 117].
* [cite_start]**Web Controller**: Endpoint externo para consultar el estado del vehículo mediante un código único[cite: 91, 118].

---

## 📂 Estructura del Repositorio
[cite_start]Organizado de forma clara para facilitar la navegación y revisión[cite: 64]:

```bash
├── models/             # Lógica de Python (clases y métodos)
├── views/              # Definiciones XML de la interfaz
├── wizards/            # Lógica y vistas del asistente de asignación
├── report/             # Plantillas QWeb para los PDF
├── controllers/        # Rutas para el acceso web externo
├── security/           # Reglas de acceso y grupos
├── static/             # Imágenes y recursos visuales
└── __manifest__.py     # Declaración oficial del módulo Odoo


