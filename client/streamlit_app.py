import streamlit as st
from utils.riddle import riddle

st.title("Welcome To Riddle Me 🤔")
st.text("Refresh your brain with little riddles")


start_riddle = st.button("start")

if start_riddle:
    riddle()

