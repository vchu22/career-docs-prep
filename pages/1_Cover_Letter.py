import streamlit as st
from helper.cover_letter import CoverLetter

cl = CoverLetter()
template_instruction = """ Please use these template tags when writing your cover letter templete:
            Company Name: [Company Name], 
            Job Title: [Job Title],
            Referral/Where did you find this job: [Referral Source],
            Applicant Name: [Applicant Name]"""

st.title("Cover Letter Prep")
st.divider()

col1, col2 = st.columns(2)

with col1:
    company_name = st.text_input("Company Name")
    cl.company_name = company_name
    job_title = st.text_input("Job Title")
    cl.job_title = job_title

with col2:
    referer = st.text_input("Referral Source")
    cl.referer = referer
    applicant_name = st.text_input("Applicant Name")
    cl.applicant_name = applicant_name

cover_letter_templete = st.text_area("Cover Letter Template", height=360,
                                     placeholder=template_instruction)
cl.template = cover_letter_templete

fill_btn = st.button("Fill")
if fill_btn:
    st.text(cl.fill_template())