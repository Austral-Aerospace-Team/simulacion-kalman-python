import streamlit as st
import numpy as np


st.title("Bienvenido a la simulacion!")
st.write("Veremos como el filtro de kalman actua en lecturas ruidosas del cohete volando")

st.markdown("### Defini el intervalo de la simulacion")

startTime = st.number_input("(Recorda que el apogeo es al segundo 9.955)", min_value=0.0, max_value=92.0, value=0.0, format="%.3f")
endTime = st.number_input("(Recorda que termina a los 92 segundos)",min_value=0.0, max_value=92.0, value= 92.0, format="%.3f")

st.markdown("### Definamos los desvios de tus sensores y el modelo")
opciones = np.arange(0.0, 30.05, 0.05).tolist()
desvio_baro = st.select_slider("Desvío del barometro: ", options = opciones,value=10.0, format_func=lambda x: f"{x:.3f}")
desvio_acel = st.select_slider("Desvío del acelerómetro: ",options = opciones,value=3.0, format_func=lambda x: f"{x:.3f}")
desvio_modelo = st.select_slider("Desvío del modelo: ", options = opciones,value=3.0, format_func=lambda x: f"{x:.3f}")