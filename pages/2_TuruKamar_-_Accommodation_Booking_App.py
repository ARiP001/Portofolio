import streamlit as st

st.set_page_config(page_title="TuruKamar Project", layout="wide")

st.title("TuruKamar - An Integrated Accommodation Booking App")
st.write("---")

st.header("Project Overview")
st.markdown("""
TuruKamar is a comprehensive mobile application built with **Flutter** that provides a centralized, one-stop solution for searching and booking accommodations in the Yogyakarta region. As a self-initiated University Final Project, this was an **individual endeavor** where I acted as the sole developer responsible for the entire project lifecycle, from concept and design to implementation.
""")

st.header("Impact & Learning")
st.markdown("""
My impact was bringing this application from a concept to a functional prototype. I designed the complete system architecture from scratch with **UML diagrams** and built a responsive, **cross-platform** UI. I then single-handedly implemented all core features, including user authentication, a dynamic search engine with **GPS integration** to **enable users to instantly find nearby accommodations**, and created a **unique user experience** by implementing a **'shake-to-confirm'** gesture for transactions. This work also included a full booking flow that generates a **PDF receipt** and managing local data persistence with **Hive**.

Through this experience, I learned the entire **end-to-end process of cross-platform mobile development** with Flutter. It was a deep dive into translating user needs into a well-architected design, combining API integration, local database management, and managing a full project independently from concept to completion. **This experience is the driving force behind my motivation to deepen my skills in building polished, user-centric applications at the Academy.**
""")

st.write("---")
st.header("Visuals and Links")

st.image("https://placehold.co/400x800/EEE/31343C?text=App+Screenshot", caption="Placeholder for App UI Screenshot")

st.markdown("""
- **Technologies Used:** Flutter, Dart, Hive, REST API, GPS
- **[Link to GitHub Repository](your-repo-link-here)**
- **[Link to Project Documentation](your-doc-link-here)**
""")

st.info("More detailed explanations and code snippets will be added here soon.")
