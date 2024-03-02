# Cargamos todas las librerías que ocuparemos en el proyecto:
import pandas as pd
import plotly.express as px
import streamlit as st

# Cargamos el conjunto de datos de anuncios de ventas de coches
car_data = pd.read_csv(
    'vehicles_us.csv')

# Generamos un encabezado
st.header('Cuadro de Mandos de la Aplicación Web')
st.write('Conjunto de datos de anuncios de venta de coches')

# creamos un botón para el histograma
hist_button = st.button('Construir histograma')

if hist_button:  # al hacer clic en el botón histograma
    # escribir un mensaje
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

# crear un botón para el gráfico de dispersión
disp_button = st.button('Construir Gráfico Dispersión')

if disp_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')

    # crear un gráfico de dispersión
    fig = px.scatter(car_data, x="odometer", y="price")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
