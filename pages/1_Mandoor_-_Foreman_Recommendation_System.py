import streamlit as st

st.set_page_config(page_title="Mandoor Project", layout="wide")

# --- HEADER & HERO IMAGE ---

st.markdown("""
<div style="text-align: center;">
    <h1 style="margin: 0;">Mandoor : AI-Powered Foreman Recommendation System</h1>
</div>
""", unsafe_allow_html=True)
col1, col2, col3 = st.columns([1,50, 1])
with col2:
    st.image("assets/Mandoor.png", caption="Connecting Project Needs with the Right Professionals")

st.write("---")

# --- PROBLEM & SOLUTION ---
with st.container():
    st.markdown("""
    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 15px; border-radius: 8px; margin: 15px 0;">
        <h2 style="color: white; text-align: center; margin: 0; font-size: 1.6em; text-shadow: 1px 1px 2px rgba(0,0,0,0.3);">
            🚧 The Challenge: The Frustration Behind Finding a Foreman
        </h2>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    Finding the right construction foreman in Indonesia is often a gamble. The process is scattered, inefficient, and heavily reliant on subjective, word-of-mouth recommendations. Home and business owners often struggle to accurately compare skills, availability, and costs, which can lead to delayed projects or unsatisfactory results.

    **This is where Mandoor comes in as the solution.** Mandoor is an intelligent application designed to revolutionize this process. By harnessing the power of **Artificial Intelligence (AI)**, Mandoor transforms a complex search into a fast, data-driven, and trustworthy experience.
    """)

# --- MY ROLE ---
with st.container():
    st.markdown("""
    <div style="background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); padding: 15px; border-radius: 8px; margin: 15px 0;">
        <h2 style="color: white; text-align: center; margin: 0; font-size: 1.6em; text-shadow: 1px 1px 2px rgba(0,0,0,0.3);">
            👨‍💻 My Role: Architect of the Recommendation Engine
        </h2>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    This was a **GROUP PROJECT** developed for the **Bangkit Academy Capstone** by a six-person team. What made this collaboration unique was that our members came from different universities (**UIN Sunan Kalijaga** and **Universitas Alma Ata**), creating a dynamic **multi-campus collaboration** across three divisions: **Machine Learning (ML)**, **Cloud Computing (CC)**, and **Mobile Development**.

    My role was **Machine Learning Engineer**. I did more than just write code; I was responsible for designing and building the **brain** behind the application. My tasks covered the entire machine learning workflow, from data collection to creating a functional model that forms the core of the Mandoor user experience.
    """)

st.write("---")

# --- TECHNICAL PROCESS ---
with st.container():
    st.markdown("""
    <div style="background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%); padding: 15px; border-radius: 8px; margin: 15px 0;">
        <h2 style="color: white; text-align: center; margin: 0; font-size: 1.6em; text-shadow: 1px 1px 2px rgba(0,0,0,0.3);">
            ⚙️ My Technical Process: From Raw Data to Smart Recommendations
        </h2>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("Every great AI model starts with quality data. My process was divided into two main stages:")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 100%); padding: 12px; border-radius: 6px; margin: 8px 0;">
            <h3 style="color: #333; margin: 0; text-align: center; font-size: 1.2em;">
                📊 1. Data Collection & Preprocessing
            </h3>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        The first step was to build the data foundation. I performed **web scraping** on foreman profiles from the Indonesian services marketplace, `sejasa.com`, to gather crucial information like skills, location, and reviews.
        
        This raw data was then cleaned and processed through a **preprocessing** stage:
        - **Tokenization:** Converting narrative user project descriptions into a format the model could understand.
        - **Normalization:** Scaling numerical features (like cost or ratings) to a uniform range, ensuring no single feature dominated the model's learning process.
        """)
    with col2:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%); padding: 12px; border-radius: 6px; margin: 8px 0;">
            <h3 style="color: #333; margin: 0; text-align: center; font-size: 1.2em;">
                🤖 2. Recommendation Model Development
            </h3>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        With the data prepared, I built the recommendation model using **TensorFlow** with a **Feedforward Neural Network (FNN)** architecture.
        
        This model is designed to 'understand' the nuances of user project descriptions (textual data) and match them with the most suitable foreman profiles (numerical data). The result is a **'relevance score'**—a number that intelligently measures how well-suited a foreman is for a job. This score is what the application uses to present a ranked list of top recommendations to the user.
        """)

# --- FINAL RESULT & LEARNINGS ---
with st.container():
    st.markdown("""
    <div style="background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%); padding: 15px; border-radius: 8px; margin: 15px 0;">
        <h2 style="color: #333; text-align: center; margin: 0; font-size: 1.6em; text-shadow: 1px 1px 2px rgba(0,0,0,0.1);">
            🎯 The Final Result: Recommendations That Work
        </h2>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("The model I developed successfully produced a list of relevant recommendations, as shown in the sample output below. This is tangible proof of how structured data can provide a far superior solution to manual searching.")
    
    # Display model evaluation and test results
    col1, col2 = st.columns(2)
    
    with col1:
        st.image("assets/evaluasi-model.png", caption="Model Evaluation Results")
    
    with col2:
        st.image("assets/tes-model.png", caption="Model Testing Results")
    
    st.markdown("""
    <div style="background: linear-gradient(135deg, #d299c2 0%, #fef9d7 100%); padding: 15px; border-radius: 8px; margin: 15px 0;">
        <h2 style="color: #333; text-align: center; margin: 0; font-size: 1.6em; text-shadow: 1px 1px 2px rgba(0,0,0,0.1);">
            💡 Learnings & Personal Impact
        </h2>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    1.  **Technical Mastery:** This project solidified my understanding of the **end-to-end machine learning lifecycle**, from the challenges of data scraping to developing a hybrid model that handles both text and numerical data in **TensorFlow**.
    2.  **Product Mindset:** I learned that data quality is the absolute foundation of any successful AI product. A model is only as good as the data it's trained on.
    3.  **Cross-Disciplinary Collaboration:** Working closely with the Cloud and Mobile teams taught me the importance of effective communication to create a well-integrated product. This experience strengthened my desire to continue learning in a collaborative, product-focused environment like the **Apple Developer Academy**.
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
    
    # Display technology logos in a tighter group
    col1, col2, col3, col4, col5 = st.columns([1, 1, 1, 5, 5])
    
    with col1:
        st.image("assets/Python-logo-notext.svg", width=50, caption="Python")
    
    with col2:
        st.image("assets/Tensorflow_logo.svg", width=50, caption="TensorFlow")
    
    with col3:
        st.image("assets/Jupyter_logo.svg", width=50, caption="Jupyter")
    
    st.markdown("""
    - **[View the Code on GitHub](https://github.com/Man-door/Machine-Learning)**
    - **[Watch the Video Presentation on YouTube](https://www.youtube.com/watch?v=0av6gDgxAWg)**
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
col1, col2 = st.columns([1, 1])

with col1:
    st.page_link("Dashboard.py", label="⬅️ Back to Dashboard", icon="🏠")

with col2:
    st.page_link("pages/2_TuruKamar_-_Accommodation_Booking_App.py", label="Next Project: TuruKamar ➡️", icon="🏨")


