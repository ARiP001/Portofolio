import streamlit as st

st.set_page_config(page_title="Crypto Tracker Project", layout="wide")

# --- HEADER & HERO IMAGE ---
st.markdown("""
<div style="text-align: center;">
    <h1 style="margin: 0;">Crypto Tracker - Crypto Currency Simulator</h1>
</div>
""", unsafe_allow_html=True)

st.write("---")

# --- PROBLEM & SOLUTION ---
with st.container():
    st.markdown("""
    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 15px; border-radius: 8px; margin: 15px 0;">
        <h2 style="color: white; text-align: center; margin: 0; font-size: 1.6em; text-shadow: 1px 1px 2px rgba(0,0,0,0.3);">
            📈 The Challenge: Building a Complete Trading Experience
        </h2>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    The world of cryptocurrency can be intimidating for newcomers. To provide a risk-free learning environment, this project aimed to create a full-stack web application that allows users to simulate buying and selling cryptocurrencies, manage a virtual portfolio, and track real-time market data.

    **The solution is Crypto Tracker,** an application built with a separate **Node.js backend** and a dynamic **React frontend**. It fetches live data from the **CoinGecko API** and provides a complete, interactive trading simulation experience.
    """)

# --- MY ROLE ---
with st.container():
    st.markdown("""
    <div style="background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); padding: 15px; border-radius: 8px; margin: 15px 0;">
        <h2 style="color: white; text-align: center; margin: 0; font-size: 1.6em; text-shadow: 1px 1px 2px rgba(0,0,0,0.3);">
            👨‍💻 My Role: Backend and Cloud Developer
        </h2>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    This was a **GROUP PROJECT** developed by a two-person team for our Final Project. My role was **Backend and Cloud Developer**. I was responsible for architecting and building the entire server-side of the application and managing its deployment, while my partner focused on the frontend.
    """)

st.write("---")

# --- TECHNICAL PROCESS ---
with st.container():
    st.markdown("""
    <div style="background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%); padding: 15px; border-radius: 8px; margin: 15px 0;">
        <h2 style="color: white; text-align: center; margin: 0; font-size: 1.6em; text-shadow: 1px 1px 2px rgba(0,0,0,0.3);">
            ⚙️ My Technical Process: Building the Server-Side Engine
        </h2>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("My process focused on creating a robust and scalable server-side foundation for the application:")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 100%); padding: 12px; border-radius: 6px; margin: 8px 0;">
            <h3 style="color: #333; margin: 0; text-align: center; font-size: 1.2em;">
                💾 1. API & Database Architecture
            </h3>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        The core of the backend is a **REST API** built from scratch using **Node.js**. I designed the **relational database schema** to logically structure data for users, their portfolios, and transaction histories.
        
        Key implementations include:
        - **Full CRUD Operations** for all entities.
        - **Secure User Authentication** with hashed passwords.
        - **Complex Business Logic** for processing buy/sell transactions and validating user balances.
        """)
    with col2:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%); padding: 12px; border-radius: 6px; margin: 8px 0;">
            <h3 style="color: #333; margin: 0; text-align: center; font-size: 1.2em;">
                ☁️ 2. Cloud Deployment
            </h3>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        To make the application reliably accessible, I handled the entire deployment process to **Google Cloud Platform (GCP)**.
        
        - The backend service was deployed using **Cloud Run**, which ensures the application is scalable and can handle varying loads efficiently.
        - This step bridged the gap between local development and a live, production-ready environment, making the API available for the frontend to consume.
        """)

# --- FINAL RESULT & LEARNINGS ---
with st.container():
    st.markdown("""
    <div style="background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%); padding: 15px; border-radius: 8px; margin: 15px 0;">
        <h2 style="color: #333; text-align: center; margin: 0; font-size: 1.6em; text-shadow: 1px 1px 2px rgba(0,0,0,0.1);">
            🎯 The Final Result: A Functional Trading API
        </h2>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("The final backend was a fully functional and deployed API, capable of handling user management, transactions, and providing real-time data to the React frontend.")
    
    st.image("https://placehold.co/1200x400/00A86B/FFFFFF?text=API+Endpoints+Example", caption="An example showcasing the structure of the API and its endpoints.")

    st.markdown("""
    <div style="background: linear-gradient(135deg, #d299c2 0%, #fef9d7 100%); padding: 15px; border-radius: 8px; margin: 15px 0;">
        <h2 style="color: #333; text-align: center; margin: 0; font-size: 1.6em; text-shadow: 1px 1px 2px rgba(0,0,0,0.1);">
            💡 Learnings & Personal Impact
        </h2>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    1.  **Full-Stack Understanding:** This project was a comprehensive experience in building the 'engine' behind an application, teaching me how to connect a separate backend and frontend from scratch.
    2.  **Cloud Deployment:** It provided me with crucial hands-on experience deploying a production-ready application to a major cloud provider, **GCP**, bridging the gap between local development and a live environment.
    3.  **Product Lifecycle Motivation:** This experience sparked my interest in understanding the full product lifecycle, motivating me to join the Academy to learn how to create seamless, end-to-end user experiences.
    """)

st.write("---")

# --- TECHNOLOGIES & LINKS ---
with st.container():
    st.markdown("""
    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 15px; border-radius: 8px; margin: 15px 0;">
        <h2 style="color: white; text-align: center; margin: 0; font-size: 1.6em; text-shadow: 1px 1px 2px rgba(0,0,0,0.3);">
            🛠️ Technologies Used & Project Links
        </h2>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3, col4, col5 = st.columns([1, 1, 1, 5, 5])
    with col1:
        st.image("assets/Node.js_logo.svg", width=50, caption="Node.js")
    with col2:
        st.image("assets/google-cloud-seeklogo.svg", width=50, caption="GCP")

    st.markdown("""
    - **[View the Backend Code on GitHub](https://github.com/ARiP001/Crypto-BE)**
    - **[View the Frontend Code on GitHub](https://github.com/ARiP001/Crypto-FE)**
    """)

st.write("---")

# --- NAVIGATION ---
st.markdown("""
<div style="background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); padding: 15px; border-radius: 8px; margin: 15px 0;">
    <h2 style="color: white; text-align: center; margin: 0; font-size: 1.6em; text-shadow: 1px 1px 2px rgba(0,0,0,0.3);">
        🚀 Navigate Projects
    </h2>
</div>
""", unsafe_allow_html=True)
col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    st.page_link("pages/2_TuruKamar_-_Accommodation_Booking_App.py", label="⬅️ Previous Project: TuruKamar", icon="🏨")

with col3:
    st.page_link("pages/4_Bike_Sharing_Data_Analytic.py", label="Next Project: Bike Sharing Data Analytic ➡️", icon="🚲")

