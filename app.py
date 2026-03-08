import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Presentaciones que Movilizan", page_icon="📈", layout="wide")

# Estilos CSS personalizados para darle un look corporativo
st.markdown("""
    <style>
    .main-header {font-size: 2.5rem; color: #1E3A8A; font-weight: 700;}
    .sub-header {font-size: 1.5rem; color: #DC2626; font-weight: 500;}
    .metric-card {background-color: #F3F4F6; padding: 20px; border-radius: 10px; text-align: center; border-left: 5px solid #1E3A8A;}
    </style>
""", unsafe_allow_html=True)

# Encabezado formal
st.markdown('<p class="main-header">Gestión del Negocio Minero: Presentaciones que Movilizan 🚀</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Profesor: Dagoberto Pérez Herrera | Ingeniería Civil Industrial UDP</p>', unsafe_allow_html=True)
st.divider()

# Navegación Lateral Interactiva
st.sidebar.header("Índice de la Clase")
menu = st.sidebar.radio(
    "Selecciona un Capítulo:",
    ["1. El Problema del Esfuerzo", 
     "2. Los 7 Pasos de Preparación", 
     "3. Títulos vs Mensajes (Interactividad)", 
     "4. De Números a Símbolos",
     "5. La Puesta en Escena"]
)

if menu == "1. El Problema del Esfuerzo":
    st.header("⚖️ El Equilibrio del Éxito: 50% Técnica / 50% Arte")
    st.markdown("Normalmente, el ingeniero dedica el 100% de su esfuerzo al análisis y olvida el diseño de la presentación hasta el último minuto. **Interactúa con el deslizador para ver el impacto:**")
    
    esfuerzo_analisis = st.slider("Porcentaje de esfuerzo dedicado solo al Análisis de Datos:", 0, 100, 95)
    esfuerzo_presentacion = 100 - esfuerzo_analisis
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="📊 Análisis (La Técnica)", value=f"{esfuerzo_analisis}%")
    with col2:
        st.metric(label="🎨 Presentación (El Arte)", value=f"{esfuerzo_presentacion}%", delta="-Peligro de no movilizar" if esfuerzo_presentacion < 40 else "Balance Ideal")
        
    if esfuerzo_presentacion < 40:
        st.error("⚠️ Cuidado: Las personas no solo compran 'Ideas Buenas'. Si no inviertes al menos 40% del esfuerzo en saber vender la idea, la presentación será inerte y sobrecargada.")
    else:
        st.success("✅ ¡Excelente balance! Trabajar en la presentación en forma simultánea al análisis permite priorizar ideas y no perder tiempo.")

elif menu == "2. Los 7 Pasos de Preparación":
    st.header("🏗️ Estructura: Los 7 Pasos de la Preparación Ágil")
    st.markdown("Seguir esta secuencia ayuda a evitar el *análisis parálisis* y a asegurar la entrega del mensaje clave.")
    
    pasos = {
        "1. Audiencia": "Identifique a quién le habla y defina qué quiere que decidan.",
        "2. Adaptación": "Ajuste el tiempo y la estructura según el conocimiento previo de la sala.",
        "3. Mensaje": "Defina la idea central con la que la audiencia debe quedarse.",
        "4. Tiempo": "Calcule, ajuste al tiempo disponible y ensaye rigurosamente.",
        "5. Ideas Ancla": "Desarrolle un guion gráfico para enlazar los temas.",
        "6. Estructura": "Trace la Introducción -> Desarrollo (Casos) -> Conclusión.",
        "7. Contenidos visuales": "Recién aquí se diagrama la diapositiva en el software."
    }
    
    for paso, desc in pasos.items():
        with st.expander(paso):
            st.write(desc)

