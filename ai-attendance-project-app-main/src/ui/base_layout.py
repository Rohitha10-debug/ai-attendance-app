import streamlit as st

def style_background_home():
    st.markdown("""
        <style>
        .stApp {
            background: #5865F2;
        }
        </style>
    """, unsafe_allow_html=True)


def style_base_layout():
    st.markdown("""
        <style>

        /* Hide Streamlit default UI */
        #MainMenu, footer, header {
            visibility: hidden;
        }

        /* Fix spacing */
        .block-container {
            padding-top: 1rem;
            max-width: 900px;
        }

        /* Fonts */
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;500;700&display=swap');

        html, body, [class*="css"] {
            font-family: 'Outfit', sans-serif;
        }

        /* Buttons */
        button {
            border-radius: 999px !important;
            padding: 0.6rem 1.2rem !important;
            font-weight: 600 !important;
        }

        button[kind="primary"] {
            background: #EB459E !important;
            color: white !important;
        }

        button:hover {
            transform: scale(1.05);
            transition: 0.2s;
        }

        </style>
    """, unsafe_allow_html=True)