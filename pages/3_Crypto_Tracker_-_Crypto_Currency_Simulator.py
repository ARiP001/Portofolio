import streamlit as st

st.set_page_config(page_title="Crypto Tracker Project", layout="wide")

st.title("Crypto Tracker - Full-Stack Portfolio Management App")
st.write("---")

st.header("Project Overview")
st.markdown("""
Crypto Tracker is a full-stack web application that allows users to simulate cryptocurrency trading, manage a virtual portfolio, and track real-time market data from the **CoinGecko API**. Developed for our Final Project, this was a two-person **GROUP PROJECT**. My role was the **Backend and Cloud Developer**, responsible for building the entire server-side infrastructure and handling its deployment.
""")

st.header("Impact & Learning")
st.markdown("""
My primary impact was creating the robust and scalable server-side foundation that powers the entire application. I designed the **relational database schema** for users, portfolios, and transactions, and built the complete **REST API** from scratch using **Node.js**. This involved implementing all server-side logic, including secure user authentication and the complex business logic for **buy/sell transactions**. I then handled the full deployment to **Google Cloud Platform (GCP)** using **Cloud Run**, ensuring the application was ready for a live production environment.

This project was a comprehensive experience in **backend development and cloud deployment**. I learned to build a secure and stateful **REST API** with **Node.js** and gained hands-on experience taking a project from local development to a live environment on **GCP**. This experience of building the 'engine' behind an application sparked my interest in understanding the full product lifecycle, motivating me to join the Academy to learn how to create seamless, end-to-end user experiences.
""")

st.write("---")
st.header("Visuals and Links")

st.image("https://placehold.co/800x400/EEE/31343C?text=System+Architecture+Diagram", caption="Placeholder for System Architecture Diagram")

st.markdown("""
- **Technologies Used:** Node.js, REST API, Google Cloud Platform (GCP), CoinGecko API
- **[Link to Backend GitHub](https://github.com/ARiP001/Crypto-BE)**
- **[Link to Frontend GitHub](https://github.com/ARiP001/Crypto-FE)**
""")

st.info("More detailed explanations and code snippets will be added here soon.")
