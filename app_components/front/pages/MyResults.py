import streamlit as st
import requests


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


AGE_GROUP_URL = "http://back:8000/customer/count_by_age_group/"
DEVICE_URL = "http://back:8000/customer/count_by_device/"
COUNTRY_URL = "http://back:8000/customer/count_by_city/"


# Function to fetch data from FastAPI endpoints
def fetch_data(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()  # Parse the JSON response into a Python object
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
            # Prepare data for Streamlit's bar chart
            import pandas as pd

            # Convert the data into a DataFrame
            age_group_df = pd.DataFrame(age_group_data)

            # Use Streamlit's bar_chart to visualize the data
            st.bar_chart(
                age_group_df.set_index("age_group")["customer_count"],
                use_container_width=True
            )

            if st.button("Details: Age Groups"):
                with st.expander("Age Group Details"):
                    for item in age_group_data:
                        st.write(f"{item['age_group']}: {item['customer_count']} customers")

    # 2. Device Segment
    with col2:
        st.subheader("Devices")
        if device_data:
            total = sum(item['customer_count'] for item in device_data)

            st.write("### Device Distribution")
            for item in device_data:
                percentage = (item['customer_count'] / total) * 100
                st.write(f"**{item['device_type']}**")
                st.progress(int(percentage))

            if st.button("Details: Devices"):
                with st.expander("Device Details"):
                    for item in device_data:
                        st.write(
                            f"{item['device_type']}: {item['customer_count']} customers ({(item['customer_count'] / total) * 100:.1f}%)")

        # 3. Country Segment
        with col3:
            st.subheader("Cities")
            if country_data:
                import pandas as pd

                # Convert the data into a DataFrame
                city_df = pd.DataFrame(country_data)

                # Sort the DataFrame by 'customer_count' in descending order and select the top 5 cities
                top_cities_df = city_df.sort_values(by="customer_count", ascending=False).head(5)

                # Create a bar chart using Streamlit for the top 5 cities
                st.bar_chart(
                    top_cities_df.set_index("city")["customer_count"],
                    use_container_width=True
                )

                if st.button("Details: Cities"):
                    with st.expander("City Details"):
                        for item in top_cities_df.to_dict(orient="records"):
                            st.write(f"{item['city']}: {item['customer_count']} customers")



my_results_page()
