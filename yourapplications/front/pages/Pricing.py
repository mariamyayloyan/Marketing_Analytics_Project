import streamlit as st


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
