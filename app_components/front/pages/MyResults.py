import streamlit as st
import pandas as pd
import requests
import altair as alt


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


# URLs of the FastAPI endpoints
AGE_GROUP_URL = "http://back:8000/customer/count_by_age_group/"
DEVICE_URL = "http://back:8000/customer/count_by_device/"
COUNTRY_URL = "http://back:8000/customer/count_by_city/"


# Function to fetch data from FastAPI endpoints
def fetch_data(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()  # Parse the JSON response into a Python object
        else:
            st.error(f"Failed to fetch data: {response.status_code}")
            return []
    except Exception as e:
        st.error(f"Error fetching data: {e}")
        return []


def my_results_page():
    set_page_background()
    st.title("My Results")

    # Fetch data from FastAPI endpoints
    age_group_data = fetch_data(AGE_GROUP_URL)
    device_data = fetch_data(DEVICE_URL)
    country_data = fetch_data(COUNTRY_URL)

    # Create three equal-sized columns for the layout
    col1, col2, col3 = st.columns([1, 1, 1])

    # 1. Age Group Segment
    with col1:
        st.subheader("Age Groups")
        if age_group_data:
            age_df = pd.DataFrame(age_group_data)
            st.bar_chart(
                age_df.set_index("age_group")["customer_count"],
                use_container_width=True,
                height = 300
            )
            if st.button("Details: Age Groups", key="age_details"):
                with st.expander("Age Group Details"):
                    for item in age_group_data:
                        st.write(f"{item['age_group']}: {item['customer_count']} customers")

    with col2:
        st.subheader("Devices")
        if device_data:
            device_df = pd.DataFrame(device_data)

            total_count = device_df["customer_count"].sum()
            device_df["percentage"] = device_df["customer_count"] / total_count * 100

            pie_chart = alt.Chart(device_df).mark_arc().encode(
                theta=alt.Theta(field="customer_count", type="quantitative"),
                color=alt.Color(field="device_type", type="nominal"),
                tooltip=["device_type", "customer_count", "percentage"],
                text=alt.Text(field="percentage", type="quantitative", format=".1f")  # Format percentage
            ).properties(
              #width=300,
                height=300
            )

            #st.write("### Device Distribution")
            st.altair_chart(pie_chart, use_container_width=True)

            if st.button("Details: Devices", key="device_details"):
                with st.expander("Device Details"):
                    for item in device_data:
                        st.write(
                            f"{item['device_type']}: {item['customer_count']} customers ({(item['customer_count'] / total_count) * 100:.1f}%)")

    # 3. City Segment
    with col3:
        st.subheader("Cities")
        if country_data:
            city_df = pd.DataFrame(country_data)

            # Select the top 5 cities by customer count
            top_cities_df = city_df.nlargest(5, "customer_count")

            st.bar_chart(
                top_cities_df.set_index("city")["customer_count"],
                use_container_width=True,
                height = 300
            )

            if st.button("Details: Cities", key="city_details"):
                with st.expander("City Details"):
                    for _, row in top_cities_df.iterrows():
                        st.write(f"{row['city']}: {row['customer_count']} customers")


my_results_page()
