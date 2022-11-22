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
------------------------------
st.title("Catálogo sísmico 1960-2021")
df_cat = pd.read_excel(r'https://www.datosabiertos.gob.pe/sites/default/files/Catalogo1960_2021.xlsx', header= 0) 
st.write(df_cat)
