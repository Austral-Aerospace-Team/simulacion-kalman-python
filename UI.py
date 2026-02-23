import streamlit as st
from src.Simulators.NoiseSimulator import NoiseSimulator
from src.Simulators.KalmanSimulator import KalmanSimulator
from src.Simulators.KalmanLR import KalmanLR
from src.Initializer import Initializer
from src.DataReader import DataReader

st.set_page_config(layout='wide')

if 'ejecutado' not in st.session_state:
    st.session_state.ejecutado = False
    st.session_state.datos_simu = None

st.title("Bienvenido a la simulacion!")
st.write("Veremos como el filtro de kalman actua en lecturas ruidosas del cohete volando")

st.markdown("### Defini el intervalo de la simulacion")

intervalo = st.slider("(Recorda que el apogeo es al segundo 9.955)", min_value=0.0, max_value=92.0, value=(0.0,20.0), format="%.3f")
#endTime = st.number_input("(Recorda que termina a los 92 segundos)",min_value=0.0, max_value=92.0, value= 92.0, format="%.3f")
startTime, endTime = intervalo

st.markdown("### Definamos los desvios de tus sensores y el modelo")
b,a,k = st.columns([1,1,1])
with b:
    desvio_baro = st.number_input("Desvío del barometro: ",value=10.0, format="%.3f")
with a:
    desvio_acel = st.number_input("Desvío del acelerómetro: ",value=3.0, format="%.3f")
with k:
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

# --- Lógica del Botón ---
if st.button("Empezar simulación"):
    dataReader = DataReader("resources/prueba_simu.csv")
    tiempos, altitudes, velocidades, aceleraciones, iniciales = dataReader.read(startTime, endTime)

    initializer = Initializer(desvio_baro=desvio_baro, desvio_acel=desvio_acel, desvio_modelo=desvio_modelo,
                              iniciales=iniciales)
    baro, acel, kalman = initializer.instances()

    # Guardamos los objetos necesarios para simular
    st.session_state.ejecutado = True
    st.session_state.sim_params = (baro, acel, kalman, tiempos, altitudes, velocidades, aceleraciones)

# --- Mostrar resultados (Fuera del if st.button) ---
if st.session_state.ejecutado:
    baro, acel, kalman, tiempos, altitudes, velocidades, aceleraciones = st.session_state.sim_params

    if not st.session_state.kalman:
        simulator = NoiseSimulator()
        figures = simulator.simulate(baro, acel, kalman, tiempos, altitudes, velocidades, aceleraciones)
        for f in figures:
            st.pyplot(f)
    else:
        simulator = KalmanLR()  # type: ignore
        col_grafico, col_controles = st.columns([3, 1])

        with col_controles:
            st.markdown("### Ver líneas")
            v_real = st.checkbox("Altura Real", value=True)
            v_kalman = st.checkbox("Altura Kalman", value=True)
            v_predicha = st.checkbox("Altura Predicha", value=True)
            v_sensada = st.checkbox("Altura Sensada", value=True)

        with col_grafico:
            figures = simulator.simulate(baro, acel, kalman, tiempos, altitudes, velocidades, aceleraciones)
            ax = figures[0].axes[0]

            # NOTA IMPORTANTE: Usamos etiquetas para encontrar y borrar líneas
            # Esto evita el error de índices que cambian al borrar
            lineas_a_borrar = []
            if not v_real: lineas_a_borrar.append("Altura Real")
            if not v_kalman: lineas_a_borrar.append("Altura Kalman")
            if not v_predicha: lineas_a_borrar.append("Altura Predicha")
            if not v_sensada: lineas_a_borrar.append("Altura Sensada")

            for line in ax.lines[:]:  # Copia de la lista para iterar seguro
                if line.get_label() in lineas_a_borrar:
                    line.remove()

            ax.legend()
            for f in figures:
                st.pyplot(f)




