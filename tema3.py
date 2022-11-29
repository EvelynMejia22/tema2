import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

walmart_data = pd.read_csv('Superstore.csv')

st.title("WALMART USA ANALYSIS :us:")
st.subheader("By: Evelyn Mejía Jiménez_A01652115")
st.write("Con este análsis, se espera predecir las ventas de productos de línea blanca en el noroeste de los Estados Unidos.")
#Histograma
st.subheader("Ship Mode en cada categoría")
st.write("La siguiente gráfica tiene como objetivo mostrar las categorías de venta de línea blanca que se tiene en Estados Unidos y el modo de embarque dentro de estas ")
st.plotly_chart(px.histogram(walmart_data, x="Category",color="Ship Mode",hover_name='Category'))
st.markdown("___")
#Gráfico de barras
st.subheader("Cantidad vendida por estado")
st.write("La siguiente gráfica tiene como objetivo mostrar las cantidades vendidas por estado.")
st.plotly_chart(px.bar(walmart_data, x='State', y='Quantity'))
st.markdown("___")
#Gráfico de pastel
st.subheader("Ventas por categoría")
st.write("La siguiente gráfica tiene como objetivo mostrar las ventas por categoría")
st.plotly_chart(px.pie(walmart_data, values='Sales', names='Category'))
