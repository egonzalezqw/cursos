```python
import streamlit as st
from urllib.parse import quote

# ============================================================
# CONFIGURACIÓN
# ============================================================

st.set_page_config(
    page_title="Catálogo de Cursos",
    page_icon="🎓",
    layout="wide"
)

# ============================================================
# CONFIGURACIÓN DE CONTACTO
# ============================================================

WHATSAPP_NUMBER = "50662614659"
EMAIL = "tu-correo@ejemplo.com"

# ============================================================
# CURSOS
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
            "Buenas prácticas y seguridad"
        ]
    },
    {
        "category": "Inteligencia Artificial",
        "icon": "🤖",
        "name": "Copilot para Empresas: Productividad con IA",
        "hours": 16,
        "price": 1000,
        "level": "Intermedio",
        "objective": "Aplicar Microsoft Copilot en escenarios empresariales para mejorar productividad y eficiencia.",
        "topics": [
            "IA generativa empresarial",
            "Microsoft Copilot",
            "Casos de uso empresariales",
            "Creación de prompts",
            "Generación de documentos",
            "Análisis de información",
            "Presentaciones con IA",
            "Outlook y Teams",
            "Gobernanza y uso responsable"
        ]
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
            "Fundamentos de IA",
            "Machine Learning",
            "IA Generativa",
            "Large Language Models",
            "Modelos multimodales",
            "Generación de texto",
            "Generación de imágenes",
            "Prompt Engineering",
            "Casos empresariales",
            "Ética y seguridad"
        ]
    },
    {
        "category": "Inteligencia Artificial",
        "icon": "✍️",
        "name": "Prompt Engineering para Profesionales",
        "hours": 16,
        "price": 1100,
        "level": "Intermedio",
        "objective": "Diseñar prompts efectivos para obtener resultados de mayor calidad con herramientas de IA.",
        "topics": [
            "Fundamentos de Prompt Engineering",
            "Anatomía de un prompt",
            "Contexto e instrucciones",
            "Zero-shot prompting",
            "Few-shot prompting",
            "Prompts estructurados",
            "Evaluación de respuestas",
            "Optimización de prompts",
            "Casos empresariales"
        ]
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
            "Diseño de casos de uso"
        ]
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
            "Monitoreo y costos"
        ]
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
            "Optimización de costos"
        ]
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
            "Introducción a DAX"
        ]
    },
    {
        "category": "Power BI",
        "icon": "📈",
        "name": "Modelado de Datos con Power BI",
        "hours": 24,
        "price": 1700,
        "level": "Intermedio",
        "objective": "Diseñar modelos de datos eficientes para facilitar análisis y generación de indicadores.",
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
            "Optimización"
        ]
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
            "Storytelling"
        ]
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
            "Caso práctico empresarial"
        ]
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
            "Gobernanza"
        ]
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
            "Microsoft 365"
        ]
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
            "Publicación"
        ]
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
            "Buenas prácticas"
        ]
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
            "Casos de integración"
        ]
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
            "Publicación"
        ]
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
            "Publicación"
        ]
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
            "Shell scripting"
        ]
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
            "Troubleshooting"
        ]
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
            "Troubleshooting"
        ]
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
            "Buenas prácticas"
        ]
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
            "DevOps"
        ]
    },
    {
        "category": "Contenedores",
        "icon": "🔧",
        "name": "Introducción a Microservicios",
        "hours": 16,
        "price": 1100,
        "level": "Intermedio",
        "objective": "Comprender los principios de arquitectura de microservicios.",
        "topics": [
            "Monolitos vs microservicios",
            "Diseño de microservicios",
            "APIs REST",
            "Comunicación",
            "Configuración",
            "Service Discovery",
            "Contenedores",
            "Observabilidad"
        ]
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
            "Gestión de incidentes"
        ]
    },
    {
        "category": "Ciberseguridad",
        "icon": "🔎",
        "name": "Introducción a un SOC",
        "hours": 24,
        "price": 1500,
        "level": "Intermedio",
        "objective": "Comprender la operación de un Security Operations Center.",
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
            "Respuesta a incidentes"
        ]
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
            "SGSI",
            "Contexto organizacional",
            "Gestión de riesgos",
            "Controles",
            "Políticas",
            "Procedimientos",
            "Auditoría",
            "Mejora continua"
        ]
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
            "Estrategia de implementación"
        ]
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
            "Gobernanza"
        ]
    }
]

# ============================================================
# FUNCIONES
# ============================================================

def money(price):
    if price is None:
        return "Consultar"
    return f"${price:,.0f}"


def hours_text(hours):
    if hours is None:
        return "Por definir"
    return f"{hours} horas"


def whatsapp_link(course):
    message = (
        f"Hola, estoy interesado(a) en el curso "
        f"'{course['name']}'. Me gustaría recibir información."
    )

    return (
        f"https://wa.me/{WHATSAPP_NUMBER}"
        f"?text={quote(message)}"
    )


# ============================================================
# ESTILOS
# ============================================================

st.markdown(
    """
    <style>

    .main {
        background: #f8fafc;
    }

    .block-container {
        max-width: 1400px;
        padding-top: 2rem;
    }

    .hero {
        background: linear-gradient(
            135deg,
            #0f172a,
            #1e3a8a,
            #2563eb
        );

        padding: 45px;
        border-radius: 25px;
        color: white;
        margin-bottom: 30px;
    }

    .hero h1 {
        color: white;
        font-size: 2.8rem;
        font-weight: 800;
    }

    .hero p {
        color: #dbeafe;
        font-size: 1.15rem;
    }

    .card {
        background: white;
        border: 1px solid #e2e8f0;
        border-radius: 18px;
        padding: 22px;
        min-height: 275px;
        margin-bottom: 12px;
        box-shadow: 0 5px 18px rgba(15,23,42,.07);
    }

    .icon {
        font-size: 2.3rem;
    }

    .tag {
        display: inline-block;
        background: #eff6ff;
        color: #1d4ed8;
        padding: 5px 10px;
        border-radius: 999px;
        font-size: .75rem;
        font-weight: bold;
        margin-top: 8px;
    }

    .level {
        display: inline-block;
        background: #f1f5f9;
        color: #475569;
        padding: 5px 10px;
        border-radius: 999px;
        font-size: .75rem;
        font-weight: bold;
        margin-left: 5px;
    }

    .title {
        color: #0f172a;
        font-size: 1.12rem;
        font-weight: 800;
        min-height: 55px;
        margin-top: 12px;
    }

    .description {
        color: #64748b;
        font-size: .9rem;
        min-height: 65px;
    }

    .price {
        color: #1d4ed8;
        font-size: 1.35rem;
        font-weight: 800;
    }

    .detail {
        background: white;
        border-radius: 18px;
        border: 1px solid #e2e8f0;
        padding: 25px;
        margin-bottom: 20px;
        box-shadow: 0 5px 18px rgba(15,23,42,.06);
    }

    .topic {
        background: #f8fafc;
        border-left: 4px solid #2563eb;
        padding: 10px 15px;
        border-radius: 8px;
        margin: 7px 0;
    }

    .footer {
        text-align: center;
        color: #64748b;
        padding: 40px;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# ============================================================
# ESTADO DE LA APLICACIÓN
# ============================================================

if "page" not in st.session_state:
    st.session_state.page = "home"

if "selected_course" not in st.session_state:
    st.session_state.selected_course = None

if "category" not in st.session_state:
    st.session_state.category = "Todas"


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.markdown("# 🎓 Catálogo")

st.sidebar.caption(
    "Capacitación tecnológica y empresarial"
)

st.sidebar.divider()

if st.sidebar.button(
    "🏠 Inicio",
    use_container_width=True
):
    st.session_state.page = "home"
    st.session_state.selected_course = None
    st.session_state.category = "Todas"
    st.rerun()

st.sidebar.markdown("### 📚 Categorías")

categories = ["Todas"] + list(
    dict.fromkeys(
        course["category"]
        for course in COURSES
    )
)

for category in categories:

    icon = {
        "Inteligencia Artificial": "🤖",
        "Azure": "☁️",
        "Power BI": "📊",
        "Power Platform": "⚡",
        "Linux": "🐧",
        "Contenedores": "📦",
        "Ciberseguridad": "🛡️",
        "Arquitectura y Gestión": "🏗️",
        "Todas": "📚"
    }.get(category, "📘")

    if st.sidebar.button(
        f"{icon} {category}",
        key=f"category_{category}",
        use_container_width=True
    ):
        st.session_state.category = category
        st.session_state.page = "home"
        st.session_state.selected_course = None
        st.rerun()

st.sidebar.divider()

st.sidebar.markdown("### 📞 Contacto")

st.sidebar.link_button(
    "💬 WhatsApp",
    f"https://wa.me/{WHATSAPP_NUMBER}",
    use_container_width=True
)

st.sidebar.write(
    f"📧 {EMAIL}"
)


# ============================================================
# PÁGINA DE DETALLE
# ============================================================

def show_course(course):

    if st.button("← Volver al catálogo"):
        st.session_state.page = "home"
        st.session_state.selected_course = None
        st.rerun()

    st.markdown(
        f"""
        <div class="hero">

            <h1>
                {course["icon"]} {course["name"]}
            </h1>

            <p>
                {course["category"]} · Nivel {course["level"]}
            </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    left, right = st.columns([2, 1])

    with left:

        st.markdown("## 🎯 Objetivo")

        st.markdown(
            f"""
            <div class="detail">
                {course["objective"]}
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown("## 📚 Temario")

        for topic in course["topics"]:

            st.markdown(
                f"""
                <div class="topic">
                    ✓ {topic}
                </div>
                """,
                unsafe_allow_html=True
            )

    with right:

        st.markdown("## 💼 Información")

        st.markdown(
            f"""
            <div class="detail">

                <h4>⏱️ Duración</h4>
                <h2>{hours_text(course["hours"])}</h2>

                <hr>

                <h4>💰 Inversión</h4>
                <h2>{money(course["price"])}</h2>

                <hr>

                <h4>📈 Nivel</h4>
                <h2>{course["level"]}</h2>

            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown("### 📌 Modalidades")

        st.write("💻 Virtual en vivo")
        st.write("🏢 Presencial")
        st.write("👥 Capacitación empresarial")
        st.write("🧪 Laboratorios prácticos")

        st.link_button(
            "💬 Consultar por WhatsApp",
            whatsapp_link(course),
            use_container_width=True
        )

    st.markdown("---")

    # ========================================================
    # FORMULARIO
    # ========================================================

    st.markdown("## 📩 Solicitar información")

    with st.form(
        f"form_{course['name']}"
    ):

        col1, col2 = st.columns(2)

        with col1:

            name = st.text_input(
                "Nombre completo *"
            )

            email = st.text_input(
                "Correo electrónico *"
            )

        with col2:

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
            )
        )

        submitted = st.form_submit_button(
            "📩 Solicitar información",
            use_container_width=True
        )

        if submitted:

            if not name or not email:

                st.error(
                    "Complete el nombre y correo electrónico."
                )

            else:

                st.success(
                    "Solicitud preparada correctamente."
                )

                msg = (
                    f"Hola, soy {name}. "
                    f"Estoy interesado(a) en el curso "
                    f"'{course['name']}'. "
                    f"Correo: {email}. "
                    f"Empresa: {company}. "
                    f"Teléfono: {phone}. "
                    f"Mensaje: {message}"
                )

                whatsapp = (
                    f"https://wa.me/"
                    f"{WHATSAPP_NUMBER}"
                    f"?text={quote(msg)}"
                )

                st.link_button(
                    "💬 Enviar solicitud por WhatsApp",
                    whatsapp
                )


# ============================================================
# PÁGINA PRINCIPAL
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
                empresas e instituciones en tecnología,
                datos, inteligencia artificial,
                cloud, automatización y ciberseguridad.
            </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    # ========================================================
    # BUSCADOR
    # ========================================================

    col1, col2 = st.columns([1, 2])

    with col1:

        category = st.selectbox(
            "Área de capacitación",
            categories,
            index=categories.index(
                st.session_state.category
            )
        )

        st.session_state.category = category

    with col2:

        search = st.text_input(
            "🔎 Buscar curso",
            placeholder=(
                "Ejemplo: Power BI, Azure, Linux, IA..."
            )
        )

    # ========================================================
    # FILTRADO
    # ========================================================

    filtered = COURSES

    if category != "Todas":

        filtered = [
            course
            for course in filtered
            if course["category"] == category
        ]

    if search:

        search_lower = search.lower()

        filtered = [
            course
            for course in filtered
            if (
                search_lower in course["name"].lower()
                or search_lower in course["category"].lower()
                or search_lower in course["objective"].lower()
            )
        ]

    st.markdown("---")

    st.markdown(
        f"### 📚 {len(filtered)} cursos disponibles"
    )

    # ========================================================
    # TARJETAS
    # ========================================================

    for start in range(
        0,
        len(filtered),
        3
    ):

        cols = st.columns(3)

        for col, course in zip(
            cols,
            filtered[start:start + 3]
        ):

            with col:

                st.markdown(
                    f"""
                    <div class="card">

                        <div class="icon">
                            {course["icon"]}
                        </div>

                        <span class="tag">
                            {course["category"]}
                        </span>

                        <span class="level">
                            {course["level"]}
                        </span>

                        <div class="title">
                            {course["name"]}
                        </div>

                        <div class="description">
                            {course["objective"][:150]}...
                        </div>

                        <div>
                            ⏱️ {hours_text(course["hours"])}
                            &nbsp;&nbsp;
                            <span class="price">
                                {money(course["price"])}
                            </span>
                        </div>

                    </div>
                    """,
                    unsafe_allow_html=True
                )

                if st.button(
                    "Ver información →",
                    key=f"open_{course['name']}",
                    use_container_width=True
                ):

                    st.session_state.selected_course = course
                    st.session_state.page = "course"
                    st.rerun()

    # ========================================================
    # SERVICIOS EMPRESARIALES
    # ========================================================

    st.markdown("---")

    st.markdown(
        "## 💼 Capacitación empresarial a la medida"
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        st.markdown(
            "### 🧩 Contenido personalizado"
        )

        st.write(
            "Adaptamos el contenido, duración y nivel "
            "según las necesidades de su organización."
        )

    with col2:

        st.markdown(
            "### 🧪 Enfoque práctico"
        )

        st.write(
            "Laboratorios, ejercicios y casos de uso "
            "orientados al entorno empresarial."
        )

    with col3:

        st.markdown(
            "### 🌐 Modalidad flexible"
        )

        st.write(
            "Capacitación virtual en vivo o presencial "
            "para equipos y organizaciones."
        )


# ============================================================
# MOSTRAR PÁGINA
# ============================================================

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

        <strong>
            🎓 Capacitación Tecnológica
        </strong>

        <br>

        Inteligencia Artificial · Azure · Power BI ·
        Power Platform · Linux · DevOps ·
        Ciberseguridad · Arquitectura

        <br><br>

        © 2026 Todos los derechos reservados.

    </div>
    """,
    unsafe_allow_html=True
)
```
