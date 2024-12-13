import streamlit as st


def set_page_background():
    st.markdown(
        """
        <style>
        body {
            background-color: #001f3f;;
            color: white;
        }
        .stApp {
            background-color: #001f3f;; 
            color: white;
        }
        h1, h2, h3, h4, h5, h6 {
            color: #FFFFFF; 
        }
        .sidebar .sidebar-content {
            background-color: #001f3f;; 
        }
        .stButton>button {
            background-color: #003366;
            color: white;
        }
        </style>
        """,
        unsafe_allow_html=True
    )


def home_page():
    set_page_background()
    st.markdown("# Grow your Business with us!")
    st.markdown("### Loyalytics – Empowering businesses to build lasting connections.")
    st.write("Why chase new customers when you can keep the ones you already have hooked and happy? #flexiblesolutions")

    st.button("Start Today")

    st.markdown("\n**LOYALYTICS**")
    st.write("Sign up | Solutions | Pricing | About")


home_page()
