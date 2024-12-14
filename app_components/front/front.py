import streamlit as st
import uuid
import requests
import pandas as pd
import altair as alt

# Configure the layout and initial state of the Streamlit page.
st.set_page_config(
    page_title="Loyalytics",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar navigation
page = st.sidebar.radio("Navigate",
                        ["Home", "Sign Up / Sign In", "My Profile", "Customer Insights", "Audience Analysis",
                         "Pricing Plans", "About Loyalytics"])


def set_page_background():
    """
    Sets the background color and overall styling of the page.

    This function uses Streamlit's markdown capability to inject custom CSS
    styles into the page, ensuring that the background color, font color, and
    various other elements like buttons and headings are styled to match the theme.

    Returns:
        None
    """
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


# Page 0: Home page
def home_page():
    """
    Displays the home page with an introduction and call to action.

    This function sets the introductory text for the "Home" page, including
    a brief description of the product and a call to action prompting users
    to engage with the platform.

    Returns:
        None
    """
    st.markdown("# Grow your Business with us!")
    st.markdown("### Loyalytics – Empowering businesses to build lasting connections.")
    st.write("Why chase new customers when you can keep the ones you already have hooked and happy? #flexiblesolutions")

    st.markdown("Start Today")

    st.markdown("\n**LOYALYTICS**")
    st.write("Sign up | Solutions | Pricing | About")


home_page()


# Page 1: Sign Up / Sign In
def signup_signin_page():
    """
    Displays the 'Sign Up' and 'Sign In' page for user authentication.

    This function allows users to either create a new account or log into an
    existing one. The page prompts the user for a username and password,
    and provides feedback based on the inputs.

    Returns:
        None
    """
    st.markdown("# Sign Up / Sign In")

    select_key = f"signup_signin_option_{str(uuid.uuid4())}"
    option = st.selectbox("Choose an option", ["Sign Up", "Sign In"], key=select_key)

    if option == "Sign Up":
        st.markdown("## Create a New Account")
        username = st.text_input("Username", key=f"signup_username_{str(uuid.uuid4())}")
        password = st.text_input("Password", type="password", key=f"signup_password_{str(uuid.uuid4())}")
        confirm_password = st.text_input("Confirm Password", type="password",
                                         key=f"signup_confirm_password_{str(uuid.uuid4())}")
        if st.button("Sign Up", key=f"signup_button_{str(uuid.uuid4())}"):

            # Ensure passwords match
            if password == confirm_password:
                st.success("Account created successfully! Please sign in.")
            else:
                st.error("Passwords do not match. Please try again.")

    elif option == "Sign In":
        st.markdown("## Sign In to Your Account")
        username = st.text_input("Username", key=f"signin_username_{str(uuid.uuid4())}")
        password = st.text_input("Password", type="password", key=f"signin_password_{str(uuid.uuid4())}")
        if st.button("Sign In", key=f"signin_button_{str(uuid.uuid4())}"):
            st.success("Signed in successfully!")


signup_signin_page()

USER_DATA = {
    "name": "Daniel",
    "surname": "Ek",
    "company": "Spotify",
    "profile_pic": "image.png"
}


def user_profile_page():
    """
    Displays the user's profile page with options for results, solutions, and settings.

    This function shows the user's profile information, including their
    name, surname, and company. The page also provides buttons to navigate
    to additional sections like 'My Results', 'Solutions', and 'Settings'.

    Returns:
        None
    """
    st.title("My Profile")

    # Check if user is signed in
    if "signed_in" in st.session_state and st.session_state["signed_in"]:
        col1, col2 = st.columns([1, 3])

        with col1:
            st.markdown("Company Image")

        with col2:
            st.markdown(f"### {USER_DATA['name']} {USER_DATA['surname']}")
            st.markdown(f"**Company:** {USER_DATA['company']}")
            st.markdown("---")

            # Navigation buttons
            if st.button("My Results", key="results_button"):
                st.session_state["page"] = "My Results"
            if st.button("Solutions", key="solutions_button"):
                st.session_state["page"] = "Solutions"
            if st.button("Settings", key="settings_button"):
                st.session_state["page"] = "Settings"

        if "page" in st.session_state:
            # Redirect to selected page
            if st.session_state["page"] == "My Results":
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

# URLs of the FastAPI endpoints
AGE_GROUP_URL = "http://back:8000/customer/count_by_age_group/"
DEVICE_URL = "http://back:8000/customer/count_by_device/"
COUNTRY_URL = "http://back:8000/customer/count_by_city/"


def fetch_data(url):
    """
    Fetches data from a given URL endpoint using a GET request.

    Args:
        url (str): The URL endpoint from which to fetch the data.

    Returns:
        list: Parsed JSON response as a list if the request is successful;
              an empty list if there is an error.
    """
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
    """
    Displays the 'My Results' page with data visualizations and user insights.

    This function fetches data from FastAPI endpoints related to age groups,
    devices, and cities, and visualizes it using bar charts and pie charts.
    It also allows users to view additional details through expandable sections.

    Returns:
        None
    """
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


if __name__ == "__main__":
    st.session_state["page"] = "MyResults"

    if st.session_state["page"] == "MyResults":
        my_results_page()


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


def solutions_page():
    """
    Renders the 'Solutions' page of the application, displaying insights and actions for different user categories.

    The function fetches user category data from a backend FastAPI endpoint (`/user_churn_categories/`), displays each category's
    percentage with a progress bar, and provides detailed email contexts for each category.
    The email contexts are displayed in expandable sections for users to view more details about each category.

    It also applies a background styling to the page using the `set_page_background()` function.

    Steps:
        - Fetches user category data using the `fetch_user_categories` function.
        - Displays the category name and percentage with a progress bar.
        - If available, shows the email context for each category in an expandable section.
    """
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
            st.markdown(
                f"""
                <div class="stMetric">
                    <h3>Percentage</h3>
                    <p>{percentage}%</p>
                </div>
                """,
                unsafe_allow_html=True
            )
            st.progress(percentage / 100)

            # Display email context in an expandable section
            if category_name in EMAIL_CONTEXTS:
                with st.expander(f"Details: {category_name}") :
                    st.write(f"**Email Context:** {EMAIL_CONTEXTS[category_name]['Email Context']}")


solutions_page()

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


st.markdown(
    """
    <style>
    /* General page style */
    body {
        background-color: #003366;
        color: #ffffff;
        font-family: 'Arial', sans-serif;
    }

    h1 {
        text-align: center;
        margin-top: 20px;
    }

    /* Card styling */
    .card {
        background-color: #003366;
        border-radius: 12px;
        padding: 20px;
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.2);
        text-align: center;
    }

    .card h3 {
        color: #ffffff;
        font-size: 24px;
        margin-bottom: 10px;
    }

    .card .price {
        color: #ffffff;
        font-size: 36px;
        font-weight: bold;
    }

    .card p {
        color: #003366;
        font-size: 16px;
        margin-bottom: 15px;
    }

    .card ul {
        list-style: none;
        padding: 0;
        margin-bottom: 20px;
    }

    .card ul li {
        color: #ffffff;
        font-size: 16px;
        margin: 5px 0;
    }

    .best-deal {
        border: 2px solid #9e6ef3;
        border-radius: 15px;
        padding: 5px;
        color: #9e6ef3;
        font-size: 14px;
        display: inline-block;
        margin-bottom: 10px;
    }

    /* Button styling */
    .button {
        background-color: #9e6ef3;
        border: none;
        color: #ffffff;
        padding: 10px 20px;
        border-radius: 50px;
        cursor: pointer;
        font-size: 16px;
        text-decoration: none;
        display: inline-flex;
        align-items: center;
        justify-content: center;
    }

    .button:hover {
        background-color: #8457cc;
    }

    .button span {
        margin-right: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# def pricing_page():
#     set_page_background()
#     """
#     Renders the 'Pricing Plans' page, showcasing different subscription tiers for Loyalytics with their respective features.

#     This page displays three pricing options available for customers: 'One Data', 'One Data', and 'Enterprise'. Each tier has a
#     specific pricing, timeline for service delivery, and associated features. The pricing structure is designed to cater to
#     different customer needs, from basic data insights to advanced analytics and security features.
#     """

#     """

#     Pricing Tiers:
#         - **One Data ($99)**:
#             - Provide a dataset
#             - Wait 14 business days for insights
#             - Get basic data insights and strategy suggestions
#             - Call to action: "Start and Think"

#         - **One Data ($299)** (Best Deal):
#             - Provide a dataset
#             - Wait 7 business days for insights
#             - Get data insights and numerous prompts for customer retention strategies
#             - Call to action: "Get Prompts"

#         - **Enterprise ($499)**:
#             - Provide a dataset
#             - Wait 3 business days for insights
#             - Get advanced analytics, enhanced security, and applied retention strategies
#             - Call to action: "Loyal Customers"

#     Purpose:
#         - Helps potential customers understand the available pricing plans.
#         - Provides clear and actionable steps based on the selected plan.
#         - Highlights the most popular and cost-effective plan using a label or badge (#bestdeal).

#     User Flow:
#         - The user can easily navigate between different pricing options and click on buttons to proceed with the respective service.
#         - Each plan is presented with its price, description, and a call-to-action button.

#     Styling:
#         - The page layout follows a card-style design with distinct blocks for each plan.
#         - A prominent #bestdeal label is used for the mid-tier option to attract attention.
#         - The call-to-action buttons are styled in a consistent color scheme to encourage user engagement.

#     """
#     # Page content goes here (using Streamlit components like st.markdown, st.write, etc. to structure the page)
#     st.markdown("<h1>Pricing Plans</h1>", unsafe_allow_html=True)


def pricing_page():
    """
    Renders the Pricing Plans page.

    The Pricing Plans page showcases three subscription options for customers, each tailored to different business needs. 
    Each pricing plan includes its description, associated features, and a call-to-action button.

    **Pricing Tiers**:
    - **One Data ($99)**: Basic data insights with a 14-day turnaround.
    - **One Data ($299)**: Solution prompts and data insights within 7 days (#BestDeal).
    - **Enterprise ($499)**: Advanced analytics, security, and applied retention strategies within 3 days.

    **Features**:
    - Pricing tiers are displayed in a card-style layout for easy comparison.
    - The "Best Deal" tier is highlighted to attract attention.
    - Interactive call-to-action buttons are styled for better user engagement.
    """
    set_page_background()
    st.markdown("<h1>Pricing Plans</h1>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    # Basic Plan
    with col1:
        st.markdown(
            """
            <div class="card">
                <h3>One Data</h3>
                <p class="price">$99</p>
                <p>Data Analyses and Visualizations for your business!</p>
                <ul>
                    <li>Provide a dataset</li>
                    <li>Wait 14 business days</li>
                    <li>Get Data insights</li>
                    <li>Think of Strategies</li>
                </ul>
                <a href="#" class="button"><span>Start and think</span> →</a>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # Pro Plan
    with col2:
        st.markdown(
            """
            <div class="card">
                <div class="best-deal">#bestdeal</div>
                <h3>One Data</h3>
                <p class="price">$299</p>
                <p>Solution Prompts for your business problem!</p>
                <ul>
                    <li>Provide a dataset</li>
                    <li>Wait 7 business days</li>
                    <li>Get Data insights</li>
                    <li>Get numerous prompts for customer retention</li>
                </ul>
                <a href="#" class="button"><span>Get Prompts</span> →</a>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # Enterprise Plan
    with col3:
        st.markdown(
            """
            <div class="card">
                <h3>Enterprise</h3>
                <p class="price">$499</p>
                <p>Everything Solved!</p>
                <ul>
                    <li>Provide a dataset</li>
                    <li>Wait 3 business days</li>
                    <li>Get Advanced Analytics</li>
                    <li>Advanced Security</li>
                    <li>Applied Retention Strategies</li>
                </ul>
                <a href="#" class="button"><span>Loyal Customers</span> →</a>
            </div>
            """,
            unsafe_allow_html=True,
        )


    col1, col2, col3 = st.columns(3)

    
pricing_page()

# Page 4: About Loyalytics


def about_loyalytics_page():
    """
    Renders the 'About Loyalytics' page, providing an overview of the Loyalytics platform and its key features.

    This page describes the core purpose of the Loyalytics platform, which is designed for subscription-based service providers
    aiming to enhance customer retention and reduce churn. The page highlights key features of the platform that enable users to
    segment and target customers effectively, automate retention efforts, and gain actionable insights into customer trends and behavior.

    Features:
        - **Segment & Target Effectively**: Identifies high-risk customer segments and tailors strategies to engage and retain them.
        - **Automate Retention Efforts**: Allows users to automate customer engagement campaigns, reducing manual effort.
        - **Gain Actionable Insights**: Provides an intuitive dashboard for tracking customer trends, predicting churn, and maximizing lifetime value.

    Steps:
        - Displays an introduction to the Loyalytics platform.
        - Outlines the main features of the platform.
        - Presents the benefits of using Loyalytics for subscription-based service providers.

    Styling:
        - Custom CSS (if any) to enhance the layout and appearance.
        - Clear and concise text with an easy-to-read layout to ensure user-friendly presentation.
    """
    st.markdown("# About Loyalytics")
    st.write(
        "Loyalytics: Data-Driven Customer Retention for Subscription-Based Services\n"
        "Loyalytics is a powerful marketing platform built exclusively for subscription-based service "
        "providers seeking to strengthen customer loyalty and reduce churn."
    )
    st.markdown("### Features:")
    st.write(
        "- Segment & Target Effectively: Identify high-risk segments and tailor "
        "strategies to engage, retain, and delight customers.")
    st.write(
        "- Automate Retention Efforts: Set up automated triggers and campaigns "
        "to keep customers engaged, without the manual effort.")
    st.write(
        "- Gain Actionable Insights: Access a user-friendly dashboard to track customer "
        "trends, predict churn, and maximize lifetime value.")


about_loyalytics_page()

if page == "Home":
    home_page()
elif page == "Sign Up / Sign In":
    signup_signin_page()
elif page == "My Profile":
    user_profile_page()
elif page == "Customer Insights":
    my_results_page()
elif page == "Audience Analysis":
    solutions_page()
elif page == "Pricing Plans":
    pricing_page()
elif page == "About Loyalytics":
    about_loyalytics_page()
