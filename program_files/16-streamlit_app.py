import matplotlib.pyplot as plt
import numpy as np
import pandas_datareader as pdr
import streamlit as st


st.sidebar.header("Parmeters")
stock = st.sidebar.text_input("Enter stock symbol", value="GOOG")
price = st.sidebar.number_input("Enter Price", value=100)

r = .05
sigma = .20
T = 21/252

values = []
ending = 1 # use price and reset in loop
for value in range(1000):
    # ending = price
    ending *= np.exp((r - .5 * sigma ** 2)* T + np.sqrt(T) * sigma * np.random.normal(0,1))
    values.append(ending)

fig, ax = plt.subplots()
ax.hist(values, bins= 50, edgecolor='w')
st.pyplot(fig)
