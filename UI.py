import matplotlib.pyplot as plt
import streamlit as st
import numpy as np
from Initializer import Initializer
from DataReader import DataReader

st.title("Bienvenido a la simulacion!")
st.write("Veremos como el filtro de kalman actua en lecturas ruidosas del cohete volando")

st.markdown("### Defini el intervalo de la simulacion")

intervalo = st.slider("(Recorda que el apogeo es al segundo 9.955)", min_value=0.0, max_value=92.0, value=(0.0,20.0), format="%.3f")
#endTime = st.number_input("(Recorda que termina a los 92 segundos)",min_value=0.0, max_value=92.0, value= 92.0, format="%.3f")
startTime, endTime = intervalo

st.markdown("### Definamos los desvios de tus sensores y el modelo")
desvio_baro = st.number_input("Desvío del barometro: ",value=10.0, format="%.3f")
desvio_acel = st.number_input("Desvío del acelerómetro: ",value=3.0, format="%.3f")
desvio_modelo = st.number_input("Desvío del modelo: ", value=3.0, format="%.3f")

# 1. Inicializamos el estado solo UNA vez al principio
if 'kalman' not in st.session_state:
    st.session_state.kalman = True

# 2. Definimos el texto según lo que hay en memoria
texto = "Kalman Activo" if st.session_state.kalman else "Kalman Desactivado"

# 3. Usamos 'key' para que Streamlit maneje la variable solo
st.toggle(texto, key='kalman')

# 4. Lógica de tu simulación
if st.session_state.kalman:
    st.success("🚀 El filtro está funcionando")
else:
    st.error("⚠️ Datos crudos (ruido activado)")

if st.button("Empezar simulación"):
    dataReader = DataReader("resources/prueba_simu.csv")
    tiempos, altitudes, velocidades,aceleraciones, iniciales = dataReader.read(startTime,endTime)


    initializer = Initializer(desvio_baro=desvio_baro, desvio_acel= desvio_acel, desvio_modelo= desvio_modelo, iniciales=iniciales)
    baro, acel, kalman = initializer.instances()

    if True:
        bar_prueba = []
        acel_prueba = []
        for s, v, a in zip(altitudes, velocidades, aceleraciones):
            bar_prueba.append(baro.lectura(s, v, a))
            acel_prueba.append(acel.lectura(a))

        altFig, alt = plt.subplots()
        alt.plot(tiempos, altitudes, label="Trayectoria Real")
        alt.plot(tiempos, bar_prueba, label="Trayectoria Sensada", color="red", linestyle="dotted")
        alt.set_xlabel("Tiempo (s)")
        alt.set_ylabel("Altitud (m)")
        alt.legend()
        alt.grid(True)
        st.pyplot(altFig)

        accFig, acc = plt.subplots()
        acc.plot(tiempos, aceleraciones, label="Aceleraciones Reales")
        acc.plot(tiempos,acel_prueba, label="Aceleraciones Sensadas")
        acc.set_xlabel("Tiempo (s)")
        acc.set_ylabel("Aceleración (m/s^2)")
        acc.legend()
        acc.grid(True)
        st.pyplot(accFig)



