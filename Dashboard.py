import streamlit as st

# Mengatur konfigurasi halaman
st.set_page_config(
    page_title="Arif Fathurrahman | Portfolio",
    page_icon="👨‍💻",
    layout="wide"
)

# --- HEADER SECTION ---
with st.container():
    st.title("Arif Fathurrahman's Portfolio")
    st.subheader("Welcome to my interactive portfolio!")
    st.write(
        "This web app, built with Streamlit, showcases some of my key projects in mobile development, machine learning, and data analysis."
    )
    st.write("Please use the navigation sidebar on the left to explore each project in more detail.")
    st.write("---")

# --- PROJECTS OVERVIEW ---
with st.container():
    st.header("Projects Overview")
    st.write("Here is a brief summary of the projects you can find in this portfolio.")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Mandoor - Foreman Recommendation System")
        st.write("An AI-powered app to find reliable construction foremen using a TensorFlow recommendation model.")

        st.subheader("TuruKamar - Accommodation Booking App")
        st.write("A comprehensive mobile booking app for accommodations in Yogyakarta, built end-to-end with Flutter.")

        st.subheader("Crypto Tracker - Crypto Currency Simulator")
        st.write("A full-stack web app to simulate cryptocurrency trading, powered by a Node.js backend and CoinGecko API.")

    with col2:
        st.subheader("Bike Sharing Data Analytic")
        st.write("An end-to-end data analysis project with an interactive Streamlit dashboard to uncover bike rental patterns.")

        st.subheader("Cashier Application (POS)")
        st.write("A desktop Point of Sale (POS) application built with Java, focusing on strong Object-Oriented Programming (OOP) principles.")

st.sidebar.success("Select a project above to see the details.")
