import streamlit as st
import matplotlib.pyplot as plt
import uuid


st.set_page_config(
    page_title="Loyalytics",
    layout="wide",
    initial_sidebar_state="expanded"
)

page = st.sidebar.radio("Navigate",
                        ["Home", "Sign Up / Sign In", "My Profile", "Customer Insights", "Audience Analysis", "Pricing Plans", "About Loyalytics"])


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


# Page 0: Home page

def home_page():
    st.markdown("# Grow your Business with us!")
    st.markdown("### Loyalytics – Empowering businesses to build lasting connections.")
    st.write("Why chase new customers when you can keep the ones you already have hooked and happy? #flexiblesolutions")

    st.markdown("Start Today")

    st.markdown("\n**LOYALYTICS**")
    st.write("Sign up | Solutions | Pricing | About")


home_page()


# Page 1: Sign Up / Sign In
def signup_signin_page():
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
    st.title("My Profile")

    if "signed_in" in st.session_state and st.session_state["signed_in"]:
        col1, col2 = st.columns([1, 3])

        with col1:
            st.markdown("Company Image")

        with col2:
            st.markdown(f"### {USER_DATA['name']} {USER_DATA['surname']}")
            st.markdown(f"**Company:** {USER_DATA['company']}")
            st.markdown("---")

            if st.button("My Results", key="results_button"):
                st.session_state["page"] = "My Results"

            if st.button("Solutions", key="solutions_button"):
                st.session_state["page"] = "Solutions"

            if st.button("Settings", key="settings_button"):
                st.session_state["page"] = "Settings"

        if "page" in st.session_state:
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


if __name__ == "__main__":
    st.session_state["page"] = "MyResults"

    if st.session_state["page"] == "MyResults":
        my_results_page()


SOLUTIONS_DATA = {
    "Canceled Users": {
        "Percentage": 11.48,
        "Email Context": "Subject: We’d Love to Have You Back—Exclusive Offer Inside! 🎶"
                         
                         "Body:"
                         "Hi [User's Name],"
                         
                         "We noticed you’ve been away from Spotify Premium, and we’d love to welcome you back! "
                         "To make it easy, we’re offering you an exclusive deal:"
                         
                         "Get 50% off your first 3 months of Premium."
                         "With Premium, you’ll enjoy:"
                         "Ad-free listening: No interruptions—just music."
                         "Offline mode: Download your favorites and listen anywhere."
                         "Unlimited skips: Always play the perfect song."
                         
                         "This special offer is available for a limited time. "
                         "Join now with This Link so you don’t miss out."
                         "We can’t wait to see you back in the groove!"
                         
                         "Best,"
                         "The Spotify Team 🎧"
    },

    "Loyal Users": {
        "Percentage": 38.31,
        "Email Context": "Subject: Your 2024 Spotify Wrapped Is Here! 🎉"
                         
                         "Body:"
                         "Hi [User's Name],"
                         
                         "It’s been an incredible year of music with you, and we’ve created "
                         "something special to celebrate!"
                         "Your Spotify Wrapped 2024 is ready! Click Here to view personalized "

                         "🎵 Top Songs: Your most-loved tracks on repeat."
                         "🎶 Favorite Genres: Discover the sounds that defined your year."
                         "⏱️ Total Listening Time: See how much time we’ve spent together!"
                         
                         "Thank you for making Spotify a part of your year. "
                         "Here’s to another year of amazing music together!"
                         
                         "Keep listening,"
                         "The Spotify Team 🎧"
    },

    "Engaged Users": {
        "Percentage": 26.09,
        "Email Context": "Subject: 🎁 Holiday Special: 3 Months of Premium for Just $3.99 🎶"
                         "Body: "
                         "Hi [User's Name],"
                         
                         "This Black Friday/Christmas, we’re bringing you an exclusive offer "
                         "to make your Spotify experience even better!"
                         
                         "Get 3 months of Spotify Premium for just $3.99."
                         
                         "With Premium, you’ll enjoy:"
                         
                         "Ad-free listening: Your music, uninterrupted."
                         "Offline mode: Download and enjoy anywhere."
                         "Unlimited skips: Always the perfect vibe."
                         
                         "This special holiday deal is only available for a limited time—don’t wait!"
                         "Click here to activate your special offer. "
                         
                         "Celebrate the season with the music you love."
                         
                         "Cheers,"
                         "The Spotify Team 🎧"
    },

    "High-Risk Users": {
        "Percentage": 24.12,
        "Email Context": "Subject: We Miss You! Enjoy 1 Month of Premium on Us 🎶"
                         "Body:"
                         "Hi [User's Name],"
                         
                         "It’s been a while, and we miss having you as part of our Spotify family. "
                         "We noticed you haven’t "
                         "been around lately and want to make it easy for you to come back and "
                         "rediscover your favorite music and podcasts."
                         "As a special offer, we’re giving you 1 month of Premium for free—no "
                         "strings attached! Dive back into ad-free listening, "
                         "unlimited skips, and offline downloads today."
                         
                         "Don’t miss this opportunity to reconnect with the music you love. "
                         "Click here to activate your "
                         
                         "We’re excited to have you back!"
                         
                         "Best,"
                         "The Spotify Team 🎧"
    }
}


def solutions_page():
    set_page_background()
    st.title("Solutions")
    st.write("Here are insights and actions applied for various user categories:")

    col1, col2 = st.columns(2)

    for i, (category, details) in enumerate(SOLUTIONS_DATA.items()):
        col = col1 if i % 2 == 0 else col2
        with col:
            st.subheader(category)

            fig, ax = plt.subplots()
            ax.pie(
                [details["Percentage"], 100 - details["Percentage"]],
                labels=[category, "Other"],
                autopct='%1.1f%%',
                startangle=90,
                colors=["#003366", "skyblue"]
            )
            ax.set_title(f"{category} Breakdown")
            st.pyplot(fig)

            if st.button(f"Details: {category}", key=category):
                with st.expander(f"{category} Details"):
                    st.write(f"**Percentage**: {details['Percentage']}%")
                    st.write(f"**Email Context**: {details['Email Context']}")


if __name__ == "__main__":
    st.session_state["page"] = "Solutions"

    if st.session_state["page"] == "Solutions":
        solutions_page()


# Page 3: Pricing
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


def pricing_page():
    st.markdown("<h1>Pricing Plans</h1>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

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