elif menu == "3. Títulos vs Mensajes (Interactividad)":
    st.header("📈 Data Storytelling: El gráfico en torno al mensaje")
    st.markdown("La mayoría de las presentaciones fallan porque usan títulos inertes. **Interactúa con el botón abajo para ver el cambio de paradigma en la gestión de un presupuesto:**")
    
    # Switch interactivo
    transformar = st.toggle("✨ Transformar Lámina (De Informativa a Movilizadora)")
    
    # Datos simulados basados en tu ppt (Desviación de presupuesto)
    datos_grafico = {
        "Contractors": 5000,
        "Expenses": 2000,
        "Power": 1000,
        "Labor": 1000,
        "Spare Parts": 2000,
        "Maintenance": 26303 # La anomalía destacada
    }
    
    if not transformar:
        st.subheader("Título inerte: Presupuesto de Operaciones Q1")
        st.write("Tabla de desviaciones de gasto por naturaleza (kUSD):")
        st.table({"Departamento": list(datos_grafico.keys()), "Desviación (kUSD)": list(datos_grafico.values())})
        st.info("❌ Resultado: La audiencia se aburre y se agota buscando dónde está el problema real entre tantos números.")
    else:
        st.subheader("🚨 Mensaje: El Presupuesto está Restringido, necesitamos gestionar el Sobregasto en Mantenimiento")
        col1, col2 = st.columns([1, 2])
        with col1:
            st.metric(label="Sobregasto Mantenimiento", value="86.303 kUSD", delta="26.303 kUSD sobre lo esperado", delta_color="inverse")
        
        with col2:
            st.markdown("**Atención Dirigida (Contraste):**")
            st.bar_chart(datos_grafico, color="#DC2626") 
        st.success("✅ Resultado: El gráfico de barras demuestra importancia y el mensaje dirige la acción directamente hacia la anomalía.")

elif menu == "4. De Números a Símbolos":
    st.header("🚦 Minimalismo Cognitivo: Tablas vs Scorecards")
    st.markdown("Cuando se utilice una tabla (ej. Disponibilidad de Pozos o Cumplimiento de Programas), es preferible llenarla con símbolos para evitar la 'sopa de números'.")
    
    mostrar_simbolos = st.radio("Compara visualmente:", ["Sopa de Números (Antiguo)", "Semáforos / Scorecard (Nuevo)"])
    
    if mostrar_simbolos == "Sopa de Números (Antiguo)":
        st.markdown("### Cumplimiento del Programa DCS (%)")
        st.code("""
        Jul-23: 83.80% | 100.0% | 92.4%
        Ago-23: 95.00% | 100.0% | 95.0%
        Sep-23: 81.00% | 100.0% | 90.0%
        Oct-23: 95.00% | 100.0% | 95.0%
        """)
    else:
        st.markdown("### Cumplimiento del Programa DCS (Scorecard)")
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.markdown("<div class='metric-card'>Jul-23<br><h1 style='margin:0;'>🔴</h1></div>", unsafe_allow_html=True)
        with col2:
            st.markdown("<div class='metric-card'>Ago-23<br><h1 style='margin:0;'>🟢</h1></div>", unsafe_allow_html=True)
        with col3:
            st.markdown("<div class='metric-card'>Sep-23<br><h1 style='margin:0;'>🟡</h1></div>", unsafe_allow_html=True)
        with col4:
            st.markdown("<div class='metric-card'>Oct-23<br><h1 style='margin:0;'>🟢</h1></div>", unsafe_allow_html=True)
        st.success("Destaca visualmente solo la anomalía. El resto de la operación normal pasa a un plano secundario.")

elif menu == "5. La Puesta en Escena":
    st.header("🎭 Exponer es Exponerse: Los 5 Elementos Esenciales")
    st.markdown("La efectividad del orador depende de dominar estos pilares físicos y estratégicos:")
    
    colA, colB = st.columns(2)
    with colA:
        st.markdown("### 🗣️ Expresión Oral")
        st.markdown("""
        * **1. Manejo del Miedo:** La contracción corporal es la imagen del miedo. Se combate con respiración y postura abierta (¡Como los superhéroes!).
        * **2. Postura y Gestos:** Mantén una postura erguida pero relajada. Gestos con palmas abiertas impulsan a la acción.
        * **3. Desplazamiento:** Muévete con propósito, no te quedes anclado ni camines erráticamente.
        * **4. Control del Lenguaje:** Evita la monotonía. El público no puede leer y escuchar a la vez. 
        * **5. Contacto Visual:** Es clave para la credibilidad. Conecta con las personas.
        """)
    with colB:
        st.markdown("### 🛡️ Estrategias Directivas")
        with st.expander("Manejo de Preguntas Difíciles"):
            st.write("""
            - **Honestidad:** Si no sabe o no corresponde a la presentación, hágalo saber de frente.
            - **Diferir:** *"Esa es una pregunta muy interesante... Justo en la próxima sesión lo veremos..."* (¡Y prepárelo!).
            - **Redirigir:** Preguntar a la audiencia o contestar enfocándose en otro ángulo.
            """)
        with st.expander("Anticiparse a la Ley de Murphy"):
            st.write("""
            - **Respaldos:** Lleve copias en múltiples formatos (USB, Nube).
            - **Terreno:** Llegue antes, verifique la iluminación y la ubicación de la pantalla.
            - **Hardware:** Compruebe la longitud de los cables, el funcionamiento del proyector y el lápiz óptico.
            """)
