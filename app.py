import pickle
import streamlit as st
model = pickle.load(open("model.pickle", "rb"))

st.title("Revenue Prediction")
temperature = st.number_input('Input Temperature').reshape(-1,1)

if st.button('Predict'):
  st.write(model.predict(temperature))
