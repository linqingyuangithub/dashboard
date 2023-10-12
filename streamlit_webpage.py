#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import streamlit as st


st.title('Have a good day')
st.title('I love cats :blue[cool] :sunglasses:')

uploaded_file = st.file_uploader(
    "Choose your database", accept_multiple_files=False)
if uploaded_file is not None:
    file_name = uploaded_file
else:
    file_name = "DatabaseSample.xlsx"
# In[3]:





# In[ ]:




