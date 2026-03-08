import streamlit as st

# Configuración de página
st.set_page_config(page_title="Gestión del Negocio Minero", page_icon="⛏️", layout="wide")

# Encabezado principal
st.title("Presentaciones que Movilizan 🚀")
st.subheader("Gestión del Negocio Minero")
st.markdown("**Profesor:** Dagoberto Pérez Herrera | *Ingeniería Civil Industrial*")
st.divider()

# Navegación por pestañas (tabs)
tab1, tab2, tab3, tab4 = st.tabs([
    "🎯 Bloque 1: El Propósito", 
    "📊 Bloque 2: Estructura", 
    "🎨 Bloque 3: Diseño Visual", 
    "🎭 Bloque 4: Puesta en Escena"
])

with tab1:
    st.header("La idea no basta, hay que saber venderla")
    col1, col2 = st.columns(2)
    with col1:
        st.info("**50% Técnica:** Tener un análisis técnico y financiero impecable.")
    with col2:
        st.success("**50% Arte:** Saber vender esa idea a los tomadores de decisiones.")
    
    st.write("> *El objetivo final de una presentación técnica no es informar, es que la audiencia compre tu idea y tome acción.*")
    
    st.markdown("""
    ### El Error Común en la Ingeniería
    Normalmente dedicamos el 95% del tiempo al **análisis de datos** y dejamos la presentación para el final.
    Esto genera:
    - Láminas sobrecargadas.
    - Mensajes inerciales.
    - Falta de foco direccional.
    
    **La Solución:** Trabajar el diseño narrativo de la presentación en estricto paralelo con el análisis de los datos.
    """)

with tab2:
    st.header("Estructura y Data Storytelling")
    
    st.markdown("### 🏗️ Los 7 Pasos de la Preparación")
    st.write("**Audiencia** ➔ **Adaptación** ➔ **Mensaje** ➔ **Tiempo** ➔ **Ideas Ancla** ➔ **Estructura** ➔ **Contenidos**")
    
    st.divider()
    
    st.markdown("### ❌ Títulos vs ✅ Mensajes")
    colA, colB = st.columns(2)
    with colA:
        st.error("**Paradigma Antiguo (Informativo)**\n\n*Título:* Presupuesto de Operaciones Q1\n\n*Dato:* Gasto de 200 kUSD, desviación 25%.")
    with colB:
        st.success("**Paradigma Nuevo (Movilizador)**\n\n*Mensaje:* 🚨 El Presupuesto está Restringido este Año: Necesitamos Gestionar el Sobregasto.")
        
    st.markdown("### 🚦 De Números a Símbolos")
    st.write("Evita la 'sopa de números'. Al presentar ante comités, usa semáforos (🔴 🟡 🟢) para métricas clave, destacando visualmente solo la anomalía.")

with tab3:
    st.header("Diseño Visual y Minimalismo Cognitivo")
    
    col_a, col_b = st.columns(2)
    
    with col_a:
        st.markdown("""
        ### ⚖️ La Fórmula del Impacto
        - **60% TÉCNICA (Fondo):** Estructura lógica, calidad y exactitud de las láminas.
        - **40% ARTE (Forma):** Creatividad, visualización limpia e histrionismo de conexión.
        
        ### 🧹 Adiós a las Viñetas
        - Regla de oro: Una lámina = Un mensaje central.
        - Usa cuadrículas, íconos limpios y fomenta el "espacio en blanco".
        - El texto en pantalla debe ser un ancla conceptual, no un teleprompter.
        """)
        
    with col_b:
        st.markdown("""
        ### 🎯 Atención Dirigida
        Utiliza el contraste a tu favor. Mantén colores neutros y utiliza un color intenso **solo en el elemento que presenta la desviación**.
        
        ### 📑 Documento vs Presentación
        Si el directorio necesita los polinomios de evaluación o el detalle operativo, entrégalo como folleto impreso o mediante un código QR. **Jamás lo proyectes.**
        """)

with tab4:
    st.header("La Puesta en Escena (Exponer es Exponerse)")
    
    st.markdown("### 🗣️ Los 5 Pilares de la Presencia Ejecutiva")
    st.markdown("""
    1. **Manejo del Miedo:** Transforma y canaliza la adrenalina como energía escénica.
    2. **Postura y Gestos:** Mantén una postura abierta y frontal.
    3. **Desplazamiento:** Muévete por la sala con intención semántica.
    4. **Control del Lenguaje:** Modula y adapta tu vocabulario a la audiencia.
    5. **Contacto Visual:** Conecta visualmente con la sala de forma constante.
    """)
    
    st.divider()
    
    col_x, col_y = st.columns(2)
    with col_x:
        st.warning("""
        **🛡️ Estrategia ante Preguntas Difíciles**
        - **Honestidad Técnica:** Si un dato escapa al alcance, decláralo de frente.
        - **Diferimiento Estratégico:** *"Ese nivel de detalle técnico lo evaluaremos a fondo en la próxima sesión..."*.
        - **Redirección:** Abre la pregunta a la experiencia de otros especialistas presentes.
        """)
        
    with col_y:
        st.error("""
        **💥 Imprevistos y Ley de Murphy**
        - **Respaldo Múltiple:** Lleva tus copias en pendrive y en la nube.
        - **Inspección de Terreno:** Verifica la iluminación y conectividad de la sala.
        - **Prueba de Equipos:** Revisa el proyector y la batería del pasador de diapositivas.
        """)
