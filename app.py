import streamlit as st
st.title("GIẢI PHƯƠNG TRÌNH BẬC NHẤT")
a = st.number_input('tham số a')
b = st.number_input('tham số b')
if (a==0):
  if (b != 0):
    res = "Phương trình vô nghiệm"
  else:
    res = "Phương trình vô số nghiệm"
else:
  res = "Phương trình có 1 nghiệm " + str(-b / a)
if st.button('Giải'):
  st.write(res)