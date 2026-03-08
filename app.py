import streamlit as st

# Configuración en modo "Pantalla Completa/Proyector"
st.set_page_config(page_title="Gestión Minera | Presentaciones Efectivas", page_icon="⛏️", layout="wide", initial_sidebar_state="collapsed")

# Inyección de CSS para forzar fuentes gigantes y aspecto de proyector
st.markdown("""
    <style>
    .titulo-gigante { font-size: 5rem !important; font-weight: 900; color: #1E3A8A; line-height: 1.1; margin-bottom: 20px;}
    .mensaje-impacto { font-size: 3rem !important; font-weight: 700; color: #DC2626; border-left: 15px solid #DC2626; padding-left: 30px; margin-top: 30px; margin-bottom: 30px;}
    .texto-proyector { font-size: 2.2rem !important; color: #374151; line-height: 1.4; }
    .stApp { background-color: #ffffff; }
    /* Ocultar elementos por defecto de Streamlit para limpiar la pantalla */
    header {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# Menú lateral discreto (solo para ti, para cambiar la slide)
st.sidebar.title("Control del Profesor")
slide = st.sidebar.radio("Navegación de Diapositivas:", [
    "1. Portada",
    "2. El Fracaso del Esfuerzo",
    "3. El Paradigma 50/50",
    "4. Caso Real: Radomiro Tomic",
    "5. El Mensaje Directivo"
])

if slide == "1. Portada":
    col1, col2 = st.columns([1.2, 1])
    with col1:
        st.markdown('<br><br><br><p class="titulo-gigante">Presentaciones<br>que Movilizan</p>', unsafe_allow_html=True)
        st.markdown('<p class="texto-proyector" style="color:#6B7280;">Gestión del Negocio Minero<br><b>Ingeniería Civil Industrial</b></p>', unsafe_allow_html=True)
    with col2:
        # Fotografía de impacto minero (Camión de extracción)
        st.image("https://images.unsplash.com/photo-1578508496410-ee0dbd4ee4d4?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80", use_container_width=True)

elif slide == "2. El Fracaso del Esfuerzo":
    st.markdown('<p class="titulo-gigante">El 90% del esfuerzo...</p>', unsafe_allow_html=True)
    
    # Fotografía abstracta de un tajo abierto / rajo
    st.image("https://images.unsplash.com/photo-1605647540924-852290f6b0d5?ixlib=rb-4.0.3&auto=format&fit=crop&w=2000&q=80", height=300, use_container_width=True)
    
    st.markdown('<p class="mensaje-impacto">...se invierte en la planilla, y solo el 10% en convencer al Directorio.</p>', unsafe_allow_html=True)
    st.markdown('<p class="texto-proyector">¿De qué sirve el mejor modelo de optimización de flota si el Gerente de Operaciones no entiende qué decisión debe tomar?</p>', unsafe_allow_html=True)

elif slide == "3. El Paradigma 50/50":
    st.markdown('<p class="titulo-gigante">La Regla del Éxito</p>', unsafe_allow_html=True)
    st.markdown('<br>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div style="background-color:#1E3A8A; padding:50px; border-radius:20px; color:white; height:350px;">'
                    '<h1 style="font-size:5rem; color:white; margin:0;">50% TÉCNICA</h1>'
                    '<br><p style="font-size:2.2rem;">El cálculo riguroso, el polinomio, la simulación geoestadística.</p></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div style="background-color:#DC2626; padding:50px; border-radius:20px; color:white; height:350px;">'
                    '<h1 style="font-size:5rem; color:white; margin:0;">50% ARTE</h1>'
                    '<br><p style="font-size:2.2rem;">Saber vender esa idea para que se convierta en una realidad operativa.</p></div>', unsafe_allow_html=True)

elif slide == "4. Caso Real: Radomiro Tomic":
    st.markdown('<p class="titulo-gigante">El Data Storytelling en la Práctica</p>', unsafe_allow_html=True)
    st.markdown('<p class="texto-proyector">Caso: Prueba Industrial Sistema IINMAS (Predictivo en Correas) - División Radomiro Tomic.</p>', unsafe_allow_html=True)
    
    tab1, tab2 = st.tabs(["❌ La Diapositiva del Novato", "✅ La Diapositiva del Líder"])
    
    with tab1:
        st.markdown('<p class="mensaje-impacto" style="border-color: grey; color: grey;">Título Inerte: "Resultados de Vibración Fase 2"</p>', unsafe_allow_html=True)
        # Imagen de un dashboard confuso lleno de números
        st.image("https://images.unsplash.com/photo-1551288049-bebda4e38f71?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80", use_container_width=True)
        st.markdown('<p class="texto-proyector">Obliga a la gerencia a descifrar los números para entender si es algo bueno o malo.</p>', unsafe_allow_html=True)
        
    with tab2:
        st.markdown('<p class="mensaje-impacto" style="border-color: #10B981; color: #10B981;">Mensaje Directivo: "IINMAS anticipó fallas con 95% de certeza: Recomendamos Roll-out inmediato para evitar detenciones."</p>', unsafe_allow_html=True)
        st.markdown('<p class="texto-proyector"><b>El Título informa. El Mensaje DIRIGE.</b><br>El gráfico que acompaña esta lámina solo sirve para demostrar esta afirmación irrefutable.</p>', unsafe_allow_html=True)

elif slide == "5. El Mensaje Directivo":
    st.markdown('<p class="titulo-gigante">Diseño Basado en la Acción</p>', unsafe_allow_html=True)
    
    # Imagen de una sala de reuniones ejecutiva
    st.image("https://images.unsplash.com/photo-1573164713988-8665fc963095?ixlib=rb-4.0.3&auto=format&fit=crop&w=2000&q=80", height=300, use_container_width=True)
    
    st.markdown('<p class="mensaje-impacto">Si la lámpara del proyector explota en el minuto 2...</p>', unsafe_allow_html=True)
    st.markdown('<p class="texto-proyector">...¿Cuál es la <b>ÚNICA frase</b> con la que el Gerente General debe quedarse en la cabeza?<br>Ese es su mensaje central. Todo el resto es ruido visual.</p>', unsafe_allow_html=True)
