import streamlit as st
import pandas as pd

st.title("🐷🐷🐷Website Developing using Python🐷🐷")
st.header("🍖🍖Website Developing using Python🍖🍖")

st.image('./ing/mayorma.jpg')
st.subheader("Dog")

col1, col2, col3 = st.columns(3)
with col1:
    st.header('Dog1')
    st.image("./ing/q1.jpg")

with col2:
    st.header('Dog2')
    st.image("./ing/w.jpg")

with col3:
    st.header('Dog3')
    st.image("./ing/e.jpg")