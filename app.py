import streamlit as st

# ==============================================================================
# CONFIGURACIÓN GENERAL
# ==============================================================================
st.set_page_config(page_title="Gestión Minera UDP", layout="wide", initial_sidebar_state="expanded")

# CSS Ajustado para enmarcar el texto y recuperar el botón del menú lateral
st.markdown("""
    <style>
    .titulo-slide { font-size: 3rem; color: #1E3A8A; font-weight: bold; margin-bottom: 15px; line-height: 1.2;}
    .texto-slide { font-size: 1.6rem; color: #333333; line-height: 1.5;}
    .destacado { background-color: #F3F4F6; border-left: 8px solid #DC2626; padding: 20px; font-size: 1.6rem;}
    .alerta { background-color: #FEF2F2; border-left: 8px solid #991B1B; padding: 20px; font-size: 1.6rem; color: #991B1B;}
    </style>
""", unsafe_allow_html=True)

st.sidebar.title("Índice de la Cátedra")
st.sidebar.info("💡 Tip: Haz clic en la 'X' para ocultar esta barra. Para volver a verla, haz clic en el pequeño símbolo '>' en la esquina superior izquierda.")

modulo = st.sidebar.radio("Seleccione el Módulo:", [
    "00. Introducción y Reglas",
    "01. El Paradigma del Esfuerzo",
    "02. Los 7 Pasos de Preparación",
    "03. Data Storytelling y El Mensaje"
])
# ==============================================================================
# INICIO MÓDULO 00: INTRODUCCIÓN Y REGLAS
# ==============================================================================
if modulo == "00. Introducción y Reglas":
    # La botonera se queda fuera del contenedor para que quede Fija arriba
    st.write("### Navegación de Diapositivas")
    slide = st.radio("Seleccione la Diapositiva:", ["Pág 1: Portada", "Pág 2: Objetivos", "Pág 3: Evaluación", "Pág 4: Condiciones"], horizontal=True, label_visibility="collapsed")
    
    # Contenedor de altura fija para enmarcar el texto y evitar el scrolling general
    pantalla = st.container(height=650, border=True)
    
    with pantalla:
        if slide == "Pág 1: Portada":
            col1, col2 = st.columns([1, 1])
            with col1:
                st.markdown('<div class="titulo-slide"><br>Gestión del Negocio Minero</div>', unsafe_allow_html=True)
                st.markdown('<div class="texto-slide"><br><b>Profesor:</b> Dagoberto Pérez Herrera<br>Ingeniería Civil Industrial</div>', unsafe_allow_html=True)
            with col2:
                st.image("https://images.unsplash.com/photo-1578508496410-ee0dbd4ee4d4?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80", use_container_width=True)

        elif slide == "Pág 2: Objetivos":
            st.markdown('<div class="titulo-slide">Objetivo de la Gestión de la Industria Minera</div>', unsafe_allow_html=True)
            st.markdown('<div class="texto-slide">El objetivo general del curso es proporcionar al alumno las herramientas necesarias para encarar su potencial incorporación profesional a la industria minera con los conocimientos generales, lenguaje técnico y cultura minera, que faciliten y contribuyan a su desarrollo profesional en esta rama de la industria o cualquier otra nacional y global.</div><br>', unsafe_allow_html=True)
            st.markdown('<div class="destacado"><b>Objetivos Específicos</b><br>Al finalizar el curso, el alumno debe haber desarrollado las siguientes competencias: entendimiento de los factores claves que permiten la viabilidad y sostenibilidad del negocio minero en Chile.<br><br>Su potencial vinculación con el mundo profesional minero radica en la capacidad que adquiere el estudiante en comprender los procesos operacionales y los aspectos claves de la gestión de los recursos en la minería, como por ejemplo: recursos mineros, gestión de las fuentes de energía, gestión de los recursos hídricos, gestión de recursos humanos.</div>', unsafe_allow_html=True)

        elif slide == "Pág 3: Evaluación":
            st.markdown('<div class="titulo-slide">Polinomio de Evaluación</div>', unsafe_allow_html=True)
            st.latex(r"NF = PM \cdot 0.3 + AP \cdot 0.1 + PS \cdot 0.25 + PC \cdot 0.1 + EX \cdot 0.25")
            st.markdown("<br>", unsafe_allow_html=True)
            col_a, col_b = st.columns(2)
            with col_a:
                st.markdown('<div class="texto-slide"><b>NF:</b> Nota Final<br><b>PM:</b> Proyecto de Mejora (0.3)<br><b>AP:</b> Avance de Proyecto de Mejora (0.1)</div>', unsafe_allow_html=True)
            with col_b:
                st.markdown('<div class="texto-slide"><b>PS:</b> Prueba Solemne (0.25)<br><b>PC:</b> Promedio de Controles (0.1)<br><b>EX:</b> Examen (0.25)</div>', unsafe_allow_html=True)

        elif slide == "Pág 4: Condiciones":
            st.markdown('<div class="titulo-slide">Condiciones de Aprobación</div>', unsafe_allow_html=True)
            st.markdown('<div class="texto-slide">Asistencia mínima obligatoria y entrega oportuna de los proyectos de mejora según el calendario académico establecido.</div>', unsafe_allow_html=True)
