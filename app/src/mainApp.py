import pandas as pd
import streamlit as st
from streamlit_extras.app_logo import add_logo
import world_bank_data as wb
import matplotlib.pyplot as plt
import numpy as np
# import streamlit_authenticator as stauth
from st_supabase_connection import SupabaseConnection



add_logo("assets/logo.png", height=320)

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

connection = st.connection("supabase", type = SupabaseConnection)
rows = connection.query("*", table="mytable", ttl="10ms").execute()
for row in rows.data:
  st.write(f"{row['name']} has :{row['pet']}:")


# st.header('World Bank Data')

# with st.echo(code_location='above'):
#     countries:pd.DataFrame = wb.get_countries()
   
#     st.dataframe(countries)

# with st.echo(code_location='above'):
#     arr = np.random.normal(1, 1, size=100)
#     test_plot, ax = plt.subplots()
#     ax.hist(arr, bins=20)

#     st.pyplot(test_plot)




