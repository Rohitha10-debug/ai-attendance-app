import streamlit as st
from src.components.header import header_home
from src.components.footer import footer_home
from src.ui.base_layout import style_base_layout, style_background_home


def home_screen():

    style_background_home()
    style_base_layout()

    header_home()

    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.markdown("<h3 style='color:#1F1F1F; font-weight:700;'>I'm Student</h3>", unsafe_allow_html=True)
        st.image("https://i.ibb.co/844D9Lrt/mascot-student.png", width=120)

        if st.button("Student Portal", use_container_width=True):
            st.session_state['login_type'] = 'student'
            st.rerun()

    with col2:
        st.markdown("<h3 style='color:#1F1F1F; font-weight:700;'>I'm Teacher</h3>", unsafe_allow_html=True)
        st.image("https://i.ibb.co/CsmQQV6X/mascot-prof.png", width=130)

        if st.button("Teacher Portal", use_container_width=True):
            st.session_state['login_type'] = 'teacher'
            st.rerun()

    footer_home()