import streamlit as st
import random
import time

# --- INTERFAZ (Las "preguntas") ---
st.title("🦸‍♂️ Generador de Superhéroes Pro")
st.write("Configura tu personaje y el backend calculará tu poder.")

nombre_real = st.text_input("¿Cómo te llamas?", "Julian")
color = st.color_picker("Elige el color de tu traje", "#FF0000")
tipo_poder = st.selectbox("Elige tu origen:", ["Mutante", "Tecnológico", "Místico", "Alien"])
nivel_energia = st.slider("Nivel de energía inicial:", 0, 100, 50)

# --- BACKEND (La lógica que corre al tocar el botón) ---
if st.button("¡Generar Héroe!"):
    with st.spinner('Calculando ADN heroico...'):
        time.sleep(1.5)  # Simulamos un proceso pesado

        # Lógica aleatoria "nada que ver con cohetes"
        adjetivos = ["Increíble", "Radiante", "Sónico", "Cibernético"]
        heroe_nombre = f"{random.choice(adjetivos)} {nombre_real}"

        poder_final = nivel_energia * random.uniform(1.1, 2.0)

    # --- RESULTADO (Lo que le mostramos al usuario) ---
    st.subheader(f"¡Tu nombre es: {heroe_nombre}!")
    st.markdown(f"Tu origen **{tipo_poder}** te da una fuerza de: `{poder_final:.2f} GigaWatts`")

    # Mostramos un gráfico simple de "Potencial"
    st.bar_chart([nivel_energia, poder_final])
    st.balloons()