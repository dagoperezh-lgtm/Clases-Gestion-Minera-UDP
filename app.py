import streamlit as st

# Configuración con el menú lateral SIEMPRE abierto
st.set_page_config(page_title="Gestión Minera UDP", layout="wide", initial_sidebar_state="expanded")

# CSS para formato de presentación (fuentes grandes, sin ocultar el menú)
st.markdown("""
    <style>
    .titulo-slide { font-size: 3.5rem; color: #1E3A8A; font-weight: bold; margin-bottom: 20px;}
    .texto-slide { font-size: 1.8rem; color: #333333; line-height: 1.6;}
    .destacado { background-color: #F3F4F6; border-left: 8px solid #DC2626; padding: 20px; font-size: 1.8rem;}
    </style>
""", unsafe_allow_html=True)

# Menú Lateral Principal
st.sidebar.title("Índice de la Cátedra")
modulo = st.sidebar.radio("Seleccione el Módulo:", [
    "00. Introducción y Reglas (Pág. 1-4)",
    "01. Próximos módulos..." # Los agregaremos en los siguientes pasos
])

if modulo == "00. Introducción y Reglas (Pág. 1-4)":
    # Navegación horizontal de láminas para que sea evidente cómo avanzar
    st.write("### Controles de la Presentación")
    slide = st.radio("Seleccione la Diapositiva:", ["Pág 1: Portada", "Pág 2: Objetivos", "Pág 3: Evaluación", "Pág 4: Condiciones"], horizontal=True)
    st.divider()

    if slide == "Pág 1: Portada":
        col1, col2 = st.columns([1, 1])
        with col1:
            st.markdown('<div class="titulo-slide">Gestión del Negocio Minero</div>', unsafe_allow_html=True)
            st.markdown('<div class="texto-slide"><br><b>Profesor:</b> Dagoberto Pérez Herrera<br>Ingeniería Civil Industrial</div>', unsafe_allow_html=True)
        with col2:
            st.image("https://images.unsplash.com/photo-1578508496410-ee0dbd4ee4d4?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80", use_container_width=True)

    elif slide == "Pág 2: Objetivos":
        st.markdown('<div class="titulo-slide">Objetivo de la Gestión de la Industria Minera</div>', unsafe_allow_html=True)
        st.markdown('<div class="texto-slide">El objetivo general del curso es proporcionar al alumno las herramientas necesarias para encarar su potencial incorporación profesional a la industria minera con los conocimientos generales, lenguaje técnico y cultura minera, que faciliten y contribuyan a su desarrollo profesional en esta rama de la industria o cualquier otra nacional y global.</div><br>', unsafe_allow_html=True)
        
        st.markdown('<div class="destacado"><b>Objetivos Específicos</b><br>Al finalizar el curso, el alumno debe haber desarrollado las siguientes competencias: entendimiento de los factores claves que permiten la viabilidad y sostenibilidad del negocio minero en Chile.<br><br>Su potencial vinculación con el mundo profesional minero radica en la capacidad que adquiere el estudiante en comprender los procesos operacionales y los aspectos claves de la gestión de los recursos en la minería, como por ejemplo: recursos mineros, gestión de las fuentes de energía, gestión de los recursos hídricos, gestión de recursos humanos.</div>', unsafe_allow_html=True)

    elif slide == "Pág 3: Evaluación":
        st.markdown('<div class="titulo-slide">Polinomio de Evaluación</div>', unsafe_allow_html=True)
        
        # Fórmula estricta en LaTeX según el PDF
        st.latex(r"NF = PM \cdot 0.3 + AP \cdot 0.1 + PS \cdot 0.25 + PC \cdot 0.1 + EX \cdot 0.25")
        st.markdown("<br>", unsafe_allow_html=True)
        
        col_a, col_b = st.columns(2)
        with col_a:
            st.markdown("""
            <div class="texto-slide">
            <b>NF:</b> Nota Final<br>
            <b>PM:</b> Proyecto de Mejora (0.3)<br>
            <b>AP:</b> Avance de Proyecto de Mejora (0.1)
            </div>
            """, unsafe_allow_html=True)
        with col_b:
            st.markdown("""
            <div class="texto-slide">
            <b>PS:</b> Prueba Solemne (0.25)<br>
            <b>PC:</b> Promedio de Controles (0.1)<br>
            <b>EX:</b> Examen (0.25)
            </div>
            """, unsafe_allow_html=True)

    elif slide == "Pág 4: Condiciones":
        st.markdown('<div class="titulo-slide">Condiciones de Aprobación</div>', unsafe_allow_html=True)
        st.markdown('<div class="texto-slide"><i>(Aquí insertaremos el texto íntegro de la página 4 de tu documento original)</i></div>', unsafe_allow_html=True)
        # Espacio preparado para el texto completo de la pág 4