# ==============================================================================
# FIN MÓDULO 00
# ==============================================================================

# ==============================================================================
# INICIO MÓDULO 01: EL PARADIGMA DEL ESFUERZO
# ==============================================================================
elif modulo == "01. El Paradigma del Esfuerzo":
    st.write("### Navegación de Diapositivas")
    slide = st.radio("Seleccione la Diapositiva:", ["Pág 5: El Propósito", "Pág 6: Secuencia Tradicional", "Pág 7: Equilibrio de Éxito"], horizontal=True, label_visibility="collapsed")
    
    pantalla = st.container(height=650, border=True)
    
    with pantalla:
        if slide == "Pág 5: El Propósito":
            col1, col2 = st.columns([1.5, 1])
            with col1:
                st.markdown('<div class="titulo-slide">La Idea no basta: El Propósito de la Presentación</div>', unsafe_allow_html=True)
                st.markdown('<div class="texto-slide">En la industria minera, los proyectos no se aprueban automáticamente por el mero hecho de tener un análisis matemático impecable. El directorio requiere entender la implicancia directiva de esos números.<br><br>El objetivo final de una presentación técnica ante un comité ejecutivo <b>no es informar</b>, es que la audiencia compre su idea y se movilice a tomar acción.</div>', unsafe_allow_html=True)
            with col2:
                st.image("https://images.unsplash.com/photo-1507537362848-9c7e70b7b5c1?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80", use_container_width=True)

        elif slide == "Pág 6: Secuencia Tradicional":
            st.markdown('<div class="titulo-slide">El Error Endémico en la Ingeniería</div>', unsafe_allow_html=True)
            st.markdown('<div class="texto-slide">El ingeniero civil industrial suele dedicar la inmensa mayoría de su tiempo (95%) a procesar el modelo de datos, dejando el diseño del mensaje para el final.</div><br>', unsafe_allow_html=True)
            col_x, col_y = st.columns(2)
            with col_x:
                st.markdown('<div class="alerta"><b>Secuencia Tradicional (Lleva al fracaso)</b><br>1. Analizar exhaustivamente los datos.<br>2. Extraer todos los resultados.<br>3. Pegar tablas en PowerPoint el día anterior.<br>4. Exponer datos sin dirección.</div>', unsafe_allow_html=True)
            with col_y:
                st.markdown('<div class="destacado"><b>Secuencia Directiva (Genera Acción)</b><br>1. Definir el mensaje y la audiencia.<br>2. Diseñar la estructura narrativa ("Storyboarding").<br>3. Levantar <b>solo</b> los datos que sustentan el mensaje.<br>4. Crear apoyos visuales de impacto.</div>', unsafe_allow_html=True)

        elif slide == "Pág 7: Equilibrio de Éxito":
            st.markdown('<div class="titulo-slide">La Fórmula del Impacto: 50/50</div>', unsafe_allow_html=True)
            st.markdown('<div class="texto-slide">Para lograr que un proyecto se ejecute, la presentación requiere balancear dos mundos con la misma rigurosidad:</div><br>', unsafe_allow_html=True)
            col_a, col_b = st.columns(2)
            with col_a:
                st.markdown('<div style="background-color:#1E3A8A; padding:30px; border-radius:10px; color:white; text-align:center;"><h1 style="font-size:4rem; color:white; margin:0;">50% TÉCNICA</h1><p style="font-size:1.6rem;">La calidad del dato, la rigurosidad del análisis y la estructura lógica de los argumentos.</p></div>', unsafe_allow_html=True)
            with col_b:
                st.markdown('<div style="background-color:#DC2626; padding:30px; border-radius:10px; color:white; text-align:center;"><h1 style="font-size:4rem; color:white; margin:0;">50% ARTE</h1><p style="font-size:1.6rem;">El diseño visual limpio, la empatía con la audiencia y la histrionismo en la puesta en escena.</p></div>', unsafe_allow_html=True)
# ==============================================================================
# FIN MÓDULO 01
# ==============================================================================

