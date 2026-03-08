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
    st.write("### Navegación Dinámica")
    # Si ves estos nuevos títulos en los botones, significa que la actualización funcionó
    slide = st.radio("Seleccione la Diapositiva:", ["1. El Interruptor Visual", "2. Simulador de Empatía", "3. Fases y 7 Pasos", "4. El Arco Narrativo"], horizontal=True, label_visibility="collapsed")
    
    # Eliminamos el st.container(height=700) que estaba cortando y dejando en blanco tu contenido
    st.markdown("<br>", unsafe_allow_html=True)
    
    if slide == "1. El Interruptor Visual":
        st.markdown('<div class="titulo-slide">La pantalla no es su ayuda de memoria</div>', unsafe_allow_html=True)
        st.markdown('<div class="texto-slide">El cerebro de su audiencia no puede leer texto complejo y escuchar su voz al mismo tiempo. <b>Active el interruptor</b> para ver la diferencia.</div><br>', unsafe_allow_html=True)
        
        modo_directivo = st.toggle("Desactivar 'Modo Teleprompter' y aplicar Diseño Directivo")
        
        if not modo_directivo:
            st.error("❌ ESTÁNDAR POBRE: La audiencia leerá esto y dejará de escucharlo.")
            st.markdown("""
            <div style="background-color: white; padding: 20px; border: 1px solid #ccc;">
                <h3 style="color: black;">Situación del Proyecto</h3>
                <ul>
                    <li>El análisis indica desviación en tiempos de ciclo.</li>
                    <li>La alternativa A cuesta $15k pero demora 2 meses.</li>
                    <li>La alternativa B cuesta $25k con disponibilidad inmediata.</li>
                    <li>Recomendamos la alternativa B para evitar detención ($50k diarios).</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.success("✅ ESTÁNDAR ICI: El mensaje es claro, el orador domina el relato.")
            st.markdown("""
            <div style="background-color: white; padding: 20px; border: 1px solid #1E3A8A; border-left: 10px solid #1E3A8A;">
                <h2 style="color: #1E3A8A; margin-bottom: 5px;">🚨 Riesgo Crítico en Línea 2</h2>
                <h3 style="color: #333; margin-top: 0;">Aprobación requerida: $25k para repuesto inmediato. Evita pérdida de $50k/día.</h3>
            </div>
            """, unsafe_allow_html=True)
            st.image("https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80", caption="El expositor entrega el detalle, la pantalla ancla el mensaje central.", use_container_width=True)

    elif slide == "2. Simulador de Empatía":
        st.markdown('<div class="titulo-slide">Simulador: Traduciendo el dato a la audiencia</div>', unsafe_allow_html=True)
        st.markdown('<div class="texto-slide"><b>Problema Base:</b> "Falla en el motor principal de la cinta transportadora."<br>Seleccione a quién le presentará este problema para ver cómo debe cambiar su mensaje:</div><br>', unsafe_allow_html=True)
        
        audiencia = st.selectbox("Seleccione su Audiencia (Tomador de decisión):", ["-- Seleccione --", "1. Jefe de Turno (Operaciones)", "2. Gerente de Finanzas (Administración)", "3. Gerente General (Estrategia)"])
        
        if audiencia == "1. Jefe de Turno (Operaciones)":
            st.info("Foco de esta audiencia: Continuidad operativa y seguridad en terreno.")
            st.markdown('<div class="destacado"><b>Mensaje Directivo:</b> "Necesitamos aislar el área del motor y asignar una cuadrilla mecánica por 4 horas para reemplazar el rodamiento."</div>', unsafe_allow_html=True)
            st.image("https://images.unsplash.com/photo-1504917595217-d4dc5ebe6122?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80", use_container_width=True)
            
        elif audiencia == "2. Gerente de Finanzas (Administración)":
            st.warning("Foco de esta audiencia: Presupuesto, OPEX y flujo de caja.")
            st.markdown('<div class="destacado"><b>Mensaje Directivo:</b> "Requiero liberar $8,500 USD urgentes para un repuesto crítico, evitando pagar penalizaciones por retraso en producción."</div>', unsafe_allow_html=True)
            st.image("https://images.unsplash.com/photo-1554224155-8d04cb21cd6c?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80", use_container_width=True)
            
        elif audiencia == "3. Gerente General (Estrategia)":
            st.success("Foco de esta audiencia: Cumplimiento de metas anuales y riesgo global.")
            st.markdown('<div class="destacado"><b>Mensaje Directivo:</b> "Para asegurar la meta del mes, debemos migrar a monitoreo predictivo ($50k CAPEX) eliminando detenciones no programadas."</div>', unsafe_allow_html=True)
            st.image("https://images.unsplash.com/photo-1551288049-bebda4e38f71?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80", use_container_width=True)

    elif slide == "3. Fases y 7 Pasos":
        st.markdown('<div class="titulo-slide">Los 7 Pasos: De la Estrategia al Diseño</div>', unsafe_allow_html=True)
        st.markdown('<div class="texto-slide">La secuencia innegociable antes de abrir el software de presentaciones.</div><br>', unsafe_allow_html=True)

        col1, col2 = st.columns(2)

        with col1:
            st.info("🎯 FASE 1: ESTRATEGIA Y MENSAJE")
            st.markdown("""
            <div style="font-size: 1.2rem; line-height: 1.6;">
            <b>1. Objetivo y Audiencia:</b> ¿Qué decisión busco? ¿Quién la toma?<br>
            <b>2. Adaptación:</b> Ajuste el nivel técnico y la jerga.<br>
            <b>3. Mensaje Central:</b> Defina el titular directivo.<br>
            <b>4. Tiempo:</b> Ensaye rigurosamente con cronómetro.
            </div>
            """, unsafe_allow_html=True)
            st.image("https://images.unsplash.com/photo-1552664730-d307ca884978?ixlib=rb-4.0.3&auto=format&fit=crop&w=500&q=80", caption="Análisis estratégico inicial", use_container_width=True)

        with col2:
            st.warning("🏗️ FASE 2: ESTRUCTURA (STORYBOARD)")
            st.markdown("""
            <div style="font-size: 1.2rem; line-height: 1.6;">
            <b>5. Ideas Ancla:</b> Seleccione solo la evidencia estrictamente necesaria.<br>
            <b>6. Estructura:</b> Ordene el flujo narrativo (Contexto -> Evidencia -> Solución).
            </div>
            """, unsafe_allow_html=True)
            st.image("https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?ixlib=rb-4.0.3&auto=format&fit=crop&w=500&q=80", caption="Creación del Guion Gráfico", use_container_width=True)

        st.error("🎨 FASE 3: DISEÑO VISUAL")
        st.markdown('<div style="font-size: 1.2rem; line-height: 1.6;"><b>7. Diapositivas:</b> Recién ahora construya las láminas, aplicando contraste, jerarquía y atención dirigida.</div>', unsafe_allow_html=True)

    elif slide == "4. El Arco Narrativo":
        st.markdown('<div class="titulo-slide">El Storytelling como herramienta directiva</div>', unsafe_allow_html=True)
        
        col_a, col_b, col_c = st.columns(3)
        with col_a:
            st.markdown('<div style="background-color: #F3F4F6; padding: 20px; border-radius: 10px; height: 350px;"><h3>1. Introducción<br>(El Gancho)</h3><p class="texto-slide">Conecte con el "dolor" operativo de inmediato. Entregue el mensaje clave de frente.</p></div>', unsafe_allow_html=True)
        with col_b:
            st.markdown('<div style="background-color: #EFF6FF; padding: 20px; border-radius: 10px; height: 350px;"><h3>2. Desarrollo<br>(La Evidencia)</h3><p class="texto-slide">Despliegue sus gráficos y análisis que validan científicamente su propuesta.</p></div>', unsafe_allow_html=True)
        with col_c:
            st.markdown('<div style="background-color: #FEF2F2; padding: 20px; border-radius: 10px; height: 350px;"><h3>3. Conclusión<br>(El Cierre)</h3><p class="texto-slide">Refuerce el impacto y establezca un llamado a la acción inconfundible (aprobación).</p></div>', unsafe_allow_html=True)
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
