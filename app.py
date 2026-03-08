import streamlit as st

# Configuración de página
st.set_page_config(page_title="Gestión Minera | Presentaciones Efectivas", page_icon="⛏️", layout="wide")

# Estilos CSS para impacto visual en la audiencia (no para el presentador)
st.markdown("""
    <style>
    .mensaje-fuerza {background-color: #1E3A8A; color: white; padding: 30px; border-radius: 10px; text-align: center; font-size: 2rem; font-weight: bold; margin-bottom: 20px;}
    .llamado-accion {background-color: #DC2626; color: white; padding: 20px; border-radius: 8px; font-size: 1.5rem; font-weight: bold; border-left: 10px solid #991B1B;}
    .concepto-clave {font-size: 1.3rem; color: #374151; line-height: 1.8;}
    </style>
""", unsafe_allow_html=True)

# Barra lateral de navegación profunda
st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Logo_UDP.svg/1024px-Logo_UDP.svg.png", width=150)
st.sidebar.title("Índice de la Cátedra (3 hrs)")
seccion = st.sidebar.radio("Navegación:", [
    "0. Intro y Reglas del Curso",
    "1. El Paradigma del Esfuerzo",
    "2. La Estructura (Los 7 Pasos)",
    "3. El Corazón: El Mensaje"
])

