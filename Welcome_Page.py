import streamlit as st
from PIL import Image

st.set_page_config(page_title = "Lego application", layout="wide")

st.sidebar.success("Menu")


image = Image.open("E:\data_science_pierwsze_Lekcje\lego_price_checker\images\welcome_image_2-removebg-preview.png")

st.markdown(f"<h1 style='text-align: center; color: white; margin-top: -80px;'>Lego Price Checker Application</h1>", unsafe_allow_html=True)

col1, col2 = st.columns([0.65, 0.35])

with col1:
    st.markdown("<style>h1 {text-align: center; color: white; margin-top: 40px;}</style>", unsafe_allow_html=True)
    st.image(image)

with col2:
    st.markdown("<style>h1 {text-align: center; color: white; margin-top: 40px;}</style>", unsafe_allow_html=True)
    st.write(f"Purpose of this project is to get information in realtime about concrete LEGO sets like price etc. from different polish shops.")
    st.write(f"Data are collected once per day from Monday to Friday")
    st.write(f"Data are avaiable only for sets which are released since 2021")
    st.subheader("Made by: Korzystka Piotr")
    st.subheader(f"Link to github: https://github.com/threaces")