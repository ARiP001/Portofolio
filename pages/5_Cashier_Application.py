import streamlit as st

st.set_page_config(page_title="Cashier App Project", layout="wide")

st.title("Java OOP Cashier Application: A Point of Sale System")
st.write("---")

st.header("Project Overview")
st.markdown("""
This project originated from a **real-world problem**, identified after **interviewing a local minimarket owner** to understand their daily operational challenges. The resulting solution was this desktop Point of Sale (POS) application, built with **Java** and grounded in strong **Object-Oriented Programming (OOP)** principles. As the **Java Developer** in a two-person **GROUP PROJECT**, my core responsibilities involved both backend logic and **implementing the code from the Figma design.**
""")

st.header("Impact & Learning")
st.markdown("""
I architected the application's **OOP structure** by designing a robust class hierarchy for entities like `Products` and `Transactions`, using principles of **encapsulation** and **inheritance**. I then translated the high-fidelity UI/UX designs from **Figma** into a functional GUI using **Java Swing/JavaFX**, implementing key features such as sales processing and the ability to **download reports in PDF format**.

This project was a valuable experience, teaching me how to translate **direct user feedback** from an interview into concrete technical requirements. It solidified my ability to apply **OOP** theory to solve a practical business need and to translate a visual design from **Figma** into a functional product. Collaborating in a team environment further honed my skills in dividing technical responsibilities to achieve a common goal, reinforcing my drive to build complete, user-centric solutions at the **Academy**.
""")

st.write("---")
st.header("Visuals and Links")

st.image("https://placehold.co/800x600/EEE/31343C?text=Application+Screenshot", caption="Placeholder for Application UI Screenshot")

st.markdown("""
- **Technologies Used:** Java, Object-Oriented Programming (OOP), Java Swing/JavaFX, Figma (for design), PDF Generation Library
- **[Link to GitHub Repository](your-repo-link-here)**
""")

st.info("More detailed explanations and code snippets will be added here soon.")
