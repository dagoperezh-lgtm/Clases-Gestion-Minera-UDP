import streamlit as st

# ==============================================================================
# Cimport streamlit as st

# ==============================================================================
# CONFIGURACIÓN GENERAL Y ESTILOS CORPORATIVOS
# ==============================================================================
st.set_page_config(page_title="Gestión Minera UDP", layout="wide", initial_sidebar_state="expanded")

# CSS Global: Patrón corporativo (Blanco, Azul, Celeste) y Slides de Impacto
st.markdown("""
    <style>
    /* Tipografía y fondos generales */
    .stApp { background-color: #FFFFFF; }
    
    /* Títulos estándar corporativos */
    .titulo-slide { font-size: 3rem; color: #003366; font-weight: bold; margin-bottom: 15px; line-height: 1.2; border-bottom: 3px solid #00A4E4; padding-bottom: 10px;}
    .texto-slide { font-size: 1.6rem; color: #333333; line-height: 1.5;}
    
    /* COMPONENTE DE IMPACTO: Slide exclusiva para mensajes explícitos */
    .slide-mensaje { 
        background-color: #003366; 
        padding: 80px 40px; 
        text-align: center; 
        border-radius: 8px; 
        margin: 40px 0;
        box-shadow: 0 10px 20px rgba(0,0,0,0.2);
        border-bottom: 8px solid #00A4E4; /* Acento corporativo trasladado al borde */
    }
    .slide-mensaje h1 { font-size: 4.5rem; color: #FFFFFF; font-weight: 900; line-height: 1.2; margin: 0; text-transform: uppercase;}
    .slide-mensaje p { font-size: 1.8rem; color: #FFFFFF; margin-top: 20px; font-weight: 400; opacity: 0.95;} /* Texto en blanco puro para contraste perfecto */
    
    /* COMPONENTE: El Salón de la Infamia (Ejemplos de mala práctica) */
    .bad-slide { background-color: #F8F9FA; border: 2px dashed #DC2626; padding: 20px; font-size: 1.6rem; color: #666666;}
    
    /* Destacados corporativos */
    .destacado-corp { background-color: #F0F8FF; border-left: 8px solid #00A4E4; padding: 20px; font-size: 1.6rem; color: #003366;}
    </style>
""", unsafe_allow_html=True)

