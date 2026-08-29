import streamlit as st
import pandas as pd
import plotly.express as px

@st.cache_data
def load_data(path):
    return pd.read_csv(path)

DATA_PATH = 'vehicles_us.csv'
car_data = load_data(DATA_PATH)

# Encabezado de la aplicación
st.header('Análisis exploratorio de datos de una lista de vehículos usados')

# Leer el archivo CSV del conjunto de datos
car_data = pd.read_csv('vehicles_us.csv')

# Casillas de verificación para seleccionar el gráfico
build_histogram = st.checkbox('Construir un histograma')
build_scatter = st.checkbox('Construir un gráfico de dispersión')

# Lógica para construir el histograma si la casilla está seleccionada
if build_histogram:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    # Crear un histograma utilizando la configuración personalizada con títulos y etiquetas
    fig_hist = px.histogram(
        car_data,
        x="odometer",
        title="Distribución del kilometraje de los vehículos",
        labels={"odometer": "Kilometraje (millas)"}
    )
    # Mostrar el gráfico interactivo en Streamlit
    st.plotly_chart(fig_hist, use_container_width=True)

# Lógica para construir el gráfico de dispersión si la casilla está seleccionada
if build_scatter:
    st.write('Creación de un gráfico de dispersión (kilometraje vs. precio)')
    # Crear un gráfico de dispersión utilizando la configuración personalizada con títulos y etiquetas
    fig_scatter = px.scatter(
        car_data,
        x="odometer",
        y="price",
        title="Relación entre el kilometraje y el precio",
        labels={"odometer": "Kilometraje (millas)", "price": "Precio (USD)"}
    )
    # Mostrar el gráfico interactivo en Streamlit
    st.plotly_chart(fig_scatter, use_container_width=True)