# ==============================================================================
# INICIO MÓDULO 02: LOS 7 PASOS DE PREPARACIÓN
# ==============================================================================
elif modulo == "02. Los 7 Pasos de Preparación":
    st.write("### Navegación de Diapositivas")
    slide = st.radio("Seleccione la Diapositiva:", ["Pág 24-25: Los 7 Pasos", "Pág 28: Esquema", "Pág 30: Guión y Problema", "Pág 32: Resumen"], horizontal=True, label_visibility="collapsed")
    
    pantalla = st.container(height=650, border=True)
    
    with pantalla:
        if slide == "Pág 24-25: Los 7 Pasos":
            st.markdown('<div class="titulo-slide">Seguir una secuencia de 7 pasos ayuda a entregar el mensaje clave</div>', unsafe_allow_html=True)
            col1, col2 = st.columns(2)
            with col1:
                st.markdown('<div class="texto-slide"><b>1º Objetivo:</b> Identifique la audiencia. Defina el Objetivo.<br><br><b>2º Adaptación:</b> Adapte la estructura, ajuste el tiempo, evalúe el conocimiento previo.<br><br><b>3º Mensaje:</b> Defina el mensaje con que quiere que la audiencia se quede. Evalúe el lenguaje y tono.<br><br><b>4º Tiempo:</b> Es requisito calcular el tiempo de la presentación y ensayar rigurosamente.</div>', unsafe_allow_html=True)
            with col2:
                st.markdown('<div class="texto-slide"><b>5º Contenidos:</b> Defina las ideas ancla. Diagrame cómo va a entregar esas ideas y mensajes.<br><br><b>6º Estructura:</b> Defina la estructura (Introducción, Capítulos, Casos, Conclusiones).<br><br><b>7º Trabaje en los contenidos:</b> Para presentaciones largas desarrolle una especie de Guión Gráfico.</div>', unsafe_allow_html=True)

        elif slide == "Pág 28: Esquema":
            st.markdown('<div class="titulo-slide">Un esquema de diapositivas es un recurso clave para un mensaje claro</div>', unsafe_allow_html=True)
            st.markdown('<div class="destacado"><b>Introducción:</b> Con énfasis en el mensaje clave.<br><br><b>Desarrollo:</b> Análisis, datos, gráficos que respalden el mensaje.<br><br><b>Conclusión:</b> Entregar una conclusión acorde a los contenidos mostrados, que refuerce el mensaje y llame a la acción.</div>', unsafe_allow_html=True)

        elif slide == "Pág 30: Guión y Problema":
            st.markdown('<div class="titulo-slide">Hacer un guión gráfico ordena las ideas</div>', unsafe_allow_html=True)
            st.markdown('<div class="texto-slide">• Permite visualizar cómo enlazan los temas de la presentación.<br>• Permite identificar desencadenantes de apoyos audiovisuales.<br>• Permite hacer cierres de objetivos intermedios y preparar el cierre final.</div>', unsafe_allow_html=True)
            st.markdown('<br><div class="titulo-slide">Se puede Movilizar a la Audiencia Mediante el Planteamiento de un Problema</div>', unsafe_allow_html=True)
            st.markdown('<div class="texto-slide"><b>Introduce el Problema con una Pregunta</b> y profundiza en los beneficios para el oyente antes de entregar la <b>Solución</b> (Nuestro Mensaje).</div>', unsafe_allow_html=True)

        elif slide == "Pág 32: Resumen":
            st.markdown('<div class="titulo-slide">Hasta Ahora: Preparar una Presentación que Movilice Requiere:</div>', unsafe_allow_html=True)
            st.markdown('<div class="texto-slide">Trabajar en el análisis y la presentación en forma simultánea, aplicando los 7 pasos:<br><br>Definir objetivo, adecuar a la audiencia, definir el mensaje clave, identificar el tiempo adecuado, hacer un diagrama, definir la estructura de láminas y trabajar en el contenido.<br><br><i>Enuncie un problema e incluya introducciones y resúmenes a lo largo de la presentación.</i></div>', unsafe_allow_html=True)
# ==============================================================================
# FIN MÓDULO 02
# ==============================================================================

