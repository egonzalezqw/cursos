from pathlib import Path
import zipfile, textwrap, json

project = Path("/mnt/data/catalogo_cursos_streamlit")
project.mkdir(exist_ok=True)

app_py = r'''import streamlit as st

st.set_page_config(
    page_title="Catálogo de Cursos | Capacitación Tecnológica",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded",
)

# -----------------------------
# Datos de cursos
# -----------------------------
COURSES = [
    # Inteligencia Artificial
    {
        "category": "Inteligencia Artificial",
        "name": "Microsoft 365 Copilot para Usuarios Finales",
        "hours": 8, "price": 600,
        "objective": "Desarrollar habilidades prácticas para utilizar Microsoft 365 Copilot como asistente de productividad en Word, Excel, PowerPoint, Outlook y Teams.",
        "topics": ["Introducción a Microsoft 365 Copilot", "Prompting aplicado a productividad", "Copilot en Word", "Copilot en Excel", "Copilot en PowerPoint", "Copilot en Outlook y Teams", "Buenas prácticas y seguridad"],
    },
    {
        "category": "Inteligencia Artificial",
        "name": "Copilot para Empresas: Productividad con IA",
        "hours": 16, "price": 1000,
        "objective": "Aplicar Microsoft Copilot en escenarios empresariales para mejorar productividad, análisis de información, generación de contenido y colaboración.",
        "topics": ["IA generativa en entornos empresariales", "Microsoft Copilot y ecosistema Microsoft 365", "Casos de uso empresariales", "Prompts para productividad", "Análisis y síntesis de información", "Creación de documentos y presentaciones", "Gobernanza y uso responsable"],
    },
    {
        "category": "Inteligencia Artificial",
        "name": "Introducción a la Inteligencia Artificial Generativa",
        "hours": 16, "price": 1000,
        "objective": "Comprender los fundamentos de la IA generativa y desarrollar capacidades para utilizar modelos generativos de forma práctica, responsable y orientada a resultados.",
        "topics": ["Conceptos fundamentales de IA", "Machine Learning vs. IA generativa", "LLM y modelos multimodales", "Generación de texto e imágenes", "Prompt Engineering", "Casos de uso empresariales", "Riesgos, ética y seguridad"],
    },
    {
        "category": "Inteligencia Artificial",
        "name": "Prompt Engineering para Profesionales",
        "hours": 16, "price": 1100,
        "objective": "Diseñar instrucciones efectivas para modelos de IA generativa, mejorando la calidad, precisión y consistencia de las respuestas.",
        "topics": ["Anatomía de un prompt", "Contexto, rol, objetivo y restricciones", "Zero-shot y few-shot prompting", "Prompts estructurados", "Evaluación y mejora de respuestas", "Prompts para análisis y automatización", "Buenas prácticas profesionales"],
    },
    {
        "category": "Inteligencia Artificial",
        "name": "Automatización de Tareas con IA",
        "hours": 16, "price": 1100,
        "objective": "Identificar y automatizar tareas repetitivas mediante herramientas de inteligencia artificial, integrando procesos y aumentando la productividad.",
        "topics": ["Identificación de oportunidades de automatización", "IA generativa aplicada a procesos", "Automatización de documentos y datos", "Integración con herramientas empresariales", "Flujos de trabajo asistidos por IA", "Validación y control de resultados", "Diseño de casos de uso"],
    },

    # Azure
    {
        "category": "Azure", "name": "Azure Fundamentals", "hours": 24, "price": 1400,
        "objective": "Comprender los conceptos esenciales de Microsoft Azure, sus principales servicios, modelos de consumo, seguridad y administración.",
        "topics": ["Conceptos de computación en la nube", "Arquitectura de Azure", "Suscripciones y grupos de recursos", "Máquinas virtuales", "Storage", "Redes virtuales", "Identidad y seguridad", "Monitoreo y costos"],
    },
    {
        "category": "Azure", "name": "Administración de Máquinas Virtuales en Azure", "hours": 24, "price": 1600,
        "objective": "Administrar máquinas virtuales en Azure aplicando buenas prácticas de implementación, seguridad, disponibilidad, monitoreo y operación.",
        "topics": ["Creación y configuración de VMs", "Imágenes y discos", "Redes y NSG", "Acceso seguro", "Backup y recuperación", "Escalabilidad y disponibilidad", "Monitoreo", "Optimización de costos"],
    },

    # Power BI
    {
        "category": "Power BI", "name": "Power BI Fundamentals", "hours": 24, "price": 1600,
        "objective": "Desarrollar competencias fundamentales para transformar datos en información útil mediante Power BI.",
        "topics": ["Introducción a Power BI", "Conexión a fuentes de datos", "Power Query", "Transformación de datos", "Visualizaciones", "Filtros y segmentadores", "Publicación de informes", "Introducción a DAX"],
    },
    {
        "category": "Power BI", "name": "Modelado de Datos con Power BI", "hours": 24, "price": 1700,
        "objective": "Diseñar modelos de datos eficientes en Power BI para facilitar análisis, cálculos y generación de indicadores empresariales.",
        "topics": ["Conceptos de modelado dimensional", "Tablas de hechos y dimensiones", "Relaciones", "Esquema estrella", "DAX básico e intermedio", "Medidas y columnas calculadas", "Optimización del modelo", "Buenas prácticas"],
    },
    {
        "category": "Power BI", "name": "Dashboards e Informes Interactivos", "hours": 16, "price": 1200,
        "objective": "Crear dashboards profesionales e interactivos que faciliten la interpretación y comunicación de información.",
        "topics": ["Principios de visualización", "Diseño de dashboards", "Visualizaciones interactivas", "Drill-down y tooltips", "Filtros y navegación", "Indicadores KPI", "Experiencia de usuario", "Publicación y distribución"],
    },
    {
        "category": "Power BI", "name": "Power BI para Analítica Empresarial", "hours": 24, "price": 1700,
        "objective": "Aplicar Power BI para resolver necesidades de analítica empresarial y apoyar la toma de decisiones basada en datos.",
        "topics": ["Analítica descriptiva", "KPIs empresariales", "Modelado y DAX", "Análisis de tendencias", "Segmentación", "Dashboards ejecutivos", "Storytelling con datos", "Caso práctico empresarial"],
    },

    # Power Platform
    {
        "category": "Power Platform", "name": "Microsoft Power Platform Fundamentals", "hours": 24, "price": 1500,
        "objective": "Comprender el ecosistema Microsoft Power Platform y seleccionar sus componentes para resolver necesidades de negocio.",
        "topics": ["Power Platform y low-code", "Power Apps", "Power Automate", "Power BI", "Power Pages", "Dataverse", "Copilot Studio", "Gobernanza y seguridad"],
    },
    {
        "category": "Power Platform", "name": "Automatización con Power Automate", "hours": 24, "price": 1700,
        "objective": "Diseñar flujos automatizados para optimizar procesos empresariales y reducir tareas manuales.",
        "topics": ["Conceptos de Power Automate", "Flujos automatizados y manuales", "Conectores", "Aprobaciones", "Condiciones y expresiones", "Manejo de errores", "Integración con Microsoft 365", "Caso práctico"],
    },
    {
        "category": "Power Platform", "name": "Desarrollo con Power Apps", "hours": 24, "price": 1800,
        "objective": "Crear aplicaciones empresariales low-code utilizando Power Apps, conectadas a fuentes de datos y servicios empresariales.",
        "topics": ["Power Apps Canvas", "Controles y formularios", "Conexión a datos", "Dataverse", "Fórmulas y expresiones", "Validaciones", "Diseño de aplicaciones", "Publicación y seguridad"],
    },
    {
        "category": "Power Platform", "name": "Gestión de Datos con Dataverse", "hours": 16, "price": 1400,
        "objective": "Administrar información empresarial en Microsoft Dataverse aplicando conceptos de estructura, seguridad y gobierno de datos.",
        "topics": ["Arquitectura de Dataverse", "Tablas y columnas", "Relaciones", "Reglas de negocio", "Seguridad y roles", "Integración con Power Apps", "Integración con Power Automate", "Buenas prácticas"],
    },
    {
        "category": "Power Platform", "name": "Integración con Microsoft 365", "hours": 16, "price": 1300,
        "objective": "Integrar Power Platform con servicios de Microsoft 365 para automatizar procesos y mejorar la colaboración.",
        "topics": ["Microsoft 365 y Power Platform", "SharePoint", "Outlook", "Teams", "Excel", "OneDrive", "Conectores y flujos", "Automatización de escenarios"],
    },
    {
        "category": "Power Platform", "name": "Introducción a Power Pages", "hours": 16, "price": 1100,
        "objective": "Construir sitios web empresariales mediante Power Pages y conectarlos con datos y procesos de negocio.",
        "topics": ["Conceptos de Power Pages", "Creación de sitios", "Diseño y navegación", "Dataverse", "Formularios y listas", "Autenticación", "Permisos", "Publicación y seguridad"],
    },
    {
        "category": "Power Platform", "name": "Desarrollo con Copilot Studio", "hours": 16, "price": 1300,
        "objective": "Diseñar agentes y experiencias conversacionales con Copilot Studio para atender consultas y automatizar interacciones.",
        "topics": ["Introducción a Copilot Studio", "Agentes y temas", "Fuentes de conocimiento", "Instrucciones y prompts", "Acciones y conectores", "Integración con Power Automate", "Pruebas y publicación", "Gobernanza"],
    },

    # Linux
    {
        "category": "Linux", "name": "Linux Essentials", "hours": 24, "price": 1400,
        "objective": "Adquirir conocimientos fundamentales para operar sistemas Linux mediante la línea de comandos y herramientas esenciales.",
        "topics": ["Arquitectura Linux", "Terminal y comandos", "Sistema de archivos", "Usuarios y grupos", "Permisos", "Procesos", "Paquetes", "Shell scripting básico"],
    },
    {
        "category": "Linux", "name": "Administración de Linux", "hours": 40, "price": 2400,
        "objective": "Desarrollar competencias para administrar servidores Linux, gestionar servicios, seguridad, almacenamiento y automatización.",
        "topics": ["Administración del sistema", "Usuarios y permisos", "Systemd", "Servicios", "Almacenamiento", "Redes", "Logs", "Seguridad", "Shell scripting", "Automatización"],
    },
    {
        "category": "Linux", "name": "Linux para Servidores", "hours": 40, "price": 2400,
        "objective": "Preparar al participante para operar servidores Linux en ambientes empresariales con enfoque en disponibilidad, seguridad y resolución de incidentes.",
        "topics": ["Instalación y configuración", "Networking", "SSH", "DNS y servicios", "Web servers", "Almacenamiento", "Backup", "Monitoreo", "Hardening", "Troubleshooting"],
    },

    # Contenedores
    {
        "category": "Contenedores", "name": "Docker Fundamentals", "hours": 24, "price": 1800,
        "objective": "Comprender y utilizar Docker para empaquetar, ejecutar y administrar aplicaciones mediante contenedores.",
        "topics": ["Conceptos de contenedores", "Docker Engine", "Imágenes", "Contenedores", "Dockerfile", "Volumes", "Networks", "Docker Compose", "Buenas prácticas"],
    },
    {
        "category": "Contenedores", "name": "Kubernetes & DevOps Fundamentals", "hours": 32, "price": 2100,
        "objective": "Comprender los fundamentos de Kubernetes y DevOps para desplegar, administrar y automatizar aplicaciones contenedorizadas.",
        "topics": ["Contenedores y orquestación", "Arquitectura Kubernetes", "Pods", "Deployments", "Services", "ConfigMaps y Secrets", "CI/CD", "Observabilidad", "Buenas prácticas DevOps"],
    },
    {
        "category": "Contenedores", "name": "Introducción a Microservicios", "hours": 16, "price": 1100,
        "objective": "Comprender los principios de arquitectura de microservicios y sus principales componentes tecnológicos.",
        "topics": ["Monolitos vs. microservicios", "Principios de diseño", "APIs REST", "Comunicación entre servicios", "Configuración", "Service discovery", "Contenedores", "Observabilidad"],
    },

    # Ciberseguridad
    {
        "category": "Ciberseguridad", "name": "Fundamentos de Ciberseguridad", "hours": 24, "price": 1400,
        "objective": "Desarrollar una base sólida en principios de ciberseguridad, amenazas, controles y buenas prácticas de protección.",
        "topics": ["Principios CIA", "Amenazas y vulnerabilidades", "Malware", "Seguridad de redes", "Identidad y acceso", "Seguridad de endpoints", "Gestión de incidentes", "Buenas prácticas"],
    },
    {
        "category": "Ciberseguridad", "name": "Introducción a un SOC", "hours": 24, "price": 1500,
        "objective": "Comprender la operación de un Security Operations Center y los procesos utilizados para monitorear, detectar y responder a incidentes.",
        "topics": ["Qué es un SOC", "Roles y procesos", "SIEM", "Logs y eventos", "Monitoreo", "Threat Intelligence", "Detección de incidentes", "Respuesta y escalamiento"],
    },
    {
        "category": "Ciberseguridad", "name": "ISO 27001",
        "hours": None, "price": None,
        "objective": "Conocer los fundamentos de ISO/IEC 27001 y los elementos necesarios para gestionar un Sistema de Gestión de Seguridad de la Información.",
        "topics": ["Fundamentos de ISO 27001", "Contexto de la organización", "Gestión de riesgos", "Controles de seguridad", "Políticas y procedimientos", "Auditoría interna", "Mejora continua", "Preparación para implementación"],
    },
    {
        "category": "Ciberseguridad", "name": "Zero Trust: Estrategias Modernas de Seguridad",
        "hours": 16, "price": 1200,
        "objective": "Comprender e implementar principios de Zero Trust para fortalecer la seguridad de usuarios, dispositivos, aplicaciones, redes y datos.",
        "topics": ["Principios Zero Trust", "Identidad como perímetro", "Least Privilege", "MFA y acceso condicional", "Segmentación", "Seguridad de endpoints", "Monitoreo y analítica", "Estrategia de implementación"],
    },

    # Arquitectura / otros
    {
        "category": "Arquitectura y Gestión",
        "name": "TOGAF",
        "hours": None, "price": None,
        "objective": "Introducir los principios y componentes de TOGAF para estructurar y gestionar iniciativas de arquitectura empresarial.",
        "topics": ["Arquitectura empresarial", "TOGAF y ADM", "Arquitectura de negocio", "Arquitectura de datos", "Arquitectura de aplicaciones", "Arquitectura tecnológica", "Gobernanza", "Gestión de cambios"],
    },
    {
        "category": "Inteligencia Artificial",
        "name": "Inteligencia Artificial para Profesionales",
        "hours": None, "price": None,
        "objective": "Explorar conceptos y aplicaciones de inteligencia artificial orientadas a la productividad, innovación y transformación de procesos profesionales.",
        "topics": ["Fundamentos de IA", "IA generativa", "Casos de uso empresariales", "Automatización", "Análisis de información", "Prompt Engineering", "Riesgos y ética", "Diseño de casos de uso"],
    },
]

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

# -----------------------------
# Estilos
# -----------------------------
st.markdown("""
<style>
    .main-title {
        font-size: 2.7rem;
        font-weight: 800;
        margin-bottom: 0.2rem;
    }
    .subtitle {
        color: #64748b;
        font-size: 1.1rem;
        margin-bottom: 1.5rem;
    }
    .hero {
        padding: 2rem;
        border-radius: 20px;
        background: linear-gradient(135deg, #0f172a 0%, #1e3a8a 55%, #2563eb 100%);
        color: white;
        margin-bottom: 1.5rem;
    }
    .hero h1 { color: white; margin-bottom: .4rem; }
    .hero p { color: #dbeafe; font-size: 1.05rem; }
    .course-card {
        border: 1px solid #e2e8f0;
        border-radius: 16px;
        padding: 1.15rem;
        min-height: 205px;
        background: white;
        box-shadow: 0 3px 12px rgba(15,23,42,.06);
        margin-bottom: .8rem;
    }
    .course-card h3 { font-size: 1.05rem; margin: .4rem 0; }
    .tag {
        display: inline-block;
        padding: .25rem .55rem;
        border-radius: 999px;
        background: #eff6ff;
        color: #1d4ed8;
        font-size: .78rem;
        font-weight: 700;
    }
    .price {
        font-size: 1.35rem;
        font-weight: 800;
        color: #0f172a;
    }
    .detail-box {
        border: 1px solid #e2e8f0;
        border-radius: 18px;
        padding: 1.5rem;
        background: #fff;
    }
    .topic {
        padding: .55rem .7rem;
        margin: .35rem 0;
        border-radius: 9px;
        background: #f8fafc;
        border-left: 3px solid #2563eb;
    }
    .muted { color: #64748b; }
</style>
""", unsafe_allow_html=True)

# -----------------------------
# Estado
# -----------------------------
if "selected_course" not in st.session_state:
    st.session_state.selected_course = None

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.title("🎓 Catálogo")
st.sidebar.caption("Capacitación tecnológica y empresarial")

categories = ["Todos"] + list(dict.fromkeys(c["category"] for c in COURSES))
selected_category = st.sidebar.radio("Área de capacitación", categories)

search = st.sidebar.text_input("🔎 Buscar curso", placeholder="Ej. Python, Azure, Power BI...")

st.sidebar.divider()
st.sidebar.markdown("### Modalidad")
st.sidebar.write("💻 Virtual")
st.sidebar.write("🏢 Presencial")
st.sidebar.write("🧪 Laboratorios prácticos")
st.sidebar.write("📚 Material y ejercicios")

if st.sidebar.button("🏠 Ver catálogo completo", use_container_width=True):
    st.session_state.selected_course = None
    st.rerun()

# -----------------------------
# Detalle de curso
# -----------------------------
def show_course(course):
    if st.button("← Volver al catálogo"):
        st.session_state.selected_course = None
        st.rerun()

    icon = CATEGORY_ICONS.get(course["category"], "🎓")
    st.markdown(f'<div class="hero"><h1>{icon} {course["name"]}</h1><p>{course["category"]}</p></div>', unsafe_allow_html=True)

    col1, col2 = st.columns([2.2, 1])

    with col1:
        st.markdown("## 🎯 Objetivo")
        st.markdown(f'<div class="detail-box">{course["objective"]}</div>', unsafe_allow_html=True)

        st.markdown("## 📚 Temario")
        for topic in course["topics"]:
            st.markdown(f'<div class="topic">✓ {topic}</div>', unsafe_allow_html=True)

    with col2:
        st.markdown("## Información")
        hours = f'{course["hours"]} horas' if course["hours"] else "Por definir"
        price = f'${course["price"]:,.0f}' if course["price"] else "Consultar"

        st.metric("Duración", hours)
        st.metric("Inversión", price)

        st.markdown("---")
        st.markdown("### 👥 Modalidades")
        st.write("• Virtual en vivo")
        st.write("• Presencial")
        st.write("• Capacitación empresarial")

        st.markdown("---")
        st.info("Los contenidos, duración y modalidad pueden adaptarse según las necesidades de la organización.")

        if st.button("📩 Solicitar información", type="primary", use_container_width=True):
            st.session_state.show_contact = True

    if st.session_state.get("show_contact", False):
        st.markdown("---")
        st.markdown("## 📩 Solicitar información")
        st.write("Complete sus datos y utilice la información mostrada para solicitar una cotización o coordinar una capacitación.")
        c1, c2 = st.columns(2)
        with c1:
            st.text_input("Nombre")
            st.text_input("Correo electrónico")
        with c2:
            st.text_input("Empresa / Organización")
            st.text_input("Teléfono")
        st.text_area("Mensaje", value=f"Me interesa el curso: {course['name']}")
        st.success("Formulario de demostración. Para producción puede conectarse a correo, Forms, CRM o una API.")

# -----------------------------
# Catálogo
# -----------------------------
if st.session_state.selected_course:
    show_course(st.session_state.selected_course)
else:
    st.markdown("""
    <div class="hero">
        <h1>🎓 Catálogo de Capacitación Tecnológica</h1>
        <p>Cursos especializados en Inteligencia Artificial, Cloud, Datos, Automatización, Linux, Contenedores y Ciberseguridad.</p>
    </div>
    """, unsafe_allow_html=True)

    filtered = COURSES
    if selected_category != "Todos":
        filtered = [c for c in filtered if c["category"] == selected_category]

    if search.strip():
        term = search.lower().strip()
        filtered = [c for c in filtered if term in c["name"].lower() or term in c["category"].lower()]

    st.markdown(f"### {len(filtered)} cursos disponibles")

    if not filtered:
        st.warning("No se encontraron cursos con ese criterio.")
    else:
        for i in range(0, len(filtered), 3):
            cols = st.columns(3)
            for col, course in zip(cols, filtered[i:i+3]):
                icon = CATEGORY_ICONS.get(course["category"], "🎓")
                price = f'${course["price"]:,.0f}' if course["price"] else "Consultar"
                duration = f'{course["hours"]} h' if course["hours"] else "Por definir"

                with col:
                    st.markdown(f"""
                    <div class="course-card">
                        <span class="tag">{icon} {course["category"]}</span>
                        <h3>{course["name"]}</h3>
                        <p class="muted">{duration} · <span class="price">{price}</span></p>
                        <p>{course["objective"][:145]}...</p>
                    </div>
                    """, unsafe_allow_html=True)

                    if st.button("Ver información →", key=f"course_{i}_{course['name']}", use_container_width=True):
                        st.session_state.selected_course = course
                        st.session_state.show_contact = False
                        st.rerun()

    st.markdown("---")
    st.markdown("## 💼 Capacitación empresarial a la medida")
    a, b, c = st.columns(3)
    with a:
        st.markdown("### 🧩 Contenido personalizado")
        st.write("Adapte temarios, duración y nivel según las necesidades de su organización.")
    with b:
        st.markdown("### 🧪 Enfoque práctico")
        st.write("Laboratorios, ejercicios y casos de uso orientados al entorno empresarial.")
    with c:
        st.markdown("### 🌐 Virtual o presencial")
        st.write("Modalidades flexibles para equipos y organizaciones.")

    st.info("💡 Los precios publicados son referencias por curso. Para grupos, programas personalizados o contratación empresarial puede solicitarse una cotización.")

st.markdown("---")
st.caption("Catálogo de capacitación tecnológica · Precios expresados en USD · Contenido adaptable según requerimientos")
'''

requirements = """streamlit>=1.40,<2.0
"""

readme = """# Catálogo de Cursos en Streamlit

Sitio web en Python + Streamlit para publicar un catálogo de cursos.

## Incluye

- Catálogo por categorías.
- Buscador de cursos.
- Tarjetas visuales para cada curso.
- Sub-sección/detalle individual al hacer clic.
- Objetivo y temario de cada curso.
- Duración y precio en USD.
- Cursos sin precio/duración definidos aparecen como "Consultar" / "Por definir".
- Sección para solicitar información.
- Diseño responsive y profesional.
- Preparado para publicar en Streamlit Community Cloud.

## Ejecutar localmente

```bash
pip install -r requirements.txt
streamlit run app.py
