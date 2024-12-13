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


def about_loyalytics_page():
    set_page_background()
    st.markdown("# About Loyalytics")
    st.write(
        "Loyalytics: Data-Driven Customer Retention for Subscription-Based Services\n"
        "Loyalytics is a powerful marketing platform built exclusively for subscription-based service "
        "providers seeking to strengthen customer loyalty and reduce churn."
    )
    st.markdown("### Features:")
    st.write(
        "- Segment & Target Effectively: Identify high-risk segments and tailor strategies to engage, retain, and delight customers.")
    st.write(
        "- Automate Retention Efforts: Set up automated triggers and campaigns to keep customers engaged, without the manual effort.")
    st.write(
        "- Gain Actionable Insights: Access a user-friendly dashboard to track customer trends, predict churn, and maximize lifetime value.")


about_loyalytics_page()
