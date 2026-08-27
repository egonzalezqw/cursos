import streamlit as st
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
# CONTACTO
# ============================================================

WHATSAPP = "50662614659"
EMAIL = "gonzalezestebanm9@gmail.com"
PHONE = "+506 6261-4659"


# ============================================================
# CATÁLOGO DE CURSOS
# ============================================================

COURSES = [

    # --------------------------------------------------------
    # INTELIGENCIA ARTIFICIAL
    # --------------------------------------------------------

    {
        "category": "Inteligencia Artificial",
        "icon": "🤖",
        "name": "Microsoft 365 Copilot para Usuarios Finales",
        "hours": 8,
        "price": 600,
        "level": "Básico",
        "objective": (
            "Desarrollar habilidades prácticas para utilizar "
            "Microsoft 365 Copilot como asistente de productividad."
        ),
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
        "objective": (
            "Aplicar Microsoft Copilot en escenarios empresariales "
            "para mejorar la productividad y eficiencia."
        ),
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
        "objective": (
            "Comprender los fundamentos de la Inteligencia Artificial "
            "Generativa y sus principales aplicaciones."
        ),
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
        "objective": (
            "Diseñar prompts efectivos para obtener resultados "
            "de mayor calidad con herramientas de Inteligencia Artificial."
        ),
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
        "objective": (
            "Identificar y automatizar tareas repetitivas mediante "
            "herramientas de Inteligencia Artificial."
        ),
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


    # --------------------------------------------------------
    # AZURE
    # --------------------------------------------------------

    {
        "category": "Azure",
        "icon": "☁️",
        "name": "Azure Fundamentals",
        "hours": 24,
        "price": 1400,
        "level": "Básico",
        "objective": (
            "Comprender los conceptos fundamentales de Microsoft Azure "
            "y sus principales servicios."
        ),
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
        "objective": (
            "Administrar máquinas virtuales en Azure aplicando buenas "
            "prácticas de seguridad, disponibilidad y operación."
        ),
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


    # --------------------------------------------------------
    # POWER BI
    # --------------------------------------------------------

    {
        "category": "Power BI",
        "icon": "📊",
        "name": "Power BI Fundamentals",
        "hours": 24,
        "price": 1600,
        "level": "Básico",
        "objective": (
            "Desarrollar competencias fundamentales para transformar "
            "datos en información útil mediante Power BI."
        ),
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
        "objective": (
            "Diseñar modelos de datos eficientes para facilitar "
            "el análisis y la generación de indicadores."
        ),
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
        "objective": (
            "Crear dashboards profesionales e interactivos para "
            "facilitar la interpretación de información."
        ),
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
        "objective": (
            "Aplicar Power BI para resolver necesidades de analítica "
            "empresarial y apoyar la toma de decisiones."
        ),
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


    # --------------------------------------------------------
    # POWER PLATFORM
    # --------------------------------------------------------

    {
        "category": "Power Platform",
        "icon": "⚡",
        "name": "Microsoft Power Platform Fundamentals",
        "hours": 24,
        "price": 1500,
        "level": "Básico",
        "objective": (
            "Comprender el ecosistema Microsoft Power Platform "
            "y sus principales componentes."
        ),
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
        "objective": (
            "Diseñar flujos automatizados para optimizar "
            "procesos empresariales."
        ),
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
        "objective": (
            "Crear aplicaciones empresariales mediante Power Apps "
            "conectadas a fuentes de datos."
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
        "objective": (
            "Administrar información empresarial mediante "
            "Microsoft Dataverse."
        ),
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
        "objective": (
            "Integrar Power Platform con servicios de Microsoft 365 "
            "para automatizar procesos."
        ),
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
        "objective": (
            "Construir sitios web empresariales mediante "
            "Power Pages."
        ),
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
        "objective": (
            "Diseñar agentes conversacionales mediante "
            "Microsoft Copilot Studio."
        ),
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


    # --------------------------------------------------------
    # LINUX
    # --------------------------------------------------------

    {
        "category": "Linux",
        "icon": "🐧",
        "name": "Linux Essentials",
        "hours": 24,
        "price": 1400,
        "level": "Básico",
        "objective": (
            "Adquirir conocimientos fundamentales para operar "
            "sistemas Linux."
        ),
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
        "objective": (
            "Administrar servidores Linux, servicios, seguridad, "
            "almacenamiento y automatización."
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
            "Operar servidores Linux en ambientes empresariales "
            "con enfoque en disponibilidad y seguridad."
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
            "Troubleshooting",
        ],
    },


    # --------------------------------------------------------
    # CONTENEDORES
    # --------------------------------------------------------

    {
        "category": "Contenedores",
        "icon": "📦",
        "name": "Docker Fundamentals",
        "hours": 24,
        "price": 1800,
        "level": "Intermedio",
        "objective": (
            "Comprender y utilizar Docker para ejecutar "
            "aplicaciones mediante contenedores."
        ),
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
        "objective": (
            "Comprender Kubernetes y DevOps para desplegar "
            "y administrar aplicaciones contenedorizadas."
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
        "objective": (
            "Comprender los principios de arquitectura de microservicios "
            "y su aplicación en ambientes modernos."
        ),
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


    # --------------------------------------------------------
    # CIBERSEGURIDAD
    # --------------------------------------------------------

    {
        "category": "Ciberseguridad",
        "icon": "🛡️",
        "name": "Fundamentos de Ciberseguridad",
        "hours": 24,
        "price": 1400,
        "level": "Básico",
        "objective": (
            "Desarrollar una base sólida en principios de "
            "ciberseguridad y protección."
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
        "objective": (
            "Comprender la operación, procesos y tecnologías "
            "utilizadas en un Security Operations Center."
        ),
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
        "objective": (
            "Conocer los fundamentos de ISO/IEC 27001 y los "
            "principales elementos de un Sistema de Gestión "
            "de Seguridad de la Información."
        ),
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
        "objective": (
            "Comprender e implementar principios Zero Trust "
            "para fortalecer la seguridad empresarial."
        ),
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


    # --------------------------------------------------------
    # ARQUITECTURA
    # --------------------------------------------------------

    {
        "category": "Arquitectura y Gestión",
        "icon": "🏗️",
        "name": "TOGAF",
        "hours": None,
        "price": None,
        "level": "Adaptable",
        "objective": (
            "Introducir los principios de TOGAF para estructurar "
            "y gestionar iniciativas de arquitectura empresarial."
        ),
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
# FUNCIONES AUXILIARES
# ============================================================

def format_price(price):
    if price is None:
        return "Consultar"

    return f"${price:,.0f}"


def format_hours(hours):
    if hours is None:
        return "Duración adaptable"

    return f"{hours} horas"


def get_whatsapp_url(course=None):

    if course:

        message = (
            "Hola, estoy interesado(a) en el curso "
            f"'{course['name']}'. "
            "Me gustaría recibir información."
        )

    else:

        message = (
            "Hola, me gustaría recibir información "
            "sobre los cursos de capacitación."
        )

    return (
        f"https://wa.me/{WHATSAPP}"
        f"?text={quote(message)}"
    )


def go_home():

    st.session_state.page = "home"
    st.session_state.selected_course = None


def open_course(course):

    st.session_state.page = "course"
    st.session_state.selected_course = course


# ============================================================
# ESTADO
# ============================================================

if "page" not in st.session_state:
    st.session_state.page = "home"

if "selected_course" not in st.session_state:
    st.session_state.selected_course = None


# ============================================================
# MENÚ SUPERIOR
# ============================================================

menu1, menu2, menu3, menu4 = st.columns(
    [4, 1, 1, 1]
)

with menu1:

    st.title("🎓 Capacitación Tecnológica")

with menu2:

    if st.button(
        "🏠 Inicio",
        use_container_width=True,
    ):

        go_home()
        st.rerun()

with menu3:

    if st.button(
        "📚 Cursos",
        use_container_width=True,
    ):

        go_home()
        st.rerun()

with menu4:

    st.link_button(
        "💬 WhatsApp",
        get_whatsapp_url(),
        use_container_width=True,
    )


st.divider()


# ============================================================
# PÁGINA INDIVIDUAL
# ============================================================

def show_course_page(course):

    if st.button("← Volver al catálogo"):

        go_home()
        st.rerun()

    st.title(
        f"{course['icon']} {course['name']}"
    )

    st.caption(
        f"{course['category']} · Nivel {course['level']}"
    )

    st.info(
        course["objective"]
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "Categoría",
            course["category"],
        )

    with col2:

        st.metric(
            "Duración",
            format_hours(course["hours"]),
        )

    with col3:

        st.metric(
            "Inversión",
            format_price(course["price"]),
        )

    st.divider()

    left, right = st.columns(
        [2, 1],
        gap="large",
    )

    with left:

        st.subheader("🎯 Objetivo")

        st.write(
            course["objective"]
        )

        st.subheader("📚 Temario")

        for number, topic in enumerate(
            course["topics"],
            start=1,
        ):

            st.write(
                f"**{number}.** {topic}"
            )

    with right:

        st.subheader("📋 Información")

        st.write(
            f"**Área:** {course['category']}"
        )

        st.write(
            f"**Nivel:** {course['level']}"
        )

        st.write(
            f"**Duración:** "
            f"{format_hours(course['hours'])}"
        )

        st.write(
            f"**Inversión:** "
            f"{format_price(course['price'])}"
        )

        st.link_button(
            "💬 Consultar este curso",
            get_whatsapp_url(course),
            use_container_width=True,
        )

    st.divider()

    st.subheader(
        "📩 Solicitar información"
    )

    with st.form(
        key=f"form_{course['name']}"
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
                "Estoy interesado(a) en el curso "
                f"'{course['name']}'."
            ),
        )

        submitted = st.form_submit_button(
            "Preparar consulta",
            use_container_width=True,
        )

    if submitted:

        if not name or not email:

            st.error(
                "Debe completar el nombre y "
                "correo electrónico."
            )

        else:

            text = (
                f"Hola, soy {name}. "
                f"Estoy interesado(a) en el curso "
                f"'{course['name']}'. "
                f"Correo: {email}. "
                f"Empresa: {company}. "
                f"Teléfono: {phone}. "
                f"Mensaje: {message}"
            )

            whatsapp = (
                f"https://wa.me/{WHATSAPP}"
                f"?text={quote(text)}"
            )

            st.success(
                "La consulta está lista para enviarse."
            )

            st.link_button(
                "💬 Enviar por WhatsApp",
                whatsapp,
                use_container_width=True,
            )


# ============================================================
# PÁGINA PRINCIPAL
# ============================================================

def show_home_page():

    st.header(
        "Formación profesional para el entorno tecnológico"
    )

    st.write(
        "Cursos especializados para profesionales, "
        "empresas e instituciones en Inteligencia Artificial, "
        "datos, cloud, automatización, infraestructura, "
        "DevOps, Power Platform, Linux y ciberseguridad."
    )

    st.write("")

    # --------------------------------------------------------
    # ESTADÍSTICAS
    # --------------------------------------------------------

    categories = sorted(
        set(
            course["category"]
            for course in COURSES
        )
    )

    s1, s2, s3, s4 = st.columns(4)

    with s1:

        st.metric(
            "📚 Cursos",
            len(COURSES),
        )

    with s2:

        st.metric(
            "🗂️ Áreas",
            len(categories),
        )

    with s3:

        st.metric(
            "⏱️ Duración",
            "8–40 h",
        )

    with s4:

        st.metric(
            "🎯 Modalidad",
            "Flexible",
        )

    st.divider()

    # --------------------------------------------------------
    # BUSCADOR
    # --------------------------------------------------------

    st.subheader(
        "🔎 Encuentre su curso"
    )

    filter1, filter2 = st.columns(
        [1, 2]
    )

    with filter1:

        category = st.selectbox(
            "Área de capacitación",
            ["Todas"] + categories,
        )

    with filter2:

        search = st.text_input(
            "Buscar curso",
            placeholder=(
                "Ejemplo: Power BI, Azure, Linux, Copilot..."
            ),
        )

    # --------------------------------------------------------
    # FILTROS
    # --------------------------------------------------------

    filtered = COURSES.copy()

    if category != "Todas":

        filtered = [
            course
            for course in filtered
            if course["category"] == category
        ]

    if search.strip():

        term = search.lower().strip()

        filtered = [
            course
            for course in filtered
            if (
                term in course["name"].lower()
                or term in course["category"].lower()
                or term in course["objective"].lower()
                or any(
                    term in topic.lower()
                    for topic in course["topics"]
                )
            )
        ]

    st.write("")

    st.subheader(
        f"📚 {len(filtered)} cursos disponibles"
    )

    # --------------------------------------------------------
    # TARJETAS
    # --------------------------------------------------------

    for start in range(
        0,
        len(filtered),
        3,
    ):

        row = filtered[
            start:start + 3
        ]

        columns = st.columns(
            3,
            gap="large",
        )

        for column, course in zip(
            columns,
            row,
        ):

            with column:

                with st.container(
                    border=True
                ):

                    st.subheader(
                        f"{course['icon']} "
                        f"{course['name']}"
                    )

                    st.caption(
                        f"{course['category']} · "
                        f"Nivel {course['level']}"
                    )

                    st.write(
                        course["objective"]
                    )

                    st.write(
                        f"⏱️ **{format_hours(course['hours'])}**"
                    )

                    st.write(
                        f"💰 **{format_price(course['price'])}**"
                    )

                    if st.button(
                        "Ver información →",
                        key=(
                            f"open_{start}_"
                            f"{course['name']}"
                        ),
                        use_container_width=True,
                    ):

                        open_course(course)
                        st.rerun()

    # --------------------------------------------------------
    # CAPACITACIÓN EMPRESARIAL
    # --------------------------------------------------------

    st.divider()

    st.header(
        "💼 Capacitación empresarial a la medida"
    )

    f1, f2, f3 = st.columns(3)

    with f1:

        with st.container(border=True):

            st.subheader(
                "🧩 Contenido personalizado"
            )

            st.write(
                "Adaptamos el contenido, duración "
                "y nivel según las necesidades "
                "de su organización."
            )

    with f2:

        with st.container(border=True):

            st.subheader(
                "🧪 Enfoque práctico"
            )

            st.write(
                "Laboratorios, ejercicios y casos "
                "de uso orientados al entorno empresarial."
            )

    with f3:

        with st.container(border=True):

            st.subheader(
                "🌐 Modalidad flexible"
            )

            st.write(
                "Capacitación virtual en vivo "
                "o presencial para equipos "
                "y organizaciones."
            )

    # --------------------------------------------------------
    # CONTACTO
    # --------------------------------------------------------

    st.divider()

    st.header(
        "📞 ¿Necesita una capacitación personalizada?"
    )

    st.write(
        "Podemos adaptar contenidos, duración, "
        "nivel, laboratorios y casos prácticos "
        "a las necesidades de su empresa o institución."
    )

    contact1, contact2 = st.columns(
        [2, 1]
    )

    with contact1:

        with st.form("general_contact"):

            name = st.text_input(
                "Nombre completo *"
            )

            email = st.text_input(
                "Correo electrónico *"
            )

            company = st.text_input(
                "Empresa / Organización"
            )

            phone = st.text_input(
                "Teléfono"
            )

            message = st.text_area(
                "¿En qué podemos ayudarle?"
            )

            submit = st.form_submit_button(
                "Enviar solicitud",
                use_container_width=True,
            )

        if submit:

            if not name or not email:

                st.error(
                    "Complete nombre y correo electrónico."
                )

            else:

                text = (
                    f"Hola, soy {name}. "
                    f"Me gustaría recibir información "
                    f"sobre las capacitaciones. "
                    f"Correo: {email}. "
                    f"Empresa: {company}. "
                    f"Teléfono: {phone}. "
                    f"Mensaje: {message}"
                )

                whatsapp = (
                    f"https://wa.me/{WHATSAPP}"
                    f"?text={quote(text)}"
                )

                st.success(
                    "Solicitud preparada correctamente."
                )

                st.link_button(
                    "💬 Enviar solicitud por WhatsApp",
                    whatsapp,
                    use_container_width=True,
                )

    with contact2:

        st.info(
            "📞 WhatsApp\n\n"
            f"{PHONE}\n\n"
            "📧 Correo\n\n"
            f"{EMAIL}"
        )

        st.link_button(
            "💬 Contactar por WhatsApp",
            get_whatsapp_url(),
            use_container_width=True,
        )


# ============================================================
# EJECUCIÓN
# ============================================================

if (
    st.session_state.page == "course"
    and st.session_state.selected_course
    is not None
):

    show_course_page(
        st.session_state.selected_course
    )

else:

    show_home_page()


# ============================================================
# FOOTER
# ============================================================

st.divider()

footer1, footer2 = st.columns(2)

with footer1:

    st.write(
        "🎓 **Capacitación Tecnológica**"
    )

    st.caption(
        "Inteligencia Artificial · Azure · Power BI · "
        "Power Platform · Linux · DevOps · "
        "Ciberseguridad · Arquitectura"
    )

with footer2:

    st.write(
        f"📞 WhatsApp: {PHONE}"
    )

    st.write(
        f"📧 {EMAIL}"
    )

st.caption(
    "© 2026 Todos los derechos reservados."
)
