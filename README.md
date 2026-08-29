# Proyecto_7
# Análisis exploratorio de datos de anuncios de venta de coches

## Descripción del Proyecto
Esta aplicación web interactiva está construida utilizando **Streamlit**, **Pandas** y **Plotly Express**. Su propósito principal es facilitar el análisis visual y la exploración del conjunto de datos de anuncios de venta de vehículos (`vehicles_us.csv`), donde los usuarios podrán visualizar de forma dinámica la distribución y correlaciones entre el kilometraje (odómetro) y el precio.

## Funcionalidades
- **Visualización mediante casillas de verificación**:
  - **Construir un histograma**: Permite analizar la distribución de frecuencias de la columna `odometer` (kilometraje de los vehículos).
  - **Construir un gráfico de dispersión**: Muestra la relación entre las variables `odometer` y `price` para identificar patrones de precio según el kilometraje transcurrido.
- **Gráficos interactivos**: Generados con Plotly Express, lo que permite hacer zoom, desplazar el cursor sobre los datos y descargar las visualizaciones.