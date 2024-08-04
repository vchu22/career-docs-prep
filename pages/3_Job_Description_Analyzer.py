import streamlit as st
from helper.text_analyzer import TextAnalyzer

ta = TextAnalyzer()

# Start of the page
st.title("Job Description Analyzer")
st.divider()

ta.description = st.text_area("Job Description", height=360)
max_num_skills = st.number_input("Maxium number of skills to display", value=10)

# Analyze Text button
analyze_btn = st.button("Analyze Text", type="primary")

if analyze_btn:
    most_common_skills = ta.find_most_common_skills(max_num_skills);
    st.write(most_common_skills)