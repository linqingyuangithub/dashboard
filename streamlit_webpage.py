#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import streamlit as st
import random
from streamlit_d3_demo import d3_line
import altair as alt
import os
import matplotlib.pyplot as plt
#from datetime import datetime
from datetime import date

st.title('Have a good day')
st.title('I love cats :blue[cool] :sunglasses:')


# In[3]:


#style = pd.read_csv('./Downloads/py/style master.csv', low_memory=False)
combined_df = pd.read_csv('./OneDrive - Delta Enterprise Corp/combined inv/combined_df.csv', dtype={"Date": str})
combined_df


# In[ ]:




