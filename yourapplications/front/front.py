import streamlit as st
import matplotlib.pyplot as plt

# Page configuration
st.set_page_config(
    page_title="Loyalytics",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Page navigation
page = st.sidebar.radio("Navigate",
                        ["Sign Up / Sign In", "Home", "Solutions", "Pricing", "About"])


# Page 0: Sign Up / Sign In
def signup_signin_page():
    st.markdown("# Sign Up / Sign In")
    option = st.selectbox("Choose an option", ["Sign Up", "Sign In"])

    if option == "Sign Up":
        st.markdown("## Create a New Account")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        confirm_password = st.text_input("Confirm Password", type="password")
        if st.button("Sign Up"):
            if password == confirm_password:
                st.success("Account created successfully! Please sign in.")
            else:
                st.error("Passwords do not match. Please try again.")
    elif option == "Sign In":
        st.markdown("## Sign In to Your Account")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.button("Sign In"):
            st.success("Signed in successfully!")


# Page 1: Home
def home_page():
    st.markdown("# Grow your Business with us!")
    st.markdown("### Loyalytics – Empowering businesses to build lasting connections.")
    st.write("Why chase new customers when you can keep the ones you already have hooked and happy? #flexiblesolutions")

    st.button("Start Today")

    st.markdown("\n**LOYALYTICS**")
    st.write("Sign up | Solutions | Pricing | About")


# Page 2: Solutions
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


# Page 3: Pricing

def pricing_page():
    st.markdown("# Pricing Plans")

    # Define the columns for pricing plans
    col1, col2, col3 = st.columns(3)

    # Basic Plan
    with col1:
        st.subheader("Basic")
        st.markdown("**Price:** $99")
        st.markdown("Data Analyses and Visualizations for your business!")
        st.write("- Provide a Dataset")
        st.write("- Waiting Time: 14 Business Days")
        st.write("- Get Data insights")
        st.write("- Think of Strategies")
        st.button("Start and Think")

    # Pro Plan
    with col2:
        st.subheader("Advanced")
        st.markdown("**Price:** $299")
        st.markdown("Solution Prompts for your Business Problem")
        st.write("- Provide a Dataset")
        st.write("- Waiting Time: 7 Business Days")
        st.write("- Get Data insights")
        st.write("- Get Numerous Prompts for Customer Retention")
        st.button("Get Prompts")

    # Enterprise Plan
    with col3:
        st.subheader("Provide a Dataset")
        st.markdown("**Price** $499")
        st.markdown("Waiting Time: 3 Business Days")
        st.write("- Advanced Data Analytics")
        st.write("- Advanced Security")
        st.write("- Applied Retention Strategies")
        st.button("Loyal Customers")


# Display the pricing page when called
pricing_page()


# Page 4: About Loyalytics
def about_loyalytics_page():
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


# Rendering pages
if page == "Sign Up / Sign In":
    signup_signin_page()
elif page == "Home":
    home_page()
elif page == "Audience Analysis":
    solutions_page()
elif page == "Retention Insights":
    solutions_page()
elif page == "About Loyalytics":
    about_loyalytics_page()

