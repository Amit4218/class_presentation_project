import streamlit as st
from utils.api import get_riddle


def riddle():

    point = st.session_state.point_counter = 0

    riddle = get_riddle()
    if not riddle:
        st.text("Something Went wrong! please refresh the page")

    st.session_state.current_riddle = st.header(riddle["riddle"])

    answer = st.text_input("Enter your guess : ")

    col1, col2 = st.columns(2)

    with col1:
        next_clicked = st.button("Next Riddle")
    with col2:
        submit_clicked = st.button("Submit")

    if next_clicked:
        riddle()
        if answer.split().lower() == riddle["answer"]:
            st.success("Correct ! 🎉")
            point += 1

    riddle()

    if submit_clicked:
        pass
