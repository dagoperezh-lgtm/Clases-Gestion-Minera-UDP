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
    "02. La Audiencia es el Centro",
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
    st.write("### Navegación Dinámica")
    slide = st.radio("Seleccione la Diapositiva:", ["1. Títulos vs Mensajes", "2. Atención Dirigida (Gráficos)", "3. De la Tabla al Scorecard"], horizontal=True, label_visibility="collapsed")
    
    st.markdown("<br>", unsafe_allow_html=True)
    import pandas as pd
    
    if slide == "1. Títulos vs Mensajes":
        st.markdown('<div class="titulo-slide">El Título informa. El Mensaje DIRIGE.</div>', unsafe_allow_html=True)
        st.markdown('<div class="texto-slide">La audiencia no debería tener que adivinar la conclusión mirando el gráfico. Su encabezado debe hacer el trabajo pesado.</div><br>', unsafe_allow_html=True)
        
        col1, col2 = st.columns([1, 1])
        with col1:
            st.image("https://images.unsplash.com/photo-1551288049-bebda4e38f71?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80", caption="Análisis en sala de control", use_container_width=True)
        
        with col2:
            st.markdown('<div class="alerta"><b>❌ El Título Inerte (Estándar Bajo):</b><br>"Resultados Operacionales y Costos Q1".<br><span style="font-size: 1.1rem;">(Obliga a la audiencia a buscar el problema entre los datos, agotando su atención).</span></div><br>', unsafe_allow_html=True)
            
            st.markdown('<div class="destacado"><b>✅ El Mensaje Directivo (Estándar ICI):</b><br>"🚨 El sobrecosto en el Área de Molienda compromete el margen anual: Se requiere ajuste de plan hoy."<br><span style="font-size: 1.1rem;">(El gráfico que acompañe esto solo sirve como evidencia innegable de esta afirmación).</span></div>', unsafe_allow_html=True)

    elif slide == "2. Atención Dirigida (Gráficos)":
        st.markdown('<div class="titulo-slide">Atención Dirigida: El gráfico no es adorno, es evidencia</div>', unsafe_allow_html=True)
        st.markdown('<div class="texto-slide">No todos los datos valen lo mismo. <b>Use el color estratégicamente</b> para guiar el ojo del directorio hacia la anomalía en un segundo.</div><br>', unsafe_allow_html=True)
        
        modo_grafico = st.toggle("Aplicar Atención Dirigida (Apagar ruido visual)")
        
        # Datos de ejemplo
        datos_costos = pd.DataFrame({
            "Área": ["Extracción", "Chancado", "Molienda", "Flotación", "Relaves"],
            "Desviación (%)": [2, -1, 18, 3, 1]
        }).set_index("Área")
        
        col_x, col_y = st.columns([1.5, 1])
        
        with col_x:
            if not modo_grafico:
                # Gráfico arcoíris (mal diseño)
                st.error("❌ Sopa Visual: Los colores no significan nada, el cerebro se confunde.")
                st.bar_chart(datos_costos, color=["#3b82f6"]) # Color genérico
            else:
                # Gráfico directivo (buen diseño)
                st.success("✅ Atención Dirigida: El gris neutraliza, el rojo acentúa el problema.")
                # Simulamos la atención dirigida pintando solo el problema
                st.markdown("""
                <div style="background-color: white; padding: 20px; border: 1px solid #ccc;">
                    <h4 style="color: #333; text-align: center;">Desviación de Costos por Área Operativa (%)</h4>
                    <div style="display: flex; align-items: flex-end; justify-content: space-around; height: 200px; padding-top: 20px;">
                        <div style="width: 15%; background-color: #D1D5DB; height: 11%; text-align: center; color: black;">2%</div>
                        <div style="width: 15%; background-color: #D1D5DB; height: 5%; text-align: center; color: black;">-1%</div>
                        <div style="width: 15%; background-color: #DC2626; height: 100%; text-align: center; color: white; font-weight: bold;">18%</div>
                        <div style="width: 15%; background-color: #D1D5DB; height: 16%; text-align: center; color: black;">3%</div>
                        <div style="width: 15%; background-color: #D1D5DB; height: 5%; text-align: center; color: black;">1%</div>
                    </div>
                    <div style="display: flex; justify-content: space-around; margin-top: 10px; font-weight: bold; font-size: 0.9rem; color: #555;">
                        <div style="width: 15%; text-align: center;">Extracción</div>
                        <div style="width: 15%; text-align: center;">Chancado</div>
                        <div style="width: 15%; text-align: center; color: #DC2626;">Molienda</div>
                        <div style="width: 15%; text-align: center;">Flotación</div>
                        <div style="width: 15%; text-align: center;">Relaves</div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
        
        with col_y:
            st.info("💡 **Regla de Diseño ICI:**\n\nSi su mensaje habla del Área de Molienda, molienda debe ser el único elemento visualmente destacado. Todo lo demás es contexto (gris).")

    elif slide == "3. De la Tabla al Scorecard":
        st.markdown('<div class="titulo-slide">Minimalismo: Evite la "Sopa de Números"</div>', unsafe_allow_html=True)
        st.markdown('<div class="texto-slide">Pegar una planilla de Excel en la presentación es abdicar de su rol como ingeniero. Usted debe procesar el dato y entregar el *Insight*. Active el interruptor.</div><br>', unsafe_allow_html=True)
        
        modo_tabla = st.toggle("Transformar Excel a Scorecard Ejecutivo")
        
        if not modo_tabla:
            st.error("❌ El error clásico: Copiar y pegar el Excel.")
            df_bruto = pd.DataFrame({
                "ID_Equipo": ["M-01", "M-02", "C-01", "C-02"],
                "Tipo": ["Molino SAG", "Molino Bolas", "Chancador", "Correa"],
                "Temp_Motor": [75.2, 78.1, 105.4, 65.0],
                "Vibracion_mm": [2.1, 2.3, 8.9, 1.5],
                "Horas_Uso": [4500, 4600, 4200, 1200],
                "Estado": ["OK", "OK", "Falla Inminente", "OK"]
            })
            st.dataframe(df_bruto, use_container_width=True)
        else:
            st.success("✅ Scorecard: Rápido, visual y enfocado en la excepción.")
            st.markdown("""
            <div style="display: flex; justify-content: space-between;">
                <div style="width: 30%; background-color: #F0FDF4; border: 1px solid #16A34A; border-radius: 10px; padding: 20px; text-align: center;">
                    <h2 style="margin:0; color: #16A34A;">🟢 Molinos</h2>
                    <p style="font-size: 1.2rem; color: #333;">Parámetros Normales</p>
                </div>
                <div style="width: 30%; background-color: #FEF2F2; border: 2px solid #DC2626; border-radius: 10px; padding: 20px; text-align: center; box-shadow: 0 4px 6px rgba(220, 38, 38, 0.3);">
                    <h2 style="margin:0; color: #DC2626;">🔴 Chancador C-01</h2>
                    <p style="font-size: 1.2rem; color: #333; font-weight: bold;">Vibración Crítica (8.9mm)</p>
                </div>
                <div style="width: 30%; background-color: #F0FDF4; border: 1px solid #16A34A; border-radius: 10px; padding: 20px; text-align: center;">
                    <h2 style="margin:0; color: #16A34A;">🟢 Correas</h2>
                    <p style="font-size: 1.2rem; color: #333;">Parámetros Normales</p>
                </div>
            </div>
            """, unsafe_allow_html=True)
            st.markdown("<br><p class='texto-slide'>El directorio solo necesita ver el cuadro central rojo para saber dónde asignar los recursos hoy.</p>", unsafe_allow_html=True)

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
