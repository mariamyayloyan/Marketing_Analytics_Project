import streamlit as st
import matplotlib.pyplot as plt


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


AGE_GROUP_DATA = {
    "Age Group": ["Under 20", "20+", "30+", "40+"],
    "Percentage": [45, 50, 40, 35]
}

DEVICE_DATA = {
    "Device": ["Android", "iOS", "Windows", "Linux"],
    "Percentage": [50, 30, 15, 5]
}

COUNTRY_DATA = {
    "Country": ["USA", "Canada", "UK", "Germany"],
    "Percentage": [40, 30, 20, 10]
}


def my_results_page():
    set_page_background()
    st.title("My Results")

    col1, col2, col3 = st.columns(3)

    # 1. Age Group Segment
    with col1:
        st.subheader("Age Groups")
        fig, ax = plt.subplots()
        ax.bar(AGE_GROUP_DATA["Age Group"], AGE_GROUP_DATA["Percentage"], color="skyblue")
        ax.set_title("Age Group Distribution")
        ax.set_ylabel("Distribution (%)")
        st.pyplot(fig)

        if st.button("Details: Age Groups"):
            with st.expander("Age Group Details"):
                for i, age_group in enumerate(AGE_GROUP_DATA["Age Group"]):
                    st.write(f"**{age_group}**: {AGE_GROUP_DATA['Percentage'][i]}% of users")

    # 2. Device Segment
    with col2:
        st.subheader("Devices")
        fig, ax = plt.subplots()
        ax.pie(DEVICE_DATA["Percentage"], labels=DEVICE_DATA["Device"], autopct='%1.1f%%', colors=["blue", "green", "lightblue", "lightgreen"])
        ax.set_title("Device Distribution")
        st.pyplot(fig)

        if st.button("Details: Devices"):
            with st.expander("Device Details"):
                for i, device in enumerate(DEVICE_DATA["Device"]):
                    st.write(f"**{device}**: {DEVICE_DATA['Percentage'][i]}% of users")

    # 3. Country Segment
    with col3:
        st.subheader("Countries")
        fig, ax = plt.subplots()
        ax.bar(COUNTRY_DATA["Country"], COUNTRY_DATA["Percentage"], color="lightgreen")
        ax.set_title("Top 4 Countries")
        ax.set_ylabel("Percentage of Users")
        st.pyplot(fig)

        if st.button("Details: Countries"):
            with st.expander("Country Details"):
                for i, country in enumerate(COUNTRY_DATA["Country"]):
                    st.write(f"**{country}**: {COUNTRY_DATA['Percentage'][i]}% of users")


my_results_page()