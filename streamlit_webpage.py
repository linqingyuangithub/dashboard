#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import streamlit as st


st.title('Daily Reporting')
st.title('I love cats :blue[cool] :sunglasses:')

uploaded_file = st.file_uploader(
    "Choose sales data", accept_multiple_files=False)
if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)
    st.dataframe(df)
    st.table(df)
else:
    file_name = "DatabaseSample.xlsx"

#style = pd.read_excel(uploaded_file)
#style
# In[3]:





# In[ ]:




