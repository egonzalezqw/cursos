from pathlib import Path

code = r'''import streamlit as st
from urllib.parse import quote

# ============================================================
# CONFIGURACIÓN
# ============================================================

st.set_page_config(
    page_title="Capacitación Tecnológica",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ============================================================
# DATOS GENERALES
# ============================================================

WHATSAPP = "50662614659"
EMAIL = "tu-correo@ejemplo.com"
PHONE = "+506 6261-4659"

COURSES = [
    # Inteligencia Artificial
    {
        "category": "Inteligencia Artificial",
        "icon": "🤖",
        "name": "Microsoft 365 Copilot para Usuarios Finales",
        "hours": 8,
        "price": 600,
        "level": "Básico",
        "objective": "Desarrollar habilidades prácticas para utilizar Microsoft 365 Copilot como asistente de productividad.",
        "topics": [
            "Introducción a Microsoft 365 Copilot",
            "Inteligencia Artificial Generativa",
            "Prompt Engineering",
            "Copilot en Word",
            "Copilot en Excel",
            "Copilot en PowerPoint",
            "Copilot en Outlook",
            "Copilot en Teams",
            "Buenas prácticas y seguridad",
        ],
    },
    {
        "category": "Inteligencia Artificial",
        "icon": "🤖",
        "name": "Copilot para Empresas: Productividad con IA",
        "hours": 16,
        "price": 1000,
        "level": "Intermedio",
        "objective": "Aplicar Microsoft Copilot en escenarios empresariales para mejorar la productividad y eficiencia.",
        "topics": [
            "IA generativa empresarial",
            "Microsoft Copilot",
            "Casos de uso empresariales",
            "Creación de prompts",
            "Generación de documentos",
            "Análisis de información",
            "Presentaciones con IA",
            "Outlook y Teams",
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
        "objective": "Comprender los fundamentos de la Inteligencia Artificial Generativa y sus principales aplicaciones.",
        "topics": [
            "Fundamentos de Inteligencia Artificial",
            "Machine Learning",
            "Inteligencia Artificial Generativa",
            "Large Language Models",
            "Modelos multimodales",
            "Generación de texto",
            "Generación de imágenes",
            "Prompt Engineering",
            "Casos empresariales",
            "Ética y seguridad",
        ],
    },
    {
        "category": "Inteligencia Artificial",
        "icon": "✍️",
        "name": "Prompt Engineering para Profesionales",
        "hours": 16,
        "price": 1100,
        "level": "Intermedio",
        "objective": "Diseñar prompts efectivos para obtener resultados de mayor calidad con herramientas de Inteligencia Artificial.",
        "topics": [
            "Fundamentos de Prompt Engineering",
            "Anatomía de un prompt",
            "Contexto e instrucciones",
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
        "objective": "Identificar y automatizar tareas repetitivas mediante herramientas de Inteligencia Artificial.",
        "topics": [
            "Identificación de tareas automatizables",
            "IA aplicada a procesos",
            "Automatización de documentos",
            "Automatización de información",
            "Flujos de trabajo",
            "Integración con herramientas empresariales",
            "Validación de resultados",
            "Diseño de casos de uso",
        ],
    },

    # Azure
    {
        "category": "Azure",
        "icon": "☁️",
        "name": "Azure Fundamentals",
        "hours": 24,
        "price": 1400,
        "level": "Básico",
        "objective": "Comprender los conceptos fundamentales de Microsoft Azure y sus principales servicios.",
        "topics": [
            "Cloud Computing",
            "IaaS, PaaS y SaaS",
            "Arquitectura de Azure",
            "Suscripciones y Resource Groups",
            "Máquinas virtuales",
            "Azure Storage",
            "Redes virtuales",
            "Identidad y seguridad",
            "Monitoreo",
            "Costos y optimización",
        ],
    },
    {
        "category": "Azure",
        "icon": "☁️",
        "name": "Administración de Máquinas Virtuales en Azure",
        "hours": 24,
        "price": 1600,
        "level": "Intermedio",
        "objective": "Administrar máquinas virtuales en Azure aplicando buenas prácticas de seguridad, disponibilidad y operación.",
        "topics": [
            "Creación de máquinas virtuales",
            "Imágenes y discos",
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

    # Power BI
    {
        "category": "Power BI",
        "icon": "📊",
        "name": "Power BI Fundamentals",
        "hours": 24,
        "price": 1600,
        "level": "Básico",
        "objective": "Desarrollar competencias fundamentales para transformar datos en información útil mediante Power BI.",
        "topics": [
            "Introducción a Power BI",
            "Power BI Desktop",
            "Fuentes de datos",
            "Power Query",
            "Transformación de datos",
            "Visualizaciones",
            "Filtros y segmentadores",
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
        "objective": "Diseñar modelos de datos eficientes para facilitar el análisis y la generación de indicadores.",
        "topics": [
            "Modelado dimensional",
            "Tablas de hechos",
            "Dimensiones",
            "Esquema estrella",
            "Relaciones",
            "Cardinalidad",
            "Medidas",
            "Columnas calculadas",
            "DAX",
            "Optimización",
        ],
    },
    {
        "category": "Power BI",
        "icon": "📊",
        "name": "Dashboards e Informes Interactivos",
        "hours": 16,
        "price": 1200,
        "level": "Intermedio",
        "objective": "Crear dashboards profesionales e interactivos para facilitar la interpretación de información.",
        "topics": [
            "Principios de visualización",
            "Diseño de dashboards",
            "KPI",
            "Filtros",
            "Segmentadores",
            "Drill-down",
            "Tooltips",
            "Navegación",
            "Experiencia de usuario",
            "Storytelling",
        ],
    },
    {
        "category": "Power BI",
        "icon": "📈",
        "name": "Power BI para Analítica Empresarial",
        "hours": 24,
        "price": 1700,
        "level": "Avanzado",
        "objective": "Aplicar Power BI para resolver necesidades de analítica empresarial y apoyar la toma de decisiones.",
        "topics": [
            "Analítica empresarial",
            "KPIs",
            "Modelado",
            "DAX",
            "Análisis de tendencias",
            "Segmentación",
            "Dashboards ejecutivos",
            "Storytelling con datos",
            "Caso práctico empresarial",
        ],
    },

    # Power Platform
    {
        "category": "Power Platform",
        "icon": "⚡",
        "name": "Microsoft Power Platform Fundamentals",
        "hours": 24,
        "price": 1500,
        "level": "Básico",
        "objective": "Comprender el ecosistema Microsoft Power Platform y sus principales componentes.",
        "topics": [
            "Power Platform",
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
        "objective": "Diseñar flujos automatizados para optimizar procesos empresariales.",
        "topics": [
            "Power Automate",
            "Flujos automatizados",
            "Flujos instantáneos",
            "Flujos programados",
            "Conectores",
            "Aprobaciones",
            "Condiciones",
            "Expresiones",
            "Manejo de errores",
            "Microsoft 365",
        ],
    },
    {
        "category": "Power Platform",
        "icon": "📱",
        "name": "Desarrollo con Power Apps",
        "hours": 24,
        "price": 1800,
        "level": "Intermedio",
        "objective": "Crear aplicaciones empresariales mediante Power Apps conectadas a fuentes de datos.",
        "topics": [
            "Power Apps Canvas",
            "Controles",
            "Formularios",
            "Galerías",
            "Conexión a datos",
            "Dataverse",
            "Fórmulas",
            "Validaciones",
            "Diseño",
            "Publicación",
        ],
    },
    {
        "category": "Power Platform",
        "icon": "🗄️",
        "name": "Gestión de Datos con Dataverse",
        "hours": 16,
        "price": 1400,
        "level": "Intermedio",
        "objective": "Administrar información empresarial mediante Microsoft Dataverse.",
        "topics": [
            "Arquitectura de Dataverse",
            "Tablas",
            "Columnas",
            "Relaciones",
            "Reglas de negocio",
            "Seguridad",
            "Roles",
            "Power Apps",
            "Power Automate",
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
        "objective": "Integrar Power Platform con servicios de Microsoft 365 para automatizar procesos.",
        "topics": [
            "Microsoft 365",
            "SharePoint",
            "Outlook",
            "Teams",
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
        "objective": "Construir sitios web empresariales mediante Power Pages.",
        "topics": [
            "Power Pages",
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
        "objective": "Diseñar agentes conversacionales mediante Microsoft Copilot Studio.",
        "topics": [
            "Copilot Studio",
            "Creación de agentes",
            "Temas",
            "Fuentes de conocimiento",
            "Prompts",
            "Acciones",
            "Conectores",
            "Power Automate",
            "Pruebas",
            "Publicación",
        ],
    },

    # Linux
    {
        "category": "Linux",
        "icon": "🐧",
        "name": "Linux Essentials",
        "hours": 24,
        "price": 1400,
        "level": "Básico",
        "objective": "Adquirir conocimientos fundamentales para operar sistemas Linux.",
        "topics": [
            "Arquitectura Linux",
            "Terminal",
            "Comandos",
            "Sistema de archivos",
            "Usuarios",
            "Grupos",
            "Permisos",
            "Procesos",
            "Paquetes",
            "Shell scripting",
        ],
    },
    {
        "category": "Linux",
        "icon": "🐧",
        "name": "Administración de Linux",
        "hours": 40,
        "price": 2400,
        "level": "Avanzado",
        "objective": "Administrar servidores Linux, servicios, seguridad, almacenamiento y automatización.",
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
        "objective": "Operar servidores Linux en ambientes empresariales con enfoque en disponibilidad y seguridad.",
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
            "Troubleshooting",
        ],
    },

    # Contenedores
    {
        "category": "Contenedores",
        "icon": "📦",
        "name": "Docker Fundamentals",
        "hours": 24,
        "price": 1800,
        "level": "Intermedio",
        "objective": "Comprender y utilizar Docker para ejecutar aplicaciones mediante contenedores.",
        "topics": [
            "Contenedores",
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
        "objective": "Comprender Kubernetes y DevOps para desplegar y administrar aplicaciones contenedorizadas.",
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
            "DevOps",
        ],
    },
    {
        "category": "Contenedores",
        "icon": "🔧",
        "name": "Introducción a Microservicios",
        "hours": 16,
        "price": 1100,
        "level": "Intermedio",
        "objective": "Comprender los principios de arquitectura de microservicios y su aplicación en ambientes modernos.",
        "topics": [
            "Monolitos vs microservicios",
            "Diseño de microservicios",
            "APIs REST",
            "Comunicación entre servicios",
            "Configuración",
            "Service Discovery",
            "Contenedores",
            "Observabilidad",
        ],
    },

    # Ciberseguridad
    {
        "category": "Ciberseguridad",
        "icon": "🛡️",
        "name": "Fundamentos de Ciberseguridad",
        "hours": 24,
        "price": 1400,
        "level": "Básico",
        "objective": "Desarrollar una base sólida en principios de ciberseguridad y protección.",
        "topics": [
            "Principios de seguridad",
            "Confidencialidad",
            "Integridad",
            "Disponibilidad",
            "Amenazas",
            "Vulnerabilidades",
            "Malware",
            "Seguridad de redes",
            "Identidad",
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
        "objective": "Comprender la operación, procesos y tecnologías utilizadas en un Security Operations Center.",
        "topics": [
            "Qué es un SOC",
            "Roles del SOC",
            "Procesos",
            "SIEM",
            "Logs",
            "Eventos",
            "Monitoreo",
            "Threat Intelligence",
            "Detección",
            "Respuesta a incidentes",
        ],
    },
    {
        "category": "Ciberseguridad",
        "icon": "🔐",
        "name": "ISO 27001",
        "hours": None,
        "price": None,
        "level": "Adaptable",
        "objective": "Conocer los fundamentos de ISO/IEC 27001 y los principales elementos de un Sistema de Gestión de Seguridad de la Información.",
        "topics": [
            "Fundamentos ISO 27001",
            "Sistema de Gestión de Seguridad de la Información",
            "Contexto organizacional",
            "Gestión de riesgos",
            "Controles",
            "Políticas",
            "Procedimientos",
            "Auditoría",
            "Mejora continua",
        ],
    },
    {
        "category": "Ciberseguridad",
        "icon": "🔒",
        "name": "Zero Trust: Estrategias Modernas de Seguridad",
        "hours": 16,
        "price": 1200,
        "level": "Avanzado",
        "objective": "Comprender e implementar principios Zero Trust para fortalecer la seguridad empresarial.",
        "topics": [
            "Principios Zero Trust",
            "Never Trust, Always Verify",
            "Identidad",
            "Least Privilege",
            "MFA",
            "Acceso condicional",
            "Segmentación",
            "Endpoints",
            "Monitoreo",
            "Estrategia de implementación",
        ],
    },

    # Arquitectura
    {
        "category": "Arquitectura y Gestión",
        "icon": "🏗️",
        "name": "TOGAF",
        "hours": None,
        "price": None,
        "level": "Adaptable",
        "objective": "Introducir los principios de TOGAF para estructurar y gestionar iniciativas de arquitectura empresarial.",
        "topics": [
            "Arquitectura empresarial",
            "TOGAF",
            "Architecture Development Method",
            "Arquitectura de negocio",
            "Arquitectura de datos",
            "Arquitectura de aplicaciones",
            "Arquitectura tecnológica",
            "Gobernanza",
        ],
    },
]

CATEGORY_ICONS = {
    "Todas": "📚",
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
# ESTILOS
# ============================================================

st.markdown(
    """
    <style>
    .stApp {
        background: #f6f8fc;
    }

    .block-container {
        max-width: 1380px;
        padding-top: 1.5rem;
        padding-bottom: 5rem;
    }

    header[data-testid="stHeader"] {
        background: transparent;
    }

    .topbar {
        background: white;
        border: 1px solid #e5e7eb;
        border-radius: 18px;
        padding: 12px 20px;
        margin-bottom: 22px;
        box-shadow: 0 5px 18px rgba(15, 23, 42, 0.05);
    }

    .brand {
        font-size: 1.25rem;
        font-weight: 900;
        color: #0f172a;
    }

    .brand span {
        color: #2563eb;
    }

    .hero {
        background: linear-gradient(135deg, #0f172a, #1d4ed8);
        border-radius: 28px;
        padding: 55px 55px;
        margin-bottom: 32px;
        color: white;
        box-shadow: 0 18px 45px rgba(30, 64, 175, 0.18);
    }

    .hero-kicker {
        color: #bfdbfe;
        font-weight: 800;
        font-size: .82rem;
        text-transform: uppercase;
        letter-spacing: .12em;
        margin-bottom: 12px;
    }

    .hero h1 {
        color: white;
        font-size: 3.1rem;
        line-height: 1.08;
        margin: 0 0 18px 0;
        font-weight: 900;
    }

    .hero p {
        color: #dbeafe;
        max-width: 900px;
        font-size: 1.08rem;
        line-height: 1.7;
        margin: 0;
    }

    .section-title {
        color: #0f172a;
        font-size: 1.65rem;
        font-weight: 900;
        margin: 28px 0 18px 0;
    }

    .stat {
        background: white;
        border: 1px solid #e5e7eb;
        border-radius: 16px;
        padding: 18px;
        text-align: center;
        box-shadow: 0 5px 18px rgba(15, 23, 42, 0.04);
    }

    .stat-number {
        font-size: 1.65rem;
        font-weight: 900;
        color: #2563eb;
    }

    .stat-label {
        color: #64748b;
        font-size: .85rem;
    }

    .course-card {
        background: white;
        border: 1px solid #e2e8f0;
        border-radius: 20px;
        padding: 24px;
        min-height: 310px;
        box-shadow: 0 8px 25px rgba(15, 23, 42, .055);
    }

    .course-icon {
        font-size: 2.6rem;
        margin-bottom: 8px;
    }

    .course-category {
        color: #2563eb;
        font-size: .72rem;
        font-weight: 900;
        text-transform: uppercase;
        letter-spacing: .05em;
    }

    .course-title {
        color: #0f172a;
        font-size: 1.08rem;
        line-height: 1.35;
        font-weight: 900;
        margin: 8px 0;
        min-height: 58px;
    }

    .course-description {
        color: #64748b;
        font-size: .88rem;
        line-height: 1.55;
        min-height: 72px;
    }

    .course-meta {
        color: #475569;
        font-size: .88rem;
        margin-top: 8px;
    }

    .course-price {
        color: #2563eb;
        font-weight: 900;
        font-size: 1.18rem;
    }

    .level-badge {
        display: inline-block;
        margin-top: 10px;
        padding: 5px 10px;
        border-radius: 999px;
        background: #eff6ff;
        color: #1d4ed8;
        font-size: .72rem;
        font-weight: 800;
    }

    .detail-box {
        background: white;
        border: 1px solid #e2e8f0;
        border-radius: 20px;
        padding: 28px;
        box-shadow: 0 8px 25px rgba(15, 23, 42, .055);
    }

    .topic {
        background: #f8fafc;
        border: 1px solid #e2e8f0;
        border-left: 4px solid #2563eb;
        border-radius: 9px;
        padding: 11px 14px;
        margin-bottom: 8px;
        color: #334155;
    }

    .feature {
        background: white;
        border: 1px solid #e2e8f0;
        border-radius: 20px;
        padding: 25px;
        min-height: 175px;
        box-shadow: 0 8px 25px rgba(15, 23, 42, .045);
    }

    .feature h3 {
        color: #0f172a;
        margin-top: 0;
    }

    .feature p {
        color: #64748b;
        line-height: 1.65;
    }

    .footer {
        margin-top: 55px;
        padding: 35px 15px;
        text-align: center;
        border-top: 1px solid #e2e8f0;
        color: #64748b;
    }

    .whatsapp-float {
        position: fixed;
        right: 24px;
        bottom: 24px;
        z-index: 999999;
        background: #16a34a;
        color: white !important;
        padding: 13px 20px;
        border-radius: 999px;
        text-decoration: none !important;
        font-weight: 900;
        box-shadow: 0 8px 25px rgba(22, 163, 74, .35);
    }

    .whatsapp-float:hover {
        background: #15803d;
        color: white !important;
    }

    @media (max-width: 800px) {
        .hero {
            padding: 35px 25px;
        }

        .hero h1 {
            font-size: 2.15rem;
        }

        .whatsapp-float {
            right: 15px;
            bottom: 15px;
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


def hours_text(value):
    if value is None:
        return "Duración adaptable"
    return f"{value} horas"


def whatsapp_url(course=None):
    if course:
        message = (
            f"Hola, estoy interesado(a) en el curso "
            f"'{course['name']}'. Me gustaría recibir información."
        )
    else:
        message = (
            "Hola, me gustaría recibir información "
            "sobre los cursos de capacitación."
        )

    return f"https://wa.me/{WHATSAPP}?text={quote(message)}"


def go_home():
    st.session_state.page = "home"
    st.session_state.selected_course = None


def go_course(course):
    st.session_state.page = "course"
    st.session_state.selected_course = course


# ============================================================
# ESTADO
# ============================================================

if "page" not in st.session_state:
    st.session_state.page = "home"

if "selected_course" not in st.session_state:
    st.session_state.selected_course = None

if "category" not in st.session_state:
    st.session_state.category = "Todas"

# ============================================================
# MENÚ SUPERIOR
# ============================================================

top1, top2, top3, top4 = st.columns([3, 1, 1, 1])

with top1:
    st.markdown(
        '<div class="topbar"><div class="brand">🎓 <span>Capacitación</span> Tecnológica</div></div>',
        unsafe_allow_html=True,
    )

with top2:
    if st.button("🏠 Inicio", use_container_width=True):
        go_home()
        st.rerun()

with top3:
    if st.button("📚 Cursos", use_container_width=True):
        go_home()
        st.rerun()

with top4:
    st.link_button(
        "💬 WhatsApp",
        whatsapp_url(),
        use_container_width=True,
    )

# ============================================================
# PÁGINA DE CURSO
# ============================================================

def course_page(course):
    if st.button("← Volver al catálogo"):
        go_home()
        st.rerun()

    st.markdown(
        f"""
        <div class="hero">
            <div class="hero-kicker">{course["category"]} · Nivel {course["level"]}</div>
            <div style="font-size:3.2rem;">{course["icon"]}</div>
            <h1>{course["name"]}</h1>
            <p>{course["objective"]}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    left, right = st.columns([2, 1], gap="large")

    with left:
        st.markdown(
            '<div class="section-title">🎯 Objetivo del curso</div>',
            unsafe_allow_html=True,
        )

        st.markdown(
            f'<div class="detail-box">{course["objective"]}</div>',
            unsafe_allow_html=True,
        )

        st.markdown(
            '<div class="section-title">📚 Temario</div>',
            unsafe_allow_html=True,
        )

        for topic in course["topics"]:
            st.markdown(
                f'<div class="topic">✓ {topic}</div>',
                unsafe_allow_html=True,
            )

    with right:
        st.markdown(
            '<div class="section-title">📋 Información</div>',
            unsafe_allow_html=True,
        )

        st.markdown(
            f"""
            <div class="detail-box">
                <p><strong>📂 Categoría</strong><br>{course["category"]}</p>
                <p><strong>📈 Nivel</strong><br>{course["level"]}</p>
                <p><strong>⏱️ Duración</strong><br>{hours_text(course["hours"])}</p>
                <p><strong>💰 Inversión</strong><br>
                    <span class="course-price">{money(course["price"])}</span>
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.write("")

        st.link_button(
            "💬 Consultar este curso por WhatsApp",
            whatsapp_url(course),
            use_container_width=True,
        )

    st.markdown(
        '<div class="section-title">📩 Solicitar información</div>',
        unsafe_allow_html=True,
    )

    with st.form("contact_course_form"):
        a, b = st.columns(2)

        with a:
            name = st.text_input("Nombre completo *")
            email = st.text_input("Correo electrónico *")

        with b:
            company = st.text_input("Empresa / Organización")
            phone = st.text_input("Teléfono")

        message = st.text_area(
            "Mensaje",
            value=f"Estoy interesado(a) en el curso '{course['name']}'.",
        )

        submitted = st.form_submit_button(
            "Preparar consulta",
            use_container_width=True,
        )

    if submitted:
        if not name or not email:
            st.error("Complete nombre y correo electrónico.")
        else:
            text = (
                f"Hola, soy {name}. "
                f"Estoy interesado(a) en el curso '{course['name']}'. "
                f"Correo: {email}. "
                f"Empresa: {company}. "
                f"Teléfono: {phone}. "
                f"Mensaje: {message}"
            )

            url = f"https://wa.me/{WHATSAPP}?text={quote(text)}"

            st.success("Consulta preparada correctamente.")
            st.link_button(
                "💬 Enviar consulta por WhatsApp",
                url,
                use_container_width=True,
            )


# ============================================================
# PÁGINA PRINCIPAL
# ============================================================

def home_page():
    st.markdown(
        """
        <div class="hero">
            <div class="hero-kicker">Formación profesional · Empresas · Instituciones</div>
            <h1>Capacitación Tecnológica</h1>
            <p>
                Cursos especializados en Inteligencia Artificial, datos,
                cloud, automatización, infraestructura, DevOps,
                Power Platform, Linux y ciberseguridad.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Estadísticas
    category_count = len(set(c["category"] for c in COURSES))

    s1, s2, s3, s4 = st.columns(4)

    with s1:
        st.markdown(
            f'<div class="stat"><div class="stat-number">{len(COURSES)}</div><div class="stat-label">Cursos disponibles</div></div>',
            unsafe_allow_html=True,
        )

    with s2:
        st.markdown(
            f'<div class="stat"><div class="stat-number">{category_count}</div><div class="stat-label">Áreas tecnológicas</div></div>',
            unsafe_allow_html=True,
        )

    with s3:
        st.markdown(
            '<div class="stat"><div class="stat-number">16–40</div><div class="stat-label">Horas por curso</div></div>',
            unsafe_allow_html=True,
        )

    with s4:
        st.markdown(
            '<div class="stat"><div class="stat-number">100%</div><div class="stat-label">Enfoque práctico</div></div>',
            unsafe_allow_html=True,
        )

    st.markdown(
        '<div class="section-title">🔎 Encuentre su curso</div>',
        unsafe_allow_html=True,
    )

    f1, f2 = st.columns([1, 2])

    categories = ["Todas"] + sorted(
        {c["category"] for c in COURSES}
    )

    with f1:
        category = st.selectbox(
            "Área de capacitación",
            categories,
            index=categories.index(st.session_state.category)
            if st.session_state.category in categories
            else 0,
        )
        st.session_state.category = category

    with f2:
        search = st.text_input(
            "Buscar curso",
            placeholder="Ejemplo: Power BI, Azure, Linux, Copilot...",
        )

    filtered = COURSES

    if category != "Todas":
        filtered = [
            c for c in filtered
            if c["category"] == category
        ]

    if search.strip():
        term = search.lower().strip()
        filtered = [
            c for c in filtered
            if term in c["name"].lower()
            or term in c["category"].lower()
            or term in c["objective"].lower()
            or any(term in t.lower() for t in c["topics"])
        ]

    st.markdown(
        f'<div class="section-title">📚 {len(filtered)} cursos disponibles</div>',
        unsafe_allow_html=True,
    )

    if not filtered:
        st.warning("No se encontraron cursos con esos criterios.")
    else:
        for start in range(0, len(filtered), 3):
            row = filtered[start:start + 3]
            columns = st.columns(3, gap="large")

            for col, course in zip(columns, row):
                with col:
                    st.markdown(
                        f"""
                        <div class="course-card">
                            <div class="course-icon">{course["icon"]}</div>
                            <div class="course-category">{course["category"]}</div>
                            <div class="course-title">{course["name"]}</div>
                            <div class="course-description">{course["objective"]}</div>
                            <div class="course-meta">
                                ⏱️ {hours_text(course["hours"])}
                                &nbsp;•&nbsp;
                                <span class="course-price">{money(course["price"])}</span>
                            </div>
                            <div class="level-badge">Nivel: {course["level"]}</div>
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )

                    if st.button(
                        "Ver información →",
                        key=f"view_{start}_{course['name']}",
                        use_container_width=True,
                    ):
                        go_course(course)
                        st.rerun()

    # Capacitación empresarial
    st.markdown(
        '<div class="section-title">💼 Capacitación empresarial a la medida</div>',
        unsafe_allow_html=True,
    )

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown(
            """
            <div class="feature">
                <h3>🧩 Contenido personalizado</h3>
                <p>
                    Adaptamos el contenido, duración y nivel según
                    las necesidades específicas de su organización.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with c2:
        st.markdown(
            """
            <div class="feature">
                <h3>🧪 Enfoque práctico</h3>
                <p>
                    Laboratorios, ejercicios y casos de uso orientados
                    al entorno empresarial.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with c3:
        st.markdown(
            """
            <div class="feature">
                <h3>🌐 Modalidad flexible</h3>
                <p>
                    Capacitación virtual en vivo o presencial para
                    equipos y organizaciones.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # Contacto
    st.markdown(
        '<div class="section-title">📞 ¿Necesita una capacitación personalizada?</div>',
        unsafe_allow_html=True,
    )

    contact1, contact2 = st.columns([2, 1], gap="large")

    with contact1:
        st.markdown(
            """
            <div class="detail-box">
                <h3>Diseñemos una capacitación para su organización</h3>
                <p>
                    Podemos adaptar contenidos, duración, nivel,
                    laboratorios y casos prácticos a las necesidades
                    de su empresa o institución.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with contact2:
        st.link_button(
            "💬 Contactar por WhatsApp",
            whatsapp_url(),
            use_container_width=True,
        )

# ============================================================
# MOSTRAR PÁGINA
# ============================================================

if (
    st.session_state.page == "course"
    and st.session_state.selected_course is not None
):
    course_page(st.session_state.selected_course)
else:
    home_page()

# ============================================================
# BOTÓN FLOTANTE WHATSAPP
# ============================================================

st.markdown(
    f'<a class="whatsapp-float" href="{whatsapp_url()}" target="_blank">💬 WhatsApp</a>',
    unsafe_allow_html=True,
)

# ============================================================
# FOOTER
# ============================================================

st.markdown(
    f"""
    <div class="footer">
        <strong>🎓 Capacitación Tecnológica</strong>
        <br><br>
        Inteligencia Artificial · Azure · Power BI · Power Platform ·
        Linux · DevOps · Ciberseguridad · Arquitectura
        <br><br>
        📞 WhatsApp: {PHONE}
        <br>
        📧 {EMAIL}
        <br><br>
        © 2026 Todos los derechos reservados.
    </div>
    """,
    unsafe_allow_html=True,
)
'''

path = Path("/mnt/data/app.py")
path.write_text(code, encoding="utf-8")

print(f"Archivo creado: {path}")
print(f"Líneas: {len(code.splitlines())}")
