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
    "03. Data Storytelling y El Mensaje",
    "04. Puesta en Escena y Contingencias"
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
# INICIO MÓDULO 02: LA AUDIENCIA ES EL CENTRO
# ==============================================================================
elif modulo == "02. La Audiencia es el Centro":
    st.write("### Navegación de Diapositivas")
    slide = st.radio("Seleccione la Diapositiva:", ["1. El Fin del Teleprompter", "2. Empatía Estratégica", "3. La Metodología (7 Pasos)", "4. El Arco Narrativo"], horizontal=True, label_visibility="collapsed")
    
    pantalla = st.container(height=700, border=True)
    import time
    
    with pantalla:
        if slide == "1. El Fin del Teleprompter":
            st.markdown('<div class="titulo-slide">La pantalla es para ellos, no para usted</div>', unsafe_allow_html=True)
            
            col1, col2 = st.columns([1, 1.2])
            with col1:
                st.image("https://images.unsplash.com/photo-1552664730-d307ca884978?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80", caption="Una audiencia intentando procesar exceso de información", use_container_width=True)
            
            with col2:
                st.markdown('<div class="alerta"><b>El Error del Estudiante:</b> Usar el PowerPoint como un documento de Word proyectado, llenando la lámina de viñetas para no olvidar qué decir.</div>', unsafe_allow_html=True)
                
                ph = st.empty()
                txt = '<div class="texto-slide"><b>El problema cognitivo:</b></div>'
                
                txt += '<div class="texto-slide">• El cerebro humano no puede leer un texto complejo y escuchar al orador con atención simultáneamente.</div>'
                ph.markdown(txt, unsafe_allow_html=True)
                time.sleep(1.5)
                
                txt += '<div class="texto-slide">• Si usted pone todo su discurso en la pantalla, la audiencia comenzará a leer, terminará antes que usted, y se desconectará.</div>'
                ph.markdown(txt, unsafe_allow_html=True)
                time.sleep(1.5)
                
                txt += '<div class="destacado"><b>Solución:</b> La presentación NO es su ayuda de memoria. Es un ancla visual diseñada exclusivamente para facilitar la comprensión de quienes están sentados frente a usted.</div>'
                ph.markdown(txt, unsafe_allow_html=True)

        elif slide == "2. Empatía Estratégica":
            st.markdown('<div class="titulo-slide">Entender a quién le hablo: El Mapa del Usuario</div>', unsafe_allow_html=True)
            st.markdown('<div class="texto-slide">Antes de abrir cualquier software, el ingeniero debe mapear a su público. Usted no presenta su proyecto, usted presenta la solución al problema de su audiencia.</div>', unsafe_allow_html=True)
            
            col_a, col_b, col_c = st.columns(3)
            with col_a:
                st.image("https://images.unsplash.com/photo-1573164713988-8665fc963095?ixlib=rb-4.0.3&auto=format&fit=crop&w=500&q=80", use_container_width=True)
                st.markdown('<div class="destacado" style="font-size: 1.2rem;"><b>1. ¿A quién le presento?</b><br>No es lo mismo pedirle presupuesto al Gerente de Finanzas que explicarle un nuevo proceso al Jefe de Turno. Adapte su lenguaje.</div>', unsafe_allow_html=True)
            with col_b:
                st.image("https://images.unsplash.com/photo-1542626991-cbc4e32524cc?ixlib=rb-4.0.3&auto=format&fit=crop&w=500&q=80", use_container_width=True)
                st.markdown('<div class="destacado" style="font-size: 1.2rem;"><b>2. ¿Qué saben del tema?</b><br>Si usa un nivel técnico excesivo para demostrar cuánto sabe, perderá a la mitad de la sala. Traduzca la complejidad a impacto.</div>', unsafe_allow_html=True)
            with col_c:
                st.image("https://images.unsplash.com/photo-1600880292203-757bb62b4baf?ixlib=rb-4.0.3&auto=format&fit=crop&w=500&q=80", use_container_width=True)
                st.markdown('<div class="alerta" style="font-size: 1.2rem;"><b>3. ¿Qué deben decidir?</b><br>Si salen de la sala diciendo "qué interesante", usted fracasó. Deben salir diciendo "aprobado", "rechazado" o "comencemos".</div>', unsafe_allow_html=True)

        elif slide == "3. La Metodología (7 Pasos)":
            st.markdown('<div class="titulo-slide">El diseño es el Paso 7, no el Paso 1</div>', unsafe_allow_html=True)
            st.markdown('<div class="texto-slide">Siga esta secuencia lógica para construir su mensaje antes de diseñar la primera diapositiva:</div>', unsafe_allow_html=True)
            
            # Representación visual de los pasos
            st.markdown("""
            <div style="background-color: #F3F4F6; padding: 20px; border-radius: 10px;">
                <p class="texto-slide"><b>1. Objetivo y Audiencia:</b> Defina la meta final y quién tiene el poder de decisión.</p>
                <p class="texto-slide"><b>2. Adaptación:</b> Ajuste el nivel de profundidad y la jerga.</p>
                <p class="texto-slide"><b>3. Mensaje:</b> Defina la frase clave. Si el proyector se apaga, esta es la frase que deben recordar.</p>
                <p class="texto-slide"><b>4. Tiempo:</b> Ensayar con cronómetro. Respetar el tiempo de los demás es la regla #1 de cortesía ejecutiva.</p>
                <p class="texto-slide"><b>5. Ideas Ancla:</b> Seleccione solo los datos estrictamente necesarios que sostienen su mensaje.</p>
                <p class="texto-slide"><b>6. Estructura:</b> Construya el Storyboard (Guion Gráfico). Ordene la narrativa.</p>
                <div class="destacado" style="margin-top: 15px;"><b>7. Diseño Visual:</b> Recién ahora abra el software de presentaciones.</div>
            </div>
            """, unsafe_allow_html=True)

        elif slide == "4. El Arco Narrativo":
            st.markdown('<div class="titulo-slide">Storytelling: Los datos sin historia son ruido</div>', unsafe_allow_html=True)
            
            col_x, col_y = st.columns([1, 1.5])
            with col_x:
                st.image("https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80", caption="Construyendo el relato", use_container_width=True)
            
            with col_y:
                ph_story = st.empty()
                txt_s = '<div class="texto-slide">Cómo estructurar la presentación para mantener la atención:</div><br>'
                
                txt_s += '<div class="destacado"><b>A. Introducción (El Gancho)</b><br>Inicie con el problema o la oportunidad. Conecte inmediatamente con el "dolor" de su audiencia para asegurar su atención. Entregue el mensaje clave.</div><br>'
                ph_story.markdown(txt_s, unsafe_allow_html=True)
                time.sleep(1.5)
                
                txt_s += '<div class="destacado"><b>B. Desarrollo (La Evidencia)</b><br>Entregue los datos, el análisis riguroso y los gráficos que demuestran lógicamente que su evaluación es la correcta. Evite datos de "relleno".</div><br>'
                ph_story.markdown(txt_s, unsafe_allow_html=True)
                time.sleep(1.5)
                
                txt_s += '<div class="alerta"><b>C. Conclusión (El Cierre)</b><br>Entregue una conclusión acorde a los contenidos mostrados, que refuerce el mensaje central y haga un llamado a la acción inconfundible.</div>'
                ph_story.markdown(txt_s, unsafe_allow_html=True)

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
    import time # Librería para las animaciones sobrias
    import pandas as pd
    
    with pantalla:
        if slide == "Pág 35: Títulos vs Mensajes":
            st.markdown('<div class="titulo-slide">El Título informa. El Mensaje DIRIGE.</div>', unsafe_allow_html=True)
            
            col1, col2 = st.columns([1, 1.2])
            with col1:
                st.image("https://images.unsplash.com/photo-1581094794329-c8112a89af12?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80", caption="Análisis técnico en centro de control", use_container_width=True)
            
            with col2:
                # Animación de aparición progresiva
                ph = st.empty()
                txt = ""
                
                txt += '<div class="alerta"><b>❌ Título Inerte (No moviliza):</b><br>"Resultados Operacionales y Costos Q1".<br><span style="font-size: 1.1rem;">Obliga a la audiencia a buscar el problema entre los datos.</span></div><br>'
                ph.markdown(txt, unsafe_allow_html=True)
                time.sleep(1.2) # Pausa sobria
                
                txt += '<div class="destacado"><b>✅ Mensaje Directivo (Moviliza):</b><br>"🚨 El sobrecosto en Mantenimiento pone en riesgo el cumplimiento del plan anual: Requiere gestión inmediata."</div><br>'
                ph.markdown(txt, unsafe_allow_html=True)
                time.sleep(1.2)
                
                txt += '<div class="texto-slide"><b>Llamado a la Acción:</b> Use el encabezado para decir qué está pasando y qué hay que hacer.</div>'
                ph.markdown(txt, unsafe_allow_html=True)

        elif slide == "Pág 40: Selección de Gráficos":
            st.markdown('<div class="titulo-slide">Atención Dirigida: El gráfico al servicio del mensaje</div>', unsafe_allow_html=True)
            
            # Datos simulados de costos mineros
            datos = pd.DataFrame({
                "Ítem": ["Energía", "Neumáticos", "Explosivos", "Repuestos", "Mantenimiento"],
                "Presupuesto": [100, 80, 60, 90, 110],
                "Real": [98, 82, 58, 92, 160] # La anomalía
            })
            
            st.markdown('<div class="texto-slide">Compare el presupuesto vs. el gasto real. El gráfico debe destacar la desviación automáticamente.</div>', unsafe_allow_html=True)
            st.bar_chart(datos.set_index("Ítem"), color=["#1E3A8A", "#DC2626"])
            
            st.markdown('<div class="alerta">💡 <b>Observación:</b> Note cómo el color rojo en "Mantenimiento" captura la mirada de inmediato. Eso es atención dirigida.</div>', unsafe_allow_html=True)

        elif slide == "Pág 45: Tablas vs Scorecards":
            st.markdown('<div class="titulo-slide">Evite la "Sopa de Números": Use Scorecards</div>', unsafe_allow_html=True)
            
            col_a, col_b = st.columns([1, 1.5])
            with col_a:
                st.image("https://images.unsplash.com/photo-1518770660439-4636190af475?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80", caption="Supervisión de flota en tiempo real", use_container_width=True)
            
            with col_b:
                st.markdown('<div class="texto-slide">En un comité operativo, la audiencia necesita saber qué está fallando AHORA.</div><br>', unsafe_allow_html=True)
                
                # Animación secuencial de indicadores
                ph2 = st.empty()
                ind = ""
                
                ind += '<div style="font-size: 2rem; border-bottom: 1px solid #ddd; padding: 10px;">Camión CAEX 402: 🟢 <b>Disponible</b></div>'
                ph2.markdown(ind, unsafe_allow_html=True)
                time.sleep(0.8)
                
                ind += '<div style="font-size: 2rem; border-bottom: 1px solid #ddd; padding: 10px;">Pala Hidráulica 05: 🟡 <b>Baja Carga</b></div>'
                ph2.markdown(ind, unsafe_allow_html=True)
                time.sleep(0.8)
                
                ind += '<div style="font-size: 2rem; background-color: #FEF2F2; padding: 10px; border-left: 10px solid #DC2626;"><b>Chancador Primario: 🔴 Fuera de Servicio</b></div>'
                ph2.markdown(ind, unsafe_allow_html=True)

