import streamlit as st
import matplotlib.pyplot as plt


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


solutions_page()

