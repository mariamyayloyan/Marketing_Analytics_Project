import streamlit as st
import matplotlib.pyplot as plt

def solutions_page():
    st.markdown("# Audience Analysis")
    st.write("Audience by Country:")
    countries = ["USA", "France", "Britain", "Russia", "Other"]
    audience_count = [3594, 1200, 800, 600, 400]

    fig, ax = plt.subplots()
    ax.pie(audience_count, labels=countries, autopct='%1.1f%%')
    st.pyplot(fig)

    st.markdown("### Active Hours")
    hours = ["09:00-12:00", "12:00-18:00", "18:00-22:00", "22:00+"]
    active_users = [20, 35, 50, 25]
    st.bar_chart(data=active_users, use_container_width=True)

    st.markdown("# Retention Insights")
    st.write("Retention Rate:")

    years = [2022, 2023, 2024]
    retention_rates = [10, 15, 20]

    fig, ax = plt.subplots()
    ax.plot(years, retention_rates, marker='o')
    ax.set_xlabel("Year")
    ax.set_ylabel("Retention Rate (%)")
    ax.set_title("Retention Rate Over Time")
    st.pyplot(fig)

    st.markdown("### Devices")
    devices = ["Iphone", "Samsung", "Xiaomi", "Google Pixel", "Other"]
    device_count = [1200, 1000, 800, 400, 200]
    st.bar_chart(data=device_count, use_container_width=True)