import streamlit as st


def footer_home():
    st.markdown("""
        <div style="
            margin-top: 40px;
            display: flex;
            justify-content: center;
            align-items: center;
            font-size: 14px;
            opacity: 0.85;
        ">
            <p style="color: white; margin: 0;">
                Created with ❤️ by 
                <span style="
                    color: #FFD700;
                    font-weight: 600;
                    letter-spacing: 0.5px;
                    margin-left: 4px;
                ">
                    Rohitha Panchamukhi M
                </span>
            </p>
        </div>
    """, unsafe_allow_html=True)


def footer_dashboard():
    st.markdown("""
        <div style="
            margin-top: 40px;
            display: flex;
            justify-content: center;
            align-items: center;
            font-size: 14px;
            opacity: 0.8;
        ">
            <p style="color: black; margin: 0;">
                Created with ❤️ by 
                <span style="
                    color: #ff9900;
                    font-weight: 600;
                    letter-spacing: 0.5px;
                    margin-left: 4px;
                ">
                    Rohitha Panchamukhi M
                </span>
            </p>
        </div>
    """, unsafe_allow_html=True)