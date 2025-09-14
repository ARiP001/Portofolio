import streamlit as st
import pandas as pd

st.set_page_config(page_title="Bike Sharing Analysis", layout="wide")

st.title("Bike Sharing Data Analytic")
st.write("---")

st.header("Project Overview")
st.markdown("""
In this **individual project**, I performed a complete analysis and visualization of the Capital Bikeshare dataset to uncover key usage patterns. My work encompassed the full data pipeline, from preprocessing and exploratory data analysis (EDA) in a Jupyter Notebook to the deployment of an interactive **Streamlit dashboard**. Through this dashboard, users can explore rental patterns and identify relationships between factors like weather and user type.
""")

st.header("Impact & Learning")
st.markdown("""
This project demonstrates strong skills in data science, including **data wrangling**, analytical thinking, and effective data visualization with **Pandals**, **Matplotlib**, and **Seaborn**. By developing and deploying an interactive **Streamlit dashboard**, I learned to present complex data insights in an accessible, user-friendly format, turning a static analysis into a dynamic data product. This experience of transforming raw data into an interactive, user-facing product is exactly what I am passionate about, and it's why I am eager to build upon these skills in the collaborative, product-focused environment of the **Academy**.
""")

st.write("---")
st.header("Visualizations and Links")

# Placeholder for an interactive chart
st.subheader("Sample Chart: Rentals by Season")
chart_data = pd.DataFrame({
    'Season': ['Spring', 'Summer', 'Fall', 'Winter'],
    'Rentals': [918589, 1061129, 841613, 471348] # Data from your notebook
})
st.bar_chart(chart_data.set_index('Season'))

st.markdown("""
- **Technologies Used:** Python, Pandas, Matplotlib, Seaborn, Streamlit, Jupyter Notebook
- **[Link to GitHub Repository/Notebook](your-repo-link-here)**
""")

st.info("The full interactive dashboard with more charts will be presented here.")