# ==============================================================================
# INICIO MÓDULO 03: DATA STORYTELLING Y EL MENSAJE
# ==============================================================================
elif modulo == "03. Data Storytelling y El Mensaje":
    st.write("### Navegación de Diapositivas")
    slide = st.radio("Seleccione la Diapositiva:", ["Pág 35: Títulos vs Mensajes", "Pág 40: Selección de Gráficos", "Pág 45: Tablas vs Scorecards"], horizontal=True, label_visibility="collapsed")
    
    pantalla = st.container(height=650, border=True)
    import time # Importamos la librería de tiempo para las animaciones
    import pandas as pd
    
    with pantalla:
        if slide == "Pág 35: Títulos vs Mensajes":
            st.markdown('<div class="titulo-slide">El Título informa. El Mensaje DIRIGE.</div>', unsafe_allow_html=True)
            
            col1, col2 = st.columns([1, 1.2])
            with col1:
                # Imagen de contexto: Ingenieros analizando datos en faena
                st.image("https://images.unsplash.com/photo-1581094794329-c8112a89af12?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80", use_container_width=True)
            
            with col2:
                # Animación sobria: Cascada de texto
                placeholder = st.empty()
                texto = ""
                
                # Aparece el primer punto
                texto += '<div class="alerta"><b>❌ Título Inerte:</b> "Ejecución Presupuestaria de Mantenimiento Q1".<br><span style="font-size: 1.2rem;">(La audiencia debe adivinar al ver la pantalla si los números son buenos o malos).</span></div><br>'
                placeholder.markdown(texto, unsafe_allow_html=True)
                
                # Pausa de 1.5 segundos
                time.sleep(1.5) 
                
                # Aparece el segundo punto
                texto += '<div class="destacado"><b>✅ Mensaje Directivo:</b> "🚨 Sobregasto crítico en Mantenimiento: Necesitamos inyectar 26 kUSD para asegurar la disponibilidad de la flota."</div><br>'
                placeholder.markdown(texto, unsafe_allow_html=True)
                
                # Pausa final
                time.sleep(1.5)
                
                # Aparece el último punto
                texto += '<div class="texto-slide">El gráfico que acompañe esta lámina debe actuar <b>únicamente</b> como evidencia visual de esta afirmación.</div>'
                placeholder.markdown(texto, unsafe_allow_html=True)

        elif slide == "Pág 40: Selección de Gráficos":
            st.markdown('<div class="titulo-slide">Selección Estratégica y Atención Dirigida</div>', unsafe_allow_html=True)
            st.markdown('<div class="texto-slide">No todos los datos se visualizan igual. En minería, el tiempo es escaso y el gráfico debe servir al mensaje central.</div>', unsafe_allow_html=True)
            
            # Gráfico de barras nativo de Streamlit comparando Presupuesto vs Real
            datos_costos = pd.DataFrame({
                "Área Operativa": ["Extracción", "Chancado", "Molienda", "Flotación", "Mantenimiento"],
                "Presupuesto (kUSD)": [150, 120, 200, 180, 250],
                "Costo Real (kUSD)": [145, 115, 195, 180, 310] # Anomalía intencional en mantenimiento
            })
            
            st.bar_chart(datos_costos.set_index("Área Operativa"), color=["#1E3A8A", "#DC2626"])
            
            st.markdown('<div class="destacado">💡 <b>Contraste Visual:</b> Note cómo el sobrecosto real de Mantenimiento (línea roja) rompe la tendencia esperada. En su presentación directiva, la anomalía es el único dato que debe tener peso visual.</div>', unsafe_allow_html=True)

        elif slide == "Pág 45: Tablas vs Scorecards":
            st.markdown('<div class="titulo-slide">Minimalismo: De la "Sopa de Números" a los Scorecards</div>', unsafe_allow_html=True)
            
            col_a, col_b = st.columns([1, 1.5])
            with col_a:
                # Imagen de contexto: Centro de control integrado minero (CIO)
                st.image("https://images.unsplash.com/photo-1518770660439-4636190af475?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80", use_container_width=True)
            
            with col_b:
                st.markdown('<div class="texto-slide">Cuando proyecte el estado de múltiples equipos, evite tablas de Excel densas. Use semáforos para acelerar la toma de decisiones.</div><br>', unsafe_allow_html=True)
                
                # Animación sobria de Scorecard
                ph = st.empty()
                contenido = ""
                
                contenido += '<div style="font-size: 2rem;">Molino SAG 1: 🟢 <b>Operativo</b> (100% Cumplimiento)</div><br>'
                ph.markdown(contenido, unsafe_allow_html=True)
                time.sleep(1)
                
                contenido += '<div style="font-size: 2rem;">Chancador Primario: 🟡 <b>Alerta Temprana</b> (Revisar desgaste)</div><br>'
                ph.markdown(contenido, unsafe_allow_html=True)
                time.sleep(1)
                
                contenido += '<div style="font-size: 2rem; background-color: #FEF2F2; padding: 10px; border-left: 5px solid #DC2626;">Correa Transportadora C1: 🔴 <b>Detención Crítica</b></div>'
                ph.markdown(contenido, unsafe_allow_html=True)
# ==============================================================================
# FIN MÓDULO 03
# ==============================================================================
