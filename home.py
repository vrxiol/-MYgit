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

html_7 = """
<div style="background-color:#EC7063;padding:15px;border-radius:15px 15px 15px 15px;border-style:'solid';border-color:black">
<center><h5>สถิติข้อมูลดอกไม้</h5></center>
</div>
"""
st.markdown(html_7, unsafe_allow_html=True)
st.markdown("")
dt = pd.read_csv("./data/iris-3.csv")
st.write(dt.head(10))