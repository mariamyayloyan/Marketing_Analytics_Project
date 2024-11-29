import streamlit as st


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


def pricing_page():
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


pricing_page()
