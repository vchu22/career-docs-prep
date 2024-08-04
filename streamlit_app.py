import streamlit as st

st.set_page_config(
    page_title="Career Docs Prep Tools",
    page_icon="📄",
)

st.write("# 🏢 Career Docs Prep Tools 📄")

st.sidebar.success("Select a tab above.")

st.markdown(
    """
    A simple web interface to help reduce mistakes when writing cover letters and resumes.
    
    **👈 Select a tab from the sidebar** for the type of writing you are preparing for!
    ## What does this do?
    ### Cover Letter 
    - Autofill cover letter template with the job and the company you are applying for
    - Replace the names on your previous cover letter with new ones
    ### Resume
    - Working in progress 🚧
    ### Job Description Analyzer
    - Working in progress 🚧
"""
)