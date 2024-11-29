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


USER_DATA = {
    "name": "Daniel",
    "surname": "Ek",
    "company": "Spotify",
    "profile_pic": "image.png"
}


def user_profile_page():
    set_page_background()
    if "signed_in" in st.session_state and st.session_state["signed_in"]:
        col1, col2 = st.columns([1, 3])

        with col1:
            st.markdown("Company Image")

        with col2:
            st.markdown(f"### {USER_DATA['name']} {USER_DATA['surname']}")
            st.markdown(f"**Company:** {USER_DATA['company']}")
            st.markdown("---")

            if st.button("My Results"):
                st.session_state["page"] = "MyResults"
            if st.button("Solutions"):
                st.session_state["page"] = "Solutions"
            if st.button("Settings"):
                st.session_state["page"] = "Settings"

        if "page" in st.session_state:
            if st.session_state["page"] == "MyResults":
                st.write("Redirecting to My Results page...")
            elif st.session_state["page"] == "Solutions":
                st.write("Redirecting to Solutions page...")
            elif st.session_state["page"] == "Settings":
                st.write("Redirecting to Settings page...")

    else:
        st.warning("Please sign in first.")


if __name__ == "__main__":
    if "signed_in" not in st.session_state:
        st.session_state["signed_in"] = True

    user_profile_page()
