import streamlit as st

# Mengatur konfigurasi halaman
st.set_page_config(
    page_title="Arif Fathurrahman | Portfolio",
    page_icon="👨‍💻",
    layout="wide"
)

# --- HEADER SECTION ---
with st.container():
    st.markdown("""
    <div style="background: #f8f9fa; padding: 25px; border-radius: 8px; margin: 20px 0; text-align: center; border-left: 4px solid #667eea;">
        <h1 style="color: #333; margin: 0; font-size: 2.5em;">
            👨‍💻 Arif Fathurrahman's Portfolio
        </h1>
        <p style="color: #666; font-size: 1.2em; margin: 10px 0 0 0;">
            Welcome to my interactive portfolio!
        </p>
        <p style="color: #555; margin: 15px 0 0 0; font-size: 1em; line-height: 1.4;">
            This web app, built with Streamlit, showcases some of my key projects in mobile development, machine learning, and data analysis. Please use the navigation sidebar on the left to explore each project in more detail.
        </p>
    </div>
    """, unsafe_allow_html=True)

# --- PROJECTS OVERVIEW ---
with st.container():
    st.markdown("""
    <div style="background: #f0f8ff; padding: 20px; border-radius: 8px; margin: 20px 0; border-left: 4px solid #4facfe;">
        <h2 style="color: #333; text-align: center; margin: 0 0 15px 0; font-size: 1.8em;">
            🚀 Projects Overview
        </h2>
        <p style="color: #666; text-align: center; margin: 0 0 20px 0; font-size: 1em;">
            Here is a brief summary of the projects you can find in this portfolio.
        </p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div style="background: #fff5f5; padding: 15px; border-radius: 6px; margin: 8px 0; border-left: 3px solid #ff6b6b;">
            <h3 style="color: #333; margin: 0 0 8px 0; font-size: 1.2em; text-align: center;">
                🏗️ Mandoor - Foreman Recommendation System
            </h3>
            <p style="color: #555; margin: 0; text-align: justify; line-height: 1.4; font-size: 0.9em;">
                An AI-powered app to find reliable construction foremen using a TensorFlow recommendation model.
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div style="background: #f0fdfa; padding: 15px; border-radius: 6px; margin: 8px 0; border-left: 3px solid #20bf6b;">
            <h3 style="color: #333; margin: 0 0 8px 0; font-size: 1.2em; text-align: center;">
                🏨 TuruKamar - Accommodation Booking App
            </h3>
            <p style="color: #555; margin: 0; text-align: justify; line-height: 1.4; font-size: 0.9em;">
                A comprehensive mobile booking app for accommodations in Yogyakarta, built end-to-end with Flutter.
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div style="background: #fff8e1; padding: 15px; border-radius: 6px; margin: 8px 0; border-left: 3px solid #ff9800;">
            <h3 style="color: #333; margin: 0 0 8px 0; font-size: 1.2em; text-align: center;">
                💰 Crypto Tracker - Crypto Currency Simulator
            </h3>
            <p style="color: #555; margin: 0; text-align: justify; line-height: 1.4; font-size: 0.9em;">
                A full-stack web app to simulate cryptocurrency trading, powered by a Node.js backend and CoinGecko API.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div style="background: #f3e5f5; padding: 15px; border-radius: 6px; margin: 8px 0; border-left: 3px solid #9c27b0;">
            <h3 style="color: #333; margin: 0 0 8px 0; font-size: 1.2em; text-align: center;">
                🚴 Bike Sharing Data Analytic
            </h3>
            <p style="color: #555; margin: 0; text-align: justify; line-height: 1.4; font-size: 0.9em;">
                An end-to-end data analysis project with an interactive Streamlit dashboard to uncover bike rental patterns.
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div style="background: #e8f4fd; padding: 15px; border-radius: 6px; margin: 8px 0; border-left: 3px solid #2196f3;">
            <h3 style="color: #333; margin: 0 0 8px 0; font-size: 1.2em; text-align: center;">
                💳 Cashier Application (POS)
            </h3>
            <p style="color: #555; margin: 0; text-align: justify; line-height: 1.4; font-size: 0.9em;">
                A desktop Point of Sale (POS) application built with Java, focusing on strong Object-Oriented Programming (OOP) principles.
            </p>
        </div>
        """, unsafe_allow_html=True)

st.markdown("""
<div style="background: #f5f5f5; padding: 15px; border-radius: 6px; margin: 15px 0; text-align: center; border-left: 3px solid #666;">
    <p style="color: #333; margin: 0; font-size: 1em;">
        ✨ Select a project above to see the details ✨
    </p>
</div>
""", unsafe_allow_html=True)

# --- CONTACT INFORMATION ---
st.header("📞 Get In Touch")
st.markdown("**Email:** ariffathurrahman0@gmail.com")
st.markdown("**WhatsApp:** www.wa.me/6285601036974")
st.markdown("**LinkedIn:** www.linkedin.com/in/arif-fathurrahman")
st.markdown("**GitHub:** www.github.com/ARiP001")