st.sidebar.title("Índice de la Cátedra")
st.sidebar.info("💡 Tip: Haz clic en la 'X' para ocultar esta barra y ganar espacio visual.")

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
# INICIO MÓDULO 01: LO QUE NO SE DEBE HACER (EL PROBLEMA)
# ==============================================================================
elif modulo == "01. El Paradigma del Esfuerzo":
    st.write("### Navegación Dinámica")
    slide = st.radio("Seleccione la Diapositiva:", ["1. El Salón de la Infamia", "2. La Sopa de Números", "3. La Regla de Oro"], horizontal=True, label_visibility="collapsed")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    if slide == "1. El Salón de la Infamia":
        st.markdown('<div class="titulo-slide">Lo que NO se debe hacer: Contraste y Saturación</div>', unsafe_allow_html=True)
        st.markdown('<div class="texto-slide">Las primeras láminas de su presentación no pueden ser un muro de texto o usar colores que impidan la lectura. Observe estos errores clásicos extraídos de presentaciones reales de ingeniería:</div><br>', unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown('<div class="bad-slide" style="background-color: #000080; color: #000000; font-weight: bold; text-align: center;">❌ ERROR 1: PÉSIMO CONTRASTE<br><br>Letra oscura sobre fondo oscuro. La audiencia se rinde a los 5 segundos intentando descifrar esto.</div>', unsafe_allow_html=True)
        with col2:
            st.markdown('<div class="bad-slide" style="background-color: #FFFF00; color: #FFFFFF; font-weight: bold; text-align: center;">❌ ERROR 2: COLORES CHILLONES<br><br>Letra blanca sobre fondo amarillo brillante. Destruye la vista del directorio e impide la concentración.</div>', unsafe_allow_html=True)
            
        st.markdown('<br><div class="destacado-corp">✅ <b>EL ESTÁNDAR CORPORATIVO:</b> Use siempre fondos claros (blanco puro o gris muy suave) con letras oscuras (azul corporativo, gris oscuro o negro) para maximizar la legibilidad en cualquier proyector.</div>', unsafe_allow_html=True)

    elif slide == "2. La Sopa de Números":
        st.markdown('<div class="titulo-slide">Lo que NO se debe hacer: Tablas sin procesar</div>', unsafe_allow_html=True)
        st.markdown('<div class="texto-slide">Pegar una planilla de Excel directamente en la lámina es transferirle su trabajo de análisis a la audiencia.</div><br>', unsafe_allow_html=True)
        
        st.markdown("""
        <div class="bad-slide" style="text-align: center;">
            <h4 style="color: #666; margin-bottom: 5px;">❌ ERROR 3: LA TABLA BRUTA</h4>
            <p style="font-size: 1.2rem; margin-top: 0;">(Imagine proyectar esto a 5 metros de distancia en una sala de reuniones)</p>
            <table style="width:80%; margin: 0 auto; font-size: 0.8rem; border: 1px solid #999; text-align: center; background-color: white; color: black;">
                <tr style="background-color: #ccc;"><th>ID_Eq</th><th>Var_X1</th><th>Var_X2</th><th>Temp</th><th>Presión</th><th>Flujo</th><th>Estado</th><th>Costo</th></tr>
                <tr><td>001</td><td>45.2</td><td>0.01</td><td>99°C</td><td>1.2</td><td>123</td><td>OK</td><td>$12k</td></tr>
                <tr><td>002</td><td>44.8</td><td>0.02</td><td>98°C</td><td>1.1</td><td>124</td><td>OK</td><td>$11k</td></tr>
                <tr><td>003</td><td>46.1</td><td>0.01</td><td>97°C</td><td>1.3</td><td>121</td><td>OK</td><td>$13k</td></tr>
                <tr><td>004</td><td>49.9</td><td>0.05</td><td>105°C</td><td>1.8</td><td>90</td><td>Falla</td><td>$45k</td></tr>
                <tr><td>005</td><td>45.0</td><td>0.01</td><td>98°C</td><td>1.2</td><td>122</td><td>OK</td><td>$12k</td></tr>
            </table>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown('<br><div class="destacado-corp">✅ <b>EL ESTÁNDAR CORPORATIVO:</b> Si un número no apoya directamente su mensaje central, elimínelo de la pantalla. Use gráficos de tendencia o destaque únicamente la anomalía (Ej: El Equipo 004).</div>', unsafe_allow_html=True)

    elif slide == "3. La Regla de Oro":
        # Aquí inyectamos el componente de impacto masivo
        st.markdown("""
        <div class="slide-mensaje">
            <h1>USE MENSAJES EN LUGAR DE TÍTULOS</h1>
            <p>El título solo informa. El mensaje le dice a la audiencia qué decisión debe tomar.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown('<div class="texto-slide" style="text-align: center;">Nunca deje que la audiencia saque sus propias conclusiones mirando sus datos.<br><b>Es su deber como ingeniero dirigir el análisis.</b></div>', unsafe_allow_html=True)
# ==============================================================================
# FIN MÓDULO 01
# ==============================================================================
# ==============================================================================
# INICIO MÓDULO 02: LA AUDIENCIA ES EL CENTRO
# ==============================================================================
elif modulo == "02. La Audiencia es el Centro":
    st.write("### Navegación Dinámica")
    slide = st.radio("Seleccione la Diapositiva:", ["1. El Teleprompter", "2. Simulador Operacional", "3. Regla de Adaptación", "4. Los 7 Pasos", "5. Storytelling"], horizontal=True, label_visibility="collapsed")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    if slide == "1. El Teleprompter":
        st.markdown('<div class="titulo-slide">La pantalla no es su ayuda de memoria</div>', unsafe_allow_html=True)
        st.markdown('<div class="texto-slide">El cerebro de su audiencia no puede leer texto complejo y escuchar su voz al mismo tiempo. <b>Active el interruptor</b> para ver el contraste corporativo.</div><br>', unsafe_allow_html=True)
        
        modo_directivo = st.toggle("Desactivar 'Modo Teleprompter' y aplicar Diseño Directivo")
        
        if not modo_directivo:
            st.error("❌ ESTÁNDAR POBRE: La audiencia leerá esto y dejará de escucharlo.")
            st.markdown("""
            <div class="bad-slide">
                <h3 style="color: black;">Situación de Mantenimiento Q3</h3>
                <ul>
                    <li>El análisis de la falla indica que hay desgaste prematuro.</li>
                    <li>La alternativa A demora 2 meses en llegar.</li>
                    <li>La alternativa B tiene disponibilidad inmediata en bodega central.</li>
                    <li>Recomendamos la alternativa B para evitar que la producción de la planta de molienda se detenga por completo durante la próxima semana.</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.success("✅ ESTÁNDAR CORPORATIVO: El mensaje es claro, el orador domina el relato.")
            st.markdown("""
            <div style="background-color: white; padding: 20px; border: 1px solid #003366; border-left: 10px solid #00A4E4; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
                <h2 style="color: #003366; margin-bottom: 5px;">🚨 Riesgo Inminente en Planta de Molienda</h2>
                <h3 style="color: #333; margin-top: 0;">Requerimos liberar repuesto de Bodega Central hoy para evitar detención total de la línea.</h3>
            </div>
            """, unsafe_allow_html=True)
            st.image("https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80", caption="El expositor entrega el detalle técnico verbalmente, la pantalla ancla el mensaje central.", use_container_width=True)

    elif slide == "2. Simulador Operacional":
        st.markdown('<div class="titulo-slide">Simulador: Traduciendo el dato a la audiencia</div>', unsafe_allow_html=True)
        st.markdown('<div class="texto-slide"><b>Evento Operacional:</b> Falla catastrófica en el sistema de lubricación del Chancador Primario.<br>Seleccione a quién le presentará este evento para ver cómo debe adaptar su mensaje en la industria:</div><br>', unsafe_allow_html=True)
        
        audiencia = st.selectbox("Seleccione su Audiencia (Tomador de decisión):", ["-- Seleccione --", "1. Jefe de Turno (Operaciones)", "2. Superintendente de Mina (Planificación)", "3. Gerencia General / Directorio (Estrategia)"])
        
        if audiencia == "1. Jefe de Turno (Operaciones)":
            st.info("Foco de esta audiencia: Seguridad y maniobra inmediata en terreno.")
            st.markdown('<div class="destacado-corp"><b>Mensaje Directivo:</b> "Aplicar protocolo de bloqueo de energía de inmediato. Requerimos aislar el área del Chancador Primario por 8 horas para el cambio seguro de componentes."</div>', unsafe_allow_html=True)
            
        elif audiencia == "2. Superintendente de Mina (Planificación)":
            st.warning("Foco de esta audiencia: Continuidad operacional y cumplimiento de metas del turno.")
            st.markdown('<div class="destacado-corp"><b>Mensaje Directivo:</b> "El chancador estará detenido por 8 horas. Debemos desviar la flota de CAEX al stock de mineral de baja ley para no detener el ritmo de extracción de la mina."</div>', unsafe_allow_html=True)
            
        elif audiencia == "3. Gerencia General / Directorio (Estrategia)":
            st.success("Foco de esta audiencia: Impacto financiero (VAN, CAPEX, OPEX) y riesgo del negocio.")
            st.markdown('<div class="destacado-corp"><b>Mensaje Directivo:</b> "La detención impactó el plan mensual en 15.000 toneladas de cobre fino. Solicitamos adelantar el CAPEX de $250k para un sistema de lubricación redundante, cuyo VAN es positivo al evitar solo una detención futura."</div>', unsafe_allow_html=True)

    elif slide == "3. Regla de Adaptación":
        # Componente de Impacto Corporativo
        st.markdown("""
        <div class="slide-mensaje">
            <h1>A AUDIENCIAS DISTINTAS, TRADUCCIONES DISTINTAS</h1>
            <p>El mismo dato técnico tiene diferentes significados dependiendo de la silla que ocupa quien lo mira.</p>
        </div>
        """, unsafe_allow_html=True)
        st.markdown('<div class="texto-slide" style="text-align: center;">No obligue al Gerente General a pensar como un Jefe de Turno. <b>Traduzca la ingeniería a impacto en el negocio.</b></div>', unsafe_allow_html=True)

    elif slide == "4. Los 7 Pasos":
        st.markdown('<div class="titulo-slide">Los 7 Pasos: La Metodología ICI</div>', unsafe_allow_html=True)
        st.markdown('<div class="texto-slide">La secuencia innegociable antes de abrir su software de presentaciones.</div><br>', unsafe_allow_html=True)

        col1, col2 = st.columns(2)

        with col1:
            st.markdown('<div class="destacado-corp" style="margin-bottom: 15px;"><b>FASE 1: ESTRATEGIA Y MENSAJE</b><br><br>'
            '<span style="font-size: 1.2rem; line-height: 1.5;">'
            '<b>1. Audiencia:</b> ¿A quién le presento y qué nivel técnico tiene?<br>'
            '<b>2. Adaptación:</b> Ajuste la profundidad y la jerga a esa audiencia.<br>'
            '<b>3. Mensaje Central:</b> Defina la idea ancla (Si el proyector falla, esto es lo que deben recordar).<br>'
            '<b>4. Tiempo:</b> Ensaye con cronómetro. El tiempo directivo es oro.'
            '</span></div>', unsafe_allow_html=True)

        with col2:
            st.markdown('<div class="destacado-corp" style="border-left-color: #003366; margin-bottom: 15px;"><b>FASE 2: ESTRUCTURA (STORYBOARD)</b><br><br>'
            '<span style="font-size: 1.2rem; line-height: 1.5;">'
            '<b>5. Ideas Ancla:</b> Filtre. Seleccione solo la evidencia que valida su mensaje.<br>'
            '<b>6. Estructura:</b> Ordene el flujo narrativo lógicamente.'
            '</span></div>', unsafe_allow_html=True)

        st.error("🎨 FASE 3: DISEÑO VISUAL")
        st.markdown('<div style="font-size: 1.2rem; background-color: #FEF2F2; padding: 15px; border-radius: 5px; color: #991B1B; border-left: 8px solid #DC2626;"><b>7. Diapositivas:</b> Recién ahora abra el programa y construya las láminas, aplicando contraste corporativo y atención dirigida.</div>', unsafe_allow_html=True)

    elif slide == "5. Storytelling":
        st.markdown('<div class="titulo-slide">El Arco Narrativo de la Ingeniería</div>', unsafe_allow_html=True)
        
        col_a, col_b, col_c = st.columns(3)
        with col_a:
            st.markdown('<div style="background-color: #F8F9FA; border-top: 5px solid #00A4E4; padding: 20px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); height: 260px;">'
                        '<h3 style="color: #003366;">1. Introducción<br>(El Gancho)</h3>'
                        '<p style="font-size: 1.2rem; color: #555;">Conecte de inmediato con el problema del negocio o la oportunidad. Plantee su mensaje clave de frente, sin rodeos.</p></div>', unsafe_allow_html=True)
        with col_b:
            st.markdown('<div style="background-color: #F8F9FA; border-top: 5px solid #003366; padding: 20px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); height: 260px;">'
                        '<h3 style="color: #003366;">2. Desarrollo<br>(La Evidencia)</h3>'
                        '<p style="font-size: 1.2rem; color: #555;">Despliegue sus gráficos limpios, análisis de alternativas y validación científica que demuestran que su propuesta es correcta.</p></div>', unsafe_allow_html=True)
        with col_c:
            st.markdown('<div style="background-color: #F0F8FF; border-top: 5px solid #DC2626; padding: 20px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); height: 260px;">'
                        '<h3 style="color: #003366;">3. Conclusión<br>(El Cierre)</h3>'
                        '<p style="font-size: 1.2rem; color: #555;">Refuerce el impacto (qué pasa si no hacemos nada) y establezca un llamado a la acción inconfundible para que el directorio apruebe.</p></div>', unsafe_allow_html=True)

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
    st.write("### Navegación Dinámica")
    slide = st.radio("Seleccione la Diapositiva:", ["1. Preguntas Difíciles", "2. Checklist de Murphy", "3. Mensaje Final"], horizontal=True, label_visibility="collapsed")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    if slide == "1. Preguntas Difíciles":
        st.markdown('<div class="titulo-slide">Manejo Estratégico de la Audiencia</div>', unsafe_allow_html=True)
        st.markdown('<div class="texto-slide">En una defensa técnica, el directorio probará la solidez de sus argumentos. <b>Haga clic en cada escenario</b> para ver la respuesta estratégica:</div><br>', unsafe_allow_html=True)
        
        col1, col2 = st.columns([1, 1.2])
        with col1:
            st.image("https://images.unsplash.com/photo-1556761175-b413da4baf72?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80", caption="El momento de la verdad", use_container_width=True)
        
        with col2:
            with st.expander("🚨 Escenario 1: Le hacen una pregunta que NO sabe (y no debería saber)"):
                st.error("**Estrategia: Honestidad Brutal.**")
                st.write("Nunca invente un dato frente a un comité. Diga: *'Esa variable escapa al alcance de este modelo, pero es un punto crítico. Lo levantaré con el equipo y le enviaré el informe mañana a primera hora.'*")
            
            with st.expander("⚠️ Escenario 2: Le hacen una pregunta que SÍ debería saber, pero olvidó"):
                st.warning("**Estrategia: Ganar Tiempo o Derivar.**")
                st.write("1. **Diferir:** *'Ese es un punto excelente que se cruza con la lámina de CAPEX que veremos en 3 minutos. Lo abordamos ahí.'*\n2. **Rebotar a la audiencia:** Si hay un experto en la sala, valídelo: *'Gerente Pérez, con su experiencia en la planta antigua, ¿cómo veíamos este indicador?'*")
            
            with st.expander("🛡️ Escenario 3: Le hacen una pregunta hostil o fuera de contexto"):
                st.success("**Estrategia: El Puente.**")
                st.write("No confronte. Reconozca y redirija a su mensaje central: *'Entiendo su preocupación por el costo del año pasado, y precisamente por eso el modelo que propongo hoy asegura que no repitamos esa desviación.'*")

    elif slide == "2. Checklist de Murphy":
        st.markdown('<div class="titulo-slide">La Ley de Murphy y la Preparación</div>', unsafe_allow_html=True)
        st.markdown('<div class="texto-slide">Si algo puede salir mal en la presentación de su proyecto final, saldrá mal. El ingeniero ICI no improvisa, mitiga riesgos.</div><br>', unsafe_allow_html=True)
        
        col_a, col_b = st.columns(2)
        with col_a:
            st.markdown('<div class="destacado"><b>Validación Pre-Vuelo (Marque para confirmar)</b></div><br>', unsafe_allow_html=True)
            c1 = st.checkbox("Tengo el archivo en USB, en el correo y en formato PDF (por si se rompen las fuentes).")
            c2 = st.checkbox("Revisé los adaptadores (HDMI/Tipo-C) y el proyector de la sala.")
            c3 = st.checkbox("Tengo impreso un resumen ejecutivo por si se corta la energía.")
            c4 = st.checkbox("Ensayé la presentación con cronómetro.")
            
            if c1 and c2 and c3 and c4:
                st.success("✅ Usted está autorizado para presentar ante el comité.")
        
        with col_b:
            st.image("https://images.unsplash.com/photo-1586771107445-d3ca888129ff?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80", use_container_width=True)

    elif slide == "3. Mensaje Final":
        st.markdown('<div class="titulo-slide" style="text-align: center;">Fin del Paradigma</div>', unsafe_allow_html=True)
        
        st.image("https://images.unsplash.com/photo-1590486803833-ffc4571713df?ixlib=rb-4.0.3&auto=format&fit=crop&w=1600&q=80", use_container_width=True)
        
        st.markdown("""
        <div style="background-color: #1E3A8A; color: white; padding: 40px; text-align: center; border-radius: 10px; margin-top: -50px; position: relative; z-index: 10; width: 80%; margin-left: auto; margin-right: auto; box-shadow: 0 10px 25px rgba(0,0,0,0.2);">
            <h1 style="color: white; margin-bottom: 10px;">Su proyecto vale lo que vale su capacidad de comunicarlo.</h1>
            <p style="font-size: 1.5rem;">Cátedra de Gestión del Negocio Minero - UDP</p>
        </div>
        """, unsafe_allow_html=True)

# ==============================================================================
# FIN MÓDULO 04
# ==============================================================================
