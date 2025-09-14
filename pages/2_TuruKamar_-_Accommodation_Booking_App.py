import streamlit as st

st.set_page_config(page_title="TuruKamar Project", layout="wide")

# --- HEADER & HERO IMAGE ---
st.markdown("""
<div style="text-align: center;">
    <h1 style="margin: 0;">TuruKamar - Integrated Accommodation Booking App</h1>
</div>
""", unsafe_allow_html=True)

st.write("---")

# --- PROBLEM & SOLUTION ---
with st.container():
    st.markdown("""
    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 15px; border-radius: 8px; margin: 15px 0;">
        <h2 style="color: white; text-align: center; margin: 0; font-size: 1.6em; text-shadow: 1px 1px 2px rgba(0,0,0,0.3);">
            🏨 The Challenge: A Fragmented Search Experience
        </h2>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    Yogyakarta is a major hub for tourists and students, leading to high demand for accommodations. However, information about hotels, guesthouses, and rooms is scattered across various platforms, from social media to word-of-mouth. This makes it difficult for users to efficiently compare prices, facilities, and availability.

    **The solution is TuruKamar,** a mobile application designed to be a centralized, one-stop platform for this process. Built with **Flutter**, it provides a reliable and integrated solution that makes finding the right room easier, faster, and more trustworthy.
    """)

# --- MY ROLE ---
with st.container():
    st.markdown("""
    <div style="background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); padding: 15px; border-radius: 8px; margin: 15px 0;">
        <h2 style="color: white; text-align: center; margin: 0; font-size: 1.6em; text-shadow: 1px 1px 2px rgba(0,0,0,0.3);">
            👨‍💻 My Role: Full-Stack Mobile Developer
        </h2>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    This was an **INDIVIDUAL PROJECT** that I developed for my **University Final Project**. As the sole developer, I was responsible for the **entire project lifecycle**, from conceptualization and system design to front-end UI/UX implementation and feature development. This project was my chance to independently manage the creation of a complete mobile application from scratch.
    """)

st.write("---")

# --- TECHNICAL PROCESS ---
with st.container():
    st.markdown("""
    <div style="background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%); padding: 15px; border-radius: 8px; margin: 15px 0;">
        <h2 style="color: white; text-align: center; margin: 0; font-size: 1.6em; text-shadow: 1px 1px 2px rgba(0,0,0,0.3);">
            ⚙️ My Technical Process: From Architecture to a Functional App
        </h2>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("To ensure a well-structured and maintainable application, my process was divided into two key stages:")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 100%); padding: 12px; border-radius: 6px; margin: 8px 0;">
            <h3 style="color: #333; margin: 0; text-align: center; font-size: 1.2em;">
                📐 1. System Architecture & Design
            </h3>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        Before writing any code, I architected the complete system using **UML diagrams**. This included creating:
        - **Use Case Diagrams** to define user interactions.
        - **Activity Diagrams** to map out user flows for processes like booking.
        - **Class Diagrams** to design the data structure for entities like users, hotels, and transactions.
        - **Sequence Diagrams** to detail object interactions.
        
        This design-first approach ensured a logical and scalable foundation for the application.
        """)
    with col2:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%); padding: 12px; border-radius: 6px; margin: 8px 0;">
            <h3 style="color: #333; margin: 0; text-align: center; font-size: 1.2em;">
                📱 2. Cross-Platform Feature Implementation
            </h3>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        Using **Flutter** and **Dart**, I implemented all core features for both Android and iOS from a single codebase. Key functionalities include:
        - **Dynamic Search & GPS:** A search engine with filters, integrated with the device's **GPS** for a 'search nearby' feature and an interactive map view.
        - **Unique User Experience:** A **'shake-to-confirm'** transaction gesture using motion sensors.
        - **End-to-End Booking:** A complete booking flow that generates a downloadable **PDF receipt**.
        - **Local Data Management:** Efficient local data persistence for user sessions and bookmarks using **Hive**.
        """)

# --- FINAL RESULT & LEARNINGS ---
with st.container():
    st.markdown("""
    <div style="background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%); padding: 15px; border-radius: 8px; margin: 15px 0;">
        <h2 style="color: #333; text-align: center; margin: 0; font-size: 1.6em; text-shadow: 1px 1px 2px rgba(0,0,0,0.1);">
            🎯 The Final Result: A Functional Booking App
        </h2>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("The final result is a fully functional prototype that solves the initial problem by centralizing accommodation information into an intuitive mobile experience.")
    
    # Display TuruKamar app screenshots - First row (2 images)
    col1, col2 = st.columns(2)
    with col1:
        st.image("assets/turukamar1.png", caption="Home screen with search and categories.")
    with col2:
        st.image("assets/turukamar3.png", caption="Detail hotel/accommodation.")
    
    # Display additional screenshots - Second row (3 images)
    col3, col4, col5 = st.columns(3)
    with col3:
        st.image("assets/turukamar2.png", caption="Google Maps integration.")
    with col4:
        st.image("assets/turukamar4.png", caption="Fitur lainnya.")
    with col5:
        st.image("assets/turukamar5.png", caption="Receipt.")

    st.markdown("""
    <div style="background: linear-gradient(135deg, #d299c2 0%, #fef9d7 100%); padding: 15px; border-radius: 8px; margin: 15px 0;">
        <h2 style="color: #333; text-align: center; margin: 0; font-size: 1.6em; text-shadow: 1px 1px 2px rgba(0,0,0,0.1);">
            💡 Learnings & Personal Impact
        </h2>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    1.  **End-to-End Development:** This project was a deep dive into the entire **cross-platform mobile development lifecycle** with Flutter, from architecture to implementation.
    2.  **Product Ownership:** I learned how to manage a full project independently, translating user needs into a well-architected design and a functional product.
    3.  **Technical Integration:** It provided me with practical experience combining API integration, local database management with **Hive**, and interacting with native hardware like **GPS** and motion sensors. This experience is the driving force behind my motivation to deepen my skills at the **Apple Developer Academy**.
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
    
    # Display technology logos
    col1, col2, col3, col4, col5 = st.columns([1, 1, 1, 5, 5])
    
    with col1:
        st.image("assets/Dart_logo.png", width=50, caption="Dart")
    
    with col2:
        st.image("assets/flutter_logo.svg", width=50, caption="Flutter")
    
    with col3:
        st.image("assets/google-maps-2020-icon.svg", width=50, caption="Google Maps")

    st.markdown("""
    - **[View the Code on GitHub](https://github.com/ARiP001/Hotel-Mobile)**
    - **[View the Project Documentation](https://docs.google.com/document/d/18eAxOyaWCwpzyZIK1w-eFOn4QVmLglc8vPEDpYtzKxs/edit?tab=t.32qtn1spo45x)**
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
    st.page_link("pages/1_Mandoor_-_Foreman_Recommendation_System.py", label="⬅️ Previous Project: Mandoor", icon="👷")

with col3:
    st.page_link("pages/3_Crypto_Tracker_-_Crypto_Currency_Simulator.py", label="Next Project: Crypto Tracker ➡️", icon="📈")

