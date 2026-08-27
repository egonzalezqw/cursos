import streamlit as st
from urllib.parse import quote

# ============================================================
# CONFIGURACIÓN
# ============================================================

st.set_page_config(
    page_title="Capacitación Tecnológica",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ============================================================
# CONFIGURACIÓN DE CONTACTO
# ============================================================

WHATSAPP_NUMBER = "50662614659"
EMAIL = "tu-correo@ejemplo.com"

# ============================================================
# CATÁLOGO
# ============================================================

COURSES = [
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
            "Suscripciones",
            "Resource Groups",
            "Máquinas virtuales",
            "Azure Storage",
            "Redes virtuales",
            "Identidad y seguridad",
            "Monitoreo y costos",
        ],
    },
    {
        "category": "Azure",
        "icon": "☁️",
        "name": "Administración de Máquinas Virtuales en Azure",
        "hours": 24,
        "price": 1600,
        "level": "Intermedio",
        "objective": "Administrar máquinas virtuales en Azure aplicando buenas prácticas de seguridad y disponibilidad.",
        "topics": [
            "Creación de máquinas virtuales",
            "Imágenes",
            "Discos",
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

# ============================================================
# CSS
# ============================================================

st.markdown(
    """
    <style>
    .stApp {
        background-color: #f8fafc;
    }

    .block-container {
        max-width: 1400px;
        padding-top: 2rem;
        padding-bottom: 4rem;
    }

    .hero {
        background: linear-gradient(135deg, #0f172a, #1e3a8a, #2563eb);
        padding: 50px 45px;
        border-radius: 28px;
        margin-bottom: 30px;
        box-shadow: 0 15px 40px rgba(15, 23, 42, .18);
    }

    .hero h1 {
        color: white;
        font-size: 2.8rem;
        font-weight: 800;
        margin: 0 0 15px 0;
    }

    .hero p {
        color: #dbeafe;
        font-size: 1.08rem;
        line-height: 1.7;
        max-width: 900px;
        margin: 0;
    }

    .section-title {
        color: #0f172a;
        font-size: 1.8rem;
        font-weight: 800;
        margin: 20px 0;
    }

    .course-card {
        background: white;
        border: 1px solid #e2e8f0;
        border-radius: 20px;
        padding: 23px;
        min-height: 325px;
        box-shadow: 0 8px 25px rgba(15, 23, 42, .07);
        transition: transform .2s ease, box-shadow .2s ease;
    }

    .course-icon {
        font-size: 2.4rem;
        margin-bottom: 10px;
    }

    .course-category {
        color: #2563eb;
        font-size: .75rem;
        font-weight: 800;
        text-transform: uppercase;
        letter-spacing: .05em;
    }

    .course-title {
        color: #0f172a;
        font-size: 1.08rem;
        font-weight: 800;
        line-height: 1.4;
        margin: 8px 0;
        min-height: 62px;
    }

    .course-description {
        color: #64748b;
        font-size: .88rem;
        line-height: 1.5;
        min-height: 78px;
    }

    .course-meta {
        color: #475569;
        font-size: .88rem;
        margin-top: 10px;
    }

    .course-price {
        color: #1d4ed8;
        font-size: 1.25rem;
        font-weight: 900;
    }

    .detail-box {
        background: white;
        border: 1px solid #e2e8f0;
        border-radius: 20px;
        padding: 28px;
        box-shadow: 0 8px 25px rgba(15, 23, 42, .06);
        margin-bottom: 20px;
    }

    .detail-label {
        color: #64748b;
        font-size: .8rem;
        font-weight: 800;
        text-transform: uppercase;
        letter-spacing: .05em;
    }

    .detail-value {
        color: #0f172a;
        font-size: 1.25rem;
        font-weight: 800;
        margin-top: 5px;
    }

    .topic {
        background: white;
        border: 1px solid #e2e8f0;
        border-left: 4px solid #2563eb;
        border-radius: 10px;
        padding: 12px 15px;
        margin: 8px 0;
        color: #334155;
    }

    .feature {
        background: white;
        border: 1px solid #e2e8f0;
        border-radius: 18px;
        padding: 25px;
        min-height: 160px;
        box-shadow: 0 6px 20px rgba(15, 23, 42, .05);
    }

    .feature h3 {
        color: #0f172a;
        margin-top: 0;
    }

    .feature p {
        color: #64748b;
        line-height: 1.6;
    }

    .footer {
        margin-top: 50px;
        padding: 30px;
        text-align: center;
        border-top: 1px solid #e2e8f0;
        color: #64748b;
        line-height: 1.8;
    }

    .footer strong {
        color: #0f172a;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ============================================================
# FUNCIONES
# ============================================================

def money(price):
    if price is None:
        return "Consultar"
    return f"${price:,.0f}"


def duration(hours):
    if hours is None:
        return "Duración por definir"
    return f"{hours} horas"


def whatsapp_url(course=None):
    if course:
        message = (
            f"Hola, estoy interesado(a) en el curso "
            f"'{course['name']}'. Me gustaría recibir información."
        )
    else:
        message = (
            "Hola, me gustaría recibir información sobre "
            "los cursos de capacitación disponibles."
        )

    return (
        f"https://wa.me/{WHATSAPP_NUMBER}"
        f"?text={quote(message)}"
    )


# ============================================================
# SESSION STATE
# ============================================================

if "page" not in st.session_state:
    st.session_state.page = "home"

if "selected_course" not in st.session_state:
    st.session_state.selected_course = None

if "category" not in st.session_state:
    st.session_state.category = "Todas"

# ============================================================
# CATEGORÍAS
# ============================================================

categories = ["Todas"]

for course in COURSES:
    if course["category"] not in categories:
        categories.append(course["category"])

category_icons = {
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
# SIDEBAR
# ============================================================

with st.sidebar:
    st.markdown("## 🎓 Capacitación")
    st.caption("Catálogo de cursos tecnológicos")

    st.divider()

    if st.button(
        "🏠 Inicio",
        use_container_width=True,
    ):
        st.session_state.page = "home"
        st.session_state.selected_course = None
        st.session_state.category = "Todas"
        st.rerun()

    st.markdown("### 📚 Categorías")

    for category in categories:
        if st.button(
            f"{category_icons.get(category, '📘')} {category}",
            key=f"category_{category}",
            use_container_width=True,
        ):
            st.session_state.category = category
            st.session_state.page = "home"
            st.session_state.selected_course = None
            st.rerun()

    st.divider()

    st.markdown("### 📞 Contacto")

    st.link_button(
        "💬 WhatsApp",
        whatsapp_url(),
        use_container_width=True,
    )

    st.write(f"📧 {EMAIL}")

# ============================================================
# DETALLE DEL CURSO
# ============================================================

def show_course(course):

    if st.button(
        "← Volver al catálogo",
        key="back_to_catalog",
    ):
        st.session_state.page = "home"
        st.session_state.selected_course = None
        st.rerun()

    st.markdown(
        f"""
        <div class="hero">
            <div style="font-size:3rem;">
                {course["icon"]}
            </div>

            <h1>
                {course["name"]}
            </h1>

            <p>
                {course["category"]} · Nivel {course["level"]}
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns(
        [2, 1],
        gap="large",
    )

    with col1:

        st.markdown(
            '<div class="section-title">🎯 Objetivo</div>',
            unsafe_allow_html=True,
        )

        st.markdown(
            f"""
            <div class="detail-box">
                {course["objective"]}
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown(
            '<div class="section-title">📚 Temario</div>',
            unsafe_allow_html=True,
        )

        for topic in course["topics"]:
            st.markdown(
                f"""
                <div class="topic">
                    ✓ {topic}
                </div>
                """,
                unsafe_allow_html=True,
            )

    with col2:

        st.markdown(
            '<div class="section-title">💼 Información</div>',
            unsafe_allow_html=True,
        )

        st.markdown(
            f"""
            <div class="detail-box">

                <div class="detail-label">
                    Duración
                </div>

                <div class="detail-value">
                    ⏱️ {duration(course["hours"])}
                </div>

                <br>

                <div class="detail-label">
                    Inversión
                </div>

                <div class="detail-value">
                    💰 {money(course["price"])}
                </div>

                <br>

                <div class="detail-label">
                    Nivel
                </div>

                <div class="detail-value">
                    📈 {course["level"]}
                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown("### Modalidad")

        st.write("💻 Virtual en vivo")
        st.write("🏢 Presencial")
        st.write("👥 Capacitación empresarial")
        st.write("🧪 Laboratorios prácticos")

        st.link_button(
            "💬 Consultar por WhatsApp",
            whatsapp_url(course),
            use_container_width=True,
        )

    st.divider()

    st.markdown(
        '<div class="section-title">📩 Solicitar información</div>',
        unsafe_allow_html=True,
    )

    with st.form(
        key=f"contact_{course['name']}"
    ):

        col_a, col_b = st.columns(2)

        with col_a:
            name = st.text_input(
                "Nombre completo *"
            )

            email = st.text_input(
                "Correo electrónico *"
            )

        with col_b:
            company = st.text_input(
                "Empresa / Organización"
            )

            phone = st.text_input(
                "Teléfono"
            )

        message = st.text_area(
            "Mensaje",
            value=(
                f"Estoy interesado(a) en el curso "
                f"'{course['name']}'."
            ),
        )

        submitted = st.form_submit_button(
            "📩 Preparar solicitud",
            use_container_width=True,
        )

        if submitted:

            if not name.strip() or not email.strip():

                st.error(
                    "Complete el nombre y el correo electrónico."
                )

            else:

                full_message = (
                    f"Hola, soy {name}. "
                    f"Estoy interesado(a) en el curso "
                    f"'{course['name']}'. "
                    f"Correo: {email}. "
                    f"Empresa: {company}. "
                    f"Teléfono: {phone}. "
                    f"Mensaje: {message}"
                )

                link = (
                    f"https://wa.me/{WHATSAPP_NUMBER}"
                    f"?text={quote(full_message)}"
                )

                st.success(
                    "Solicitud preparada correctamente."
                )

                st.link_button(
                    "💬 Enviar solicitud por WhatsApp",
                    link,
                    use_container_width=True,
                )

# ============================================================
# HOME
# ============================================================

def show_home():

    st.markdown(
        """
        <div class="hero">

            <h1>
                🎓 Capacitación Tecnológica
            </h1>

            <p>
                Cursos especializados para profesionales,
                empresas e instituciones en Inteligencia Artificial,
                datos, cloud, automatización, infraestructura,
                DevOps y ciberseguridad.
            </p>

        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="section-title">🔎 Encuentre su curso</div>',
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns(
        [1, 2],
        gap="large",
    )

    with col1:

        current_index = categories.index(
            st.session_state.category
        )

        selected_category = st.selectbox(
            "Área de capacitación",
            categories,
            index=current_index,
        )

        st.session_state.category = selected_category

    with col2:

        search = st.text_input(
            "Buscar curso",
            placeholder="Ejemplo: Power BI, Azure, Linux, IA...",
        )

    filtered = COURSES

    if selected_category != "Todas":

        filtered = [
            course
            for course in filtered
            if course["category"] == selected_category
        ]

    if search.strip():

        term = search.strip().lower()

        filtered = [
            course
            for course in filtered
            if (
                term in course["name"].lower()
                or term in course["category"].lower()
                or term in course["objective"].lower()
            )
        ]

    st.divider()

    st.markdown(
        f"""
        <div class="section-title">
            📚 {len(filtered)} cursos disponibles
        </div>
        """,
        unsafe_allow_html=True,
    )

    if not filtered:

        st.warning(
            "No se encontraron cursos con esos criterios."
        )

    else:

        for start in range(
            0,
            len(filtered),
            3,
        ):

            row = filtered[start:start + 3]

            columns = st.columns(
                3,
                gap="large",
            )

            for column, course in zip(
                columns,
                row,
            ):

                with column:

                    st.markdown(
                        f"""
                        <div class="course-card">

                            <div class="course-icon">
                                {course["icon"]}
                            </div>

                            <div class="course-category">
                                {course["category"]}
                            </div>

                            <div class="course-title">
                                {course["name"]}
                            </div>

                            <div class="course-description">
                                {course["objective"]}
                            </div>

                            <div class="course-meta">
                                ⏱️ {duration(course["hours"])}
                                &nbsp;&nbsp;•&nbsp;&nbsp;
                                <span class="course-price">
                                    {money(course["price"])}
                                </span>
                            </div>

                            <div style="
                                margin-top:8px;
                                color:#64748b;
                                font-size:.8rem;
                            ">
                                Nivel: {course["level"]}
                            </div>

                        </div>
                        """,
                        unsafe_allow_html=True,
                    )

                    if st.button(
                        "Ver información →",
                        key=f"open_{course['name']}",
                        use_container_width=True,
                    ):

                        st.session_state.selected_course = course
                        st.session_state.page = "course"
                        st.rerun()

    st.divider()

    st.markdown(
        '<div class="section-title">💼 Capacitación empresarial a la medida</div>',
        unsafe_allow_html=True,
    )

    col_a, col_b, col_c = st.columns(
        3,
        gap="large",
    )

    with col_a:

        st.markdown(
            """
            <div class="feature">

                <h3>
                    🧩 Contenido personalizado
                </h3>

                <p>
                    Adaptamos el contenido, duración y nivel
                    según las necesidades de su organización.
                </p>

            </div>
            """,
            unsafe_allow_html=True,
        )

    with col_b:

        st.markdown(
            """
            <div class="feature">

                <h3>
                    🧪 Enfoque práctico
                </h3>

                <p>
                    Laboratorios, ejercicios y casos de uso
                    orientados al entorno empresarial.
                </p>

            </div>
            """,
            unsafe_allow_html=True,
        )

    with col_c:

        st.markdown(
            """
            <div class="feature">

                <h3>
                    🌐 Modalidad flexible
                </h3>

                <p>
                    Capacitación virtual en vivo o presencial
                    para equipos y organizaciones.
                </p>

            </div>
            """,
            unsafe_allow_html=True,
        )

# ============================================================
# EJECUCIÓN
# ============================================================

if (
    st.session_state.page == "course"
    and st.session_state.selected_course is not None
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

        <strong>
            🎓 Capacitación Tecnológica
        </strong>

        <br>

        Inteligencia Artificial · Azure · Power BI ·
        Power Platform · Linux · DevOps ·
        Ciberseguridad · Arquitectura

        <br><br>

        📞 WhatsApp: +506 6261-4659
        <br>
        📧 tu-correo@ejemplo.com

        <br><br>

        © 2026 Todos los derechos reservados.

    </div>
    """,
    unsafe_allow_html=True,
)
