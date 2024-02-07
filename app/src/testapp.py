import pandas as pd
import streamlit as st
import world_bank_data as wb
import matplotlib.pyplot as plt
import numpy as np

st.title('Welcome to the Brussels 2024 Dialogue Sample App')

st.write("""
        This is a little sample application to 
        demonstrate what you will be able to do by the 
        end of the project.  

        This may seem trivial as it is running in a
        browser, but what you aren't seeing is that 
        the code for this small app is bundled up in a 
        Docker container and deployed to the public internet
        using Fly.io.
        """)  

st.header('World Bank Data')

with st.echo(code_location='above'):
    countries:pd.DataFrame = wb.get_countries()
   
    st.dataframe(countries)

with st.echo(code_location='above'):
    arr = np.random.normal(1, 1, size=100)
    test_plot, ax = plt.subplots()
    ax.hist(arr, bins=20)

    st.pyplot(test_plot)




