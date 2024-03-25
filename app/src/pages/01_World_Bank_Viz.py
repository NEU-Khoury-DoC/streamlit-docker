import pandas as pd
import streamlit as st
from streamlit_extras.app_logo import add_logo
import world_bank_data as wb
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px


st.set_page_config(page_title="World Bank Data Viz", page_icon="🏦")

add_logo("assets/logo.png", height=320)

st.header('World Bank Data')

with st.echo(code_location='above'):
    countries:pd.DataFrame = wb.get_countries()
   
    st.dataframe(countries)

with st.echo(code_location='above'):
    arr = np.random.normal(1, 1, size=100)
    test_plot, ax = plt.subplots()
    ax.hist(arr, bins=20)

    st.pyplot(test_plot)


with st.echo(code_location='above'):
    slim_countries = countries[countries['incomeLevel'] != 'Aggregates']
    data_crosstab = pd.crosstab(slim_countries['region'], 
                                slim_countries['incomeLevel'],  
                                margins = False) 
    st.table(data_crosstab)