# ==============================================================================
# FIN MÓDULO 03
# ==============================================================================

# ==============================================================================
# INICIO MÓDULO 04: PUESTA EN ESCENA Y CONTINGENCIAS
# ==============================================================================
elif modulo == "04. Puesta en Escena y Contingencias":
    st.write("### Navegación de Diapositivas")
    slide = st.radio("Seleccione la Diapositiva:", ["Pág 122: Preguntas Difíciles", "Pág 123: Ley de Murphy", "Pág 124: Mensaje Final"], horizontal=True, label_visibility="collapsed")
    
    pantalla = st.container(height=650, border=True)
    import time
    
    with pantalla:
        if slide == "Pág 122: Preguntas Difíciles":
            st.markdown('<div class="titulo-slide">Manejo Estratégico de Preguntas Difíciles</div>', unsafe_allow_html=True)
            
            col1, col2 = st.columns([1, 1.2])
            with col1:
                # Imagen de contexto: Un directorio minero haciendo preguntas
                st.image("https://images.unsplash.com/photo-1556761175-b413da4baf72?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80", use_container_width=True)
            
            with col2:
                ph_preg = st.empty()
                txt_preg = '<div class="texto-slide"><b>Las preguntas difíciles conviene manejarlas con estrategia:</b></div><br>'
                
                txt_preg += '<div class="destacado">1. Sea honesto: Si la pregunta no corresponde o no conoce la respuesta, hágalo saber.</div><br>'
                ph_preg.markdown(txt_preg, unsafe_allow_html=True)
                time.sleep(1.5)
                
                txt_preg += '<div class="texto-slide"><b>Si debería saberla y no la sabe:</b></div>'
                txt_preg += '<ul><li>Diferirla para más adelante.</li><li>"Justo en la próxima sesión lo veremos..."</li><li>Preguntar a la audiencia.</li><li>Contestar otra cosa.</li></ul>'
                ph_preg.markdown(txt_preg, unsafe_allow_html=True)

        elif slide == "Pág 123: Ley de Murphy":
            st.markdown('<div class="titulo-slide">Anticípese a los Imprevistos</div>', unsafe_allow_html=True)
            
            col_a, col_b = st.columns(2)
            with col_a:
                st.markdown('<div class="alerta"><b>🛡️ Medidas de Seguridad</b><br><br>'
                            '• Lleve copias de seguridad en múltiples formatos (USB, Nube).<br>'
                            '• Verifique la sala con anticipación (iluminación, disposición).<br>'
                            '• Verifique el equipo: Cables, proyector, lápiz óptico.</div>', unsafe_allow_html=True)
            with col_b:
                st.image("https://images.unsplash.com/photo-1586771107445-d3ca888129ff?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80", caption="Preparación técnica previa", use_container_width=True)
            
            st.markdown('<br><div class="texto-slide"><i>"De esta manera, podrá evitar los contratiempos que la ley de Murphy puede depararle en su presentación."</i></div>', unsafe_allow_html=True)

        elif slide == "Pág 124: Mensaje Final":
            st.markdown('<div class="titulo-slide">Mensaje Final</div>', unsafe_allow_html=True)
            
            # Imagen de gran impacto: Faena minera al atardecer
            st.image("https://images.unsplash.com/photo-1590486803833-ffc4571713df?ixlib=rb-4.0.3&auto=format&fit=crop&w=1600&q=80", use_container_width=True)
            
            st.markdown('<div class="mensaje-fuerza" style="background-color: #1E3A8A; color: white; padding: 20px; text-align: center; font-size: 2.5rem; border-radius: 10px;">'
                        '¡Muchas Gracias!<br><span style="font-size: 1.5rem;">Presentaciones que Movilizan - Gestión Minera UDP</span></div>', unsafe_allow_html=True)

# ==============================================================================
# FIN MÓDULO 04
# ==============================================================================
