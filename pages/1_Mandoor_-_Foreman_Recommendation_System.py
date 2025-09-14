import streamlit as st

st.set_page_config(page_title="Mandoor Project", layout="wide")

# --- HEADER & HERO IMAGE ---
st.title("Mandoor - AI-Powered Foreman Recommendation System")
st.image("assets/Mandoor.png", caption="Connecting Project Needs with the Right Professionals")

st.write("---")

# --- PROBLEM & SOLUTION ---
with st.container():
    st.header("The Challenge: The Frustration Behind Finding a Foreman")
    st.markdown("""
    Finding the right construction foreman in Indonesia is often a gamble. The process is scattered, inefficient, and heavily reliant on subjective, word-of-mouth recommendations. Home and business owners often struggle to accurately compare skills, availability, and costs, which can lead to delayed projects or unsatisfactory results.

    **This is where Mandoor comes in as the solution.** Mandoor is an intelligent application designed to revolutionize this process. By harnessing the power of **Artificial Intelligence (AI)**, Mandoor transforms a complex search into a fast, data-driven, and trustworthy experience.
    """)

# --- MY ROLE ---
with st.container():
    st.header("My Role: Architect of the Recommendation Engine")
    st.markdown("""
    This was a **GROUP PROJECT** developed for the **Bangkit Academy Capstone** by a six-person team. What made this collaboration unique was that our members came from different universities (**UIN Sunan Kalijaga** and **Universitas Alma Ata**), creating a dynamic **multi-campus collaboration** across three divisions: **Machine Learning (ML)**, **Cloud Computing (CC)**, and **Mobile Development**.

    My role was **Machine Learning Engineer**. I did more than just write code; I was responsible for designing and building the **brain** behind the application. My tasks covered the entire machine learning workflow, from data collection to creating a functional model that forms the core of the Mandoor user experience.
    """)

st.write("---")

# --- TECHNICAL PROCESS ---
with st.container():
    st.header("My Technical Process: From Raw Data to Smart Recommendations")
    st.markdown("Every great AI model starts with quality data. My process was divided into two main stages:")

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("1. Data Collection & Preprocessing")
        st.markdown("""
        The first step was to build the data foundation. I performed **web scraping** on foreman profiles from the Indonesian services marketplace, `sejasa.com`, to gather crucial information like skills, location, and reviews.
        
        This raw data was then cleaned and processed through a **preprocessing** stage:
        - **Tokenization:** Converting narrative user project descriptions into a format the model could understand.
        - **Normalization:** Scaling numerical features (like cost or ratings) to a uniform range, ensuring no single feature dominated the model's learning process.
        """)
    with col2:
        st.subheader("2. Recommendation Model Development")
        st.markdown("""
        With the data prepared, I built the recommendation model using **TensorFlow** with a **Feedforward Neural Network (FNN)** architecture.
        
        This model is designed to 'understand' the nuances of user project descriptions (textual data) and match them with the most suitable foreman profiles (numerical data). The result is a **'relevance score'**—a number that intelligently measures how well-suited a foreman is for a job. This score is what the application uses to present a ranked list of top recommendations to the user.
        """)

# --- FINAL RESULT & LEARNINGS ---
with st.container():
    st.header("The Final Result: Recommendations That Work")
    st.markdown("The model I developed successfully produced a list of relevant recommendations, as shown in the sample output below. This is tangible proof of how structured data can provide a far superior solution to manual searching.")
    
    # You can replace this placeholder with a real image of your model's output.
    st.image("https://i.imgur.com/8xYtJ6n.png", caption="Sample output from the model, showing the top 10 foremen ranked by predicted relevance score.")
    
    st.header("Learnings & Personal Impact")
    st.markdown("""
    1.  **Technical Mastery:** This project solidified my understanding of the **end-to-end machine learning lifecycle**, from the challenges of data scraping to developing a hybrid model that handles both text and numerical data in **TensorFlow**.
    2.  **Product Mindset:** I learned that data quality is the absolute foundation of any successful AI product. A model is only as good as the data it's trained on.
    3.  **Cross-Disciplinary Collaboration:** Working closely with the Cloud and Mobile teams taught me the importance of effective communication to create a well-integrated product. This experience strengthened my desire to continue learning in a collaborative, product-focused environment like the **Apple Developer Academy**.
    """)

st.write("---")

# --- TECHNOLOGIES & LINKS ---
with st.container():
    st.header("Technologies Used & Project Links")
    st.markdown("""
    - **Languages & Libraries:** Python, TensorFlow, Pandas
    - **[View the Code on GitHub](https://github.com/Man-door/Machine-Learning)**
    - **[Watch the Video Presentation on YouTube](https://www.youtube.com/watch?v=0av6gDgxAWg)**
    """)

st.write("---")

# --- NAVIGATION ---
st.header("Navigate Projects")
col1, col2 = st.columns([1, 1])

with col1:
    st.page_link("Dashboard.py", label="⬅️ Back to Dashboard", icon="🏠")

with col2:
    st.page_link("pages/2_TuruKamar_-_Accommodation_Booking_App.py", label="Next Project: TuruKamar ➡️", icon="🏨")

