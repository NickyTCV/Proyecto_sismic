import streamlit as st
import pandas as pd
import gdown

import pip
pip.main(["install", "openpyxl"])
pip.main(["install", "pandas"])
import plotly.figure_factory as ff
pip.main(["install", "matplotlib"])
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.figure_factory as ff
import scipy

with st.sidebar: 
    st.markdown("###")
    st.sidebar.header('Programación Avanzada')
    selected = option_menu(
        menu_title = 'Menú',
        options = ['Inicio', 'Reporte','Equipo'],
        icons = ['house', 'book', 'book','people'],
        menu_icon='cast',
        default_index = 0,
    )

if selected == 'Inicio':
  st.markdown("<h1 style ='text-align: center'>Titulo:</h1>", unsafe_allow_html=True)
  st.markdown("---")
  st.header("Dataset")

st.title("Catálogo sísmico 1960-2021")
df_cat = pd.read_excel(r'https://www.datosabiertos.gob.pe/sites/default/files/Catalogo1960_2021.xlsx', header= 0) 
st.write(df_cat)
st.header("Sismos ocurridos en el Perú para el período 1960-2021")
st.write("Esta base de datos sísmicos contiene todos los parámetros que caracterizan a un sismo, calculados en las mismas condiciones a fin de constituirse como una base homogénea: fecha, hora, latitud, longitud, profundidad y magnitud. En este dataset se podrá encontrar el Catálogo de Sismos Instrumentales para el período de 1960 – 2021.")

option = st.selectbox('¿Si desea más información puede contactarnos mediante las siguientes opciones?',('Email', 'Teléfono', 'Whatsapp', 'Instagram'))
st.write('Seleccionó:', option)

st.header("Histogramas de datos sísmicos:")
for i in range(5,7):
    fig = px.histogram(df_cat, df_cat.columns[i])
    st.plotly_chart(fig, use_container_width=True)
