import streamlit as st
import matplotlib.pyplot as plt
import requests
import pandas as pd

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

# URLs of the FastAPI endpoints (adjusted for 'customer' instead of 'customers')
AGE_GROUP_URL = "http://back:8000/customer/count_by_age_group/"
DEVICE_URL = "http://back:8000/customer/count_by_device/"
COUNTRY_URL = "http://back:8000/customer/count_by_city/"

# Function to fetch data from FastAPI endpoints
def fetch_data(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()  # Parse the JSON response into a Python object
            st.write(data)  # Debugging step to check the data format
            return data
        else:
            st.error(f"Failed to fetch data: {response.status_code}")
            return []
    except Exception as e:
        st.error(f"Error fetching data: {e}")
        return []

# Function to display results
def my_results_page():
    set_page_background()
    st.title("My Results")

    # Fetch data from FastAPI endpoints
    age_group_data = fetch_data(AGE_GROUP_URL)
    device_data = fetch_data(DEVICE_URL)
    country_data = fetch_data(COUNTRY_URL)


    # Create three columns for the layout
    col1, col2, col3 = st.columns(3)

    # 1. Age Group Segment
    with col1:
        st.subheader("Age Groups")
        if age_group_data:
            fig, ax = plt.subplots()
            # Extract the data and plot the bar chart
            age_groups = [item['age_group'] for item in age_group_data]
            percentages = [item['customer_count'] for item in age_group_data]
            ax.bar(age_groups, percentages, color="skyblue")
            ax.set_title("Age Group Distribution")
            ax.set_ylabel("Number of Customers")
            st.pyplot(fig)

            if st.button("Details: Age Groups"):
                with st.expander("Age Group Details"):
                    for item in age_group_data:
                        st.write(f"**{item['age_group']}**: {item['customer_count']} customers")

    # 2. Device Segment
    with col2:
        st.subheader("Devices")
        if device_data:
            fig, ax = plt.subplots()
            # Extract the data and plot the pie chart
            devices = [item['device_type'] for item in device_data]
            percentages = [item['customer_count'] for item in device_data]
            ax.pie(percentages, labels=devices, autopct='%1.1f%%', colors=["blue", "green", "lightblue", "lightgreen"])
            ax.set_title("Device Distribution")
            st.pyplot(fig)

            if st.button("Details: Devices"):
                with st.expander("Device Details"):
                    for item in device_data:
                        st.write(f"**{item['device_type']}**: {item['customer_count']} customers")

    # 3. Country Segment
    with col3:
        st.subheader("Cities")
        if country_data:
            fig, ax = plt.subplots()
            # Extract the data and plot the bar chart
            cities = [item['city'] for item in country_data]
            percentages = [item['customer_count'] for item in country_data]
            ax.bar(cities, percentages, color="lightgreen")
            ax.set_title("Customers by City")
            ax.set_ylabel("Number of Customers")
            st.pyplot(fig)

            if st.button("Details: Cities"):
                with st.expander("City Details"):
                    for item in country_data:
                        st.write(f"**{item['city']}**: {item['customer_count']} customers")

# Run the Streamlit app
my_results_page()
