import pickle
import numpy as np
import streamlit as st
model = pickle.load(open("model.pickle", "rb"))

st.title("Revenue Prediction")
temperature = st.number_input('Input Temperature')
# temperature = np.array([temperature]).reshape(-1,1)

if st.button('Predict'):
  st.write("Revenue Prediction")
  st.write(model.predict(temperature))
