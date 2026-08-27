```python
import streamlit as st
from urllib.parse import quote

# ============================================================
# CONFIGURACIÓN
# ============================================================

st.set_page_config(
    page_title="Catálogo de Cursos | Capacitación Tecnológica",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ============================================================
# DATOS DE CONTACTO
# ============================================================

WHATSAPP_NUMBER = "50662614659"
CONTACT_EMAIL = "gonzalezestebanm9@gmail.com"
COMPANY_NAME = "Capacitación Tecnológica"

# ============================================================
# CURSOS
# ============================================================

COURSES = [

    # ========================================================
    # INTELIGENCIA ARTIFICIAL
    # ========================================================

    {
        "category": "Inteligencia Artificial",
        "icon": "🤖",
        "name": "Microsoft 365 Copilot para Usuarios Finales",
        "hours": 8,
        "price": 600,
        "level": "Básico",
        "objective": (
            "Desarrollar habilidades prácticas para utilizar Microsoft 365 Copilot "
            "como asistente de productividad en las principales herramientas de Microsoft 365."
        ),
        "topics": [
            "Introducción a Microsoft 365 Copilot",
            "Conceptos de Inteligencia Artificial Generativa",
            "Prompt Engineering aplicado a productividad",
            "Copilot en Microsoft Word",
            "Copilot en Microsoft Excel",
            "Copilot en Microsoft PowerPoint",
            "Copilot en Outlook",
            "Copilot en Microsoft Teams",
            "Buenas prácticas y uso responsable de IA",
        ],
    },

    {
        "category": "Inteligencia Artificial",
        "icon": "🤖",
        "name": "Copilot para Empresas: Productividad con IA",
        "hours": 16,
        "price": 1000,
        "level": "Intermedio",
        "objective": (
            "Aplicar Microsoft Copilot en escenarios empresariales para mejorar "
            "la productividad, generación de contenido, análisis de información y colaboración."
        ),
        "topics": [
            "IA generativa en entornos empresariales",
            "Microsoft Copilot y Microsoft 365",
            "Casos de uso empresariales",
            "Creación de prompts efectivos",
            "Generación de documentos",
            "Análisis y resumen de información",
            "Presentaciones asistidas por IA",
            "Productividad con Outlook y Teams",
            "Gobernanza y uso responsable",
        ],
    },

    {
        "category": "Inteligencia Artificial",
        "icon": "🧠",
        "name": "Introducción a la Inteligencia Artificial Generativa",
        "hours": 16,
        "price": 1000,
        "level": "Básico",
        "objective": (
            "Comprender los fundamentos de la Inteligencia Artificial Generativa "
            "y utilizar modelos generativos en escenarios profesionales y empresariales."
        ),
        "topics": [
            "Fundamentos de Inteligencia Artificial",
            "Machine Learning e Inteligencia Artificial",
            "Inteligencia Artificial Generativa",
            "Large Language Models",
            "Modelos multimodales",
            "Generación de texto",
            "Generación de imágenes",
            "Prompt Engineering",
            "Casos de uso empresariales",
            "Riesgos, ética y seguridad",
        ],
    },

    {
        "category": "Inteligencia Artificial",
        "icon": "✍️",
        "name": "Prompt Engineering para Profesionales",
        "hours": 16,
        "price": 1100,
        "level": "Intermedio",
        "objective": (
            "Diseñar instrucciones efectivas para modelos de Inteligencia Artificial "
            "Generativa, mejorando la calidad, precisión y consistencia de las respuestas."
        ),
        "topics": [
            "Fundamentos del Prompt Engineering",
            "Anatomía de un prompt",
            "Definición de contexto",
            "Roles e instrucciones",
            "Restricciones y formato de salida",
            "Zero-shot prompting",
            "Few-shot prompting",
            "Prompts estructurados",
            "Evaluación de respuestas",
            "Optimización de prompts",
            "Casos empresariales",
        ],
    },

    {
        "category": "Inteligencia Artificial",
        "icon": "⚙️",
        "name": "Automatización de Tareas con IA",
        "hours": 16,
        "price": 1100,
        "level": "Intermedio",
        "objective": (
            "Identificar y automatizar tareas repetitivas mediante Inteligencia Artificial, "
            "mejorando la productividad y eficiencia de los procesos empresariales."
        ),
        "topics": [
            "Identificación de tareas automatizables",
            "IA aplicada a procesos empresariales",
            "Automatización de documentos",
            "Automatización de análisis de información",
            "Flujos de trabajo con IA",
            "Integración con herramientas empresariales",
            "Automatización con asistentes inteligentes",
            "Validación de resultados",
            "Diseño de casos de uso",
        ],
    },

    {
        "category": "Inteligencia Artificial",
        "icon": "🧠",
        "name": "Inteligencia Artificial para Profesionales",
        "hours": None,
        "price": None,
        "level": "Adaptable",
        "objective": (
            "Explorar conceptos y aplicaciones de Inteligencia Artificial orientadas "
            "a la productividad, innovación y transformación de procesos profesionales."
        ),
        "topics": [
            "Fundamentos de Inteligencia Artificial",
            "IA Generativa",
            "Modelos de lenguaje",
            "Automatización",
            "Análisis de información",
            "Productividad con IA",
            "Casos de uso empresariales",
            "Prompt Engineering",
            "Ética y uso responsable",
        ],
    },

    # ========================================================
    # AZURE
    # ========================================================

    {
        "category": "Azure",
        "icon": "☁️",
        "name": "Azure Fundamentals",
        "hours": 24,
        "price": 1400,
        "level": "Básico",
        "objective": (
            "Comprender los conceptos fundamentales de Microsoft Azure, "
            "sus principales servicios, arquitectura, seguridad y modelos de consumo."
        ),
        "topics": [
            "Conceptos de Cloud Computing",
            "Modelos IaaS, PaaS y SaaS",
            "Arquitectura de Azure",
            "Regiones y Availability Zones",
            "Suscripciones",
            "Resource Groups",
            "Azure Virtual Machines",
            "Azure Storage",
            "Azure Networking",
            "Identidad y seguridad",
            "Monitoreo",
            "Costos y administración",
        ],
    },

    {
        "category": "Azure",
        "icon": "☁️",
        "name": "Administración de Máquinas Virtuales en Azure",
        "hours": 24,
        "price": 1600,
        "level": "Intermedio",
        "objective": (
            "Administrar máquinas virtuales en Microsoft Azure aplicando buenas prácticas "
            "de implementación, seguridad, disponibilidad, monitoreo y operación."
        ),
        "topics": [
            "Creación de máquinas virtuales",
            "Imágenes",
            "Discos administrados",
            "Redes virtuales",
            "Network Security Groups",
            "Acceso remoto",
            "Backup",
            "Alta disponibilidad",
            "Escalabilidad",
            "Monitoreo",
            "Seguridad",
            "Optimización de costos",
        ],
    },

    # ========================================================
    # POWER BI
    # ========================================================

    {
        "category": "Power BI",
        "icon": "📊",
        "name": "Power BI Fundamentals",
        "hours": 24,
        "price": 1600,
        "level": "Básico",
        "objective": (
            "Desarrollar competencias fundamentales para transformar datos "
            "en información útil mediante Microsoft Power BI."
        ),
        "topics": [
            "Introducción a Power BI",
            "Power BI Desktop",
            "Conexión a fuentes de datos",
            "Power Query",
            "Transformación de datos",
            "Visualizaciones",
            "Filtros",
            "Segmentadores",
            "Creación de informes",
            "Publicación",
            "Introducción a DAX",
        ],
    },

    {
        "category": "Power BI",
        "icon": "📈",
        "name": "Modelado de Datos con Power BI",
        "hours": 24,
        "price": 1700,
        "level": "Intermedio",
        "objective": (
            "Diseñar modelos de datos eficientes en Power BI para facilitar "
            "el análisis y la generación de indicadores empresariales."
        ),
        "topics": [
            "Fundamentos de modelado",
            "Modelo dimensional",
            "Tablas de hechos",
            "Tablas de dimensiones",
            "Esquema estrella",
            "Relaciones",
            "Cardinalidad",
            "Medidas",
            "Columnas calculadas",
            "DAX",
            "Optimización del modelo",
        ],
    },

    {
        "category": "Power BI",
        "icon": "📊",
        "name": "Dashboards e Informes Interactivos",
        "hours": 16,
        "price": 1200,
        "level": "Intermedio",
        "objective": (
            "Crear dashboards profesionales e interactivos que faciliten "
            "la interpretación y comunicación de información empresarial."
        ),
        "topics": [
            "Principios de visualización",
            "Diseño de dashboards",
            "Selección de visualizaciones",
            "KPI",
            "Filtros",
            "Segmentadores",
            "Drill-down",
            "Tooltips",
            "Navegación",
            "Experiencia de usuario",
            "Storytelling con datos",
        ],
    },

    {
        "category": "Power BI",
        "icon": "📈",
        "name": "Power BI para Analítica Empresarial",
        "hours": 24,
        "price": 1700,
        "level": "Avanzado",
        "objective": (
            "Aplicar Power BI para resolver necesidades de analítica empresarial "
            "y apoyar la toma de decisiones basada en datos."
        ),
        "topics": [
            "Analítica empresarial",
            "Indicadores de gestión",
            "KPIs",
            "Modelado de datos",
            "DAX",
            "Análisis de tendencias",
            "Segmentación",
            "Dashboards ejecutivos",
            "Storytelling",
            "Caso práctico empresarial",
        ],
    },

    # ========================================================
    # POWER PLATFORM
    # ========================================================

    {
        "category": "Power Platform",
        "icon": "⚡",
        "name": "Microsoft Power Platform Fundamentals",
        "hours": 24,
        "price": 1500,
        "level": "Básico",
        "objective": (
            "Comprender el ecosistema Microsoft Power Platform y seleccionar "
            "sus componentes para resolver necesidades de negocio."
        ),
        "topics": [
            "Introducción a Power Platform",
            "Power Apps",
            "Power Automate",
            "Power BI",
            "Power Pages",
            "Dataverse",
            "Copilot Studio",
            "Conectores",
            "Seguridad",
            "Gobernanza",
        ],
    },

    {
        "category": "Power Platform",
        "icon": "⚡",
        "name": "Automatización con Power Automate",
        "hours": 24,
        "price": 1700,
        "level": "Intermedio",
        "objective": (
            "Diseñar flujos automatizados para optimizar procesos empresariales "
            "y reducir tareas manuales."
        ),
        "topics": [
            "Introducción a Power Automate",
            "Flujos automatizados",
            "Flujos instantáneos",
            "Flujos programados",
            "Conectores",
            "Aprobaciones",
            "Condiciones",
            "Expresiones",
            "Manejo de errores",
            "Integración con Microsoft 365",
            "Caso práctico",
        ],
    },

    {
        "category": "Power Platform",
        "icon": "📱",
        "name": "Desarrollo con Power Apps",
        "hours": 24,
        "price": 1800,
        "level": "Intermedio",
        "objective": (
            "Crear aplicaciones empresariales mediante Power Apps, "
            "conectadas a fuentes de datos y servicios empresariales."
        ),
        "topics": [
            "Power Apps Canvas",
            "Controles",
            "Formularios",
            "Galerías",
            "Conexión a datos",
            "Dataverse",
            "Fórmulas",
            "Validaciones",
            "Diseño de aplicaciones",
            "Publicación",
            "Seguridad",
        ],
    },

    {
        "category": "Power Platform",
        "icon": "🗄️",
        "name": "Gestión de Datos con Dataverse",
        "hours": 16,
        "price": 1400,
        "level": "Intermedio",
        "objective": (
            "Administrar información empresarial en Microsoft Dataverse "
            "aplicando conceptos de estructura, seguridad y gobierno de datos."
        ),
        "topics": [
            "Arquitectura de Dataverse",
            "Tablas",
            "Columnas",
            "Relaciones",
            "Reglas de negocio",
            "Seguridad",
            "Roles",
            "Integración con Power Apps",
            "Integración con Power Automate",
            "Buenas prácticas",
        ],
    },

    {
        "category": "Power Platform",
        "icon": "🔗",
        "name": "Integración con Microsoft 365",
        "hours": 16,
        "price": 1300,
        "level": "Intermedio",
        "objective": (
            "Integrar Power Platform con servicios de Microsoft 365 "
            "para automatizar procesos y mejorar la colaboración."
        ),
        "topics": [
            "Power Platform y Microsoft 365",
            "SharePoint",
            "Outlook",
            "Microsoft Teams",
            "Excel",
            "OneDrive",
            "Conectores",
            "Automatización",
            "Casos de integración",
        ],
    },

    {
        "category": "Power Platform",
        "icon": "🌐",
        "name": "Introducción a Power Pages",
        "hours": 16,
        "price": 1100,
        "level": "Intermedio",
        "objective": (
            "Construir sitios web empresariales mediante Power Pages "
            "y conectarlos con datos y procesos de negocio."
        ),
        "topics": [
            "Introducción a Power Pages",
            "Creación de sitios",
            "Diseño",
            "Navegación",
            "Dataverse",
            "Formularios",
            "Listas",
            "Autenticación",
            "Permisos",
            "Publicación",
        ],
    },

    {
        "category": "Power Platform",
        "icon": "🤖",
        "name": "Desarrollo con Copilot Studio",
        "hours": 16,
        "price": 1300,
        "level": "Intermedio",
        "objective": (
            "Diseñar agentes y experiencias conversacionales mediante "
            "Microsoft Copilot Studio para automatizar interacciones."
        ),
        "topics": [
            "Introducción a Copilot Studio",
            "Creación de agentes",
            "Temas",
            "Fuentes de conocimiento",
            "Instrucciones",
            "Prompts",
            "Acciones",
            "Conectores",
            "Power Automate",
            "Pruebas",
            "Publicación",
            "Gobernanza",
        ],
    },

    # ========================================================
    # LINUX
    # ========================================================

    {
        "category": "Linux",
        "icon": "🐧",
        "name": "Linux Essentials",
        "hours": 24,
        "price": 1400,
        "level": "Básico",
        "objective": (
            "Adquirir conocimientos fundamentales para operar sistemas Linux "
            "mediante la línea de comandos y herramientas esenciales."
        ),
        "topics": [
            "Arquitectura Linux",
            "Terminal",
            "Comandos básicos",
            "Sistema de archivos",
            "Usuarios",
            "Grupos",
            "Permisos",
            "Procesos",
            "Paquetes",
            "Shell scripting básico",
        ],
    },

    {
        "category": "Linux",
        "icon": "🐧",
        "name": "Administración de Linux",
        "hours": 40,
        "price": 2400,
        "level": "Avanzado",
        "objective": (
            "Desarrollar competencias para administrar servidores Linux, "
            "gestionar servicios, seguridad, almacenamiento y automatización."
        ),
        "topics": [
            "Administración del sistema",
            "Usuarios y grupos",
            "Permisos",
            "Systemd",
            "Servicios",
            "Almacenamiento",
            "Networking",
            "Logs",
            "Seguridad",
            "Shell scripting",
            "Automatización",
            "Troubleshooting",
        ],
    },

    {
        "category": "Linux",
        "icon": "🖥️",
        "name": "Linux para Servidores",
        "hours": 40,
        "price": 2400,
        "level": "Avanzado",
        "objective": (
            "Preparar al participante para operar servidores Linux "
            "en ambientes empresariales con enfoque en disponibilidad y seguridad."
        ),
        "topics": [
            "Instalación",
            "Configuración",
            "Networking",
            "SSH",
            "DNS",
            "Web Servers",
            "Almacenamiento",
            "Backup",
            "Monitoreo",
            "Hardening",
            "Resolución de incidentes",
        ],
    },

    # ========================================================
    # CONTENEDORES
    # ========================================================

    {
        "category": "Contenedores",
        "icon": "📦",
        "name": "Docker Fundamentals",
        "hours": 24,
        "price": 1800,
        "level": "Intermedio",
        "objective": (
            "Comprender y utilizar Docker para empaquetar, ejecutar "
            "y administrar aplicaciones mediante contenedores."
        ),
        "topics": [
            "Conceptos de contenedores",
            "Docker Engine",
            "Imágenes",
            "Contenedores",
            "Dockerfile",
            "Volumes",
            "Networks",
            "Docker Compose",
            "Registry",
            "Buenas prácticas",
        ],
    },

    {
        "category": "Contenedores",
        "icon": "☸️",
        "name": "Kubernetes & DevOps Fundamentals",
        "hours": 32,
        "price": 2100,
        "level": "Avanzado",
        "objective": (
            "Comprender los fundamentos de Kubernetes y DevOps "
            "para desplegar, administrar y automatizar aplicaciones contenedorizadas."
        ),
        "topics": [
            "Contenedores",
            "Orquestación",
            "Arquitectura Kubernetes",
            "Pods",
            "Deployments",
            "Services",
            "ConfigMaps",
            "Secrets",
            "CI/CD",
            "Git",
            "Observabilidad",
            "Buenas prácticas DevOps",
        ],
    },

    {
        "category": "Contenedores",
        "icon": "🔧",
        "name": "Introducción a Microservicios",
        "hours": 16,
        "price": 1100,
        "level": "Intermedio",
        "objective": (
            "Comprender los principios de arquitectura de microservicios "
            "y sus principales componentes tecnológicos."
        ),
        "topics": [
            "Monolitos vs microservicios",
            "Principios de diseño",
            "APIs REST",
            "Comunicación entre servicios",
            "Configuración",
            "Service Discovery",
            "Contenedores",
            "Observabilidad",
            "Buenas prácticas",
        ],
    },

    # ========================================================
    # CIBERSEGURIDAD
    # ========================================================

    {
        "category": "Ciberseguridad",
        "icon": "🛡️",
        "name": "Fundamentos de Ciberseguridad",
        "hours": 24,
        "price": 1400,
        "level": "Básico",
        "objective": (
            "Desarrollar una base sólida en principios de ciberseguridad, "
            "amenazas, controles y buenas prácticas de protección."
        ),
        "topics": [
            "Principios de seguridad",
            "Confidencialidad",
            "Integridad",
            "Disponibilidad",
            "Amenazas",
            "Vulnerabilidades",
            "Malware",
            "Seguridad de redes",
            "Identidad y acceso",
            "Seguridad de endpoints",
            "Gestión de incidentes",
        ],
    },

    {
        "category": "Ciberseguridad",
        "icon": "🔎",
        "name": "Introducción a un SOC",
        "hours": 24,
        "price": 1500,
        "level": "Intermedio",
        "objective": (
            "Comprender la operación de un Security Operations Center "
            "y los procesos utilizados para monitorear, detectar y responder a incidentes."
        ),
        "topics": [
            "Qué es un SOC",
            "Roles del SOC",
            "Procesos de seguridad",
            "SIEM",
            "Logs",
            "Eventos",
            "Monitoreo",
            "Threat Intelligence",
            "Detección",
            "Respuesta a incidentes",
            "Escalamiento",
        ],
    },

    {
        "category": "Ciberseguridad",
        "icon": "🔐",
        "name": "ISO 27001",
        "hours": None,
        "price": None,
        "level": "Adaptable",
        "objective": (
            "Conocer los fundamentos de ISO/IEC 27001 y los principales "
            "elementos necesarios para gestionar un Sistema de Gestión de Seguridad de la Información."
        ),
        "topics": [
            "Fundamentos de ISO 27001",
            "Sistema de Gestión de Seguridad de la Información",
            "Contexto de la organización",
            "Gestión de riesgos",
            "Controles de seguridad",
            "Políticas",
            "Procedimientos",
            "Auditoría interna",
            "Mejora continua",
            "Preparación para implementación",
        ],
    },

    {
        "category": "Ciberseguridad",
        "icon": "🔒",
        "name": "Zero Trust: Estrategias Modernas de Seguridad",
        "hours": 16,
        "price": 1200,
        "level": "Avanzado",
        "objective": (
            "Comprender e implementar principios de Zero Trust para fortalecer "
            "la seguridad de usuarios, dispositivos, aplicaciones, redes y datos."
        ),
        "topics": [
            "Principios Zero Trust",
            "Never Trust, Always Verify",
            "Identidad como perímetro",
            "Least Privilege",
            "MFA",
            "Acceso condicional",
            "Segmentación",
            "Seguridad de endpoints",
            "Monitoreo",
            "Analítica",
            "Estrategia de implementación",
        ],
    },

    # ========================================================
    # ARQUITECTURA
    # ========================================================

    {
        "category": "Arquitectura y Gestión",
        "icon": "🏗️",
        "name": "TOGAF",
        "hours": None,
        "price": None,
        "level": "Adaptable",
        "objective": (
            "Introducir los principios y componentes de TOGAF para estructurar "
            "y gestionar iniciativas de arquitectura empresarial."
        ),
        "topics": [
            "Arquitectura empresarial",
            "Introducción a TOGAF",
            "Architecture Development Method",
            "Arquitectura de negocio",
            "Arquitectura de datos",
            "Arquitectura de aplicaciones",
            "Arquitectura tecnológica",
            "Gobernanza",
            "Gestión de cambios",
        ],
    },
]

# ============================================================
# ICONOS POR CATEGORÍA
# ============================================================

CATEGORY_ICONS = {
    "Inteligencia Artificial": "🤖",
    "Azure": "☁️",
    "Power BI": "📊",
    "Power Platform": "⚡",
    "Linux": "🐧",
    "Contenedores": "📦",
    "Ciberseguridad": "🛡️",
    "Arquitectura y Gestión": "🏗️",
}

# ============================================================
# CSS
# ============================================================

st.markdown(
    """
<style>

    /* General */
    .main {
        background-color: #f8fafc;
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 1400px;
    }

    /* Header */
    .hero {
        padding: 45px;
        border-radius: 24px;
        background:
            radial-gradient(circle at top right, rgba(59,130,246,.35), transparent 35%),
            linear-gradient(135deg, #0f172a, #1e3a8a 55%, #2563eb);
        color: white;
        margin-bottom: 30px;
        box-shadow: 0 15px 40px rgba(15,23,42,.18);
    }

    .hero h1 {
        color: white;
        font-size: 2.8rem;
        font-weight: 800;
        margin-bottom: 10px;
    }

    .hero p {
        color: #dbeafe;
        font-size: 1.15rem;
        max-width: 850px;
    }

    /* Cards */
    .course-card {
        background: white;
        border: 1px solid #e2e8f0;
        border-radius: 18px;
        padding: 22px;
        min-height: 290px;
        margin-bottom: 12px;
        box-shadow: 0 5px 18px rgba(15,23,42,.06);
        transition: all .2s ease;
    }

    .course-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 12px 28px rgba(15,23,42,.12);
        border-color: #93c5fd;
    }

    .course-icon {
        font-size: 2.2rem;
    }

    .category-tag {
        display: inline-block;
        background: #eff6ff;
        color: #1d4ed8;
        border-radius: 999px;
        padding: 5px 10px;
        font-size: .75rem;
        font-weight: 700;
    }

    .level-tag {
        display: inline-block;
        background: #f1f5f9;
        color: #475569;
        border-radius: 999px;
        padding: 5px 10px;
        font-size: .75rem;
        font-weight: 700;
        margin-left: 5px;
    }

    .course-title {
        font-size: 1.12rem;
        font-weight: 750;
        color: #0f172a;
        min-height: 55px;
        margin-top: 12px;
    }

    .course-description {
        color: #64748b;
        font-size: .9rem;
        min-height: 75px;
    }

    .price {
        color: #0f172a;
        font-size: 1.35rem;
        font-weight: 800;
    }

    .hours {
        color: #64748b;
        font-weight: 600;
    }

    /* Detail */
    .detail-header {
        padding: 35px;
        border-radius: 22px;
        background: linear-gradient(135deg, #0f172a, #1e40af);
        color: white;
        margin-bottom: 25px;
    }

    .detail-header h1 {
        color: white;
        font-size: 2.2rem;
    }

    .detail-header p {
        color: #bfdbfe;
    }

    .info-box {
        background: white;
        border: 1px solid #e2e8f0;
        border-radius: 16px;
        padding: 25px;
        margin-bottom: 20px;
        box-shadow: 0 5px 15px rgba(15,23,42,.05);
    }

    .topic-item {
        background: #f8fafc;
        padding: 11px 15px;
        border-radius: 9px;
        margin: 7px 0;
        border-left: 4px solid #2563eb;
    }

    .stat-card {
        background: white;
        border: 1px solid #e2e8f0;
        border-radius: 16px;
        padding: 20px;
        text-align: center;
        box-shadow: 0 5px 15px rgba(15,23,42,.05);
    }

    .stat-number {
        font-size: 1.7rem;
        font-weight: 800;
        color: #1d4ed8;
    }

    .stat-label {
        color: #64748b;
        font-size: .85rem;
    }

    /* Section */
    .section-title {
        font-size: 1.7rem;
        font-weight: 800;
        color: #0f172a;
        margin-top: 20px;
    }

    .footer {
        text-align: center;
        color: #64748b;
        padding: 30px 0;
        font-size: .85rem;
    }

</style>
""",
    unsafe_allow_html=True,
)

# ============================================================
# FUNCIONES
# ============================================================

def money(value):
    if value is None:
        return "Consultar"
    return f"${value:,.0f}"


def duration(hours):
    if hours is None:
        return "Por definir"
    return f"{hours} horas"


def whatsapp_url(course_name):
    message = (
        f"Hola, estoy interesado(a) en el curso "
        f"'{course_name}'. Me gustaría recibir más información."
    )
    return f"https://wa.me/{WHATSAPP_NUMBER}?text={quote(message)}"


def show_home():
    """Página principal."""

    st.markdown(
        """
        <div class="hero">
            <h1>🎓 Capacitación Tecnológica</h1>
            <p>
                Formación especializada para profesionales y organizaciones
                en Inteligencia Artificial, Cloud, Datos, Automatización,
                Linux, Contenedores, Ciberseguridad y Arquitectura.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Métricas
    total_courses = len(COURSES)
    categories = len(set(c["category"] for c in COURSES))
    total_hours = sum(c["hours"] for c in COURSES if c["hours"])

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown(
            f"""
            <div class="stat-card">
                <div class="stat-number">{total_courses}+</div>
                <div class="stat-label">Cursos disponibles</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with c2:
        st.markdown(
            f"""
            <div class="stat-card">
                <div class="stat-number">{categories}</div>
                <div class="stat-label">Áreas tecnológicas</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with c3:
        st.markdown(
            f"""
            <div class="stat-card">
                <div class="stat-number">{total_hours}+</div>
                <div class="stat-label">Horas de formación</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown(
        '<div class="section-title">🚀 Explora nuestros cursos</div>',
        unsafe_allow_html=True,
    )

    st.write(
        "Selecciona un área o utiliza el buscador para encontrar "
        "la capacitación que necesitas."
    )

    # Filtros
    col1, col2 = st.columns([1, 2])

    with col1:
        categories_filter = ["Todas"] + list(
            dict.fromkeys(c["category"] for c in COURSES)
        )

        category = st.selectbox(
            "Área de capacitación",
            categories_filter,
        )

    with col2:
        search = st.text_input(
            "🔎 Buscar curso",
            placeholder="Ejemplo: Power BI, Azure, Linux, IA...",
        )

    # Filtrado
    filtered_courses = COURSES.copy()

    if category != "Todas":
        filtered_courses = [
            c for c in filtered_courses
            if c["category"] == category
        ]

    if search:
        search_lower = search.lower()

        filtered_courses = [
            c for c in filtered_courses
            if search_lower in c["name"].lower()
            or search_lower in c["category"].lower()
            or search_lower in c["objective"].lower()
        ]

    st.write("")

    st.markdown(
        f"**{len(filtered_courses)} cursos encontrados**"
    )

    # Tarjetas
    for row_start in range(0, len(filtered_courses), 3):

        cols = st.columns(3)

        row_courses = filtered_courses[row_start:row_start + 3]

        for col, course in zip(cols, row_courses):

            with col:

                st.markdown(
                    f"""
                    <div class="course-card">

                        <div>
                            <span class="course-icon">
                                {course["icon"]}
                            </span>
                        </div>

                        <div>
                            <span class="category-tag">
                                {course["category"]}
                            </span>

                            <span class="level-tag">
                                {course["level"]}
                            </span>
                        </div>

                        <div class="course-title">
                            {course["name"]}
                        </div>

                        <div class="course-description">
                            {course["objective"][:160]}...
                        </div>

                        <div>
                            <span class="hours">
                                ⏱️ {duration(course["hours"])}
                            </span>

                            &nbsp;&nbsp;

                            <span class="price">
                                {money(course["price"])}
                            </span>
                        </div>

                    </div>
                    """,
                    unsafe_allow_html=True,
                )

                if st.button(
                    "Ver información del curso →",
                    key=f"course_{course['name']}",
                    use_container_width=True,
                ):
                    st.session_state.selected_course = course
                    st.session_state.page = "course"
                    st.rerun()

    # Sección empresarial
    st.markdown("---")

    st.markdown(
        '<div class="section-title">💼 Capacitación empresarial</div>',
        unsafe_allow_html=True,
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("### 🧩 Contenido personalizado")
        st.write(
            "Adaptación de contenidos, duración y nivel según "
            "las necesidades de su organización."
        )

    with col2:
        st.markdown("### 🧪 Enfoque práctico")
        st.write(
            "Ejercicios, laboratorios y casos de uso orientados "
            "al entorno empresarial."
        )

    with col3:
        st.markdown("### 🌐 Modalidad flexible")
        st.write(
            "Capacitación virtual en vivo o presencial para "
            "equipos y organizaciones."
        )


def show_course(course):
    """Página individual del curso."""

    if st.button("← Volver al catálogo"):
        st.session_state.page = "home"
        st.session_state.selected_course = None
        st.rerun()

    st.markdown(
        f"""
        <div class="detail-header">

            <h1>
                {course["icon"]} {course["name"]}
            </h1>

            <p>
                {course["category"]} · Nivel {course["level"]}
            </p>

        </div>
        """,
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns([2.1, 1])

    with col1:

        st.markdown("## 🎯 Objetivo")

        st.markdown(
            f"""
            <div class="info-box">
                {course["objective"]}
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown("## 📚 Temario")

        for topic in course["topics"]:
            st.markdown(
                f"""
                <div class="topic-item">
                    ✓ {topic}
                </div>
                """,
                unsafe_allow_html=True,
            )

    with col2:

        st.markdown("## Información del curso")

        st.markdown(
            f"""
            <div class="info-box">

                <h3>⏱️ Duración</h3>
                <h2>{duration(course["hours"])}</h2>

                <hr>

                <h3>💰 Inversión</h3>
                <h2>{money(course["price"])}</h2>

                <hr>

                <h3>📈 Nivel</h3>
                <h2>{course["level"]}</h2>

            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown("### 📌 Modalidades")

        st.write("💻 Virtual en vivo")
        st.write("🏢 Presencial")
        st.write("👥 Capacitación empresarial")
        st.write("🧪 Laboratorios prácticos")

        st.markdown("---")

        # WhatsApp
        st.link_button(
            "💬 Consultar por WhatsApp",
            whatsapp_url(course["name"]),
            use_container_width=True,
        )

        st.info(
            "Los contenidos, duración y modalidad pueden adaptarse "
            "según los requerimientos de la organización."
        )

    # Formulario
    st.markdown("---")

    st.markdown("## 📩 Solicitar información")

    st.write(
        "Complete el siguiente formulario para solicitar información "
        "sobre este curso."
    )

    with st.form("contact_form"):

        col1, col2 = st.columns(2)

        with col1:
            name = st.text_input("Nombre completo *")
            email = st.text_input("Correo electrónico *")

        with col2:
            company = st.text_input("Empresa / Organización")
            phone = st.text_input("Teléfono")

        message = st.text_area(
            "Mensaje",
            value=f"Estoy interesado(a) en el curso: {course['name']}",
        )

        submitted = st.form_submit_button(
            "📩 Solicitar información",
            type="primary",
            use_container_width=True,
        )

        if submitted:

            if not name or not email:

                st.error(
                    "Por favor complete al menos el nombre y correo electrónico."
                )

            else:

                st.success(
                    "¡Gracias! Su solicitud ha sido registrada. "
                    "Para una respuesta inmediata también puede contactarnos por WhatsApp."
                )

                whatsapp_message = (
                    f"Hola, soy {name}. "
                    f"Estoy interesado(a) en el curso "
                    f"'{course['name']}'. "
                    f"Mi correo es {email}. "
                    f"Empresa: {company}. "
                    f"Teléfono: {phone}. "
                    f"Mensaje: {message}"
                )

                url = (
                    f"https://wa.me/{WHATSAPP_NUMBER}"
                    f"?text={quote(whatsapp_message)}"
                )

                st.link_button(
                    "💬 Enviar solicitud por WhatsApp",
                    url,
                )


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.markdown(
    """
    # 🎓 Catálogo
    ### Capacitación Tecnológica

    Formación especializada para profesionales y empresas.
    """,
)

st.sidebar.divider()

if st.sidebar.button(
    "🏠 Inicio",
    use_container_width=True,
):
    st.session_state.page = "home"
    st.session_state.selected_course = None
    st.rerun()

st.sidebar.markdown("### 📚 Categorías")

categories_sidebar = list(
    dict.fromkeys(c["category"] for c in COURSES)
)

for category_item in categories_sidebar:

    icon = CATEGORY_ICONS.get(category_item, "📘")

    if st.sidebar.button(
        f"{icon} {category_item}",
        key=f"sidebar_{category_item}",
        use_container_width=True,
    ):

        st.session_state.category_filter = category_item
        st.session_state.page = "home"
        st.session_state.selected_course = None
        st.rerun()

st.sidebar.divider()

st.sidebar.markdown("### 📞 Contacto")

st.sidebar.write(
    "¿Necesita una capacitación personalizada?"
)

st.sidebar.link_button(
    "💬 WhatsApp",
    f"https://wa.me/{WHATSAPP_NUMBER}",
    use_container_width=True,
)

st.sidebar.write(
    f"📧 {CONTACT_EMAIL}"
)

st.sidebar.divider()

st.sidebar.caption(
    "© 2026 Capacitación Tecnológica"
)

# ============================================================
# NAVEGACIÓN
# ============================================================

if "page" not in st.session_state:
    st.session_state.page = "home"

if "selected_course" not in st.session_state:
    st.session_state.selected_course = None

if "category_filter" in st.session_state:

    selected_category = st.session_state.category_filter

    filtered = [
        c for c in COURSES
        if c["category"] == selected_category
    ]

    # Página de categoría
    st.markdown(
        f"""
        <div class="hero">

            <h1>
                {CATEGORY_ICONS.get(selected_category, "📚")}
                {selected_category}
            </h1>

            <p>
                Cursos especializados de {selected_category}.
            </p>

        </div>
        """,
        unsafe_allow_html=True,
    )

    if st.button("← Ver todos los cursos"):
        del st.session_state.category_filter
        st.rerun()

    for row_start in range(0, len(filtered), 3):

        cols = st.columns(3)

        for col, course in zip(
            cols,
            filtered[row_start:row_start + 3],
        ):

            with col:

                st.markdown(
                    f"""
                    <div class="course-card">

                        <div class="course-icon">
                            {course["icon"]}
                        </div>

                        <span class="category-tag">
                            {course["category"]}
                        </span>

                        <div class="course-title">
                            {course["name"]}
                        </div>

                        <div class="course-description">
                            {course["objective"][:150]}...
                        </div>

                        <span class="hours">
                            ⏱️ {duration(course["hours"])}
                        </span>

                        <span class="price">
                            {money(course["price"])}
                        </span>

                    </div>
                    """,
                    unsafe_allow_html=True,
                )

                if st.button(
                    "Ver curso →",
                    key=f"cat_{course['name']}",
                    use_container_width=True,
                ):
                    st.session_state.selected_course = course
                    st.session_state.page = "course"
                    del st.session_state.category_filter
                    st.rerun()

else:

    if (
        st.session_state.page == "course"
        and st.session_state.selected_course
    ):
        show_course(
            st.session_state.selected_course
        )

    else:
        show_home()

# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
    <div class="footer">
        <hr>
        <strong>Capacitación Tecnológica</strong><br>
        Inteligencia Artificial · Cloud · Datos · Automatización ·
        Linux · DevOps · Ciberseguridad · Arquitectura
    </div>
    """,
    unsafe_allow_html=True,
)
```
