import streamlit as st
import uuid


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


def signup_signin_page():
    set_page_background()
    st.markdown("# Sign Up / Sign In")

    selectbox_key = f"signup_signin_option_{str(uuid.uuid4())}"
    option = st.selectbox("Choose an option", ["Sign Up", "Sign In"], key=selectbox_key)

    if option == "Sign Up":
        st.markdown("## Create a New Account")
        username = st.text_input("Username", key=f"signup_username_{str(uuid.uuid4())}")
        password = st.text_input("Password", type="password", key=f"signup_password_{str(uuid.uuid4())}")
        confirm_password = st.text_input("Confirm Password", type="password", key=f"signup_confirm_password_{str(uuid.uuid4())}")
        if st.button("Sign Up", key=f"signup_button_{str(uuid.uuid4())}"):
            if password == confirm_password:
                st.success("Account created successfully! Please sign in.")
            else:
                st.error("Passwords do not match. Please try again.")

    elif option == "Sign In":
        st.markdown("## Sign In to Your Account")
        username = st.text_input("Username", key=f"signin_username_{str(uuid.uuid4())}")
        password = st.text_input("Password", type="password", key=f"signin_password_{str(uuid.uuid4())}")
        if st.button("Sign In", key=f"signin_button_{str(uuid.uuid4())}"):
            st.success("Signed in successfully!")


signup_signin_page()
