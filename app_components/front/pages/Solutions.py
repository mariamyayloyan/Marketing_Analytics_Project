import streamlit as st
import requests

# Function to set the page background
def set_page_background():
    st.markdown(
        """
        <style>
        body {
            background-color: #001f3f;
            color: white;
        }
        .stApp {
            background-color: #001f3f; 
            color: white;
        }
        h1, h2, h3, h4, h5, h6 {
            color: #FFFFFF; 
        }
        .sidebar .sidebar-content {
            background-color: #001f3f; 
        }
        .stButton>button {
            background-color: #003366;
            color: white;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# Static email contexts for each category
EMAIL_CONTEXTS = {
    "Dormant Users": {
        "Email Context": "We noticed you’ve been away from Spotify Premium, and we’d love to welcome you back! ...",
    },
    "Loyal Users": {
        "Email Context": "Your 2024 Spotify Wrapped Is Here! Celebrate your most-loved tracks and favorite genres!",
    },
    "Engaged Users": {
        "Email Context": "Holiday Special: Get 3 Months of Premium for Just $3.99!",
    },
    "High-Risk Users": {
        "Email Context": "We Miss You! Enjoy 1 Month of Premium on Us.",
    },
}

# Function to fetch data from FastAPI
def fetch_user_categories():
    try:
        response = requests.get("http://back:8000/user_churn_categories/")
        if response.status_code == 200:
            return response.json()
        else:
            st.error(f"Failed to fetch data: {response.status_code}")
            return []
    except Exception as e:
        st.error(f"Error fetching data: {e}")
        return []

# Display Solutions Page
def solutions_page():
    set_page_background()
    st.title("Solutions")
    st.write("Here are insights and actions applied for various user categories:")

    # Fetch data from backend
    solutions_data = fetch_user_categories()

    if solutions_data:
        for category_data in solutions_data:
            category_name = category_data["Category"]
            percentage = category_data["Percentage"]

            st.subheader(category_name)

            # Display percentage with a progress bar
            st.metric(label="Percentage", value=f"{percentage}%")
            st.progress(percentage / 100)

            # Display email context in an expandable section
            if category_name in EMAIL_CONTEXTS:
                with st.expander(f"Details: {category_name}"):
                    st.write(f"**Email Context:** {EMAIL_CONTEXTS[category_name]['Email Context']}")

# Run the Streamlit app
solutions_page()
