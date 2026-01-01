import streamlit as st
from src.Simulators.NoiseSimulator import NoiseSimulator
from src.Simulators.KalmanSimulator import KalmanSimulator
from src.Initializer import Initializer
from src.DataReader import DataReader

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

    if not st.session_state.kalman:
        simulator = NoiseSimulator()
        figures = simulator.simulate(baro,acel,kalman,tiempos, altitudes, velocidades, aceleraciones)
        for f in figures:
            st.pyplot(f)
    else:
        simulator = KalmanSimulator()
        col_grafico, col_controles = st.columns([3, 1])
        with col_controles:
            st.markdown("### Ver líneas")
            # Creamos un checkbox por cada línea y guardamos su estado (True/False)
            ver_real = st.checkbox("Altura Real", value=True)
            ver_kalman = st.checkbox("Altura Kalman", value=True)
            ver_predicha = st.checkbox("Altura Predicha", value=True)
            ver_sensada = st.checkbox("Altura Sensada", value=True)
        with col_grafico:
            figures = simulator.simulate(baro,acel,kalman,tiempos, altitudes, velocidades, aceleraciones)
            axs = figures[0].axes[0]
            if not ver_sensada:
                del axs.lines[3]
            if not ver_predicha:
                del axs.lines[2]
            if not ver_kalman:
                del axs.lines[1]
            if not ver_kalman:
                del axs.lines[0]
            axs.legend()
            for f in figures:
                st.pyplot(f)





