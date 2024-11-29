import streamlit as st

USER_DATA = {
    "name": "Daniel",
    "surname": "Ek",
    "company": "Spotify",
    "profile_pic": "image.png"
}


def user_profile_page():
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