if seccion == "0. Intro y Reglas del Curso":
    st.markdown('<div class="mensaje-fuerza">Gestión del Negocio Minero<br><span style="font-size: 1.2rem; font-weight: normal;">Profesor: Dagoberto Pérez Herrera | Ingeniería Civil Industrial</span></div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.header("🎯 Objetivo de la Gestión de la Industria Minera")
        st.markdown('<p class="concepto-clave">Proporcionar las herramientas necesarias para encarar la incorporación profesional a la industria minera. Desarrollaremos conocimientos generales, lenguaje técnico y cultura minera que faciliten la comprensión de los procesos operacionales y la gestión de recursos (mineros, hídricos, energéticos y humanos).</p>', unsafe_allow_html=True)
    
    with col2:
        st.header("⚖️ Polinomio de Evaluación")
        st.info("La Nota Final (NF) se calcula mediante la siguiente estructura:")
        # Uso estricto de LaTeX para la fórmula matemática del curso
        st.latex(r"NF = PM \cdot 0.3 + AP \cdot 0.1 + PS \cdot 0.25 + PC \cdot 0.1 + EX \cdot 0.25")
        
        st.markdown("""
        * **PM:** Proyecto de Mejora (30%)
        * **AP:** Avance Proyecto de Mejora (10%)
        * **PS:** Prueba Solemne (25%)
        * **PC:** Promedio de Controles (10%)
        * **EX:** Examen (25%)
        """)

elif seccion == "1. El Paradigma del Esfuerzo":
    st.markdown('<div class="mensaje-fuerza">La idea no basta: Si no sabes venderla, el proyecto muere.</div>', unsafe_allow_html=True)
    
    st.header("El Error Endémico del Ingeniero")
    st.markdown('<p class="concepto-clave">El ingeniero civil industrial suele invertir todo su capital intelectual en el modelo de datos, la planilla y la simulación. Al momento de enfrentar al directorio, la presentación se arma la noche anterior. El resultado: una exposición inerte que no moviliza a la toma de decisiones.</p>', unsafe_allow_html=True)
    
    colA, colB = st.columns(2)
    with colA:
        st.error("### ❌ Secuencia Tradicional (Destinada al fracaso)")
        st.markdown("""
        1. Levantar datos durante semanas.
        2. Procesar en software de ingeniería.
        3. Obtener resultados técnicos.
        4. **(Día anterior):** Abrir PowerPoint, pegar tablas de Excel completas, poner títulos descriptivos.
        """)
    with colB:
        st.success("### ✅ Secuencia Directiva (Genera Acción)")
        st.markdown("""
        1. Definir el **Objetivo y la Audiencia** (¿Qué decisión necesito hoy?).
        2. Diseñar la estructura narrativa (El "Storyboarding").
        3. Levantar los datos específicos que *sustentan* esa historia.
        4. Crear apoyos visuales de alta retención.
        """)
    
    st.markdown('<div class="llamado-accion">Llamado a la Acción para el Alumno: A partir de hoy, el diseño de la presentación se inicia el DÍA 1 del proyecto, en paralelo al análisis técnico.</div>', unsafe_allow_html=True)

elif seccion == "2. La Estructura (Los 7 Pasos)":
    st.markdown('<div class="mensaje-fuerza">Sin estructura, los datos son solo ruido.</div>', unsafe_allow_html=True)
    
    st.markdown('<p class="concepto-clave">Una presentación de alto nivel en la minería requiere una planificación táctica antes de tocar cualquier software de diseño. Siga estos 7 pasos innegociables:</p>', unsafe_allow_html=True)
    
    tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(["1. Audiencia", "2. Adaptación", "3. Mensaje", "4. Tiempo", "5. Ideas Ancla", "6. Estructura", "7. Visuales"])
    
    with tab1:
        st.subheader("1. La Audiencia")
        st.write("¿Quiénes son? ¿Gerentes de mina, directorio corporativo, operadores? ¿Qué les preocupa (costos, seguridad, producción)? Su presentación debe responder a *sus* dolores, no a los suyos.")
    with tab2:
        st.subheader("2. Adaptación")
        st.write("Ajuste el nivel de jerga técnica. No le hable de 'polinomios de interpolación Kriging' al gerente de finanzas; háblele de 'certeza en la estimación de reservas'.")
    with tab3:
        st.subheader("3. El Mensaje")
        st.write("Si el proyector se quema a los 2 minutos, ¿cuál es la única frase que la audiencia debe recordar? Ese es su mensaje central.")
    with tab4:
        st.subheader("4. El Tiempo")
        st.write("La atención ejecutiva es limitada. Si le dan 20 minutos, prepare 15 y deje 5 para preguntas. Ensayar con cronómetro es obligatorio.")
    with tab5:
        st.subheader("5. Ideas Ancla")
        st.write("Desarrolle un *Storyboard* (guion gráfico). Defina los 3 o 4 hitos fundamentales que sostienen su mensaje central y que guiarán la narrativa.")
    with tab6:
        st.subheader("6. Estructura Lógica")
        st.write("Organice: Introducción (Contexto/Problema) -> Desarrollo (Datos/Alternativas) -> Conclusión (Recomendación/Decisión).")
    with tab7:
        st.subheader("7. Contenidos Visuales")
        st.write("El último paso. Recién ahora se abren las herramientas (Streamlit, PPT). Se diseñan los gráficos y esquemas que actúan como evidencia de las ideas ancla.")

elif seccion == "3. El Corazón: El Mensaje":
    st.markdown('<div class="mensaje-fuerza">Los Títulos informan, los Mensajes DIRIGEN.</div>', unsafe_allow_html=True)
    
    st.markdown('<p class="concepto-clave">En la minería, el tiempo es el recurso más escaso del directorio. Si usted titula una lámina con "Evolución de Costos de Mantenimiento", obliga a la gerencia a estudiar su gráfico para adivinar el problema. Usted debe entregar la conclusión procesada en el encabezado.</p>', unsafe_allow_html=True)
    
    st.divider()
    
    col_x, col_y = st.columns(2)
    with col_x:
        st.markdown("### El Título Inerte (No usar)")
        st.error("❌ **Ejecución Presupuestaria de Operaciones Q1 2024**")
        st.write("Este título no dice nada. Puede ser una ejecución perfecta, un ahorro masivo o una quiebra inminente. La audiencia está ciega hasta que descifra los datos.")
        
    with col_y:
        st.markdown("### El Mensaje Directivo (Obligatorio)")
        st.success("✅ **🚨 Sobregasto crítico en Mantenimiento: Necesitamos inyectar 26kUSD para asegurar la disponibilidad de la flota.**")
        st.write("El mensaje entrega el problema, el dato clave y la acción requerida. El gráfico que acompaña esta lámina solo sirve para *demostrar* esta afirmación como evidencia.")
        
    st.markdown('<div class="llamado-accion">Regla de Oro: Escriba el mensaje de su lámina. Si alguien lee SOLO ese texto y entiende perfectamente qué decisión se debe tomar, su lámina es exitosa.</div>', unsafe_allow_html=True)
